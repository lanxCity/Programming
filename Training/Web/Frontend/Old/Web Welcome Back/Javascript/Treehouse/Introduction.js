//1. first Lesson

//---------------------------The use of Javascript commands e.g alert, console.log, document.write

/*alert("Welcome back Engr. Lanx"); 
console.log("You are highly welcome Engr. Lanx");

document.write("This is printed within the body tag directly"); //This is printed within the body tag directly

document.write("<h3>This is printed within the <code>&lt;h3&gt;</code> tag&period;</h3>")*/

/*alert('"Warning! This message will self destruct in"');

alert ('3...');
alert ('2...');
alert ('1...');

document.getElementById("head1").firstChild.nodeValue= "BOOM!";

console.log("Message destroyed");*/



// --------------------------- Variables in Javascript

/*Global: This can be used anywhere within the script or the linked html. And (var) could also be omitted.
  Local variables: This is limited only within the function it's created. */

/*Declaring variables by "var", "let", or "const". */

/* const score = 15;

var score += 30;

let score += 10 
console.log('old answer='+ score);

score += 10;

console.log('new answer=' + score);
*/

let name = "Sodiq";

console.log(name);



// ------------------------------ Data types in javascript (strings, numbers, boolean/logical, and null value.....)

let club = "chelsea";

let score = 50; 

console.log(`The club is ${club} and`, `the score is ${score}`);


// ------------------------------ Spacing in JS

let multiLineWith_Backslash = "Hello world! \
This is Engr. Lanx of the LanxtEchwoRld. \
Glad to meet you all."

console.log(multiLineWith_Backslash);



//-------------------------------- The strings' (or object) properties and method  e.g. ppty => length, method => toUpperCase(), etc.

/*let userName = prompt("Your name please?");

let greetings = "Hi " + userName.toUpperCase() +"!" + " Nice to meett you.\n" +
"Feel free to explore " +"So go on and download anything"; //Concatenation

//Note: the method ".toUpperCase" doesn't change the original case of the input string.

alert(greetings);

console.log(userName);

console.log("The length of the user's name is " + userName.length);*/


//-------- The use of the "template literals" to multi-lines of strings by the use of "backticks (``) with ${}" 


const userName = prompt("Your name please?");

function isUserNameEmpty() {
  if (!userName || !isNaN(userName)) /*means if the username is empty*/ {
  
    return true;
  } else {

    return false;
  }
}

const userNameEmptied = isUserNameEmpty();

if (userNameEmptied) {

  alert('Sorry, you need to enter your name.');

} else {

  let nameToUppercase = userName.toUpperCase();

  let greetings = `Hi  ${nameToUppercase}! Nice to meet you.
  Do you mind playing a game with me?? Let's get started...`; 
  alert(greetings);

  // ---------------------------------------------------class work------ Quiz program

  //Instruction before starting the test and numbering

  let instruction = alert('Note that there are some questions that require you to enter DIGITs and "not words"');

  let numbering = 0;

  // 1. storing the correct answers

  let answer_1 = 7;
  let answer_2 = 'ASIA';
  let answer_3 = 36;
  let answer_4 = 'ENGLISH';
  let answer_5 = 1963;

  // 2. declaring correct answers, rank, and output

  let correctAnswers = 0;
  let rank;
  let main = document.querySelector('main')

  // 3. setting questions

  const quiz_1 = prompt(`${++numbering}. How many continents do we have in the world?`); // Q
  if (+quiz_1 === answer_1) {

    alert('Correct!');
    correctAnswers++;
  } else {

    alert(`Sorry, the correct answer is ${answer_1}.`);
  }

  const quiz_2 = prompt(`${++numbering}. South Korea is located in what continent?`);  // Q
  if (quiz_2.toUpperCase() === answer_2) {

    alert('Correct!');
    correctAnswers++;
  } else {

    alert(`Sorry, the correct answer is ${answer_2}.`);
  }

  const quiz_3 = prompt(`${++numbering}. There are how many states in Nigeria?`);  // Q
  if (+quiz_3 === answer_3) {

    alert('Correct!');
    correctAnswers++;
  } else {

    alert(`Sorry, the correct answer is ${answer_3}.`);
  }

  const quiz_4 = prompt(`${++numbering}. What is the official language that is used in Nigeria (without 'LANGUAGE' included)?`); // Q
  if (quiz_4.toUpperCase() === answer_4) {

    alert('Correct!');
    correctAnswers++;
  } else {

    alert(`Sorry, the correct answer is ${answer_4}.`);
  }

  const quiz_5 = prompt(`${++numbering}. Nigeria became republic immediately after independence in what year?`);  // Q
  if (+quiz_5 === answer_5) {

    alert('Correct!');
    correctAnswers++;
  } else {

    alert(`Sorry, the correct answer is ${answer_5}.`);
  }

  // 4. Result processing

  if (correctAnswers === 5) {
    rank = "GOLD";
  } else if (correctAnswers >= 3) {
   rank = "SILVER"
  } else if (correctAnswers >=1) {
   rank = "BRONZE"
  } else {
    rank = "NONE"
  } 

  main.innerHTML = `
  <h1>Hi ${nameToUppercase}! You got ${correctAnswers} correctly out of ${numbering} questions</h1>
  <p>Crown earned: <span>${rank}!</span></p>`;

}
  

