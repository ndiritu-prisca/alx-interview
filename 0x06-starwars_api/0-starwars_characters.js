#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function getMovieCharacters (movieId) {
  // Base URL of the Star Wars API
  const baseUrl = 'https://swapi-api.alx-tools.com/api/';

  // Request to the /films endpoint to get the movie details
  const movieUrl = `${baseUrl}films/${movieId}/`;

  request(movieUrl, (error, response, body) => {
    if (error) {
      console.error(`Failed to retrieve movie data for Movie ID ${movieId}.`);
      return;
    }

    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Function to fetch and print character data sequentially
    const fetchAndPrintCharacter = (index) => {
      if (index < characters.length) {
        request(characters[index], (charError, charResponse, charBody) => {
          if (charError) {
            console.error(`Failed to retrieve character data for URL: ${characters[index]}`);
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
          // Fetch and print the next character
          fetchAndPrintCharacter(index + 1);
        });
      }
    };

    // Start fetching and printing characters from the beginning
    fetchAndPrintCharacter(0);
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./swapi_characters.js <Movie ID>');
  process.exit(1);
}

getMovieCharacters(movieId);
