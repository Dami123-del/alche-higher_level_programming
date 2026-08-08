#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const completedCount = {};
    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId;
        if (completedCount[userId] === undefined) {
          completedCount[userId] = 0;
        }
        completedCount[userId] += 1;
      }
    }
    console.log(completedCount);
  }
});
