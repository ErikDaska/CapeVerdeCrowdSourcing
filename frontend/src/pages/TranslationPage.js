import styles from './TranslationPage.css';
import React, { useState } from "react";


// Alterar isto para um ficheiro.json
const frasesAleatorias = [
  "How are you?",
  "Good morning!",
  "What is your name?",
  "Where are you from?",
  "I love Cape Verde!"
];


export default function TranslationPage() {
    const [frase, setFrase] = useState("");
  const [traducao, setTraducao] = useState("");

  // Função para gerar uma frase aleatória
  const gerarFrase = () => {
    const randomIndex = Math.floor(Math.random() * frasesAleatorias.length);
    setFrase(frasesAleatorias[randomIndex]);
    setTraducao("");
  };

  // Função para atualizar a tradução
  const handleTraducaoChange = (event) => {
    setTraducao(event.target.value);
  };

  const handleSubmit = () => {
    alert(`Obrigado pelo seu contributo`);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Traduza para o crioulo de Cabo Verde</h1>
      </header>
      <main>
        <div className="frase-container">
          <button onClick={gerarFrase}>Gerar frase</button>
          {frase && <p className="frase">Frase: "{frase}"</p>}
        </div>
        {frase && (
          <div className="traducao-container">
            <textarea
              placeholder="Escreva sua tradução aqui..."
              value={traducao}
              onChange={handleTraducaoChange}
            />
            <button onClick={handleSubmit}>Enviar Tradução</button>
          </div>
        )}
      </main>
    </div>
  );
}
