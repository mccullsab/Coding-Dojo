import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom'

import AuthorForm from '../components/AuthorForm';

const UpdatePage = () => {
    const nav = useNavigate();
    const { id } = useParams();
    const [oneAuthor, setOneAuthor] = useState({});
    
    const [formErrors, setFormErrors] = useState([]);

    useEffect(() => {
        axios
            .get(`http://localhost:8000/api/authors/${id}`)
            .then((res) => {
                const author = res.data.author
                // console.log(res);
                // for (var i=0; i < 1000000000; i++){
                //     let x = i*i;
                // }
                setOneAuthor(author);
            })
            .catch((err) => console.log(err))
    }, [])

    const updateAuthor = (authorToUpdate) => {
        axios
            .put(`http://localhost:8000/api/authors/${id}`, authorToUpdate)
            .then((results) => {
                console.log(results)
                nav(`/authors`);
            })
            .catch((err) => {
                // console.log(err)
                const errorResponse = err.response.data.error.errors
                const errorArr = []
                for(const key in errorResponse){
                    errorArr.push(errorResponse[key].message)
                    setFormErrors(errorArr);
                }
            })
    };


    return (
        <div>
            <h2>Favoite Authors</h2>
            <p>Edit this author:</p>
            {/* { oneAuthor.title !== undefined && */}
            <AuthorForm useForm={updateAuthor} author={oneAuthor} />
            {formErrors && formErrors.map((val, i) => 
                <p className='text-danger'>{val}</p>)}
            {/* } */}
        </div>
    )
}

export default UpdatePage;