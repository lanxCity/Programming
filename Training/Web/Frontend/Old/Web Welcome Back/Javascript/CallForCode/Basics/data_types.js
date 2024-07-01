/*
1. Introduction to Data types.

----------Two Types of data types

a. Primitives:- string,number,boolean,undefined,null,symbol(new)
b. Objects:- Array,Object, and function. All these are categorized as "object"
	because of what is known as a the "prototype chain"; it's basically to say 
	"javascript inheritance". S

Note: A function created inside an object is called a method, 
	and a key is called a prpty 

*/

// Objects

/*
a. Defining the object
*/

/*let person = {
	name: 'Lanx',
	age: 30,
	email: 'sodiqramon0@gmail.com',
	greeting: function(name) {

		message = `Hi ${name}.`;

		return message;
	}
}

console.log(person.greeting(person.name))*/

// let grades = [30,40,50];

/*
	b. Apart from defining "object" by yourself, we also have other 
	objects such as "Date" object 
*/

let today = new Date();

console.log(today);

/*2. Difference between primitives and objects
	=> Primitives have no property or methods. But when assign any prpty or method to them, 
	they are converted to an object behind the scene, and return them to primitives after that 
	certain action has been performed. 

	E.g. "name.toUpperCase" returns uppercase and turn it back to string. which means primitives 
		are immutable; they can't be changed 

	Except we declare primitives this way; "let name = new String('Lanx')", and that is an object.

*/

let name = "Akanmu Olayode";
name.toUpperCase();

// ----------------the process of using method or prpty on primitives

/*name = new String(name); //it's turn to an object

console.log(name.toUpperCase()) //action is carried out

name = name.valueOf(); //And turns back to string.

console.log(typeof name);*/

/*3. --------------------------------The numeric data type*/

// -----------------Checking the maximum digit we could stored in programming.

/*let x = 560;

let y = new Number(1000);

console.log(Number.isSafeInteger(x));

console.log(Number.MAX_SAFE_INTEGER);

// LET'S SAY

max_int = 9007199254740995;  //the maximum safe integer

console.log(Number.isSafeInteger(x));

console.log(x);*/

// ------Representing "infinity","-infinity","NaN" using numbers

// "pow(the value, exp)"

/*console.log(`The exponential of maximum integer is ${Math.pow(max_int, 200)}`);
console.log(`The exponential of maximum integer is ${1/0}`);

console.log(`The exponential of maximum integer is ${Math.pow(-max_int, 201)*2}`);
console.log(`The exponential of maximum integer is ${-1/0}`);

console.log(name - 5) //if you use "+", concatenation occurs*/

// ---------------Arithmetic operation, precedence, and Associativity.
/*
a. (*, /, %) have equal precedence
*/

/*let precedence1 = 5+2/5-10*3+10;
console.log(precedence1);

let precedence2 = 5+(2/5)-(10*3)+10;
console.log(precedence2)*/

// -----------Properties and method of a number

//a. ParseInt() and ParseFloat

/*let x = "17";
let y = 10;

// let xInt = Number.parseInt(x);
// let xInt = Number(x); //-----------------either of the 3 is correct
let xInt = parseInt(x);

console.log(y+x)
console.log(xInt + y)
*/

// b. Converting decimal numbers to binary, octal, & hexadecimal.

// let input = parseInt(prompt('Enter a number to convert'));

// let input = Number(prompt('Enter a number to convert'));

// the following returns the decimal of the input
/*console.log('user input in base 10 is =', parseInt(input,10));
console.log('user input from base 2 to base 10 is =', parseInt(input, 2));
console.log('user input from base 8 to base 10 is =', parseInt(input, 8));
console.log('user input from base 16 to base 10 is =', parseInt(input, 16));*/

// To covert decimal to other bases, we have the following:

// console.log(input, ' base ten to base two is ', input.toString(2)); // the input type must be 'number'.

// the above convert the input number to the "radix" before to string.

// c. Number instance methods and Math object

/*There are two ways to call methods when it comes to numbers
a. Number.method()---------------- "new Number()" is an object constructor
b. primitive.method() ----------primitive is called "instance"
*/

/*let numberObj = new Number(40);
console.log(numberObj.toString(2));

let ordinaryNum = 30;
console.log(ordinaryNum.toString(16));*/

//-------- Some Number methods

/*let number = new Number(3000574);

console.log(number.toExponential(6)) // this returns the exp of the number; 3.000574e+6 means 3 * 10^6. nums after the decimal
console.log('Account balance: $' + number.toFixed(2))
console.log(number.toPrecision(6)) //to significant digits
console.log('Account balance: $' + number.toLocaleString())
console.log(number.valueOf()) //return the object "Number" to primitive.
console.log(typeof(number.valueOf()))



// The "Math" object

{
	// block

	let goUp = Math.ceil(0.999); //1
	let goDown = Math.floor(4.788) //4
	let roundUp = Math.round(5.76) //6
	let roundDown = Math.round(5.4) //5
	let power = Math.pow(5,3) // 5^3 = 125
	let absolute = Math.abs(-12.64) //12.64
	let truncation = Math.trunc(5.8768787878) // 5
	let isPositive = Math.sign(-Infinity) // -1(false)
}*/

/*---------------------The String data type*/

{
  let myName = "Olawale";

  // Using special characters with strings
  let myFullName = "Sodiq\nRamon\nDamilare";
  console.log(myFullName);

  // Accessing each letter of the string using "array-like syntax"; [] and string methods.
  console.log("The fourth character of my name is ", myName[3]);
  console.log(myFullName[6]);
  console.log(myFullName.charAt(12)); //same as myName[12]
  console.log(myFullName.indexOf("Ramon", 7));
  console.log(myFullName.lastIndexOf("Ramon")); //backward searching
  console.log(myFullName.concat(" is my name."));
  console.log(myFullName.includes("Sodiq")); //returns "true" or "false"
  console.log(myFullName.substring(6, 11)); //substring(startIndex,stopIndex) and the last argument isn't included
  console.log(myFullName.substr(0, 10)); // the 2nd argument is the length of characters we want from the 1st arg.
  console.log(myFullName.slice(6, 11)); // cut a portion of the string from the start index to the end(not included) index
  console.log(myFullName.trim()); //removes any extra spaces b4 and after the text.
  // in addition, we have trimLeft(),trimRight() or trimStart(),trimEnd().
  console.log(myFullName.split("\n"));

  console.log(myFullName.search("a")); //Searches the letter "a" within the myName variable
  console.log(myFullName.repeat(3)); // Repeats the string 3times
  console.log(myFullName.replace("lawale", "yewale")); //replaces old string with new string ("old string", 'new string')
}
