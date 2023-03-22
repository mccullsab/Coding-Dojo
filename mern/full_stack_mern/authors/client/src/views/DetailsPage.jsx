import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom'
import DeleteButton from '../components/DeleteButton';

const DetailsPage = () => {
    const [author, setAuthor] = useState()
    const { id } = useParams();
    const nav = useNavigate();

    useEffect(() => {
        axios
            .get(`http://localhost:8000/api/authors/${id}`)
            .then((res) => {
                setAuthor(res.data.author)
            })
            .catch((err) => console.log(err))
    }, [])

    const goBackToDashboard = () => {
        nav('/authors')
    }

    return(
        <div>
            <h2>Info</h2>
            {author && (
                <div>
                    <p>Name: {author.name}</p>
                    <DeleteButton authorId = {author._id} successCallback={goBackToDashboard}/>
                </div>
            )}
        </div>
    )
}

export default DetailsPage;