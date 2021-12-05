import React, { useState, useEffect } from 'react';
import Container from '@mui/material/Container';
import './App.css';

import AlbumCard from './components/AlbumCard';
import AppHeader from './components/AppHeader';

function App() {
  const [library, setLibrary] = useState(null);

  useEffect(() => {
    fetch('/api', {
      headers: {
        'Accept': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }).then(data => {
      return data.json();
    }).then(data => {
      setLibrary(data.collection);
    });
  }, []);

  const renderAlbumCard = ({ main_artist, title, image_url }) => {
    return <AlbumCard main_artist={main_artist} title={title} image_url={image_url} key={image_url}/>
  };

  return (
    <div>
      <AppHeader />
      <Container maxWidth="sm" className="App">
        <div className='records-list'>
          { library && library.map(renderAlbumCard) }
        </div>
      </Container>
    </div>
  );
}

export default App;
