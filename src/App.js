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
  },[setReview])
  
  function handleDelete(id) {
    const newReview = review.filter((review) => review.id !== id);
    setReview(newReview);
  }

  function handleEdit(e){
    const newRating = e.target.rating.value;
    const newReview = review.map((review) => {
      if(review.id === e.target.id.defaultValue){
        newRating = review.rating;
      }
      return review;
    }
    );
    setReview(newReview);
  }
  
  function saveChange(stateData){
    fetch("/save", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
        },
        body: JSON.stringify(stateData)
      })
      .then((response) => {return response.json()})
      .then(alert("Save Successfully"))
  }

return (
    <div className="App">
      <center>
        <h1>Your Reviews:</h1>
        <table>
          {review && review.map((review) => 
            <tr>
              <td>{review.movie_id}</td>&nbsp;
              <td><input type="number" defaultValue={review.rating}></input></td>
              <td><input type="text" defaultValue={review.comment}></input></td>
              <td><button onClick = {() => handleDelete(review.id)}>Delete</button></td>
            </tr>
          )}
        </table>
        <button onClick = {() => saveChange(review)}>Save</button>
      </center>
    </div>
  );
}

export default App;
