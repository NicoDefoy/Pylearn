import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';

interface Exercise {
  id: string;
  theme: string;
  instruction: string;
  level: number;
  title?: string;
}

const themeColors: Record<string, string> = {
  variables: 'bg-purple-300 text-gray-900',
  functions: 'bg-indigo-300 text-gray-900',
  loops: 'bg-orange-300 text-gray-900',
  conditions: 'bg-emerald-300 text-gray-900',
  lists: 'bg-pink-300 text-gray-900',
  dictionaries: 'bg-rose-300 text-gray-900',
  pandas_basics: 'bg-yellow-300 text-gray-900',
  numpy_basics: 'bg-indigo-200 text-gray-900',
  sets_tuples: 'bg-teal-300 text-gray-900',
  files_exceptions: 'bg-red-300 text-gray-900',
  classes: 'bg-cyan-200 text-gray-900',
  scikit_learn: 'bg-fuchsia-300 text-gray-900',
  env_imports: 'bg-lime-300 text-gray-900',
  strings: 'bg-blue-200 text-gray-900',
};

const capitalize = (word: string) =>
  word.charAt(0).toUpperCase() + word.slice(1).replaceAll('_', ' ');

export default function ExerciseList() {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const { theme } = useParams<{ theme?: string }>();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const url = theme
          ? `http://localhost:5000/api/exercises/${theme}`
          : 'http://localhost:5000/api/exercises';

        const res = await fetch(url);
        const data = await res.json();
        setExercises(data);
      } catch (err) {
        console.error('Erreur chargement exercices', err);
      }
    };

    fetchData();
  }, [theme]);

  if (!theme) {
    // Affichage des THÈMES
    const uniqueThemes = Array.from(new Set(exercises.map((ex) => ex.theme)));

    return (
      <div className="p-8">
        <h1 className="text-3xl font-bold mb-6 text-white">Choisis un thème</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {uniqueThemes.map((theme) => (
            <div
              key={theme}
              className={`rounded-lg p-6 cursor-pointer hover:scale-[1.02] transition shadow-md ${
                themeColors[theme] || 'bg-gray-200 text-gray-900'
              }`}
              onClick={() => navigate(`/exercises/${theme}`)}
            >
              <h2 className="text-xl font-semibold">{capitalize(theme)}</h2>
              <p className="text-sm opacity-80 mt-2">
                Voir les exercices sur {capitalize(theme)}
              </p>
            </div>
          ))}
        </div>
      </div>
    );
  }

  // Affichage des EXERCICES pour un thème donné
  return (
    <div className="p-6 text-white">
      <h1 className="text-3xl font-bold mb-6">Exercices : {capitalize(theme)}</h1>
      <div className="space-y-4">
        {exercises.map((exercise) => (
          <div
            key={exercise.id}
            onClick={() => navigate(`/exercises/${theme}/${exercise.id}`)}
            className="bg-gray-800 p-4 rounded-lg shadow-md cursor-pointer hover:bg-gray-700 transition-all"
          >
            <h2 className="text-xl font-semibold">{exercise.title}</h2>
            <p className="mt-1">{exercise.instruction}</p>
            <p className="mt-2 italic text-sm text-gray-400">Niveau : {exercise.level}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
