#!/usr/bin/node

exports.converter = function (base) {
	return function f(number) {
		return number.toString(base);
	};
};
