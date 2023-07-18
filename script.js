function checkAnswers() {
  let score = 0;
  let results = document.getElementById("results");
  
  // Check answer to question 1
  let answer1 = document.querySelector('input[name="question1"]:checked').value;
  if (answer1 === "DMCM") {
    score++;
  }
  
  // Check answer to question 2
  let answer2 = document.querySelector('input[name="question2"]:checked').value;
  if (answer2 === "TWT") {
    score++;
  }
  
  // Check answer to question 3
  let answer3 = document.querySelector('input[name="question3"]:checked').value;
  if (answer3 === "safe") {
    score++;
  }
  
  // Display results
  results.innerHTML = "<h3>You scored " + score + " out of 3!</h3>";
}