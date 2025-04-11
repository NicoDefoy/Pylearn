import { useState, useEffect } from 'react';
import CodeEditor from './CodeEditor';
import { useParams, useNavigate } from 'react-router-dom';

interface ExerciseData {
  id: string;
  title: string;
  instruction: string;
  initial_code: string;
  expected_output: string;
}

export default function Exercise() {
  const { theme, id } = useParams();
  const navigate = useNavigate();
  const [exercise, setExercise] = useState<ExerciseData | null>(null);
  const [code, setCode] = useState('');
  const [result, setResult] = useState('');
  const [feedback, setFeedback] = useState('');
  const [feedbackColor, setFeedbackColor] = useState('text-white');
  const [completed, setCompleted] = useState(false);
  const [themeExercises, setThemeExercises] = useState<ExerciseData[]>([]);

  useEffect(() => {
    fetch(`http://localhost:5000/api/exercises/${theme}`)
      .then((res) => res.json())
      .then((data: ExerciseData[]) => {
        console.log("💡 Data brute reçue :", JSON.stringify(data, null, 2)); // 🕵️ Log pour vérification

        setThemeExercises(data);
        const ex = data.find((e) => e.id === id);
        if (ex) {
          setExercise(ex);

          setCode((current) => {
            const isNewExercise = exercise?.id !== ex.id;
            const isEmpty = current.trim() === '' || current === code;
            if (isNewExercise || isEmpty) {
              return ex.initial_code || '';
            }
            return current;
          });
        }
      })
      .catch((err) => console.error('Erreur chargement exercice', err));
  }, [id, theme]);

  const handleCodeChange = (value: string) => {
    setCode(value);
  };

  const handleRunCode = async () => {
    try {
      const res = await fetch('http://localhost:5000/api/execute', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          code,
          expected_output: exercise?.expected_output || ''
        }),
      });

      const data = await res.json();
      setResult(data.output || '');
      const matchType = data.match;

      if (matchType === 'exact') {
        setFeedback('✅ Bravo, c’est tout bon !');
        setFeedbackColor('text-green-400');
        setCompleted(true);

        const completedList = JSON.parse(localStorage.getItem('completed') || '[]');
        if (!completedList.includes(exercise!.id)) {
          completedList.push(exercise!.id);
          localStorage.setItem('completed', JSON.stringify(completedList));
        }

      } else if (matchType === 'close') {
        setFeedback('🟡 Tu y es presque ! Vérifie bien les retours à la ligne, ponctuation ou les espaces.');
        setFeedbackColor('text-yellow-400');

      } else {
        setFeedback('❌ Essaie encore, tu peux le faire !');
        setFeedbackColor('text-red-400');
      }

    } catch (err) {
      setFeedback('❌ Erreur lors de l’exécution.');
      setFeedbackColor('text-red-400');
    }
  };

  const goToNextExercise = () => {
    if (!exercise) return;

    const currentIndex = themeExercises.findIndex((e) => e.id === exercise.id);
    const next = themeExercises[currentIndex + 1];

    if (next) {
      navigate(`/exercises/${theme}/${next.id}`);
    } else {
      navigate('/exercises');
    }
  };

  if (!exercise) return <div className="text-white p-6">Chargement...</div>;

  const isLastExercise = themeExercises[themeExercises.length - 1]?.id === exercise.id;

  return (
    <div className="p-8 text-white">
      <h2 className="text-xl font-semibold mb-2">{exercise.title}</h2>
      <p className="text-md mb-6 text-white/90 whitespace-pre-wrap">{exercise.instruction}</p>

      <CodeEditor initialCode={code} onCodeChange={handleCodeChange} />

      <button
        className="mt-4 px-4 py-2 bg-indigo-500 text-white rounded hover:bg-indigo-600"
        onClick={handleRunCode}
      >
        Exécuter le code
      </button>

      {result && (
        <div className="mt-6 bg-slate-800 p-4 rounded">
          <p className="font-semibold text-white">Résultat :</p>
          <pre className="text-green-300 whitespace-pre-wrap">{result}</pre>
        </div>
      )}

      {feedback && (
        <div className={`mt-4 text-lg font-medium ${feedbackColor}`}>
          {feedback}
        </div>
      )}

      {completed && (
        <button
          className="mt-6 px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
          onClick={goToNextExercise}
        >
          {isLastExercise ? '✅ Terminé' : '➡️ Exercice suivant'}
        </button>
      )}
    </div>
  );
}
