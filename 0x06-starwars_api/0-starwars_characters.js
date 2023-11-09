#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function getMovieCharacters (movieId) {
  // Base URL of the Star Wars API
  const baseUrl = 'https://swapi.dev/api/';

  // Request to the /films endpoint to get the movie details
  const movieUrl = `${baseUrl}films/${movieId}/`;

  request(movieUrl, (error, response, body) => {
    if (error) {
      console.error(`Failed to retrieve movie data for Movie ID ${movieId}.`);
      return;
    }

    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Print the characters for the specified movie
    const fetchCharacterData = characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(`Failed to retrieve character data for URL: ${characterUrl}`);
          return;
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    };

    Promise.all(characters.map(fetchCharacterData))
      .catch(charError => {
        console.error('Failed to retrieve character data for one or more characters.');
      });
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./swapi_characters.js <Movie ID>');
  process.exit(1);
}

getMovieCharacters(movieId);
