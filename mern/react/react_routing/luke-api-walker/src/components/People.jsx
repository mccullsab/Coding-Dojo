import axios from 'axios';
import react, { useEffect, useState } from 'react';
import {useParams } from 'react-router-dom';

const People = () => {
    const[person, setPerson] = useState("")
    const{id} = useParams();


    useEffect(() => {
        axios
        .get(`https://swapi.dev/api/people/${id}`)
        .then((response) => {
            console.log(response);
            setPerson(response.data);
        })
        .catch((error) => {
            console.log(error);
        });
    }, [id]);

    return(
        <div>
            <h1>{person.name}</h1>
            <p>Height: {person.height}</p>
            <p>Mass: {person.mass}</p>
            <p>Hair Color: {person.hair_color}</p>
            <p>Skin Color: {person.skin_color}</p>
        </div>
    )
};

export default People;

