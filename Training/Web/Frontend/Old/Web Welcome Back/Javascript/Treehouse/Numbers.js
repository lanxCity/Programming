const name = prompt('Your name please?');


// --------------Class work-------

// declaring variables
/*const secondsPerMinute = 60;
const minutePerHour = 60;
const hoursPerDay = 24;
const daysPerWeek = 7;
const weekPerMonth = 4;
const weekPerYear = 52;
const monthsPerYear = 12;

// declaring conversion variables
const secondsToHour = secondsPerMinute * minutePerHour;
const secondsToDay =  secondsToHour * hoursPerDay;
const secondsToWeek =  secondsToDay * daysPerWeek;
const secondsToYear = secondsToWeek * weekPerYear;

//Getting user's input and output message

const yearsAlive = prompt(`How old are you ${name}?\nAnd let's convert it to seconds for you.`);

const  yearAliveToSeconds = +yearsAlive * secondsToYear;

alert(`Yo ${name}! You've used ${yearAliveToSeconds} seconds on earth.\nAge with no limit ahead.`);
console.log(`Yo ${name}! You've used ${yearAliveToSeconds} seconds on earth.\nAge with no limit ahead.`);*/


// 1. Converting "strings" to "integers" by using methods (parseInt() and parseFloat()) and "typeof" operator to check the data type.

let gibbrish = "34lanx";

console.log(parseInt(gibbrish));

/* 2. Javascript objects. And it includes primitive objects (strings, boolean, and numbers), math object, etc. Objects usually have properties (some sets of variables attached to each obj) and method (some functions used to perform action on obj). 

----- All the datatype are treated as object. 
And which unlock some useful functionalities such as "properties" and "method"

---- 2a. The Math object (a built-in library)

---- Math method include .random(), .floor(), .ceil(), etc.

a) .random() displays numbers between 0(inclusive)-1
*/

const leastOutcome = 1;

const  mostOutcome = 6;

const die = Math.floor((Math.random() * mostOutcome)) + leastOutcome;

console.log(die);

//--------------------class work----------

/*let userRange = prompt(`Please enter any number to generate any number for you from 1 to the number entered`);
let highNumber = parseInt(userRange);

let randomNumber = Math.floor(Math.random() * highNumber)  + 1;

if (isNaN(parseInt(userRange))) {

	alert("You've entered no number");	
} else {

	alert(`${randomNumber} is the number generated for you between 1 and ${highNumber}.`);
}*/

/*let leastRange = prompt(`Please enter any least number to generate a number for you ranging from this least to highest number you'll enter next.`);
let leastNumber = parseInt(leastRange);

let highestRange = prompt(`Please enter any highest number`);
let highestNumber = parseInt(highestRange);

let randomNumber = Math.floor(Math.random() * ((highestNumber-leastNumber) + 1))  + leastNumber;

if (leastNumber && highestNumber) {

	alert(`${randomNumber} is the number generated for you between ${leastNumber} and ${highestNumber}.`);	
} else if (!leastNumber && !highestNumber) {

	alert(`Sorry, Both the least value and the highest value you've entered are not numbers`);
} else if (!leastNumber) {

	alert(`Sorry, the value you entered as your least value was actually not a number.`);
}  else if (!highestNumber) {

	alert(`Sorry, the value you entered as your highest value was actually not a number.`);
} */


