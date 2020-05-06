#!/usr/bin/node
/* Write a funciton that increments and calls a function */
exports.addMeMaybe = function (i, theFunction) {
  i++;
  theFunction(i);
};
