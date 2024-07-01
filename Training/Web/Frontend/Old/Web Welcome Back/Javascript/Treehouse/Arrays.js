// -------------A. Introduction: An array is referred to as data structure. It's a way to store and organize (multiple) data.

/*const names = [
	'Aisha',
	'Ife',
	'Waris',
	'Ridwan',
	'Segun',
	'Edward',
	'Emmanuel',
	'Abdulrasheed',
	'Kareemot',
	'Muhammad'
	];

let kitchenUtensils = [
	'Knife',
	'Dishes', 
	'Stirrer', 
	'Cooking equipment'
	];*/

// console.log(typeof names);

// -------------B. Pointing a value inside an array, we use "index" value. Because programming are "zero based" or "zero indexed".

/*for (let i=0;i<=names.length;i++) { coming back to this

	console.log(`${names[0]}`);
} */

/*console.log(`${names[0]}\n${names[1]}\n${names[2]}\n${names[3]}`);*/

/*  -------------C. Adding and removing elements to arrays (Mozilla Developer Network)
	---Prpties and methods of an array

	a) length,prototype (properties)
	b) indexOf(), push(), unshift(), etc.
	*/

// 1. Adding new items to the end of an existing list using "push()" method.

/*console.log(names.push('Sodiq','Rasheed', 'Kareemot')); //returns the number of total items


// 2. Adding new items to the beginning an existing list using "unshift()" method.

names.unshift('Adigun', 'Iqmah', 'Fatimah'); //Will also returns the number of total items

console.log(names);
console.log(`There are ${names.length} names in the list.\n`);*/

// 3. Removing item from the end of an existing list using "pop()" method (the opposite of push).
/*let lastName = names.pop();  //returns the last item removed.

console.log(names+"\n");

console.log(lastName);*/

// 4. Removing item from the beginning of an existing list using "shift()" method (the opposite of unshift()).

/*let firstName = names.shift(); //returns the first item removed.

console.log(names+"\n");
console.log(firstName);*/

//.-------------D. Combining and manipulating of arrays using "spread" operator using "...nameOfTheArray".

//let firstAndEnd = ['First',names,'End'];   //This shows a list inside a list

/*let firstAndEnd = ['First',...names,'End'];  // The "..." operator or syntax removes the list values and combine with the new list.
console.log(firstAndEnd);

let swallow = ['Amala', 'Eba', 'Pounded yam', 'Fufu', 'Semovita'];
let otherFood = ['Rice', 'Beans', 'Tuwo', 'Yam', 'Pap'];

let food = [...swallow,...otherFood];

console.log(food);

otherFood.push('Bread');

console.log(otherFood);

console.log(food); //This means even though "otherFood" array is updated, it doesn't reflect in the "food" array.*/

// "Spread" operator can also be used to pass array as an argument to a function.

/*let numbers = [10,20,30,40,50];
console.log(Math.max(numbers)); //This returns "NaN"...........................
console.log(Math.max(...numbers));*/

//----------------- E. Loop through an array or Iteration

/*const randomValue = () => Math.floor(Math.random()*((255-1)+1)) + 1;

function getRandomValue(value) {
	let randomRGB = `rgb(${value()},${value()},${value()})`;
	return randomRGB;
}

let orderedList = '';

for(var i = 0, length1 = names.length; i < length1; i++){
	// console.log(names[i]);

	orderedList += `<li style = "background: ${getRandomValue(randomValue)};" >${names[i]}</li>`;
}

document.querySelector('#list').innerHTML = orderedList;*/

/*---------------Quiz game--------*/

/*let numbering = 1;

const questions = [
	'How many continents do we have in the world?',
	'South Korea is located in what continent?',
	'There are how many states in Nigeria?',
	'What is the official language that is used in Nigeria (without "LANGUAGE" included)?',
	'Nigeria became republic immediately after independence in what year?'
];

const answers = [
	7,
	'ASIA',
	36,
	'ENGLISH',
	1963
	];

for(let i = 0, length1 = questions.length; i < length1; i++){

	let userInput = prompt(`${numbering}. ${questions[i]}`);

	if (userInput.toUpperCase() === answers[i] || parseFloat(userInput) === answers[i]) {
		alert("Correct");
	} else {
		alert("Sorry, you are wrong");
	}

	numbering++;
}*/

