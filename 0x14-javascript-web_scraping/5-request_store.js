#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const link = process.argv[2];
request(link, function (error, response, body) {
  if (error) throw error;
  fs.writeFile(process.argv[3], body.toString(), (err) => {
    if (err) throw err;
  });
});
