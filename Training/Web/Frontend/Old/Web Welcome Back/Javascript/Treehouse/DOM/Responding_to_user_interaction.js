/* 1. Some events in javascript---------
		
	click, dblclick, mousedown, mouseup, mousemove, mouseover, etc.

	And for mobile phone, we have touchstart, touchmove, toucheend, etc.

	And for keyboard, we have keyup, keydown, keypress, etc.
	
*/

/* Recap of "function" */

/*function say(something) {

	console.log(something);
}*/

/*function parentFunction(childFunc, arg) {

	childFunc(arg);

}*/

/*parentFunction(say,'Hello World!');*/

/*parentFunction(
	function say(something) {

		console.log(something);}, 'Hello Adigun'
);
*/
/*parentFunction( //Anonymous function as an argument.

	 (something) => {console.log(something);}, 'Hello Tobi'
);*/

/*The main purpose of going through "function" and specifically, "anonymous function", is its advantages. 
	
	1. Let's say we want to delay the execution of a function, we could use "window" obj with "setTimeout()" method. And the function inside the "setTimeout(event or funct, duration before funct runs(the time is in milliseconds), parameter)" method is called the call back function, as it only runs after a certain amount of time have passed.

	when it's passed to an instance, it returns the number of "ms" that was set. And it can then be passed to "window.clearTimeout" to cancel the timeout

*/

window.setTimeout(
  (something) => {
    console.log(something);
  },
  3000,
  "Hello World"
);

let listItems = document.getElementsByTagName("li");

/*for (let i = 0; i < listItems.length; i++) {

	listItems[i].addEventListener('mouseover', () => {

		listItems[i].textContent = listItems[i].textContent.toUpperCase();
	});

	listItems[i].addEventListener('mouseout', () => {

		listItems[i].textContent = listItems[i].textContent.toLowerCase();
	});

} */

/*But when you add new list to initial items, it won't take the effent of the event*/

/*-------------2. Event bubbling---------------

	"event is an object with info and method"

	"event.target" is a property that reference to the target to which the event was originally dispatched.

	Action affecting others. And the use of 'tagNAME' PRPTY
*/

console.log(listDiv.tagName);

//returns capital letter of "DIV"

/*document.addEventListener('click', (event) => {

	console.log(event.target);
});*/

/*listDiv.addEventListener('mouseover', (event) => {

	if (event.target.tagName === 'LI') {

	event.target.textContent = event.target.textContent.toUpperCase();
	}
});

listDiv.addEventListener('mouseout', (event) => {

	if (event.target.tagName === 'LI') {
		
	event.target.textContent = event.target.textContent.toLowerCase();
	}
});*/
