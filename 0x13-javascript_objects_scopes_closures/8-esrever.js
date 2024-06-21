#!/usr/bin/node

exports.esrever = function (list) {
	const size = list.length;
	const newList = [];
	for (let i = size - 1; i >= 0; i--) {
		newList.push(list[i]);
	}
	return newList;
};
