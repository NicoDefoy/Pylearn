import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

interface ExerciseType {
  id: string;
  title: string;
  instruction: string;
  level: number;
  theme: string;
}

export default function ThemeExercises() {
  const { theme } = useParams();
  const [exercises, setExercises] = useState<ExerciseType[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://localhost:5000/api/exercises")
      .then((res) => res.json())
      .then((data) => {
        const filtered = data.filter(
          (exercise: ExerciseType) => exercise.theme === theme
        );
        setExercises(filtered);
      });
  }, [theme]);

  return (
    <div className="p-8 text-white">
      <h1 className="text-3xl font-bold mb-6">
        Exercices : {theme?.toUpperCase()}
      </h1>

      <div className="space-y-4">
        {exercises.map((ex) => (
          <div
            key={ex.id}
            className="bg-zinc-800 p-4 rounded hover:bg-zinc-700 cursor-pointer"
            onClick={() => navigate(`/exercises/${theme}/${ex.id}`)}
          >
            <h2 className="font-semibold text-lg">{ex.title}</h2>
            <p className="text-sm mt-1 opacity-80">{ex.instruction}</p>
            <p className="text-xs italic mt-2">Niveau : {ex.level}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
