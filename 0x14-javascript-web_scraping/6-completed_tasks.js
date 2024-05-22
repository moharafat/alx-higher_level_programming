#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const TO_DO = JSON.parse(body);
  const TASKS_COMPLETED = {};
  TO_DO.forEach(Element => {
    if (Element.completed === true) {
      if (Element.userId in TASKS_COMPLETED) {
        TASKS_COMPLETED[Element.userId] += 1;
      } else {
        TASKS_COMPLETED[Element.userId] = 1;
      }
    }
  });
  console.log(TASKS_COMPLETED);
});
