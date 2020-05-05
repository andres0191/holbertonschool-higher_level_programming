#!/usr/bin/node
/* script that prints 3 lines:
(like 1-multi_languages.js) but
by using an array of string and a loop */

let i = 0;
const arrayMultilanguages = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (i in arrayMultilanguages) {
  console.log(arrayMultilanguages[i]);
}