/*------------- F. Some other "array methods" e.g. indexOf(), includes(), join() */

/*const userName = prompt('Your name please?');


const nameEmptied = () => {

	if(!userName) alert("You didn't enter a name!");
}

function getUserNames() {
	
	let userNames;

	if (!nameEmptied()) {

		userNames += userName;
		
	} else {
		nameEmptied();
	}
	return userNames;
}

console.log(getUserNames());
*/
// 1. join()

/*let combineNames = names.join(': ');
console.log(combineNames);
console.log(names.length);

// 2. split();

let splittedNames = combineNames.split(': ');
console.log(splittedNames);
*/

// 3. "includes()" returns "true" if a particular item is present in a list;

/*console.log(names.includes('Abdulrasheed')); //Case sensitive

// 4. "indexOf()" returns the position of an element in a list

console.log(names.indexOf('Abdulrasheed')); 
console.log(names.lastIndexOf('Aisha'));
*/

// --------------Menu section
/*let menu = ['RICE','BEANS','CHICKEN', 'FISH',
	'SALAD','CHIPS','CHICKEN AND CHIPS','PLANTAIN',
	'AMALA','POUNDED YAM','SEMOVITA','SOFT DRINK','BOTTLE WATER'
	];

function getMenuList(listOfItems) {

	/*for (let i=0; i<menu.length;i++) {
		menuList += `<li>${menu[i]}</li>`;
	}*

	// Or for general purposes, we assign the function a parameter.

	let menuList = '';

	for (let i=0; i<listOfItems.length;i++) {

		menuList += `<li>${menu[i]}</li>`;
	}
	return menuList;
}

let search = prompt('Search for your favorite. Or press "OK" to view what we have.');

// -----------------Messages section

let message = document.querySelector('main');


if (!search || !isNaN(search)) {

	message.innerHTML = `<p id="menu-title">OUR MENU</p>
		<ol>${getMenuList(menu)}</ol>`;

} else if (menu.includes(search.toUpperCase())) {

	message.innerHTML = `<p>Yes, we have <strong>${search.toUpperCase()}</strong>. 
				It's #${menu.indexOf(search.toUpperCase())+1} on the list.</p>`;
} else {

	message.innerHTML = `<p>Sorry, we do not have <strong>${search.toUpperCase()}</strong>.</p>`;
}*/

// ------------- G. Multidimensional Array: A list containing other lists

// ---1. Two dimensional array: (Think of it as a spreadsheet; list within a list)

let grades = [
	[80, 64, 90],
	[70, 65, 87],
	[65, 88, 64],
];

// Accessing the element within the multidimensional array

console.log(`The first grid in the last array is ${grades[2][0]}`);

/* ---------- Class work ------------------*/

/*let playList = [
	['Insha Allah','Beat it','Thriller','The chosen one','Awaken','Hold my hands'],
	['Maher Zain','Michael Jackson','Michael Jackson','Maher Zain','Maher Zain','Maher Zain'],
	['4:30','3:01','3:49','4:02','3:39','4:30']
];

function createPlayList(list) {

	let orderedList = '';

	for (let i = 0; i < list[0].length; i++) {
		orderedList += `<li>${playList[0][i]}, by ${playList[1][i]} - ${playList[2][i]}</li>`;
	}
	return orderedList;
}*/

/*let playList = [
	['Insha Allah', 'Maher Zain', '4:30'],
	['Beat it', 'Michael Jackson', '3:01'],
	['Thriller', 'Michael Jackson', '3:49'],
	['The chosen one', 'Maher Zain', '4:02'], 
	['Awaken', 'Maher Zain', '3:39'],
	['Hold my hands','Maher Zain','4:30']
];

function createPlayList(list) {

	let orderedList = '';

	for (let i = 0; i < list.length; i++) {
		orderedList += `<li>${playList[i][0]}, by ${playList[i][1]} - ${playList[i][2]}</li>`;
	}
	return orderedList;
}

document.querySelector('#list').innerHTML = createPlayList(playList) ;*/

