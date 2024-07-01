/* ---------------The uae of function in javascript-------- */

// A. -----------"Function Decoration" (the normal method of declaring a
// function)---

//Note that you can call a function decoration before declaring the function.
//Because it loads before any code is executed.------------

// 1. Introduction

/*function getRandomNumber() { const randomNumber = Math.floor(Math.random
  () * (6-1+1)) + 1; alert(randomNumber); }

getRandomNumber();*/

/*function getRandomNumber() { const randomNumber = Math.floor(Math.random
  () * (6-1+1)) + 1; return randomNumber; }

console.log(getRandomNumber());*/

// 2. Using "multiple" returns in a function by verifying a from field

/*function isFieldEmpty() { const userName = document.querySelector
  ('#username'); if (!userName.value) {

		return true; } else {
		
		return false; } }

const testField = isFieldEmpty(); 

if (testField) {

	alert('Please enter your username!'); }*/

// 3. Pass information into a function (argument and parameters)

/*//userName function function greetings (name) /*parameter* { alert(`Hello $
    {name.toUpperCase()}! Welcome to my website.`); alert('Please enter the
    dimensions of the rectangle you need to calculate.') }

// Rectangle calculating function function getAreaOfRectangle
   (widthPara,lengthPara,unitPara = "ft") { const area = widthPara *
   lengthPara; alert(`The area of the dimensions ${widthPara} x $
   {lengthPara} sq ${unitPara} gives ${area} sq ${unitPara}.`); }

// Code for username and rectangle calculation.

const username = prompt('Your name please?');

if (!username) {

	alert('Hi'); } else {

	greetings(username);

	// For the rectangle

	let widthEntered = prompt('Enter the width.'); let lengthEntered = prompt
	('Enter the length.'); let unit = undefined;

	const width = parseFloat(widthEntered); const length = parseFloat
	(lengthEntered);

	// Setting condition

	if (!width || !length) {

		alert("You've entered no number(s) in either or both of the field
		(s)."); } else {

		 getAreaOfRectangle(width,length,unit); } }*/

/* 4. "Scope" in javascript; (scope is the context in which values are visible
   or can be reference)the use of same variable name within and outside a
   function.*/

/*let name = 'Waris';

function greetings () { name = 'Sodiq'; //not declaring the local variable
using "let" or "const" affect the global variable. alert(`Good evening $
{name}.`); }

alert(`Hello ${name}!`); greetings(); alert(`Hello ${name}!`);*/

// B.-------------- "Function Expression" (defining functions by assigning to
// a variable)------

// A function without a name after the "function" keyword is
// called "Anonymous" function. Therefore, ";" come after the "{}".

/*let name = 'Waris';

const greetings = function() { name = 'Sodiq'; //not declaring the local
variable using "let" or "const" affect the global variable. alert
(`Good evening ${name}.`); };

alert(`Hello ${name}!`); greetings(); alert(`Hello ${name}!`);*/

// C. Arrow function expression

/*let name = 'Waris';

const greetings = () => { name = 'Sodiq'; //not declaring the local variable
using "let" or "const" affect the global variable. alert(`Good evening $
{name}.`); };

alert(`Hello ${name}!`); greetings(); alert(`Hello ${name}!`);*/

// D. Default parameters for a function. By assigning a default value to the
// parameter right inside the function

/*const greetings = (name = 'Students') => { alert(`Good evening $
  {name}.`); };

greetings('Engr. Lanx');*/

// 1. Default for multiple params.

/*const sayGreeting = (greeting ='Good Morning',name = 'Students') =>{ return
  (`${greeting}, ${name}.`); };

alert(sayGreeting(undefined,'Engr. Lanx')); // The undefined instruct that
default should be used. */

/*---------------Class Work------------------------*/

const getRandomNumber = function (leastRange, highestRange) {
	if (isNaN(leastRange) || isNaN(highestRange)) {
		// Verifying the input values are numbers.

		throw Error("Sorry, both values must be numbers.");
	}

	const randomNumber =
		Math.floor(Math.random() * (highestRange - leastRange + 1)) + leastRange;

	return randomNumber;

	/*const randomNumber = (isNaN(leastRange) || isNaN(highestRange)) ? alert
	  ("Sorry, both values must be numbers.") : Math.floor(Math.random() * (
	  (highestRange - leastRange) + 1)) + leastRange;

	return randomNumber;*/
};

alert(
	"Welcome! You can generate a random number within the range of numbers\
you would enter next."
);

const leastNumber = parseInt(prompt("Enter any lowest number you want."));
const highestNumber = parseInt(prompt("Enter any highest number"));

alert(`${getRandomNumber(leastNumber, highestNumber)} is a random number
generated from ${leastNumber} and ${highestNumber}.`);

/*Other method*/

/*const getRandomNumber = function (leastRange,highestRange = 100) {

	if (isNaN(leastRange) || isNaN(highestRange)) {
		
		throw Error("Sorry, both values must be numbers."); }
		
	return Math.floor(Math.random() * ((highestRange - leastRange) + 1)) +
	leastRange;

}

console.log(`${getRandomNumber(10,'six')} is a random number generated from 10
and 100.`);*/
