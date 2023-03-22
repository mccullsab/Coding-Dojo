import React, { useState, useEffect } from 'react';

const AuthorForm = (props) => {
    const [name, setName] = useState(props.author.name)

    const handleSubmit = (e) => {
        e.preventDefault();

        const authorInfo = {
            name
        };

        props.useForm(authorInfo);
    };

    useEffect(() => {
        setName(props.author.name);
        }, [props.author._id])

    return (
            <form onSubmit={handleSubmit}>
                <p>
                    Name:
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </p>
                <button className='btn btn-primary'>Submit</button>
                <button className='btn btn-secondary ml-3'>Cancel</button>
            </form>
    )
}

export default AuthorForm;