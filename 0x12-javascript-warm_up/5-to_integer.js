#!/usr/bin/node
if (Number(process.argv[2])) {
  console.log('My number: %d', parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
