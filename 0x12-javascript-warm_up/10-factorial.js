#!/usr/bin/node

function factorial(num) {
	if (num <= 1 || isNaN(num)) {
		return 1;
	} else {
		return num * factorial(--num);
	}
}

const number = parseInt(process.argv[2]);
console.log(factorial(number));
