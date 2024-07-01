// -----------------------Introduction--------------------------
/*const confirmParagraph = document.getElementById("confirm");
const confirmBtn = document.getElementById("confirm-btn");

function confirmButton() {
	confirmParagraph.textContent =
		"PAYMENT SUCCESFUL! CHECK EMAIL TO PRINT RECEIPT.";
	confirmBtn.style.display = "none";
}*/

/*function changeColour() {
	confirmBtn.style.outline = "none";
	confirmBtn.style.background = "#333";
	confirmBtn.style.color = "#aaa";
}*/

// A. -----------------Variables & Scope--------------------

/*let name = "Sodiq";

let newName = () => {
	name = "LanxCity";
	return name;
};

// NB: The functioin goes out of the function scope and changes the value of the already defined name
// Just like IIFE, the use of "var" keyword is a must.

console.log(newName());
console.log(name);
*/

// -------------------The following variables "count" and "my_name" are accessible from the outside

/*for (var count = 0; count < 13; count++) {
	var my_name = "sodiq";
	console.log(my_name);
}*/

// -------------------While these are not accessible from the outside

/*for (let count = 0; count < 13; count++) {
	let my_name = "sodiq";
	console.log(my_name);
}*/

// ----------------------------------The Global and Local  variables----------
// 1. If you create a variable with the "var", such variable is only attached and limited to that
// "function scope" it's been defined in.

// NB: "var" is function level while "let" and "const" are block level. Because using "var" in a code
// block, excluding funct e.g. "if" and "for", still looks up for function scope or global's.

// =======================================>>>>The use of block level variables using let and const

/*{
	let x = 56;
	let y = 5;

	{
		let x = 36;
		z = 100;
		console.log(x);
		console.log(y);
	}

	console.log(x);

	/*	

	Output=> x: 36
	Output=> y: 5
	Output=> x: 56

	*
}*/

// ----------------Number Methods-----------------
// An instance is a variable of a certain data type with the use of its object

// let num = 56        //This is an instance

// let myNum = new Number(34)   //This is an object

/*let myNum = '25343hjghsgdgdg'

console.log(Number(myNum))   //this returns NaN because all the string value must be a number
console.log(Number.parseInt(myNum))
*/

//----------------------------The importance of "parseInt" in converting number from any base to decimal
//The "ParseInt("num_string, radix or base of the num input")" convert numbers from different base to decimal

// let myNum = '11'

// console.log(`Convert ${myNum} base 10 to base 10: ${Number.parseInt(myNum, 10)}`)
// console.log(`Convert ${myNum} base 2 to base 10: ${Number.parseInt(myNum, 2)}`)
// console.log(`Convert ${myNum} base 8 to base 10: ${Number.parseInt(myNum, 8)}`)
// console.log(`Convert ${myNum} base 16 to base 10: ${Number.parseInt(myNum, 16)}`)

// -------------------------The importance of "toString()" method in converting numbers from decimal to a certain base
// let myNum = Number('11')  //In base 2

// console.log(`Convert ${myNum} base 2 to base 8: ${myNum.toString(8)}`)

// -------------------------------Instance methods on numbers.
// Although, primitives does not have prpties and methods but their objects counterpart does.
// Therefore, any instance (e.g. x = 4) of a certain data type is converted to its object counterpart (e.g. x = new Number(4))under the hood.
// And allows us to use prpties and methods created for such data type

// --------------------------------The "for" loops
/*let myName = "Sodiq";

for (i in myName) {
	if ("q" === myName[i]) {
		console.log(`I found character ${myName[i]} in ${myName}`);
		break;
	}
}*/

// -------------------------------------------------------------------------------------------From Sodiq.js file-----------------------
// B----------------------Javascript Engine-----------------------

/*const confirm = document.getElementById("confirm")

function paymentConfirmation() {
	confirm.textContent = "PAYMENT SUCCESSFUL!!! Check Email for Receipt"

	confirmBtn = document.getElementById('confirm-btn')
	confirmBtn.style.display = 'none'
}*/

// console.log('Helloooooo')
// let name = 56
// console.log(name)

// ----------------------------------The Global and Local  variables----------
// 1. If you create a variable with the "var", such variable is only attached and limited to that
// "function scope" it's been defined in.

// NB: "var" is function level while "let" and "const" are block level. Because using "var" in a code
// block, excluding funct e.g. "if" and "for", still looks up for function scope or global's.

