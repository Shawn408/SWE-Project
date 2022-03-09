import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [review, setReview] = useState([]);
  useEffect(() => {
    fetch("/edit", { method: "POST" }).then((response) => 
      response.json().then((data) => { 
        setReview(data.review);
      })
    );
  })

  return (
    <div className="App">
      <h1>Your Reviews:</h1>
      <table>
        {review && review.map((review) => 
          <tr>
            <tb>{review.movie_id}</tb>
            <tb>{review.rating}</tb>
            <tb>{review.comment}</tb>
          </tr>
          )}
      </table>
    </div>
  );
}

export default App;
