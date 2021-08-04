#!/usr/bin/node
function fact (f) {
  if (f > 1) {
    return (f * fact(f - 1));
  } else {
    return (1);
  }
}
const f = parseInt(process.argv[2]);
console.log(fact(f));
