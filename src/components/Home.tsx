
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="min-h-screen pt-24 pb-12">
      <div className="container-padding mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-6xl font-bold mb-4 text-white">
            <span className="text-primary">Py</span>Learn
          </h1>
          <p className="text-xl text-neutral-300 max-w-3xl mx-auto">
            Apprenez Python de manière interactive avec des exercices pratiques et un retour immédiat
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <div className="glass-card p-6 rounded-lg">
            <div className="text-3xl text-primary mb-4">📝</div>
            <h3 className="text-xl font-semibold mb-2 text-white">Exercices progressifs</h3>
            <p className="text-neutral-300">Des exercices variés pour améliorer vos compétences Python étape par étape</p>
          </div>
          
          <div className="glass-card p-6 rounded-lg">
            <div className="text-3xl text-primary mb-4">💻</div>
            <h3 className="text-xl font-semibold mb-2 text-white">Éditeur intégré</h3>
            <p className="text-neutral-300">Un éditeur de code Python avec coloration syntaxique et autocomplétion</p>
          </div>
          
          <div className="glass-card p-6 rounded-lg">
            <div className="text-3xl text-primary mb-4">📊</div>
            <h3 className="text-xl font-semibold mb-2 text-white">Suivi de progression</h3>
            <p className="text-neutral-300">Suivez votre progression et visualisez vos accomplissements</p>
          </div>
        </div>
        
        <div className="flex flex-col md:flex-row justify-center gap-4 items-center">
          <Link 
            to="/exercises" 
            className="px-6 py-3 bg-primary text-white rounded-lg hover:bg-accent transition-colors"
          >
            Commencer les exercices
          </Link>
          <Link 
            to="/progress" 
            className="px-6 py-3 bg-dark-300 text-white rounded-lg hover:bg-dark-200 transition-colors"
          >
            Voir ma progression
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
