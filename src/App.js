import './App.css';
import { useState } from 'react';

function App() {
  const [review, setReview] = useState();
  const handleClick = () => {
    fetch("/edit")
      .then(response => response.json())
      .then(data => { console.log(data); });
  }   
    
  return (
    <div className="App">
      <h1>Your Reviews:</h1>

      <button onClick={handleClick}>Click me!</button>
    </div>
  );
}

export default App;