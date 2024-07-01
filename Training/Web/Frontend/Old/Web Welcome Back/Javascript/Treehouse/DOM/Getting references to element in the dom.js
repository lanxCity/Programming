/*Traversing the DOM: this is similar to selection; obtaining a reference to an element. It is a way of moving from one 
product of DOM to another. And selecting element based on its relationship to another element.

 1. For example, let's say I want to remove a paragraph from the DOM, the we have the following;

*/


/*listDiv.addEventListener('click', (event) => {

	if (event.target.tagName === 'P') {

		let p = event.target;

		let div = p.parentNode;
		
		div.removeChild(p)
	}

})*/


let ul = document.querySelector('#list-of-fruits');

ul.addEventListener('click', (event) => {

	if (event.target.tagName === 'BUTTON') {

		if(event.target.className === 'up-button') {

			let span = event.target.parentNode;
			let li = span.parentNode;
			let ul = li.parentNode;

			let prevLi = li.previousElementSibling; //the reference element
			let ulFirstLi = ul.firstElementChild;

			/*if (prevLi && ulFirstLi === prevLi) {

				ul.insertBefore(li,prevLi);
				span.removeChild(event.target);

			}*/ 
			
			if (prevLi) { //That is, the code would only run if there is an element above the target element.

				ul.insertBefore(li,prevLi);
			} 

		}

		if(event.target.className === 'down-button') {

			let span = event.target.parentNode;
			let li = span.parentNode;
			let ul = li.parentNode;

			let nextLi = li.nextElementSibling; //the reference element

			if (nextLi) { //That is, the code would only run if there is an element above the target element.

				ul.insertBefore(nextLi,li); //there is no insert after.

			}
		}

		if (event.target.className === 'remove-item') {

			let span = event.target.parentNode;
			let li = span.parentNode;
			let ul = li.parentNode;
			
			ul.removeChild(li)
		}

	}
})


/*----------------2. How to find and work with sibling elements.
	
	a. Finding previous sibling immediately prior to the current one, we make use of "previousElementSibling" ----------
	rather than "previousSibling" which seems to be a "Node" property. Mainly because of its flaws.

	For example,
*/

let li = document.getElementsByTagName('li')[2]; 

console.log(li.previousSibling);  /*the "#text" only returns document node that's not an html element; the empty string the sit btwn the 
								  /two items which helps to format the html document itself; the property has flaws.*/

console.log(li.previousSibling.previousSibling); //this works!

// But better option is as follows;

console.log(li.previousElementSibling);


// And the use of "inertBefore(newNode,referenceNode)" method place the current reference element (or clicked item) before the previous item.


// Therefore, for the up button, we have

/*ul.addEventListener('click', (event) => {

	if (event.target.tagName === 'BUTTON') {
		if(event.target.className === 'up-button') {

			let span = event.target.parentNode;
			let li = span.parentNode;
			let ul = li.parentNode;

			let prevLi = li.previousElementSibling;

			ul.insertBefore(prevLi, li);
		}
	}


})*/


/*Getting hold no all the children node using "parentNode.children" property which get the collection of the list items.

For example, let's remove all the buttons and replace them using javascript.
*/

// Adding buttons to the existing items in HTML. The parent node has already been defined

let existingItems = ul.children;

for (let i=0; i<existingItems.length; i++) {

	getListButtons(existingItems[i]);

}



/*The use of "firstElement" and "lastElement" properties. E.g. parentNode.firstElement

Or better options are "firstChild" and "lastChild".

For example, removing "up" button from the 

*/
