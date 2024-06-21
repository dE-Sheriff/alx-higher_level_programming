#!/usr/bin/node

const person = {
	name: ["Bob", "Smith"],
};

person.name.first;
person.name.last;

console.log(`Hi! I'm ${person.name[0]} ${person.name[1]}.`);

class Product{
	constructor(item, price){
		this.item = item;
		this.price = price;
	}

	displayTotal(tax){ 
		return this.price + (this.price * tax);
	}
}

const tax = 0.1
const product1 = new Product("Gucci", 100);

console.log(`product cost $${product1.displayTotal(tax)}`);
  