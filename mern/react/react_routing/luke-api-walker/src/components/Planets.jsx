import axios from 'axios';
import react, { useEffect, useState } from 'react';
import {useParams } from 'react-router-dom';

const Planets = () => {
    const[planet, setPlanet] = useState("")
    const{id} = useParams();


    useEffect(() => {
        axios
        .get(`https://swapi.dev/api/planets/${id}`)
        .then((response) => {
            console.log(response);
            setPlanet(response.data);
        })
        .catch((error) => {
            console.log(error);
        });
    }, [id]);

    return(
        <div>
            <h1>{planet.name}</h1>
            <p>Climate: {planet.climate}</p>
            <p>Terrain: {planet.terrain}</p>
            <p>Surface Water: {planet.surface_water > 0 ? 'true' : 'false'}</p>
            <p >Population: {planet.population}</p>
        </div>
    )
};

export default Planets;

