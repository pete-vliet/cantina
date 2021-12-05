import React from 'react';
import { Box, Card, CardContent, CardMedia, IconButton } from '@mui/material';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';

const cardStyling = {
  display: 'flex',
  maxHeight: '100px',
};

const cardInfoStyling = {
  display: 'flex',
  flexDirection: 'column',
  width: 122,
};

const AlbumCard = ({main_artist, title, image_url}) => {
  return (
    <div className='card-container'>
      <Card sx={cardStyling}>
        <Box sx={cardInfoStyling}>
          <CardContent sx={{ flex: '1 0 auto', pt: 1, pb: 1 }}>
              <div><i>{title}</i></div>
              <div>{main_artist}</div>
          </CardContent>
          <Box sx={{ display: 'flex', justifyContent: 'center', pl: 1, pb: 1 }}>
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

export default AlbumCard;
