// LOCATION API

var results = document.getElementById("results")

function getLocation(event){
    event.preventDefault()
    var location = document.querySelector("#location").value
    // console.log(weatherDate)
    // console.log(event)
    fetch(`https://maps.googleapis.com/maps/api/place/autocomplete/json
    ?input=${location}
    &radius=500
    &types=establishment
    &key=AIzaSyCzpMpLO5OPd-AA37z3TM1sPuvt49EZC0s
    `)
    .then(function(someServerResponse){
        // console.log(someServerResponse)
        return someServerResponse.json()
    })
    .then(function(data){
        results.innerHTML = `
            <h3>${data.description}</h3>
        `
    })
    .catch(function(err){
        console.log("We have a problem", err)
        results.innerHTML = `
        <h3>Sorry, no location is found.</h3>
        `

    })
}




