#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      const hasWedge = film.characters.some(
        (character) => character.includes('/people/18/')
      );
      if (hasWedge) {
        count += 1;
      }
    }
    console.log(count);
  }
});
