//--------------------------Intro to debugging

/*function factorial(x) {
	let total = 1;

	for (let i = x; i > 1; i--) {
		total *= i;
	}

	return total;
}

console.log(`The factorial of 5 is ${factorial(5)}`);

// Using the browser "source breakpoint" to debug

// ---------------Event listener breakpoint

let submit = () => alert("Payment confirmed");*/

// ---------------------Intro to Exemptions (Throw,Catch, Finally)

// For further reading (MDN: Control flow and error handling)
// Runtime error: error that occur while running a program.

/* A. Without "catch" arg
	try {
		statement...
	} catch {
		//But it is used to escape an error and get subsequent codes executed

		catches error if there is one...(optional)
	} finally {
		execute these statement either there is an error or not... 
	}

	N.B: But anything after the entire "exemptions" is not going to be executed except those
	in "finally"
*/

/*B. With "catch" arg
try {
	let message = 19 * b;
} catch {
	console.log("There was an error in 'try' block");
} finally {
	console.log("Hello World! I'm executed either an error is caught or not");
}*/

/*try {
	let message = 19 * b;
} catch (error) {
	console.log(error);
} finally {
	console.log("Hello World! I'm executed either an error is caught or not");
}

alert("I wouldn't be running if an error was caught in the 'catch' block");*/

// C. "throw": used to purposely throw errors

function throwError() {
	let message = "Hi! I'm an error that's purposely thrown";
}

try {
	throw message;
} catch (error) {
	console.log(e);
	console.log("Error was caught!");
} finally {
	console.log("Hello World! I'm executed either an error is caught or not");
}

console.log(name);

let name = "sodiq";
