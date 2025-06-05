import React, { useState, useEffect } from "react";
import ReactMarkdown from "react-markdown";

const lessonsList = [
  { file: "variables.md", title: "Variables et Types" },
  { file: "conditions.md", title: "Conditions" },
  { file: "loops.md", title: "Boucles" },
  { file: "functions.md", title: "Fonctions" },
  { file: "lists.md", title: "Listes et Dictionnaires" },
  { file: "numpy.md", title: "Numpy" },
  { file: "pandas.md", title: "Pandas" },
  { file: "pandas_basics.md", title: "Pandas : Premiers pas" },
  { file: "scikit_learn.md", title: "Scikit-learn" },
  { file: "conclusion.md", title: "Conclusion & Astuces" },
];

const LessonPage = () => {
  const [selected, setSelected] = useState(0);
  const [content, setContent] = useState("");

  useEffect(() => {
    fetch(`/lessons/${lessonsList[selected].file}`)
      .then((res) => res.text())
      .then(setContent);
  }, [selected]);

  return (
    <div className="flex flex-col md:flex-row min-h-screen pt-24 pb-12">
      <aside className="md:w-1/4 w-full bg-dark-400 p-4 rounded-lg mb-4 md:mb-0 md:mr-8">
        <nav className="flex flex-row md:flex-col gap-2">
          {lessonsList.map((lesson, idx) => (
            <button
              key={lesson.file}
              className={`text-left px-4 py-2 rounded transition-colors w-full ${selected === idx ? "bg-primary text-white" : "bg-dark-300 text-neutral-200 hover:bg-dark-200"}`}
              onClick={() => setSelected(idx)}
            >
              {lesson.title}
            </button>
          ))}
        </nav>
      </aside>
      <main className="flex-1 bg-dark-500 p-6 rounded-lg overflow-x-auto">
        <ReactMarkdown className="prose prose-invert max-w-none">{content}</ReactMarkdown>
      </main>
    </div>
  );
};

export default LessonPage;
