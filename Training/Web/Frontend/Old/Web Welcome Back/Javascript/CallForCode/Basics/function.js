// ---------------------------------Introduction to functions

// 1. Function decoration
// If you parse an argument to a function and you modify the param within the funct,
// it would affect the original value of the outside object or primitives (arg)

// a. Modify within function

/*let grades = [1, 2, 3, 4, 5];

function arrayAvrg(array) {
	let total = 0;

	array.push(6);

	array.forEach(function (element) {
		total += element;
	});

	return total;
}

console.log(`The average of grades is ${arrayAvrg(grades)}`);
console.log(`The new grades after modification is [${grades}]`);*/

// b. Re-assignment of parameter to a new object(it won't affect the outer grades)
/*
let grades = [1, 2, 3, 4, 5];

function arrayAvrg(array) {
	array = [7, 8, 9, 10];

	let total = 0;

	array.push(6);

	array.forEach(function (element) {
		total += element;
	});

	return total;
}

console.log(`The average of grades is ${arrayAvrg(grades)}`);
console.log(`The new grades after modification is [${grades}]`);*/

// 2. Call back function
// this is when a function is parse as an argument to another function
// and that function invokes or call the function we parse in.
// The function that took in another function is called "higher order function".
/* ------Asychronize call back function 

--This when you parse a function to an higher order function as an argument and set a time
before the inner function is invoked without preventing other codes from running.

e.g. setTimeout(function, time)


*/

/*let num = 4;
let message = function (number) {
	//the time function doesn't require "return" statement.
	number += 6;

	console.log(`Hello Engr. ${number}`);
};

setTimeout(message, 1000, num);

for (let i = 1; i <= 100; i++) {
	console.log(`${i}. This is for loop message`);
}*/

let userName = ""; //--------i noticed the re-assignment from the funct doesn't take effect outside

// 3. Hoisting in javascript
// Hoisting is the behaviour of javascript syntax which allows variable to be used or called
// before being declared e.g. function decoration.
//which means the engine scan the code twice.
// where "function decorations" are stored and their funct. body and "var decoration" variables is attached to the windows ppty without their values included

//a. "var"

// console.log(x);

//var x = 10;
// --it's accessed but excluding value; (var x; console.log(x); x=10)

// let x = 5;
// --couldn't accessed

//b. "funct" and using "var" in function expression are treated as normal variable declaration

// doStuff();

// This function is read completely

/*function doStuff() {
	console.log("hello world");
}*/

// the variable name is store as normal variable; var dosStuff; ~= undefined

/*var doStuff = function () {
	console.log("hello world");
};
*/

// c. "let" and "const"
// if you use "let" and "const", the variable wouldn't not be used before initialized
//----------- website(hoisting in modern javascript) => for further reading...

/*function pow(x, y) {
	// y is the power
	let total = 1;
	for (let i = 0; i < y; i++) {
		total *= x;
	}

	return total;
}*/

// console.log(pow(3, 3));

// d. Assigning function to an array

// let myArray = [pow, 5, 4];
/*let myArray = [pow];

console.log(myArray[0](5, 4));*/

// f. adding property to a function

/*pow.description = "This will raise a number power given ";
console.log(pow.description);

// g. Returning a function from another function (section 1)

const number = (func) => func(4, 4);

console.log(`${number(pow)}`);

// h. Returning a function from a function (section 1)

function returnFunction() {
	return pow;
}

console.log(`This is a returned function ${returnFunction()(10, 4)}`);*/

// 3. --------------------> Momoization and Algorithm Optomization

// a. Functions are treated as an object which can have properties.
// b. And for the concept above, we can attach a prpty to a function to keep a memory
// of all the computed values.

// -----storing both the "numbers input" and their "output"*/
/*	pow.calculated = {};

	function pow(x, y) {
		// y is the power
		let inputToString = x + "^" + y;

		let total = 1;

		// Checking

		if (inputToString in pow.calculated) {
			return console.log(`${inputToString} already exist`);

			// other code outside the loop wouldn't run again since "return" is used
		}

		for (let i = 0; i < y; i++) {
			total *= x;
			console.log("hi");
		}

		// pow.calculated.push(total);

		// pow.calculated.inputToString = total;
		//doesn't work since "inputToString" is assumed to be the "key" name; pow.calculated['inputToString']

		pow.calculated[inputToString] = total;

		console.log(pow.calculated);

		return total;
	}

	//---- creating property
	// pow.calculated = [];

	//----- changing storage to an "object"; using "key" and "object" method

	// -----calling the function
	pow(50, 2);
	pow(4, 16);
	pow(50, 4);
	pow(2, 6);
	pow(50, 4);*/

// log the updated pperty
// console.log(pow.calculated);

// 4. Default params, rest params, implicit params
/* Testing the use of function instead of "eval()"
	[ let exp = "2+2";
  console.log(`This 'eval()' function evaluates to ${eval(exp)}`);

  //the Function statement is called a "function constructor"
  let result = Function(`return ${exp}`)(); 
   //running the function directly produces the answer 
  console.log(result);

	let name = [21,32]]
	*/

//a. Setting default value for parameter(s) in 3 ways

/*function modulo(value = 45, divisor) {
		///-------2nd method
		if (divisor === undefined) divisor = 2;*/

/*// --------3rd method: Ternary operator
		divisor = typeof divisor === "undefined" ? 10 : divisor;

		let answer = `The modulo of ${value} % ${divisor} is ${value % divisor}`;

		return console.log(answer);
	}

	modulo(18);*/

// b. Parsing numerous argument with limited params and how to access those args
// And to access the excess args, we use "..." with a name e.g. "...extra"

/*let functionLargestScore = new Function(
	"x",
	"...extra",
	`
		let largest = x;

		for (let i = 0; i < extra.length; i++){

			largest = extra[i] > largest ? extra[i] : largest

		}
		
		return console.log(largest);
	`
);

functionLargestScore(100, 2, 3, 50, 7, 29, 50.9, 20);*/

/* c. The "implicit parameter": 
this means we are not explicitly stating the function behind the scene.
And it involves the use of "this" and "argument". which are windows properties
*/

/*function pow(x, y) {
	console.log(this); //return window object
	console.log(arguments); //returns all args parsed to a function. 
	// y is the power

	let total = 1;

	// for loop

	for (let i = 0; i < y; i++) {
		total *= x;
	}

	return total;
}

console.log(pow(5, 8));*/
