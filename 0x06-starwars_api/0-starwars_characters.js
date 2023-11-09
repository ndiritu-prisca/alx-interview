#!/usr/bin/node

const axios = require('axios');
const movieId = process.argv[2];

function getMovieCharacters (movieId) {
  // Base URL of the Star Wars API
  const baseUrl = 'https://swapi.dev/api/';

  // Request to the /films endpoint to get the movie details
  const movieUrl = `${baseUrl}films/${movieId}/`;

  axios.get(movieUrl)
    .then(response => {
      const movieData = response.data;
      const characters = movieData.characters;

      // Print the characters for the specified movie
      const fetchCharacterData = characterUrl => {
        axios.get(characterUrl)
          .then(characterResponse => {
            const characterData = characterResponse.data;
            console.log(characterData.name);
          })
          // eslint-disable-next-line n/handle-callback-err
          .catch(error => {
            console.error(`Failed to retrieve character data for URL: ${characterUrl}`);
          });
      };

      Promise.all(characters.map(fetchCharacterData))
        // eslint-disable-next-line n/handle-callback-err
        .catch(error => {
          console.error(`Failed to retrieve movie data for Movie ID ${movieId}.`);
        });
    })
    // eslint-disable-next-line n/handle-callback-err
    .catch(error => {
      console.error(`Failed to retrieve movie data for Movie ID ${movieId}.`);
    });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./swapi_characters.js <Movie ID>');
  process.exit(1);
}

getMovieCharacters(movieId);
