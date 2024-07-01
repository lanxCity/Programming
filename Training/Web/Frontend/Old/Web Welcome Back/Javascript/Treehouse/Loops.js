/* The use of "loops" in javascript */

// 1. The use of "while" loop

// defining a function
/*const getRandomNumber = (upper) => {
	return Math.floor(Math.random() * upper) + 1;
}

// keeping track of the output
let counter = 0;*/

// "while" loop

/*while (counter < 10) {
	console.log(`${getRandomNumber(10)} is a random number generated from 1-10.`);
	counter++;
}*/

// 2. The use of the "do-while" loop

/*do {
	console.log(`${getRandomNumber(10)} is a random number generated from 1-10.`);
	counter++;
} while (counter < 0);*/

// The use of the "for" loop  "for (declare variable; condition; variable stepwise){}"

/*for (counter; counter < 10; counter++ ) {
	console.log(`${getRandomNumber(10)} is a random number generated from 1-10.`);
}

for(let i = 0; i <= counter; i++){
	console.log(`${getRandomNumber(50)} is a random number generated from 1-50.`);
}
*/
/*--------------Class Work----------------*/

/*let body = document.querySelector('#list');

let orderedList = '';

for (let pageCounter = 5; pageCounter <= 100; pageCounter +=5) {

	orderedList += `<li>${pageCounter}</li>`;

	// It's not advisable to include "body.inner..." inside the for loop as it causes the browser to do extra work.
}


body.innerHTML = orderedList;
console.log(orderedList);*/


// Note that you should always improve unimproved codes with DRY principle "Don't Repeat Yourself".


/*-------------Class Work--------------- 

Refactoring: This is the process of improving and simplifying code an existing code without changing its behavior.
*/

/*const getRandomHexadecimal = () => {
	let randomHexadecimal = Math.floor(Math.random() * 256);
	return randomHexadecimal;
}
     OR */ 

 // -------------------Creating function

 const getRandomValue = () => Math.floor(Math.random() * 256);   
 // This automatically return the value.

 /*function getRandomValue() {
 	return Math.floor(Math.random() * 256);
 }*/

function getRandomRGB(value) { 
	const randomRGB = `rgb(${value()},${value()},${value()})`;  
	//The "getRandomValue" get assigned to the "value" parameter, and it would be executed 3x.  
	return randomRGB; 
}      

let body = document.querySelector('#list');

let orderedList = '';

// Creating loops

for (let pageCounter = 1; pageCounter <= 10; pageCounter++) {

	// // Setting colors
	// let red = Math.floor(Math.random() * 256);
	// let green = Math.floor(Math.random() * 256);
	// let blue = Math.floor(Math.random() * 256);

	/*// Creating RGB
	let randomRGB = `rgb(${getRandomHexadecimal()},${getRandomHexadecimal()},${getRandomHexadecimal()})`;*/

	// Stored the value inside the "orderedList" variable 
	orderedList += `<li style = "background-color: ${getRandomRGB(getRandomValue)};">${pageCounter}</li>`;

		// The "getRandomValue" function is treated as a variable so it wouldn't executed b4 getting into "getRandomRGB" function. 
}

body.innerHTML = orderedList;

