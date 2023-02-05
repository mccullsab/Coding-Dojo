function dismiss() {
    document.querySelector('.cookieContainer').remove();
}


// temperature testing below

function farConvert() {
    for (var i = 1; i <= 8; i++) {
        var convertTemp = Number(document.querySelector('#temp' + i).innerText)
        convertTemp = Math.round((convertTemp * (9 / 5)) + 32)
        document.querySelector('#temp' + i).innerText = convertTemp
    }
}

// function farConvert(){
    // document.querySelector('.high1').innerText = "75°"
    // document.querySelector('.high2').innerText = "80°"
    // document.querySelector('.high3').innerText = "69°"
    // document.querySelector('.high4').innerText = "78°"
    // document.querySelector('.low1').innerText = "65°"
    // document.querySelector('.low2').innerText = "66°"
    // document.querySelector('.low3').innerText = "61°"
    // document.querySelector('.low4').innerText = "70°"