// ---------------Operator precedence continued......

// ----------------Number Methods-----------------
// An instance is a variable of a certain data type with the use of its object

// let num = 56        //This is an instance

// let myNum = new Number(34)   //This is an object

/*let myNum = '25343hjghsgdgdg'

console.log(Number(myNum))   //this returns NaN because all the string value must be a number
console.log(Number.parseInt(myNum))
*/

//----------------------------The importance of "parseInt" in converting number from any base to decimal
//The "ParseInt("num_string, radix or base of the num inputed")" convert numbers from different base to decimal

// let myNum = '11'

// console.log(`Convert ${myNum} base 10 to base 10: ${Number.parseInt(myNum, 10)}`)
// console.log(`Convert ${myNum} base 2 to base 10: ${Number.parseInt(myNum, 2)}`)
// console.log(`Convert ${myNum} base 8 to base 10: ${Number.parseInt(myNum, 8)}`)
// console.log(`Convert ${myNum} base 16 to base 10: ${Number.parseInt(myNum, 16)}`)

// -------------------------The importance of "toString()" method in converting numbers from decimal to a certain base
// let myNum = Number('11')  //In base 2

// console.log(`Convert ${myNum} base 2 to base 8: ${myNum.toString(8)}`)

// ------------------The "nested for loop"---------
// let profile = {
// 	name: 'sodiq',
// 	age: 56,
// 	gender: 'male',
// 	eyeColor: 'black'
// }

// let ages = [12,3,4,14,65]
// ages.length = 33
// ages[26] = 15
// ages[35] = 10

// for (let i= 0; i < ages.length; i++) {
// 	if (!ages[i]) continue;
// 	console.log(ages[i]);

// }

// let ages = [12,64,53,2,3,5,6,66,16]

// smallestAge = ages[0]
// smallestAgeIndex = 0
// for (let i = 0; i < ages.length; i++) {
// 	if (ages[i] > smallestAge) continue;
// 	smallestAge = ages[i]
// 	smallestAgeIndex = i
// }
// console.log('The smallest age is:',smallestAge+'.', 'And it\'s at index', smallestAgeIndex)

// ---------------Filling Array from user input using "while" loop----------
// And the use of "sentinel value"

// ------------------------"Label" with "break" and "continue"-----------------------------

// label: means labelling an outer "for" loop so as to use "continue" or break out of that  outer loop.

/*multiList = [
	[24,54,62,22,23,43],
	[53,62,21,12,15,63,45,55,65,123,45,22,65],
	[24,54,62,64,53,55],
	[21,65,46,42,61,34,56,43]
]*/

/*multiList.forEach(function(row,index) {

	row.forEach((col) => console.log(col))

	console.log('Done with row ' + (index + 1))
})*/

/*outerLoop: for (let row = 0; row < multiList.length; row++) {

	for (let col = 0; col < multiList[row].length; col++) {

		console.log(multiList[row][col])

		if (multiList[row][col] === 55) {

			console.log(`I found the number ${multiList[row][col]} at row ${row+1}`)

			continue outerLoop    

			// equivalent to ~= "break" inside the inner loop but codes inside the outer loop is not read
			// if "break" is used, codes inside the outer loop is read

		}
		
		console.log('Doing stuff')
	}
}
*/

/*outerLoop: for (let row = 0; row < multiList.length; row++) {

	for (let col = 0; col < multiList[row].length; col++) {

		console.log(multiList[row][col])

		if (multiList[row][col] === 55) {

			console.log(`I found the number ${multiList[row][col]} at row ${row+1}`)

			break outerLoop  //This breaks out of the loop entirely

		}
		console.log('Doing stuff')
		
	}
	
	console.log('Yeh------------------------------')
}*/

// ----------------------------Introduction to Date object
// To create "date object", we use the date constructor.

// ---> A Constructor is a special function that's going to return an instance of something.
// e.g. string constructor, "new String"

// Date(year,month,day)
// NB: the "month" is 0 base; Jan ~= 0, Feb ~= 1, etc.
// The use of UNIX Epoch
// new Date(year,month,day,hour,minute,second,millisecond)
// Date(), If a single argument is parsed, it's going to counted as millisecond
// Date(2020,12) ~= 2021, Jan 1
// Date.now() returns the number of milliseconds from 1970

