// ----------------------------The Arrow Function

// A. The value of "this": It changes in "function decoration" based on
// how you invoke the function. But in the case of "arrow function",
// its value remains the same. Depending on where the function is created rather than
// how it's been called.
// If a single param is parsed, the use of "()" is optional. But if no param or more than 1 param is parsed, then it's reqired
// the "return" is implicit for arrow function if no "{}" is used.

// The introduction to "object literal"

// ----Example 1.

// defining functions
/*
let arrow = () => this;

function normal() {
	return this;
}

// Calling those functions to view the initial values of "this"

console.log(normal());
console.log(arrow());

// Creating an "object literal"

console.log("Finish---------------------------------");

let myObject = {
	name: "Lanx",
	normal: normal,
	arrow: arrow,
	arrowTest: () => this,
};

// Calling those functions

console.log(myObject.normal());

console.log(myObject.arrow()); //The value of "this" remains the same; the window object.

//The value of "this" remains the same; the window object.
console.log(
	"This function was declared inside the object",
	myObject.arrowTest()
);*/

// --------Example 2.

// -----------Using of "bind" with arrow function
/*
let arrow = () => this;

let funcValue = arrow.bind('New "this" value')();

console.log(funcValue);*/

// That means, in the case of "arrow function",
//value of "this" can never be changed; as a "window object"
