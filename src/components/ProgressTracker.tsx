
import { useState, useEffect } from 'react';

interface Exercise {
  id: number;
  title: string;
  description: string;
  initialCode: string;
  difficulty: 'easy' | 'medium' | 'hard';
  completed: boolean;
}

const ProgressTracker = () => {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const [solutions, setSolutions] = useState<Record<number, string>>({});

  useEffect(() => {
    // Charger les exercices et les solutions
    const savedExercises = localStorage.getItem('exercises');
    const savedSolutions = localStorage.getItem('solutions');
    
    if (savedExercises) {
      setExercises(JSON.parse(savedExercises));
    }
    
    if (savedSolutions) {
      setSolutions(JSON.parse(savedSolutions));
    }
  }, []);

  const resetProgress = () => {
    if (confirm('Êtes-vous sûr de vouloir réinitialiser votre progression? Cette action ne peut pas être annulée.')) {
      const resetExercises = exercises.map(ex => ({...ex, completed: false}));
      setExercises(resetExercises);
      setSolutions({});
      
      localStorage.setItem('exercises', JSON.stringify(resetExercises));
      localStorage.setItem('solutions', JSON.stringify({}));
    }
  };

  // Calculer les statistiques
  const totalExercises = exercises.length;
  const completedExercises = exercises.filter(ex => ex.completed).length;
  const completionPercentage = totalExercises > 0 
    ? Math.round((completedExercises / totalExercises) * 100) 
    : 0;

  return (
    <div className="py-8">
      <h2 className="text-2xl font-semibold mb-6 text-white">Votre Progression</h2>
      
      <div className="glass-card p-6 rounded-lg mb-8">
        <div className="flex flex-col md:flex-row justify-between items-center mb-6">
          <div>
            <h3 className="text-lg font-medium text-white">Progression globale</h3>
            <p className="text-neutral-300 text-sm">Continuez à pratiquer pour améliorer vos compétences</p>
          </div>
          <div className="text-3xl font-bold text-primary mt-4 md:mt-0">
            {completionPercentage}%
          </div>
        </div>
        
        {/* Barre de progression */}
        <div className="w-full bg-dark-500 rounded-full h-4 mb-6">
          <div 
            className="bg-primary h-4 rounded-full"
            style={{ width: `${completionPercentage}%` }}
          ></div>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
          <div className="glass-card p-4 rounded-lg">
            <div className="text-2xl font-bold text-white">{totalExercises}</div>
            <div className="text-neutral-300 text-sm">Exercices totaux</div>
          </div>
          <div className="glass-card p-4 rounded-lg">
            <div className="text-2xl font-bold text-white">{completedExercises}</div>
            <div className="text-neutral-300 text-sm">Exercices terminés</div>
          </div>
          <div className="glass-card p-4 rounded-lg">
            <div className="text-2xl font-bold text-white">{totalExercises - completedExercises}</div>
            <div className="text-neutral-300 text-sm">Exercices restants</div>
          </div>
        </div>
      </div>
      
      <h3 className="text-xl font-medium mb-4 text-white">Détails des exercices</h3>
      <div className="space-y-4">
        {exercises.map(exercise => (
          <div key={exercise.id} className="glass-card p-4 rounded-lg">
            <div className="flex justify-between items-center">
              <h4 className="font-medium text-white">{exercise.title}</h4>
              {exercise.completed ? (
                <span className="text-xs bg-green-800/20 text-green-400 px-2 py-1 rounded-full">
                  Complété
                </span>
              ) : (
                <span className="text-xs bg-yellow-800/20 text-yellow-400 px-2 py-1 rounded-full">
                  En cours
                </span>
              )}
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-8 flex justify-end">
        <button 
          onClick={resetProgress}
          className="px-4 py-2 bg-red-900/20 text-red-400 rounded-lg hover:bg-red-800/30 transition-colors"
        >
          Réinitialiser la progression
        </button>
      </div>
    </div>
  );
};

export default ProgressTracker;
