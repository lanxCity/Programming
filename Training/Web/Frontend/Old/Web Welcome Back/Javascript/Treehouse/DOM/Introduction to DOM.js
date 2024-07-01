/*----------------------------Introduction to DOM
	
	-Bringing interactivity into three basic actions-

	1. Selecting elements on the page;
	2. Manipulating elements;
	3. And listening for user actions.

	//--------Some browsers' functions or global environment: There are some many variables in the global environment.
		That is, global variables are properties of a single global object or global scope. Which in browser, is called "windows".
		e.g. type "window" and see all the properties it contains.
	=> alert: this prints messages on a page.
	=> location.href: gets the url of the current page. 

*/

// console.log(window);

/* Throughout this course, we'd be focusing on "document" object------

	The "document" object is a global variable of window representing the html and the contents of a webpage
	
	The "DOM" represent a webpage as a tree-like structure.

	=> Basic tasks JS can do with the DOM include:
	1. Select the element;
	2. Read or manipulate the element
	3. Respond to users' actions

*/


/*
window.document.getElementById('heading').style.background = 'yellow';

// Or

document.getElementById('heading').style.backgroundColor = 'pink';
*/



// -------Class 1. {Accessing element by it "ID" on a page} 

/* this method returns a collection of the same elements; an array */

/*const myHeading = document.getElementById("heading");
const headingColorInput = document.getElementById('heading-color-input');
const headingColorButton = document.getElementById('heading-color-button');
const resetButton = document.getElementById('reset-color-button');


headingColorButton.addEventListener('click', () => {

	// The 'click' specifies the event while the second argument specifies the action once the event took place. And we start by adding a function.

	myHeading.style.color = headingColorInput.value;
});

resetButton.addEventListener('click', () => {

	myHeading.style.color = 'inherit';
});*/

/* Coming back to this

headingCheckbox.addEventListener("click", () => {
	myHeading.style.color = "black";

});*/



/*--------- Class 2: {Accessing elements with its tag name, Or accessing multiple elements using "getElementsByTagName".} 

	Notice: the plural form of "Elements". And the method returns a collection of the same elements; an array.

	Then, you can access any element inside the array using its index.

*/

/*const myParagraph = document.getElementsByTagName('p')[0];
const colorInput = document.getElementsByTagName('input')[0];
const getButtonsArray = document.getElementsByTagName('button');

const addColorButton = getButtonsArray[0];
const resetButton = getButtonsArray[1];

console.log(myParagraph.length);
console.log(myParagraph[0]);


addColorButton.addEventListener('click', () => {
	
	myParagraph.style.backgroundColor = colorInput.value;
});

resetButton.addEventListener('click', () => {

	myParagraph.style.backgroundColor = 'gray';
});

*/



/*const myList = document.getElementsByTagName('li');

for (let i = 0; i < myList.length; i++) {

	myList[i].style.color = 'purple';
}*/



/*---------- Class 3: {Accessing elements with its "class"} */

/*const errorNotPurple = document.getElementsByClassName('error-not-purple');

for (let i = 0; i < errorNotPurple.length; i++) {

	errorNotPurple[i].style.color = 'red';
}*/


/*------------Class 4: {Accessing elements with flexible selectors; "querySelector" or "querySelectorAll".

Those two let you select tag name, id, class, etc.}

The interesting part is that we can select element by its attribute.

*/

/*const allSameItems = document.querySelectorAll('li');  /*Access all the same element on the page*

const theFirstOfSameItems = document.querySelector('li'); /*Access the very first element among a list of same element*

console.log(allSameItems); 
console.log(theFirstOfSameItems);

const buttons = document.querySelectorAll('.btn');

for (let i = 0; i < buttons.length; i++) {

	buttons[i].style.backgroundColor = 'green';

}


// Accessing element with attribute

const resetButton = document.querySelector('[type = reset]');

console.log(resetButton);


// The pseudo selector "nth-child". Others are not supported yet e.g hover.

const evenList = document.querySelectorAll('li:nth-child(even)');

for (let i = 0; i < evenList.length; i++) {

	evenList[i].style.backgroundColor = 'lightgreen';
}*/


