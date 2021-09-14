#!/usr/bin/node
const request = require('request');
const link = process.argv[2];
let matches = 0;
request(link, function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    const chars = data[i].characters;
    if (chars.find(str => str.includes('/api/people/18/'))) {
      matches++;
    }
  }
  console.log(matches);
});
