/* ------------------A. Introduction to Objects

An object is a variable or an element that has properties and method.
e.g built in objects (Math, console, etc.), string, array, etc.

It allows the storage of data using "key: value" or "property: value" pairs.
A "key" or "property" name is like a variable name while the "value" is like
a value assign to the variable.

In summary, an object is single item that holds multiple variables.

In creating object, we use "object literal" or "{}".


Diff btw Array and Object

1. You access array elements using "index value" or position while Object
	uses a "key" or "property name" to access its element.
* 

let food = ['yam','beans','amala'];

const student = {
	name: 'Waris',
	age: 20,
	isStudent: true,
	courses: ['MAT221','ENG211', 'ENG212', 'ENG213', 'ENG215'],
	grades: [68,72,72,93,83]
};

console.log(student['courses']); /*One method*

console.log(student.grades); /*Another method*

// Note the following
console.log(food['length']); /* OR*
console.log(food.length);


/*--------------------B. Adding new value or properties to an object*

student.name = 'Gabriel'; /* New value *
student.city = 'Ibadan'; /* New property and value*

console.log(student);


/*------------------C. Accessing elements of a property using "bracket notation" "[]" */

/*for (key in student) {

	console.log(key);
}*

for (let propties in student) {

	console.log(`${propties}: ${student[propties]}`);
}

for (let propties in student) {

	console.log(`${propties}: ${student['name']}`);
}

/*for (let prop in student) {

	console.log(student[prop]);
}*

console.log(Math.max(student['grades'])); /*Returns NaN*/


/* Array of objects */

const quiz = [
	{
		question: 'How many continents do we have in the world?',
		answer: 7
	},

	{
		question: 'South Korea is located in what continent?',
		answer: 'ASIA'
	},

	{
		question: 'There are how many states in Nigeria?',
		answer: 36
	},

	{
		question: 'What is the official language that is used in Nigeria (without "LANGUAGE" included)?',
		answer: 'ENGLISH'
	},

	{
		question: 'Nigeria became republic immediately after independence in what year?',
		answer: 1963
	}
];

/*const quiz = {
	questions: [
		'How many continents do we have in the world?',
		'South Korea is located in what continent?',
		'There are how many states in Nigeria?',
		'What is the official language that is used in Nigeria (without "LANGUAGE" included)?',
		'Nigeria became republic immediately after independence in what year?'
	],
	answers: [
		7,
		'ASIA',
		36,
		'ENGLISH',
		1963
		]
};*/

/*let numbering = 1
let correctAnswers = 0;
/*let questionsGotten = '';
let questionsMissed = ''; *

let questionsGotten = [];
let questionsMissed = []; 


for (let i = 0; i < quiz.length; i++) {

	let question = quiz[i].question;
	let answer = quiz[i].answer;

	let userInput = prompt(`${numbering}. ${question}`);

// creating new array on the page

	if (!userInput) {

		alert(`You got it wrong because you entered no value!`);
		/*questionsMissed += `<li>${question} ${answer}</li>`;*

		questionsMissed.push(`${question} ${answer}`);
	}
	else if (userInput.toUpperCase() === answer || parseFloat(userInput) === answer) {

		alert(`Correct!`);
		correctAnswers++;
		/*questionsGotten += `<li>${question} <br> Your answer was ${userInput}</li>`;*

		questionsGotten.push(`${question} <br> Your answer was "${userInput}"`);
	} else {

		alert(`Sorry, the correct answer is ${answer}`);
		/*questionsMissed += `<li>${question} ${answer}</li>`;*

		questionsMissed.push(`${question} ${answer}`);
	}

	numbering++;
}


// Create function to get list of items from the new array

function getListItems(listOfItems) {

	/*for (let i=0; i<menu.length;i++) {
		menuList += `<li>${menu[i]}</li>`;
	}*

	// Or for general purposes, we assign the function a parameter.

	let items = '';

	for (let i=0; i < listOfItems.length; i++) {

		items += `<li>${listOfItems[i]}</li>`;
	}
	return items;
}


// Test outcome the page

let testOutcome =  document.querySelector('main');

if (correctAnswers === 10) {

	testOutcome.innerHTML = `
	<h1>Excellent ${userName.toUpperCase()}! You got all the ${correctAnswers} questions correctly.</h1>
	<p>You got all the questions correctly:</p>
	<ol>
		${getListItems(questionsGotten)}
	</ol>`;

} else if (correctAnswers >= 8) {

	testOutcome.innerHTML = `
	<h1>Great! You got ${correctAnswers} correctly out of ${quiz.length} questions.</h1>
	<p>You got the following questions correctly</p>
	<ol>${getListItems(questionsGotten)}</ol>
	<p>And you got these other questions wrongly</p>
	<ol>${getListItems(questionsMissed)}</ol>`;
 
} else if (correctAnswers >= 5) {

	testOutcome.innerHTML = `
	<h1>Good job! You got ${correctAnswers} correctly out of ${quiz.length} questions.</h1>
	<p>You got the following questions correctly</p>
	<ol>${getListItems(questionsGotten)}</ol>
	<p>And you got these other questions wrongly</p>
	<ol>${getListItems(questionsMissed)}</ol>`;
 
} else if (correctAnswers >= 1) {

	testOutcome.innerHTML = `
	<h1>Nice! You got ${correctAnswers} correctly out of ${quiz.length} question(s).</h1>
	<p>You got the following questions correctly</p>
	<ol>${getListItems(questionsGotten)}</ol>
	<p>And you got these other questions wrongly</p>
	<ol>${getListItems(questionsMissed)}</ol>`;

} else {

	testOutcome.innerHTML = `
	<h1>Sorry, You got ${correctAnswers} correctly out of ${quiz.length} questions.</h1>
	<p>And they are as follows:</p>
	<ol>${getListItems(questionsMissed)}</ol>`;
}*/


/*-------------------Class Work------------------
	Create an array of "pet" object. And each object should have the following properties:

	Name, Type, Breed, Age, and Photo.
*/

const petDirectory = [
	{name: 'Joey', type:'Dog', breed: 'Australian Shepherd', age: 8, photo: 'aussie.jpg'},
	{name: 'Patches', type:'Cat', breed: 'Domestic Shorthair', age: 1, photo: 'tabby.jpg'},
	{name: 'Pugsley', type:'Dog', breed: 'Pug', age: 6, photo: 'pug.jpg'},
	{name: 'Simba', type:'Cat', breed: 'Persian', age: 5, photo: 'persian.jpg'},
	{name: 'Comet', type:'Dog', breed: 'Golden Retriever', age: 3, photo: 'golden.jpg'}
];


let container = '';

let main = document.querySelector('main');

for (let file = 0; file < petDirectory.length; file++) {

	/*let name = petDirectory[file].name;
	let type = petDirectory[file].type;
	let breed = petDirectory[file].breed;
	let age = petDirectory[file].age;
	let photo = petDirectory[file].photo;*/

	let pet = petDirectory[file];

	container += `<div>
					<h2>${pet.name}</h2>
					<h3>${pet.type} | ${pet.breed}</h3>
					<p>Age: ${pet.age}</p>
					<img src="./img/${pet.photo}" alt="${pet.breed}">
				  	<hr noshade="">
				  </div>`
				  ;
}
	/*"pipe char" or "vertical bar" = | */

main.insertAdjacentHTML('beforeend',container);

/*The "insertAdjacentHTML" placed the element inside the main without tampering with
already exist elements. And the "beforeend" string placed the element just before the end of the container;
after all the previously existed elements*/