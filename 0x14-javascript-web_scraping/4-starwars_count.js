#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const ACTOR_ID = '/people/18';

request(URL, function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body);
  let COUNTER = 0;
  content.results.forEach((F) => {
    F.characters.forEach(character => {
      if (character.includes(ACTOR_ID)) {
        COUNTER += 1;
      }
    });
  });
  console.log(COUNTER);
});
