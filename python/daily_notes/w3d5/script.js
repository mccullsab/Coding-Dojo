
// function doStuff(){
//     console.log("I clicked a button")
// }

var BASE_URL = "https://akabab.github.io/superhero-api/api/id/"

function getHero(event){
    event.preventDefault()
    var HeroId = document.querySelector("#heroNum").value
    console.log(HeroId)
    // console.log(event)
    fetch(BASE_URL + HeroId + ".json")
    .then(function(someServerResponse){
        // console.log(someServerResponse)
        return someServerResponse.json()
    })
    .then(function(data){
        console.log(data.images.md)
        results.innerHTML = `
            <h3>${data.name}</h3>
            <img src="${data.images.md}" alt="">
        `
    })
    .catch(function(err){
        console.log("We have a problem", err)
        results.innerHTML = `
        <h4>Check your location.</h4>
        `

    })
}

var results = document.getElementById("results")









//https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid=6f9811d2decaf213baf769b6f347fcd5

