import React from 'react';
import axios from 'axios';

const DeleteButton = (props) => {
    const { authorId, successCallback } = props

    const deleteAuthor = (authorToDelete) => {
        axios.delete(`http://localhost:8000/api/authors/${authorId}`)
        .then((res) => {
            successCallback();
        })
        .catch((err) => console.log(err))
    }

    return(
    <button 
    className='btn btn-danger' 
    onClick={deleteAuthor}>
        Delete
    </button>

    )
};

export default DeleteButton;