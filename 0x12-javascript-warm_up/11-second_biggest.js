#!/usr/bin/node

const myArgs = process.argv.slice(2);
if (myArgs.length <= 1) {
	console.log(0);
} else {
	console.log(myArgs.map((item) => Number(item)).sort((a, b) => a - b).reverse()[1]);
}