// let newYearStart = new Date(2022,0)
// let newYearPresently = new Date(2022,2,26,00,00,00)
// console.log(newYearPresently - newYearStart)

// let time = Date.now()
// console.log(time)

// Calculate number of days between two date

/*let newYearStart = new Date(2022,0)
let newYearPresently = new Date(2022,2,26)

milliSecondsInDay = (60 * 60 * 24) * 1000

numberOfDays = (newYearPresently - newYearStart)/milliSecondsInDay


console.log(`${numberOfDays}`)*/

// -----------------------The Date() method
// 1. Date.parse(string): It's not compatible with all browsers

// let myDateOfBirth = Date.parse('27 may 1997')

// let myDateOfBirth = Date.parse('1 jan 1970 00:00:00')
// let myDate = Date.parse('2 jan 1970 00:00:00')

// let myDate = Date.parse('1 jan 1970')
// let yourDate = new Date('1 jan 1970')  //
// let yourDate = new Date('1996-12-25')
// // let startDate = Date.parse('1 Jan 1970 01:00:00')   // 0

// // console.log(myDate)
// console.log(yourDate)
// console.log(myDate)

// 2. Date.UTC()

// Whatever time is stored, the browser would print it
// e.g. if I stored "new Date(2022,1,14,01,10,10)", it would be printed out the same way but base on my location, either GMT+01 or GMT-0600

// But if the date is given GMT and needs it to be printed base on my location, we would add "Date. utc()"

// 3. Setters: these are used to set a date e.g. setHours()

// let myDate = new Date('14-5-2022')  //Invalid Date
// let myDate = new Date('14 Jan 2022') //valid Date

// myDate.setHours(16)

// let myDate = new Date() //valid Date

// //this returns how many minutes we are far more than the GMT.
// // And for West Africa, it's GMT+0100; "60minutes". But (It would returns -60 instead of +60 )

// console.log(myDate.getTimezoneOffset())

// ----------------------------------Introduction to functions---------------
// Two methods of passing an argument to a function are;

// Pass by value---- and Pass by reference------

// A. Passed by value
/*let x = 5

function square(num) {

	return num * num
}

console.log(square(x))
console.log(x)*/

// For the above, the value of x is copied as the value of param "num".
// So any changes inside the function do not affect the original value outside the function.

// B. Parsed by reference
// If an object is assigned to variable, unlike primitives, the object is stored in the memory
// where the variable only refer to such object and not storing it like primitives.
// For primitives, that variable stores the value.

/*let info = {}


function person(profile) {

	profile.name = 'Sodiq';
	profile['age'] = 65
	profile['matricNumber'] = 200268

	return profile
}

console.log(person(info))*/

// 1.--------------Callback function--------------
// This is passing a function as an argument to another function.
// And that outer function that took another function as an argument is called the "higher order function".

// --------The "async" callback function
//This involves the use of "setTimeOut(callback fn, time (in milliseconds))"

// --------------------------------------FUNCTIONS IN JS-----------

// -----------------Function Declaration and Expression

// 1. function decoration

/*function basicArithmetic(x) {

	return Function(` 

		//The function constructor

		return ${x}
		`)()
}

let myExpression = '2 + (6-6)'

console.log(basicArithmetic(myExpression))*/

// 2. function expression

/*let thePowerOfNumber = function(x,y){

	// let total = 1

	// for(let i = 0; i < y; i++) total *= x;

	return x**y

}
 
console.log(thePowerOfNumber(5,4))*/

// A. ---------Introduction to Hoisting
// variable decoration (e.g. var x = 5), let and const.
// diff btw func declaration and expression
// We can also add properties to function because functions are treated as objects in javascript.
// E.g.

// thePowerOfNumber.description = 'This takes two args x, y. Where y is the exponent of x'

// console.log(thePowerOfNumber.description)

// -------------------Memoization and Algorithm optimization

// This is attaching a property to a function in order to keep in memory of all the computed value.

/*pow.description = 'This function takes two args x, y. Where y is the exponent of x' 
pow.calculated = {}

function pow(x,y) {

	let stringVersion = x + '^' + y
	total = 1

	if(stringVersion in pow.calculated) return `Expression ${stringVersion} exist already and it gives: ${pow.calculated[stringVersion]}`

	for(let i = 0; i < y; i++) {

		total *= x
	}

	pow.calculated[stringVersion] = total

	return `The expression ${stringVersion} gives: ${total}`
}

// console.log(pow.description)
console.log(pow(6,4))
console.log(pow(4,4))
console.log(pow(5,4))
console.log(pow(3,5))
console.log(pow(12,2))
console.log(pow(5,4))*/

