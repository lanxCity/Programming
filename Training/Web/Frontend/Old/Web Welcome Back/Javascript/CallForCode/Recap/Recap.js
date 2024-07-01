// Recap of the previous videos

//--------------------------Introduction

function confirmButton() {
	const confirm = document.getElementById("confirm");
	const confirmBtn = document.getElementById("confirm-btn");

	confirm.textContent = "Payment Confirmed";
	confirmBtn.style.display = "none";
}

// 1.-----------------------Variable and variable names

// a. var name = "-----", this "name" is called the identifier or variable name
// The above is 2 in 1; declaration and initialization
// i. decoration: is declaring that 'name' exist e.g. "var name;"
// ii. initialization: "name = 'Sodiq'"

// 2. ---------------------Expression

//This is something that evaluates to a value e.g addition = 2 + 54
// "2+54" is an expression yielding a new value.

// 3.---------------------IIFE, Scope, and Window object

// When we create a variable, it get attached to "window object" (also known as the "global scope") as a property.
// To avoid the global scope, codes should be put inside a function. so that when a variable is created,
// it's in a new scope and not the windows object.

// i. create a function decoration, add "()" at the end to invoke it.
//ii. And wrap the whole function inside "()" just after the (executable parenthesis)to turns it to an expression and not just a function

// The above method is called "IIFE" (encapsulation); Immediately Invoked Function Expression

/*(function () {
	var name = prompt("Enter your name please");

	age = 35;

	console.log(
		`Hi ${name.toUpperCase()} of ${age} years old! Welcome to LanxCity.`
	);
	alert(`Hi ${name.toUpperCase()} of ${age} years old! Welcome to LanxCity.`);
})();*/

// NB: This is where the use of "var" is essential. If a variable is not defined, but initialized
// the engine would looks up to outer scopes to see if that variable has already been defined.
// And if not, the engine defines it automatically and attach the variable to window pprties.
// e.g. "age" variable. And that means the use of "IIFE" is useless.

// 4. --------------------JS engine and environment

// --------Firefox: SpiderMonkey
// --------Chrome: V8
// --------MicrosoftEdge: Shakra
// --------Safari: Nitro

//a. Compiler: One Time and Just In Time (JIT)

// i. One Time: like "fortran", compile the source code and gives you a new file to execute
// ii. JIT: compile the code (but still keeping the source code) and execute it or run it line by line.

// b. interpreter

// Takeaway::: JS could also be a compiled language on the justification that it throws error (if there is any) before anything could runs.

// 5.----------------------Global and local variables

// *** The "window object" is the global scope.
// That is,
// Function level variable: is a variable limited to that scope or func alone using "var".
//But if "var" is used anywhere else (including "if" block) aside function, it would still looks up to nesting or parent function (if exist) or windows object .

/*var name = "Lanx";

if (name === "ALADE") {
	alert(`Hello ${name}!`);
} else {
	var newName = "Alade";
	alert(`Hello ${newName}!`);
}*/

//***Therefore, the advent of "let" and "const" allows the creation of "block level variable" within the "block level scope"
// Block level variable: is a variable created within a block, e.g. "if" using "let" or "const"
// without going out of that block.

//In replace of IIFE or function scoping, block scoping was along with "let" and "const"
// that is, "{}" and using "let" for declaration

// The block scoping
/*{
	let name = "Sodiq";
	const age = 25;

	// Let's try "var" and see that we can still access it. And it's only 
	// looking out for the object scope. 
	//therefore, "var" is "function level" variables.
 
	var matNum = 200268;

	console.log(
		`I am ${name} of matric no. ${matNum}. I'm ${age} years of age.`
	);
}*/

// 6.---------------------------------- Primitives and objects

// JS is a dynamically typed language and some are statically typed language.

//6A. Primitives data type: str,num,boolean,undefined,null,symbol.

// Coercion occurs between these types; converting from a data type to another (usually to strings).
// primitives are immutable calling ppties or methods on them don't affect their original state

