#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let r = 0;
  while ((len - r) > 0) {
    const aux = list[len];
    list[len] = list[r];
    list[r] = aux;
    r++;
    len--;
  }
  return list;
};
