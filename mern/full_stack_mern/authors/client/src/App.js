import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';

import Dashboard from './views/Dashboard';
import CreatePage from './views/CreatePage';
import DetailsPage from './views/DetailsPage';
import UpdatePage from './views/UpdatePage';

function App() {
  return (
    <div className="App">
      <div>
        <Link to='/authors'>Home</Link> | 
        <Link to='/authors/new'>Create</Link>

      </div>
      <Routes>
        <Route path='/authors' element={<Dashboard/> } />
        <Route path='/authors/new' element={<CreatePage/> } />
        <Route path='/authors/:id' element={<DetailsPage/>} />
        <Route path='/authors/:id/edit' element={<UpdatePage/>} />
      </Routes>
    </div>
  );
}

export default App;
