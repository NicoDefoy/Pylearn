import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

interface Lesson {
  title: string;
  description: string;
  examples: { code: string; explanation: string }[];
  tips?: string[];
  common_mistakes?: string[];
}

// Fonction pour remplacer les guillemets typographiques par des guillemets droits
function sanitizeQuotes(text: string) {
  return text
    .replace(/[‘’]/g, "'")
    .replace(/[“”]/g, '"');
}

// Ajoute un saut de ligne après chaque point de liste pour aérer
function addListSpacing(text: string) {
  return text.replace(/(\n- [^\n]+)/g, '$1\n');
}

// Utilitaire pour découper la description en blocs pédagogiques
function parseDescriptionBlocks(description: string) {
  // On découpe par titres ### (Markdown)
  const blocks = description.split(/### /g).filter(Boolean);
  return blocks.map((block) => {
    // Le premier mot jusqu'à la fin de la ligne est le titre du bloc
    const [titleLine, ...rest] = block.split('\n');
    const title = sanitizeQuotes(titleLine.trim());
    let content = rest.join('\n').trim();
    // Nettoyage : retire les ** gras Markdown et les # inutiles (hors code)
    content = sanitizeQuotes(content.replace(/\*\*/g, ''));
    // On ne garde les # que dans les blocs "Exemples" ou "code"
    if (!title.toLowerCase().includes('exemple') && !title.toLowerCase().includes('code')) {
      content = content.replace(/^# ?/gm, '');
      // Ajoute de l'aération pour les listes
      content = addListSpacing(content);
    }
    return { title, content };
  });
}

export default function LessonDetail() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [lesson, setLesson] = useState<Lesson | null>(null);

  useEffect(() => {
    fetch(`http://localhost:5000/api/lessons/${id}`)
      .then((res) => res.json())
      .then(setLesson)
      .catch((err) => console.error('Erreur chargement leçon', err));
  }, [id]);

  if (!lesson) return <div className="text-white p-6">Chargement...</div>;

  // On découpe la description en blocs pédagogiques
  const blocks = parseDescriptionBlocks(lesson.description);

  // Pour éviter les doublons d'encadrés Astuce/Erreur fréquente
  const hasTipBlock = blocks.some(b => b.title.toLowerCase().includes('astuce'));
  const hasMistakeBlock = blocks.some(b => b.title.toLowerCase().includes('erreur'));

  // Icônes pédagogiques par type de bloc
  const blockIcons: Record<string, string> = {
    "Qu'est-ce qu'une variable ?": 'ℹ️',
    'Comment créer une variable ?': '📝',
    'Les types de valeurs (expliqué simplement)': '📦',
    'Exemples': '▶️',
    'Afficher une variable': '👀',
    "Changer la valeur d'une variable": '🔄',
    'Règles pour nommer une variable': '📏',
    'Astuces': '💡',
    'Erreurs fréquentes': '⚠️',
  };

  // Couleurs par type de bloc
  const blockColors: Record<string, string> = {
    "Qu'est-ce qu'une variable ?": 'bg-blue-900/80 border-blue-400',
    'Comment créer une variable ?': 'bg-indigo-900/80 border-indigo-400',
    'Les types de valeurs (expliqué simplement)': 'bg-purple-900/80 border-purple-400',
    'Exemples': 'bg-green-900/80 border-green-400',
    'Afficher une variable': 'bg-cyan-900/80 border-cyan-400',
    "Changer la valeur d'une variable": 'bg-yellow-900/80 border-yellow-400',
    'Règles pour nommer une variable': 'bg-orange-900/80 border-orange-400',
    'Astuces': 'bg-blue-900/80 border-blue-400',
    'Erreurs fréquentes': 'bg-red-900/80 border-red-400',
  };

  return (
    <div className="p-8 text-white max-w-3xl mx-auto">
      <button onClick={() => navigate(-1)} className="mb-4 text-indigo-400 hover:underline">← Retour</button>
      <h2 className="text-3xl font-bold mb-8 text-primary">{sanitizeQuotes(lesson.title)}</h2>
      <div className="space-y-6">
        {blocks.map((block, idx) => (
          <div
            key={idx}
            className={`p-5 rounded-lg border-l-8 shadow-md ${blockColors[block.title] || 'bg-dark-400 border-dark-300'}`}
          >
            <div className="flex items-center mb-2">
              <span className="text-2xl mr-2">{blockIcons[block.title] || 'ℹ️'}</span>
              <span className="text-xl font-semibold text-white">{block.title}</span>
            </div>
            <div className="whitespace-pre-line text-base text-white/90 leading-relaxed">{block.content}</div>
          </div>
        ))}
      </div>
      {lesson.examples && lesson.examples.length > 0 && (
        <div className="mt-10 mb-8">
          <h3 className="text-2xl font-semibold mb-4 text-secondary">Exemples</h3>
          {lesson.examples.map((ex, idx) => (
            <div key={idx} className="mb-6 bg-gray-900 p-4 rounded-lg border-l-4 border-green-400">
              <pre className="bg-gray-800 p-3 rounded text-green-300 mb-2 overflow-x-auto whitespace-pre-wrap font-mono text-base">{sanitizeQuotes(ex.code)}</pre>
              <p className="text-sm text-gray-200 italic">{sanitizeQuotes(ex.explanation)}</p>
            </div>
          ))}
        </div>
      )}
      {!hasTipBlock && lesson.tips && lesson.tips.length > 0 && (
        <div className="mt-8 bg-blue-900/80 p-4 rounded border-l-4 border-blue-400">
          <h4 className="font-semibold text-blue-200 mb-2">Astuce</h4>
          <ul className="list-disc ml-6">
            {lesson.tips.map((tip, idx) => (
              <li key={idx} className="text-blue-100 text-base">{sanitizeQuotes(tip)}</li>
            ))}
          </ul>
        </div>
      )}
      {!hasMistakeBlock && lesson.common_mistakes && lesson.common_mistakes.length > 0 && (
        <div className="mt-8 bg-red-900/80 p-4 rounded border-l-4 border-red-400">
          <h4 className="font-semibold text-red-200 mb-2">Erreurs fréquentes</h4>
          <ul className="list-disc ml-6">
            {lesson.common_mistakes.map((err, idx) => (
              <li key={idx} className="text-red-100 text-base">{sanitizeQuotes(err)}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
