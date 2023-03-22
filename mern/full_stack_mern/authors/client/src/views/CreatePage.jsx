import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom'

import AuthorForm from '../components/AuthorForm';


const CreatePage = () => {
    const nav = useNavigate();
    const [formErrors, setFormErrors] = useState([]);
    const [authorList, setAuthorList] = useState([])

    const createAuthor = (newAuthor) => {
        axios
            .post('http://localhost:8000/api/authors', newAuthor)
            .then((results) => {
                console.log(results);
                setAuthorList([...authorList,results.data.author])
                nav('/authors');
            })
            .catch((err) => {
                // console.log(err)
                const errorResponse = err.response.data.error.errors
                const errorArr = []
                for(const key in errorResponse){
                    // console.log(errorResponse[key].message)
                    errorArr.push(errorResponse[key].message)
                    setFormErrors(errorArr);
                }
            })
    };

    return (
        <div>
            <div className=''>
                <h2>Favorite Authors</h2>
                <p>Add a new author:</p>
                <AuthorForm useForm={createAuthor} author ={{ name: ''}}/>
                {formErrors && formErrors.map((val, i) => 
                <p className='text-danger'>{val}</p>)}
            </div>
        </div>
    )
}

export default CreatePage;