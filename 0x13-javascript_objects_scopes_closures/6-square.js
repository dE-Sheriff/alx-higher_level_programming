#!/usr/bin/node

const Square5 = require('./5-square.js');

module.exports = class Square extends Square5 {
	charPrint (c) {
		const sign = c === undefined ? 'X' : c;
		for (let i = 0; i < this.height; i++) {
			console.log(sign.repeat(this.width));
		}
	}
};
