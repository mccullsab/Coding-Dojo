import axios from 'axios';
import react, { useEffect, useState } from 'react';
import {useParams } from 'react-router-dom';

const Starships = () => {
    const[starship, setStarship] = useState("")
    const{id} = useParams();


    useEffect(() => {
        axios
        .get(`https://swapi.dev/api/starships/${id}`)
        .then((response) => {
            console.log(response);
            setStarship(response.data);
        })
        .catch((error) => {
            console.log(error);
        });
    }, [id]);

    return(
        <div>
            <h1>{starship.name}</h1>
            <p>Model: {starship.model}</p>
            <p>Crew: {starship.crew}</p>
            <p>Passengers: {starship.passengers}</p>
            <p>Cargo Capacity: {starship.cargo_capacity}</p>
        </div>
    )
};

export default Starships;

