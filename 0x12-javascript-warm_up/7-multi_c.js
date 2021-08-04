#!/usr/bin/node
if (Number(process.argv[2])) {
  for (let n = 0; n < process.argv[2]; n++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
