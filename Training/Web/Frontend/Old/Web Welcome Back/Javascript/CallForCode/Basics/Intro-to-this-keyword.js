//------------ Introduction to "this", a window global property or function context
// In function, we have explicit and implicit args.
// When you invoke funct, you parse it args, and that's called explicit args; they are outside of a the function
// While the implicit args is when we do not type them out but only using "this" arg
// Which means, we can access the so called "virtual arg" using "this" inside the function.
// NB: the value of "this" can changed depending on how and where we call the function.
// NB: Most of the time, "this" is going to refer to an object that get a method on it.
// That is, there is an object "foodItem" and a funct "getListItem".
// So we have, "foodItem.getListItem". Therefore, the "this" arg inside the funct would be
// refer to the object "foodItem".
// Meaning that the behaviour of the funct changes based on how you use "this"
// Make makes creating of "predictable function" a little bit challenging.
// Q1: The use of "strict mode"
// In other languages like C# & Java, "this" always mean an object that a method (the funct) is attached to.
// Because everything is in "object" form and all funct are method in those languages

// ---------------------Examples
// -----1. function as a method
/*let counter = 1;

let student = {
	name: "",
	message: function () {
		this.name = prompt("Enter your name please");

		if (this.name && this.name.length >= 3) {
			alert(`Hello ${this.name}`);
			// the "this" refer to the current object; "student.message.names"
			this.message.names[counter] = this.name.toUpperCase();
			counter++;
		}
	},
};

// Storing the names
student.message.names = {};

// A. invoking the function as a method
student.message();
student.message();
student.message();*/

// -----2. invoking as a normal function

/*let student = {
	name: "",
	message: greetings,
};

function greetings() {
	this.name = prompt("Enter your name please");

	if (this.name && this.name.length >= 3) {
		alert(`Hello ${this.name}`);
	}
}

student.message();
student.message();*/

// ----function strict; "use strict" & not using strict

// a.
/*function greetings() {
	console.log(this);
}

greetings();

// b.
function greetings2() {
	"use strict";
	console.log(this); //this produces "undefined"
}

greetings2();*/

// ------3. Calling a function as a "constructor"; object constructor.
// Normal convention is we use Uppercase to name this type of funct.
// Therefore, using "this" would refer to the new object created.
// Meaning: Using a function to create new object.

/*function Person() {
	console.log(this);
	// let's have a value
	this.name = "lanx";
	console.log(this);
}

let person = new Person(); //so we have an object on this line

console.log(person);*/

// In summary, we called the funct with "new" keyword, and empty "obj" is parsed to the
// "this" implicit parameter

// ----------------------------The use of "call", "apply", and "bind" functions along with "this" function-------------

// -------------"Call" and "apply" methods: useful when dealing with "this" keyword
// Using these methods allow us to modify what the value of "this" is (explicitly)
// Specifically, when you are invoking the function
// e.g theFunct.call("thisValueFirst",arg1,arg2,...)  'thisValueFirst' means the value of "this" inside that particular function

// e.g. theFunct.apply('thisValueFirst',[arg1,arg2])

/*function myPeople(name1, name2, ...others) {
	let otherNames = "";
	// checking if there are other names

	if (others.length > 0) {
		// statement
		others.forEach((name) => {
			otherNames += name;

			if (others.indexOf(name) !== others.length - 1) {
				otherNames += ", ";
			} else {
				otherNames += ".";
			}
		});

		return console.log(
			`I have ${this} brothers. And they are ${name1}, ${name2}, ${otherNames}
			`
		);
	}

	console.log(this); //Just like have a "Number object"
	return console.log(
		`I have ${this} brothers. And they are ${name1} and ${name2}`
	);

	// -----------end myPeople Function-------------------
}
*/
// myPeople.call(2, "Abdulwaris", "Abdulrasheed");
// myPeople.apply(3, ["Abdulwaris", "Abdulrasheed", "Muhammad"]);

// -------------------The "bind" method
// This is a little bit diff from "call" and "apply" in such that it will returns a
// new function where the value of "this" is permanently changed.
// That is, this returns a function, rather than invoking
// function "myPeople" directly (unlike "call" and "apply").
// And the new funct needs to be called.
// the value of "this" could be any custom object such as "string", "Number", etc.

/*let names = myPeople.bind(
	5,
	"Waris",
	"Abdulrasheed",
	"Muhammad",
	"Lanx",
	"Adigun"
);

console.log(names);*/
