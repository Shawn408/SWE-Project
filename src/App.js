import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [review, setReview] = useState([]);
  const [delreview, setDelete] = useState([]);
  useEffect(() => {
    fetch("/edit", { method: "POST" }).then((response) => 
      response.json().then((data) => { 
        setReview(data.review);
      })
    );
  })
function handleDelete(id) {
  fetch(`/edit/${id}`, { method: "POST" }).then((response) => 
    response.json().then((data) => { 
      setDelete(data.delreview);
    })
  );
}

function Button(props) {
  return (
    <button onClick={() => handleDelete(props.id)}>Delete</button>
  );
}
 
return (
    <div className="App">
      <h1>Your Reviews:</h1>
      <table>
        {review && review.map((review) => 
          <tr>
            <tb>{review.movie_id}</tb>&nbsp;
            <tb>{review.rating}</tb>&nbsp;
            <tb>{review.comment}</tb>
            <Button id={review.id} />
          </tr>
          )}
      </table>
    </div>
  );
}

export default App;
