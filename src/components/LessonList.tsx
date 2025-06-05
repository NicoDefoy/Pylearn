import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface LessonMeta {
  id: string;
  title: string;
}

export default function LessonList() {
  const [lessons, setLessons] = useState<LessonMeta[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('http://localhost:5000/api/lessons')
      .then((res) => res.json())
      .then(setLessons)
      .catch((err) => console.error('Erreur chargement leçons', err));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6 text-white">Choisis une leçon</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {lessons.map((lesson) => (
          <div
            key={lesson.id}
            className="rounded-lg p-6 cursor-pointer hover:scale-[1.02] transition shadow-md bg-indigo-300 text-gray-900"
            onClick={() => navigate(`/lesson/${lesson.id}`)}
          >
            <h2 className="text-xl font-semibold">{lesson.title}</h2>
            <p className="text-sm opacity-80 mt-2">Voir la leçon sur {lesson.title}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