/*---------Class work---------------*/

// Username Verification

let message = `Hey there! Welcome to LanxCity. This is the QUIZ section of the website.\n 
Before you can continue with the quiz, note that you need to enter your name`;

let userName;

let userNameConfirmed = false;
let userNameCountDown = 3;

do {
	// Welcoming message on the first visit.
	if (userNameCountDown === 3) alert(message);

	// creating username variable
	userName = prompt(`Enter your name please?`);

	userNameCountDown--;

	// -----If the input field is not empty

	if (userName) {
		let refinedName = "";

		for (let i = 0; i < userName.length; i++) {
			// --------Checking the name input if empty space or number is not included

			if (userName[i] === " " || !isNaN(parseFloat(userName[i]))) {
				if (userNameCountDown !== 0) {
					alert(
						`Sorry, you need to enter the right data. Is either there are spaces or numbers in the data you've entered. And you have ${userNameCountDown} chances left.`
					);
					break;
				} else {
					alert(`Sorry, you have no chances left.`);
					alert(
						`Dear student, since you refuse to enter correct data as your username for 3 times, we believe you are not ready for the quiz. See you next time!`
					);
				}
			} else {
				refinedName += userName[i];

				// -----------after the username entered is correct.
				if (i === userName.length - 1) {
					// -------------checking if it is more that 2 letters
					if (refinedName.length > 2) {
						//----------- confirming username
						userNameConfirmed = true;
					} else {
						alert(
							`Name is expected to be more than 2 letters. And you have ${userNameCountDown} chance(s) left.`
						);
						break;
					}
				}
			}
		}

		if (userNameConfirmed) {
			// --------Re-assignment of the username
			userName = refinedName;
			break;
		}

		// -----------If the input field is empty
	} else {
		if (userNameCountDown !== 0) {
			alert(
				`Hello dear! I can see you haven't entered any data yet. But you still have ${userNameCountDown} chances left.`
			);
		} else {
			alert(`Sorry dear, you have no chances left.`);
			alert(
				`Dear student, since you refuse to enter correct data as your username for 3 times, we believe you are not ready for the quiz. See you next time!`
			);
		}
	}
} while (!userNameConfirmed || userNameCountDown > 0);

//-----------------------------------------------------------Quiz

