#!/usr/bin/node
const request = require('request');
URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2]

request(URL, function (error, response, body) {
  if (error) throw error;
  console.log(body);
});