// WEATHER API - FIX LAT, LON, and DATE
var API_KEY = "6f9811d2decaf213baf769b6f347fcd5"

function getWeather(event, index, weatherLocation){
    event.preventDefault()
    // var weatherDate = document.querySelector("#weatherDate").value
    // var weatherLocation = document.querySelector("#weatherLocation").innerText
    var results = document.getElementById("results."+index+"."+weatherLocation)
    var button = document.getElementById("button."+index+"."+weatherLocation)
    button.style.display = "none"
    console.log(weatherLocation)

    fetch("http://api.openweathermap.org/data/2.5/weather?q=" + weatherLocation + "&units=imperial&appid=" + API_KEY)
    .then(function(someServerResponse){
        // console.log(someServerResponse)
        return someServerResponse.json()
    })
    .then(function(data){
        console.log(data)
        console.log(results)
        results.innerHTML = `
            <p>${data.main.temp} °f  -   ${data.weather[0].description}</p>
        `
    })
    .catch(function(err){
        console.log("We have a problem", err)
        results.innerHTML = `
        <h3>Sorry, no weather was captured on this day.</h3>
        `
    })

}



// axios.get("http://api.openweathermap.org/data/2.5/weather?q=" + input + "&units=imperial&appid=" + API_KEY)
// .then(res => {
//     console.log(res.data);
//     const API_RES = res.data;
//     // set temperature
//     setFdeg(Math.round(API_RES.main.temp));
//     // set name
//     setName(API_RES.name);
//     // set weather description
//     setDesc(API_RES.weather[0].description);
//     // set LAT
//     setCoordLat(API_RES.coord.lat);
//     // set LON
//     setCoordLon(API_RES.coord.lon);
//     // set icon
//     setIcon(API_RES.weather[0].icon);

// })
// .catch(err => {
//     console.log(err);
//     setName("");
// })


