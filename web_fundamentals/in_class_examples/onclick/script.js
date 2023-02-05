console.log("Hello from the console!")

function alertmsg(message){
    alert(message);
}

function thisEL(element){
    console.log(element.innerText);
    element.innerText = 'Meep is the best meep!'
}

function turnOff(element) {
    element.innerText = "Off";
}

function matt(element){
    element.src = 'https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1f60d.png'
}