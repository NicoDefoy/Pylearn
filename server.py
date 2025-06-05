from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import io
import contextlib
import importlib.util
import glob
from rapidfuzz.distance import Levenshtein  # ✅ Remplace Levenshtein standard

app = Flask(__name__, static_folder='dist')
CORS(app)

# === Servir l'app React ===
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# === Route pour exécuter du code Python ===
@app.route('/api/execute', methods=['POST'])
def execute_code():
    data = request.json
    code = data.get('code', '')
    expected_output = data.get('expected_output', '')

    buffer = io.StringIO()
    result = {'output': '', 'error': None, 'match': 'wrong'}

    try:
        with contextlib.redirect_stdout(buffer):
            exec(code)
        output = buffer.getvalue().strip()
        result['output'] = output

        # Nettoyage avant comparaison
        clean_output = output.replace('\n', '').replace(' ', '')
        clean_expected = expected_output.replace('\n', '').replace(' ', '')

        distance = Levenshtein.distance(clean_output, clean_expected)

        if distance == 0:
            result['match'] = 'exact'
        elif distance <= 3:
            result['match'] = 'close'
        else:
            result['match'] = 'wrong'

    except Exception as e:
        result['error'] = str(e)

    return jsonify(result)

# === Charger les exercices dynamiquement ===
def load_exercises_from_file(filepath):
    spec = importlib.util.spec_from_file_location("module.name", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, 'exercises', [])

# === Route pour tous les exercices ===
@app.route('/api/exercises')
def get_all_exercises():
    exercises = []
    exercise_dir = os.path.join(os.path.dirname(__file__), 'exercises')
    py_files = glob.glob(os.path.join(exercise_dir, '*.py'))
    for file_path in py_files:
        if '__init__' not in file_path and '__pycache__' not in file_path:
            file_exercises = load_exercises_from_file(file_path)
            exercises.extend(file_exercises)
    return jsonify(exercises)

# === Route : exercices filtrés par thème ===
@app.route('/api/exercises/<theme>')
def get_exercises_by_theme(theme):
    all_exercises = get_all_exercises().json
    filtered = [ex for ex in all_exercises if ex.get('theme') == theme]
    return jsonify(filtered)

def load_lesson_from_file(filepath):
    spec = importlib.util.spec_from_file_location("lesson_module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, 'lesson', None)

@app.route('/api/lessons')
def get_all_lessons():
    lessons = []
    lesson_dir = os.path.join(os.path.dirname(__file__), 'lessons')
    py_files = glob.glob(os.path.join(lesson_dir, '*.py'))
    for file_path in py_files:
        if '__init__' not in file_path and '__pycache__' not in file_path:
            lesson = load_lesson_from_file(file_path)
            if lesson:
                lessons.append({
                    'id': os.path.splitext(os.path.basename(file_path))[0],
                    'title': lesson.get('title', ''),
                })
    return jsonify(lessons)

@app.route('/api/lessons/<lesson_id>')
def get_lesson_by_id(lesson_id):
    lesson_dir = os.path.join(os.path.dirname(__file__), 'lessons')
    file_path = os.path.join(lesson_dir, f'{lesson_id}.py')
    if not os.path.exists(file_path):
        return jsonify({'error': 'Leçon non trouvée'}), 404
    lesson = load_lesson_from_file(file_path)
    if not lesson:
        return jsonify({'error': 'Leçon vide'}), 404
    return jsonify(lesson)

# === Lancement du serveur ===
if __name__ == '__main__':
    app.run(debug=True, port=5000)
