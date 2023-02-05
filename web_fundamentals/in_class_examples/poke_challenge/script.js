console.log('script online!');

async function getPokemonData(pokeName) {
    // await executes this code and does not run the next line until it is completed.
    var response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokeName}`);
    var pokeData = await response.json();

    return pokeData;
}




async function displayPokemonData() {

    var pokemon = await getPokemonData(document.querySelector('#pokeSearch').value.toLowerCase());
    var pokeDiv = document.querySelector('#pokemonData')

    pokeDiv.innerHTML = "";
    pokeDiv.innerHTML += `<h1> ${pokemon.name} </h1>`;
    pokeDiv.innerHTML += `<img src='${pokemon.sprites.front_default}' alt='${pokemon.name}'>`
}


var pokeName = document.querySelector('#pokemonName')
var pokeImg = document.querySelector('.img-wrapper')
var pokeStats = document.querySelector('#stats')
var pokeWeight = document.querySelector('#pokeWeight')
var pokeHeight = document.querySelector('#pokeHeight')


async function displayPokemonData() {
    // asynch is a decorator to decleare the function is asynch and to awai 
    var response = await fetch("https://pokeapi.co/api/v2/pokemon/" + pokeSearch.value);
    var pokeData = await response.json();
    pokeName.innerHTML += `<h1>${pokeData.name}</h1>`
    pokeImg.innerHTML += `<img src = '${pokeData.sprites.front_default}'>`
    pokeStats.innerHTML += `<p>${pokeData['stats'][1]['stat']['name']}</p>` + `<p>${pokeData['stats'][2]['stat']['name']}</p>` + `<p>${pokeData['stats'][3]['stat']['name']}</p>` + `<p>${pokeData['stats'][4]['stat']['name']}</p>`
    pokeWeight.innerText += pokeData.weight
    pokeHeight.innerHTML += `<p>${pokeData.height}</p>`
}