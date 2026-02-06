let h2 = document.querySelector('h2');

const minNum = 1 ;
const maxNum = 100 ;
const answer = Math.floor(Math.random() * (maxNum - minNum + 1))

let attempts = 0 ;
let guess ;
let running = true ;

while(running){
    guess = prompt(`Guess a number between ${minNum} and ${maxNum}`) ;
    guess = Number(guess) ;

    if(isNaN(guess)){
        alert('Invalid input. Please enter a number.');
    }else if (guess < minNum || guess > maxNum){
        alert('Please enter a valid Number');
    }else {
        attempts++;
        if(guess < answer){
            alert('Too low!');
        }else if(guess > answer) {
            alert('Too Hight');
        }else{
            alert(`CORRECT! The awnser was ${answer}. It took you ${attempts} attempts`);
            running = false ;
        }
    }
}