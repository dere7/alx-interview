#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie
 */
const request = require('request');

const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + movieId;

// promisifys request
function getJSON (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, response, body) {
      if (err) reject(err);
      if (response.statusCode === 200) resolve(JSON.parse(body));
      else reject(new Error(response.statusMessage));
    });
  });
}

getJSON(URL).then(function (data) {
  const charactersUrl = data.characters;
  return Promise.all(charactersUrl.map(getJSON));
}).then(function (actors) {
  actors.forEach(function (actor) {
    console.log(actor.name);
  });
}).catch(console.error);
