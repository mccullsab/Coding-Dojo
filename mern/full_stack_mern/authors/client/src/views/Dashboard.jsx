import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom'

import AuthorForm from '../components/AuthorForm';
import DeleteButton from '../components/DeleteButton';


const Dashboard = () => {
    const nav = useNavigate();
    const [authorList, setAuthorList] = useState([])

    const removeFromDom = (authorToDelete) => {
        setAuthorList(authorList.filter((author) => author._id !== authorToDelete))
    }

    useEffect(() => {
        axios.get('http://localhost:8000/api/authors')
            .then((res) => {
                setAuthorList(res.data.author)
                console.log(res)
            })
            .catch((err) => console.log(err));
    }, [])

    return (
        <div>
            <h1>Favorite Authors:</h1>
            <table className='table'>
                <tbody>
                    <tr>
                        <td className='font-weight-bold'>Name</td>
                        <td className='font-weight-bold'>Actions Available</td>
                    </tr>
                    {authorList.map((author, indx) => (
                        <tr key={indx}>
                            <td>{author.name}</td>
                            <td className='align-middle'>
                                <Link to={`/authors/${author._id}`}>Details</Link>
                                <br />
                                <Link to={`/authors/${author._id}/edit`} >Edit</Link>
                                <br />
                                <DeleteButton authorId={author._id} successCallback={() => removeFromDom(author._id)} />
                            </td>
                        </tr>
                    ))};
                </tbody>
            </table>
        </div>
    )
}

export default Dashboard;