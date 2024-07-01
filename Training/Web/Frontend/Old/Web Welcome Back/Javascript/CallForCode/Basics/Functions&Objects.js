// 1. Objects

{
	// Creating object
	let oldData = {
		x: 10, //prpty
		y: 20,
		print: function () {
			console.log("This is this: ", this);
			console.log(`X is ${this.x} and Y is ${this.y}`);

			//using "this" method points to the properties in the object directly.
		},
	};

	// Creating primitive
	let myName = "Lanx";

	/*------------------Parsing object and primitive to new variable-------------
		
		Diff between objects and primitives is their behaviour when parsing 
		them to variables.

	*/

	//-------- primitive before reassignment
	let newName = myName;

	// console.log(`This the original name: ${myName}`);
	// console.log(`This the new name before reassignment: ${newName}`);

	// object before reassignment
	// let newData = oldData;

	// // console.log(oldData);
	// // console.log(newData);

	// // -----------primitive after reassignment
	newName = "Sodiq";
	// console.log(`This the original name after reassignment: ${myName}`);

	// // object after reassignment
	// newData.x = 60; // This will reflect in the oldObject
	// newData.z = 1000; // This will reflect in the oldObject
	// console.log(oldData);

	// /*-----------------Calling function and the use of "this" inside a function created within an object----------*/

	// oldData.print(); //object method

	function print() {
		console.log(this.name);
		console.log(`Name is ${this.myName} and new name is ${this.newName}`);

		//using "this" method points to the properties in the object directly.
	}

	print();

	/*var name = "hello world";
	//using "let" wouldn't make the variable the prpty of window

	console.log(this.name);*/

	//--------------------------- NB: The value of "this" depends on the way we call a certain function;
	// A. Function as Method (usage of func inside an object): Using "this" inside of such func refers
	// to the "parent object" directly.

	// B. Function in the global scope(calling function as a func): The values of "this" is either
	// refers to the window object or undefined (when a function is in the "strict" mode).

	// TAKEAWAY: The concept of what "this" means is known as the function context; The function context
	// of a method, "this" is always refers to that instance of the object. Which in contrast to calling
	// function as a func but not as a method

	// ---------JSON: Javascript object notation
	// This is where the properties have quotation (just like in python)
	// This is important in that JSON would be used when one is working with website through an API,
	// and also for configuration in different Frameworks.
}
