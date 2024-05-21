#!/usr/bin/node
const request = require('request');
const URL = process.argv[2]
request(URL, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).films);
});
