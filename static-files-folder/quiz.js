// function to calculate the result of the survey
function tabulateAnswers() {
    // initialize variables for each choice's score
    // If you add more choices and outcomes, you must add another variable here.
    var c1score = 0;
    var c2score = 0;
    var c3score = 0;
    var c4score = 0;
    
    // get a list of the radio inputs on the page
    var choices = document.getElementsByTagName('input');
    // loop through all the radio inputs
    for (i=0; i<choices.length; i++) {
      // if the radio is checked..
      if (choices[i].checked) {
        // add 1 to that choice's score
        if (choices[i].value == 'c1') {
          c1score = c1score + 1;
        }
        if (choices[i].value == 'c2') {
          c2score = c2score + 1;
        }
        if (choices[i].value == 'c3') {
          c3score = c3score + 1;
        }
        if (choices[i].value == 'c4') {
          c4score = c4score + 1;
        }
        // If you add more choices and outcomes, you must add another if statement below.
      }
    }
    
    // Find out which choice got the highest score.
    // If you add more choices and outcomes, you must add the variable here.
    var maxscore = Math.max(c1score,c2score,c3score,c4score);
    var level = 0;
    if(maxscore == 0){
        level = 0;
    }
    else{
        if(maxscore==c1score){
            level = 1;
        }
        if(maxscore==c2score){
            level = 2;
        }
        if(maxscore==c3score){
            level = 3;
        }
        if(maxscore==c4score){
            level = 4;
        }
    }
    
    // Display answer corresponding to that choice
    var answerbox = document.getElementById('answer');
    if(level == 0){
        answerbox.innerHTML = "Please take the quiz to get your mood score!"
    }
    if(level == 1){
        answerbox.innerHTML = "Trust me, everything will be okay. Smile!"
    }
    if(level == 2){
        answerbox.innerHTML = "Don't worry and look ahead!"
    }
    if(level == 3){
        answerbox.innerHTML = "Keep up the mood! Have a great day!"
    }
    if(level == 4){
        answerbox.innerHTML = "Wow you feel really good today! Keep up!"
    }

    setTimeout(()=>{
        window.location.href="/s/chart.html"
    },3000)
  }
  