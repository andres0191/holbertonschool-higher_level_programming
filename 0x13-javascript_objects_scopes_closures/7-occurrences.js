#!/usr/bin/node
/* Write a function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  var i = 0; var count = 0; var size = 0;
  size = list.length;
  for (i = 0; i <= size; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return (count);
};
