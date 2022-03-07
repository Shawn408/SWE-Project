import './App.css';
import { useState } from 'react';

function App() {
  const [fact, setFact] = useState(" ");
  function handleClick() {
    fetch("/fact", { method: "POST" }).then((response) => 
      response.json().then((data) => { 
        setFact(data.fact);
        console.log(data.fact);
      })
    );
  }
  return (
    <div className="App">
      <h1>Fun Fact</h1>
      <p>{fact}</p>
      <button onClick={handleClick}>Click me!</button>
    </div>
  );
}

export default App;
