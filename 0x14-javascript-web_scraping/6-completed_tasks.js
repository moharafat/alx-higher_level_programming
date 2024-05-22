#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const to_do_objs = JSON.parse(body);
  const TASKS_COMPLETED = {};
  to_do_objs.forEach(Element => {
    if(Element.completed == true)
        
  });
});
