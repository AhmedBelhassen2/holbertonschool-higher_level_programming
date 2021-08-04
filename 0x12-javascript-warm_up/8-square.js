#!/usr/bin/node
if (!Number(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let c = 0; c < process.argv[2]; c++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
