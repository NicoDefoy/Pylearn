import { useState, useEffect } from 'react';
import CodeEditor from './CodeEditor';
import { useParams, useNavigate } from 'react-router-dom';

interface ExerciseData {
  id: string;
  title: string;
  instruction: string;
  initial_code: string;
  expected_output: string;
  hint?: string;
  solution_code?: string;
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
  const [showHint, setShowHint] = useState(false);
  const [showSolution, setShowSolution] = useState(false);

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

          // Réinitialisation des états visuels à chaque nouvel exercice
          setResult('');
          setFeedback('');
          setFeedbackColor('text-white');
          setCompleted(false);
          setShowHint(false);
          setShowSolution(false);
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
        setFeedback("✅ Bravo, c'est tout bon !");
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
      setFeedback("❌ Erreur lors de l'execution.");
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

      <div className="flex flex-row items-center gap-4 mt-4">
        <button
          className="px-4 py-2 bg-indigo-500 text-white rounded hover:bg-indigo-600"
          onClick={handleRunCode}
        >
          Exécuter le code
        </button>
        {!showHint && (
          <button
            className="px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600"
            onClick={() => setShowHint(true)}
          >
            Aide
          </button>
        )}
        {!showSolution && (
          <button
            className="px-4 py-2 bg-orange-500 text-white rounded hover:bg-orange-600"
            onClick={() => setShowSolution(true)}
          >
            Voir le code attendu
          </button>
        )}
      </div>

      {showHint && (
        <div className="mt-6 bg-yellow-900/80 p-4 rounded border border-yellow-400">
          <p className="font-semibold text-yellow-200 mb-1">Indice :</p>
          <pre className="text-yellow-100 whitespace-pre-wrap">{exercise.hint || '(Pas d\'indice renseigné)'}</pre>
        </div>
      )}

      {showSolution && (
        <div className="mt-6 bg-orange-900/80 p-4 rounded border border-orange-400">
          <p className="font-semibold text-orange-200 mb-1">Code attendu :</p>
          <pre className="text-orange-100 whitespace-pre-wrap mb-2">{exercise.solution_code || '(Pas de code de solution renseigné)'}</pre>
          <p className="font-semibold text-orange-200 mb-1">Résultat attendu :</p>
          <pre className="text-orange-100 whitespace-pre-wrap">{exercise.expected_output || '(Pas de résultat attendu renseigné)'}</pre>
        </div>
      )}

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