if (userNameConfirmed) {
	let instruction =
		alert(`Hi ${userName.toUpperCase()}! Welcome to QuizHome.\n
	=> Note that there are some questions that require you to enter DIGITs and "NOT WORDS"`);

	let numbering = 1;

	/*const quiz = [
		 [
			'How many continents do we have in the world?',
			'South Korea is located in what continent?',
			'There are how many states in Nigeria?',
			'What is the official language that is used in Nigeria (without "LANGUAGE" included)?',
			'Nigeria became republic immediately after independence in what year?'
		],

		[
			7,
			'ASIA',
			36,
			'ENGLISH',
			1963
		]
	];


	// Displaying of questions And Checking for correct answers 

	let correctAnswers = 0;

	for (let i = 0; i < quiz[0].length; i++) {

		let userInput = prompt((`${numbering}. ${quiz[0][i]}`));

		if (!userInput) {

			alert(`You got it wrong because you entered no input!`);
		}
		else if (userInput.toUpperCase() === quiz[1][i] || parseFloat(userInput) === quiz[1][i]) {

			alert(`Correct!`);
			correctAnswers++;
		} else {

			alert(`Sorry, the correct answer is ${quiz[1][i]}`);
		}

		numbering++;
	}*/

	// -------------------OR

	const quiz = [
		["How many continents do we have in the world?", 7],
		["South Korea is located in which continent?", "ASIA"],
		["There are how many states in Nigeria?", 36],
		[
			'What is the official language that is used in Nigeria (without "LANGUAGE" included)?',
			"ENGLISH",
		],
		[
			"Nigeria became republic immediately after independence in what year?",
			1963,
		],
		["There are how many planet in the solar system?", 8],
		[
			"The first alleged ninth planet, Pluto, was discovered in what year?",
			1930,
		],
		[
			"The existence of the second alleged ninth planet was revealed in what year?",
			2016,
		],
		["The name of the second alleged ninth planet is?", "PLANET X"],
		["University of Ibadan consists of how many faculties?", 12],
	];

	// Displaying of questions And Checking for correct answers

	let correctAnswers = 0;
	/*let questionsGotten = '';
	let questionsMissed = ''; */

	let questionsGotten = [];
	let questionsMissed = [];

	for (let i = 0; i < quiz.length; i++) {
		let question = quiz[i][0];
		let answer = quiz[i][1];

		let userInput = prompt(`${numbering}. ${question}`);

		// creating new array on the page

		if (!userInput || userInput.trim().length === 0) {
			alert(`You got it wrong because you entered no value!`);
			/*questionsMissed += `<li>${question} ${answer}</li>`;*/

			questionsMissed.push(`${question} ${answer}`);
		} else if (
			userInput.trim().toUpperCase() === answer ||
			parseFloat(userInput) === answer
		) {
			alert(`Correct!`);
			correctAnswers++;
			/*questionsGotten += `<li>${question} <br> Your answer was ${userInput}</li>`;*/

			questionsGotten.push(
				`${question} <br> Your answer was "${userInput}"`
			);
		} else {
			alert(`Sorry, the correct answer is ${answer}`);
			/*questionsMissed += `<li>${question} ${answer}</li>`;*/

			questionsMissed.push(`${question} ${answer}`);
		}

		numbering++;
	}

	// Create function to get list of items from the new array

	function getListItems(listOfItems) {
		/*for (let i=0; i<menu.length;i++) {
			menuList += `<li>${menu[i]}</li>`;
		}*/

		// Or for general purposes, we assign the function a parameter.

		let items = "";

		for (let i = 0; i < listOfItems.length; i++) {
			items += `<li>${listOfItems[i]}</li>`;
		}
		return items;
	}

	// Test outcome the page

	let testOutcome = document.querySelector("main");

	if (correctAnswers === 10) {
		testOutcome.innerHTML = `
		<h1>Excellent ${userName.toUpperCase()}! You got all the ${correctAnswers} questions correctly.</h1>
		<p>And those questions are as follows:</p>
		<ol>
			${getListItems(questionsGotten)}
		</ol>`;
	} else if (correctAnswers >= 8) {
		testOutcome.innerHTML = `
		<h1>Great ${userName.toUpperCase()}! You got ${correctAnswers} correctly out of ${
			quiz.length
		} questions.</h1>
		<p>You got the following questions correctly</p>
		<ol>${getListItems(questionsGotten)}</ol>
		<p>And you got these other questions wrongly</p>
		<ol>${getListItems(questionsMissed)}</ol>`;
	} else if (correctAnswers >= 5) {
		testOutcome.innerHTML = `
		<h1>Good job ${userName.toUpperCase()}! You got ${correctAnswers} correctly out of ${
			quiz.length
		} questions.</h1>
		<p>You got the following questions correctly</p>
		<ol>${getListItems(questionsGotten)}</ol>
		<p>And you got these other questions wrongly</p>
		<ol>${getListItems(questionsMissed)}</ol>`;
	} else if (correctAnswers >= 1) {
		testOutcome.innerHTML = `
		<h1>Nice ${userName.toUpperCase()}! You got ${correctAnswers} correctly out of ${
			quiz.length
		} question(s).</h1>
		<p>You got the following questions correctly</p>
		<ol>${getListItems(questionsGotten)}</ol>
		<p>And you got these other questions wrongly</p>
		<ol>${getListItems(questionsMissed)}</ol>`;
	} else {
		testOutcome.innerHTML = `
		<h1>Sorry ${userName.toUpperCase()}, You got ${correctAnswers} correctly out of ${
			quiz.length
		} questions.</h1>
		<p>And they are as follows:</p>
		<ol>${getListItems(questionsMissed)}</ol>`;
	}
}
