import { Menu, X } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router-dom";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-dark-500/90 backdrop-blur-lg border-b border-dark-300">
      <nav className="container-padding mx-auto flex h-16 items-center justify-between">
        <Link to="/" className="text-xl font-semibold text-white">
          <span className="text-primary">Py</span>Learn
        </Link>
        
        <div className="hidden md:flex items-center gap-8">
          <Link to="/" className="text-neutral-400 hover:text-primary transition-colors">
            Accueil
          </Link>
          <Link to="/exercises" className="text-neutral-400 hover:text-primary transition-colors">
            Exercices
          </Link>
          <Link to="/progress" className="text-neutral-400 hover:text-primary transition-colors">
            Progression
          </Link>
          <Link to="/lesson" className="text-neutral-400 hover:text-primary transition-colors">
            Leçon
          </Link>
        </div>

        <button 
          className="md:hidden text-white"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          {isMenuOpen ? <X /> : <Menu />}
        </button>
      </nav>

      {isMenuOpen && (
        <div className="md:hidden absolute top-16 left-0 right-0 bg-dark-500/90 backdrop-blur-lg border-b border-dark-300">
          <div className="container-padding py-4 flex flex-col gap-4">
            <Link to="/" className="text-neutral-400 hover:text-primary transition-colors">
              Accueil
            </Link>
            <Link to="/exercises" className="text-neutral-400 hover:text-primary transition-colors">
              Exercices
            </Link>
            <Link to="/progress" className="text-neutral-400 hover:text-primary transition-colors">
              Progression
            </Link>
            <Link to="/lesson" className="text-neutral-400 hover:text-primary transition-colors">
              Leçon
            </Link>
          </div>
        </div>
      )}
    </header>
  );
};

export default Header;
