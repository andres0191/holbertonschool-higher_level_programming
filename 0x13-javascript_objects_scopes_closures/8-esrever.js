#!/usr/bin/node
/* Write a function that returns the list in reverse */
exports.esrever = function (list) {
  let i = 0; const arr = [];
  for (i = list.length - 1; i >= 0; i--) {
    arr.push(list[i]);
  }
  return (arr);
};