// ----------------------------------------Default params, rest params, and implicit params.

/*let [me, you, ...others] = [1, 2, 3, 4, 4];

console.log(others);*/

// The concept of overloading is not in javascript func. It takes more args more than expected params.

// A. Default params or values for param: This is advisable should in case less args are parsed to a function while invoked.
// E.g. maybe you create a library or reusable function which is open source.

// pow.description = "This takes two numbers (x,y). Where y is the exponent of x. And y = 1 if no arg is parsed for y";

/*function pow(x, y = 1) {
	// OR
	x = x === undefined ? 1 : x;

	let total = 1;

	for (let i = 0; i < y; i++) {
		total *= x;
	}

	return total;
}*/

// console.log(pow(4));
// console.log(pow());

// B. Rest params or extra

// let [a, b, ...c] = [5, 3, 10, 4, 5];

/*function pow(x, y, ...others) {
	// OR
	x = x === undefined ? 1 : x;

	console.log(others);
	let total = 1;

	for (let i = 0; i < y; i++) {
		total *= x;
	}

	return total;
}

// console.log(pow(a, ...c));
console.log(pow(a, b, 5, 1, 2, 3, 4, 23));*/

// C. Implicit params: The use "this" inside a function

// The "arguments" is not an actual array but array-like object. We can make use of it instead of the "rest param"

/*function pow(x, y = 1) {
	console.log(this);
	console.log(...arguments);

	x = x === undefined ? 1 : x;

	let total = 1;

	for (let i = 0; i < y; i++) {
		total *= x;
	}

	return total;
}

// pow();
pow(1, 2, 3, 4, 5, 6, 67);*/

// -----------------------------Intro to "this" keyword-----------------

/*let profile = {
	name: "Sodiq",
};

console.log(profile);
*/
/*function greetings() {
	"use strict";
	console.log(this);

	// console.log(`Hi! I'm glad to have you on board ${this.name}`);
}*/

/*profile.message = greetings;

profile.message(); // as a method

// greetings(); //as function without strict returns "window object"

greetings(); //as function with strict returns "undefined"*/

/*function Person() {
	this.name = "sodiq";
	console.log(this);
}

let person = new Person(); // parsing a function to a variable using "new" keyword create new object for the variable

let anotherPerson = new Person();
*/

// ----------------------------The use of "call", "apply", and "bind" functions along with "this" function-------------

// Check "intro-to-this-keyword" file.......

// ----------------------------Using "this" with the arrow function--------
// Takeaway: The value of "this" remains the same as the "windows object".

// let square = (x) => x * x;

// console.log(square(6));

// ---------------------------Debugging in javascript------------

/*function factorial(x) {
	let total = 1;
	// for (let i = x; i > 1; i--) total *= i;
	for (let i = x; i > 1; i--) {
		total *= i;
	}

	return total;
}
console.log(factorial(5));*/

// -----------------------Setting "breakpoints" for EventListners

// ------------------------Exemptions handling (throw, catch, finally)
// More details on Mozilla, "Control flow and Error handling"

// doesNotExist();

/*try {
	console.log(myName);
} catch (e) {
	console.log(e);
	// The arg "e" receives the info about the error caught. Although, it's optional
	// And the codes inside the "catch" would executed only if "error" caught.
} finally {
	// The codes inside "finally" is executed either there is an error or not...

	console.log("Hello world");
}

console.log("I'm on the global scope"); */ //The codes outside the "finally" block wouldn't be executed if "catch" is not used.

// ----We can also throw an exemption of various e.g. generic Error, EvalError, ReferenceError, etc. types
// The generic error is as follows,

/*function throwExemption() {
	// throw "DataTypeError: Invalid characters are used within the input values";
	/*throw {
		myType: (function () {
			return "I'm an object";
		})(),
	};*

	throw new Error("I'm an error");

	// The type of the error could be string or object
}

// throwExemption();  // Uncaught error which is called from the windows obj

// -----Caught error is as follows

try {
	throwExemption();
} catch (e) {
	console.log(e);
} finally {
	console.log("Done...");
}*/
