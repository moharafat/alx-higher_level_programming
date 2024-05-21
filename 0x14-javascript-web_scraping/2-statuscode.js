#!/usr/bin/node
const request = require('request');
request(process.argv[2], 'utf-8', function (err, response, body) {
  if (err) throw err;
  console.log('code: ', response && response.statusCode);
});
