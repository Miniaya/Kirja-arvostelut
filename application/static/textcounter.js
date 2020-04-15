
var el;                                                    

function countCharacters(e) {                                    
  var textEntered, countRemaining, counter;          
  textEntered = document.getElementById('review').value;  
  counter = (400 - (textEntered.length));
  countRemaining = document.getElementById('charactersRemaining'); 
  countRemaining.textContent = counter;       
}

el = document.getElementById('review');                   
el.addEventListener('keyup', countCharacters, false);