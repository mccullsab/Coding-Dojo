console.log('script online!')

// API (Application programing interface)

var pokeDiv = document.querySelector('#pokemonData')
var pokesearch = document.querySelector('#pokeSearch')

async function getPokeData() {
    // asynch is a decorator to decleare the function is asynch and to awai 
    var response = await fetch("https://pokeapi.co/api/v2/pokemon/" + pokesearch.value);
    var pokeData = await response.json();
    pokeDiv.innerHTML += `<h1>Pokemon Name: ${pokeData.name}</h1>`
    pokeDiv.innerHTML += `<img src = '${pokeData.sprites.front_shiny}'>`

}
    
getCoderData();

// + pokeSearch.value
