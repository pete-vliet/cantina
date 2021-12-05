import React, { useState, useEffect } from 'react';
import { Box, Card, CardContent, CardMedia, Container, IconButton } from '@mui/material';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import './App.css';

const cardStyling = {
  display: 'flex',
  maxHeight: '100px',
};


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

  const renderLibraryItem = ({ main_artist, title, image_url }) => {
    return (
      <div className='card-container'>
      <Card sx={cardStyling}>
        <Box sx={{ display: 'flex', flexDirection: 'column' }}>
          <CardContent sx={{ flex: '1 0 auto' }}>
              <div><i>{title}</i></div>
              <div>{main_artist}</div>
          </CardContent>
          <Box sx={{ display: 'flex', alignItems: 'center', pl: 1, pb: 1 }}>
            <IconButton aria-label="play/pause">
              <PlayArrowIcon sx={{ height: 38, width: 38 }} />
            </IconButton>
          </Box>
        </Box>
        <CardMedia
          component="img"
          sx={{ width: 100 }}
          image={image_url}
          alt={`${title} album cover`}
        />
      </Card>
      </div>
    );
  };

  return (
    <div className="App">
      <Container maxWidth="sm">
        <header>
          <h1 className='c-h1'>Cantina</h1>
        </header>
        <div className='records-list'>
          { library && library.map(renderLibraryItem) }
        </div>
      </Container>
    </div>
  );
}

export default App;
