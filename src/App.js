import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [review, setReview] = useState([]);
  useEffect(() => {
    fetch("/edit", { method: "POST" }).then((response) => 
      response.json().then((data) => { 
        setReview(data.review);
        console.log(data.review);
      })
    );
  })
  function handleDelete(id) {
    console.log(id);
    const newReview = review.filter(review => review.id !== id);
    setReview(newReview);
  }

return (
    <div className="App">
      <center>
        <h1>Your Reviews:</h1>
        <table>
          {review && review.map((review) => 
            <tr>
              <tb>{review.movie_id}</tb>&nbsp;
              <tb><input type="text" defaultValue={review.rating} size ="3"></input></tb>
              <tb><input type="text" defaultValue={review.comment}></input></tb>
              <tb><button onClick = {() => handleDelete(review.id)}>Delete</button></tb>
            </tr>
            )}
        </table>
      </center>
    </div>
  );
}

export default App;
