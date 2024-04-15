#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Retrieve the movie ID from the command line argument

// Function to fetch characters for a given movie ID
function getMovieCharacters(movieId) {
    // Construct the URL for fetching movie details
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;
    
    // Make a GET request to fetch movie details
    request.get(movieUrl, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
        } else if (response.statusCode === 404) {
            console.error('Movie not found. Please provide a valid movie ID.');
        } else if (response.statusCode !== 200) {
            console.error('Failed to fetch movie details. Status Code:', response.statusCode);
        } else {
            const movieData = JSON.parse(body);
            const characters = movieData.characters;
            
            // Print each character's name
            characters.forEach((characterUrl) => {
                request.get(characterUrl, (error, response, body) => {
                    if (error) {
                        console.error('Error:', error);
                    } else if (response.statusCode !== 200) {
                        console.error('Failed to fetch character details. Status Code:', response.statusCode);
                    } else {
                        const characterData = JSON.parse(body);
                        console.log(characterData.name);
                    }
                });
            });
        }
    });
}

// Call the function with the provided movie ID
getMovieCharacters(movieId);
