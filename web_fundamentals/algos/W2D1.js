var floor = Math.floor(1.8);
var ceiling = Math.ceil(Math.PI);
var random = Math.random();

console.log(floor);
console.log(ceiling);
console.log(random);


// dice roll

function d6(max) {
    var roll = Math.random();
    return Math.ceil(roll * (max));
}

var playerRoll = d6(6);
console.log("The player rolled: " + playerRoll);

// oracle

var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];

function oracle() {   
    var roll = Math.random();
    var spot = Math.ceil(roll * (lifesAnswers.length));
    return lifesAnswers[spot];
}

var playerShake = oracle();
console.log("The player shook: " + playerShake);

//use the length of the array as an idea for how to randomize within the array
//think of this like an 18 sided die