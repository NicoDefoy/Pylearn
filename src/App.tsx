import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";

import Header from "./components/Header";
import Home from "./components/Home";
import ExerciseList from "./components/ExerciseList";
import ThemeExercises from "./components/ThemeExercises";
import Exercise from "./components/Exercise";
import ProgressTracker from "./components/ProgressTracker";
import LessonList from "./components/LessonList";
import LessonDetail from "./components/LessonDetail";

// Type pour les exercices (ajustable selon structure réelle)
interface ExerciseType {
  id: string;
  theme: string;
  title: string;
  instruction: string;
  level: number;
  example: string;
  expected_output?: string;
}

const queryClient = new QueryClient();

const App = () => {
  const [selectedExercise, setSelectedExercise] = useState<ExerciseType | null>(null);
  const [exercises, setExercises] = useState<ExerciseType[]>([]);

  // Charger les exercices depuis localStorage au démarrage (optionnel)
  useEffect(() => {
    const saved = localStorage.getItem("exercises");
    if (saved) {
      setExercises(JSON.parse(saved));
    }
  }, []);

  const handleSelectExercise = (exercise: ExerciseType) => {
    setSelectedExercise(exercise);
  };

  const handleCompleteExercise = (id: string) => {
    const updated = exercises.map((ex) =>
      ex.id === id ? { ...ex, completed: true } : ex
    );
    setExercises(updated);
    localStorage.setItem("exercises", JSON.stringify(updated));
    setSelectedExercise(null);
  };

  const handleBackToList = () => {
    setSelectedExercise(null);
  };

  // Page des exercices simples
  const ExercisesPage = () => (
    <div className="min-h-screen pt-24 pb-12">
      <div className="container-padding mx-auto">
        {selectedExercise ? (
          <Exercise
            exercise={selectedExercise}
            onComplete={handleCompleteExercise}
            onBack={handleBackToList}
          />
        ) : (
          <ExerciseList onSelectExercise={handleSelectExercise} />
        )}
      </div>
    </div>
  );

  // Page des thèmes (avec navigation vers exercices par URL)
  const ThemePage = () => (
    <div className="min-h-screen pt-24 pb-12">
      <div className="container-padding mx-auto">
        <ThemeExercises />
      </div>
    </div>
  );

  const ProgressPage = () => (
    <div className="min-h-screen pt-24 pb-12">
      <div className="container-padding mx-auto">
        <ProgressTracker />
      </div>
    </div>
  );

  return (
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        <Toaster />
        <Sonner />
        <BrowserRouter>
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/exercises" element={<ExercisesPage />} />
            <Route path="/exercises/:theme" element={<ThemePage />} />
            <Route path="/exercises/:theme/:id" element={<Exercise />} />
            <Route path="/progress" element={<ProgressPage />} />
            <Route path="/lesson" element={<LessonList />} />
<Route path="/lesson/:id" element={<LessonDetail />} />
          </Routes>
        </BrowserRouter>
      </TooltipProvider>
    </QueryClientProvider>
  );
};

export default App;