/*let nameToUppercase = userName.toUpperCase();

let greetings = `Hi  ${nameToUppercase}! Nice to meet you.
Do you mind playing a game with me?? Let's get started...`;                  //Concatenation using "intrapolation" ${}

//Note: the method ".toUpperCase" doesn't change the original case of the input string.

alert(greetings);*/

/*console.log(userName);

console.log("The length of the user's name is " + userName.length);*/


// -------------------------------------------- Class work 1----------------------------- Story maker program



/*let noun = prompt(`Please ${nameToUppercase}, enter  a noun.`).toUpperCase();
let verb = prompt(`Enter an action verb.`).toUpperCase();
let adjective = prompt('Enter an adjective.').toUpperCase();

const storyMaker = `<h2>For over thousand years, there has always being a/an ${adjective} king who ${verb} with ${noun}</h2>`;


document.querySelector('body').innerHTML = storyMaker;*/


// ------------------------------------------The use of "conditional statement"

/* Note: No ";" at the end of the code block in the curly braces,
   the parenthesis after "if" statement is for the condition
   the code runs if the condition is met
*/

/*Operators used include ==, ===, <, <=, >, >=, !=, !==. where (! is logical not operator )*/

// 1.

/*const answer = prompt("The surname of the Oyo state governor is?");

if (answer.toUpperCase() == "MAKINDE") {

  document.querySelector("body").innerHTML= `<h1>Well done ${nameToUppercase}! You are the best.</h1>`;

} else {
  document.querySelector("body").innerHTML= `<h1>Sorry ${nameToUppercase}, you are wrong.</h1>`;
}*/

// 2. guessing game

/*const correctNumber = 6;

let userGuess = prompt("Can you guess any number ranging from 1-10?");

let correctGuessing = false;  //since the user hasn't guess any number yet

 // reassigning value to 'correctGuessing' if a condition is met

if (+userGuess === correctNumber) { // note the '+' sign converts the string entered to number
    correctGuessing = true;
  }

if (correctGuessing) { // Rather than "correctGuessing === true"
    alert(`Well done ${nameToUppercase}. You are correct`);
  }  else {
    alert(`Sorry ${userName}, The correct number was ${correctNumber}.`);
  }*/

// 3. The use of "else if" statement

/*let daySection = prompt('What section of the day are we?');

let testForString = parseInt(daySection);

if (daySection === "morning") {

  alert("I'm taking bread and tea as my breakfast.");
} else if (daySection === "afternoon") {

  alert("I'm having Amala with meat this afternoon.");
} else if (daySection === "evening") {

  alert("I think rice and fried stew with fish is okay this evening.");
} else if (isNaN(testForString)){

  alert("what  am I eating now...?");
} else {

  alert("Sorry, you've entered a number");
}*/


// ---------------------------------------------------class work------ Quiz program

//Instruction before starting the test and numbering

/*let instruction = alert('Note that there are some questions that require you to enter DIGITs and "not words"');

let numbering = 0;

// 1. storing the correct answers

let answer_1 = 7;
let answer_2 = 'ASIA';
let answer_3 = 36;
let answer_4 = 'ENGLISH';
let answer_5 = 1963;

// 2. declaring correct answers, rank, and output

let correctAnswers = 0;
let rank;
let main = document.querySelector('main')

// 3. setting questions

const quiz_1 = prompt(`${++numbering}. How many continents do we have in the world?`); // Q
if (+quiz_1 === answer_1) {

  alert('Correct!');
  correctAnswers++;
} else {

  alert(`Sorry, the correct answer is ${answer_1}.`);
}

const quiz_2 = prompt(`${++numbering}. South Korea is located in what continent?`);  // Q
if (quiz_2.toUpperCase() === answer_2) {

  alert('Correct!');
  correctAnswers++;
} else {

  alert(`Sorry, the correct answer is ${answer_2}.`);
}

const quiz_3 = prompt(`${++numbering}. There are how many states in Nigeria?`);  // Q
if (+quiz_3 === answer_3) {

  alert('Correct!');
  correctAnswers++;
} else {

  alert(`Sorry, the correct answer is ${answer_3}.`);
}

const quiz_4 = prompt(`${++numbering}. What is the official language that is used in Nigeria (without 'LANGUAGE' included)?`); // Q
if (quiz_4.toUpperCase() === answer_4) {

  alert('Correct!');
  correctAnswers++;
} else {

  alert(`Sorry, the correct answer is ${answer_4}.`);
}

const quiz_5 = prompt(`${++numbering}. Nigeria became republic immediately after independence in what year?`);  // Q
if (+quiz_5 === answer_5) {

  alert('Correct!');
  correctAnswers++;
} else {

  alert(`Sorry, the correct answer is ${answer_5}.`);
}

// 4. Result processing

if (correctAnswers === 5) {
  rank = "GOLD";
} else if (correctAnswers >= 3) {
 rank = "SILVER"
} else if (correctAnswers >=1) {
 rank = "BRONZE"
} else {
  rank = "NONE"
} 

main.innerHTML = `
<h1>Hi ${nameToUppercase}! You got ${correctAnswers} correctly out of ${numbering} questions</h1>
<p>Crown earned: <span>${rank}!</span></p>`; */