/*{
	let num = 55;
	let str = "1000";

	let coerce = num + str; //using "+" is a method of concatenation.

	console.log(coerce);

	//--------- Diff btw "undefined" and "null"-------------------

	let username = prompt("Enter your name please");

	alert("Hi " + username);
}*/

// i.---------Primitives also have their object versions such as "new String()", "new Number()", etc
// And those object versions have both prpties and methods.
// Therefore, once primitives are used, usually "str" and "number", they are first converted their respective object versions behind the scene
// which allows the use of prpties and methods on them.

/*{
	let name = "Sodiq";
	console.log("the initial name is " + name.toUpperCase());
	console.log("I'm a primitive " + typeof name);

	// the process of the above "name.toUpperCase()" is the following. because primitives don't have prpties and methods

	name = "Sodiq" //primritve

	new String("Sodiq").toUpperCase(); //object & terminate

	console.log(
		"I'm an object but converted to primitive string " +
			'"' +
			name.valueOf() +
			'"'
	); //terminate to become primitive again.....

	console.log(typeof name);
}*/

//6B. objects: arrays, functions, and objects.

// 7. -----------------Numeric data type

// i. Max and min-number 64bits can accept. At this point, not all numbers can be represented as binary.

// 2**1023 to 2**1024

/*let maxNum = Number.MAX_SAFE_INTEGER;

console.log(maxNum);
*/

/*maxNum = Number.MAX_SAFE_INTEGER + 3; //this can't be converted.

console.log(maxNum);*/

/*let maxNum = Number.MAX_SAFE_INTEGER + 2;

console.log(Number.isSafeInteger(maxNum));*/

/*maxNum = 2 ** 52.99999999999;

console.log(maxNum, Number.isSafeInteger(maxNum));*/

// ii. --------------------------3 special numbers that is with 64bits are Infinity, -Infinity, NaN.

/*let special_1 = Number.MAX_SAFE_INTEGER ** 201; //or Infinity (1/0)

let special_2 = Math.pow(-Number.MAX_SAFE_INTEGER, 201); //-Infinity (1/-0)

let special_3 = NaN;

console.log(`Special numbers are ${special_1}, ${special_2}, ${special_3}.`);

console.log(
	`The type of those special numbers are ${typeof special_1}, ${typeof special_2}, ${typeof special_3}`
);*/

// iii. ------------Using "parseInt()" to convert from diff bases to base 10

// parseInt("num", the Base of the number entered) returns decimal

/*let userBase = prompt("Base of the value to be converted to 'decimal'");

let userInput = prompt("Enter the value to convert to decimal number please");

switch (Number(userBase)) {
	case 2:
		console.log(
			`Binary ${userInput} is "${parseInt(userInput, 2)}" in decimal`
		);
		break;

	case 8:
		console.log(
			`octal ${userInput} is "${parseInt(userInput, 8)}" in decimal`
		);
		break;

	case 16:
		console.log(
			`hex ${userInput} is "${parseInt(userInput, 16)}" in decimal`
		);

		// you must enter letters to rep from 10 and above e.g. 10 ~ a, 15 ~ f, etc.
		break;
	default:
		console.log("Sorry, that base is not available");
		break;
}*/

// --------------------password checker revision------------

/*let name = prompt("Enter your name please");
let password = prompt("Create new password");

hiddenPassword = "";

for (let i = 0; i < password.length; i++) {
	hiddenPassword += i === password.length - 1 ? password[i] : "*";

}

alert(
	`Hi ${name}! Your password ${hiddenPassword} is of ${password.lenggth} characters`
);*/

// let matrix = [
// 	[2, 3, 4],
// 	[1, 2, 3],
// 	[0, 3, 1],
// ];

// let myMatrix = "";

// matrix.forEach((row) => {
// 	for (i in row) {
// 		myMatrix += row[i];
// 	}
// 	myMatrix += "\n";
// });

// console.log(myMatrix);
