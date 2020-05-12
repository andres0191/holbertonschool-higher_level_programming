#!/usr/bin/node
/* Write a function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  let i = 0; let count = 0; let size = 0;
  size = list.length;
  for (i = 0; i <= size; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return (count);
};
