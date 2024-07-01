/*---------1. How to read and change text using two DOM element properties e.g. textContent, innerHTML*/

const desciption = document.querySelector('p.description');

const newDescription = document.querySelector('.new-description-input');

const newDescriptionButton = document.querySelector('.new-description-button');

newDescriptionButton.addEventListener('click', () => {

	// description.textContent = input.value + ':';

	desciption.innerHTML = newDescription.value + ':';

	newDescription.value = ''; //This set the input value to empty again by removing the content from the text field.
});


/* As the name suggest, "innerHTML" do more just altering an element content only but also 
	can read element and alter elements on a webpage.
*/



/*------------------ 2. Setting Attribute of an element.

	The "attribute" is a property of an "element" object e.g. input.attribute.

	And the "class" attribute has exception property called "className" e.g. p.className


*/

desciption.title = 'Non-list Description';  //Assigning new title to the description. 


/* ----------. Element style property---
	Unlike most other attribute, style property is an object, which has properties that
	can be set on an element using CSS.


*/

//To check all the style properties of an element, I use the following;

console.log(desciption.style); //And note that not properties shown are associated with that particular element.
 

// Using style to hide and display element

const toggler = document.getElementById('toggler');
const listDiv = document.querySelector('.list');

toggler.addEventListener('click', () => { //since our function is managing "inline display property"; property set inside the element itself, therefore, we can rely on the value it returns.

	const togglerContent =document.getElementById('toggler-content');

	if (toggler.checked) { //Note that input.

		listDiv.style.visibility = 'hidden';

		togglerContent.textContent = 'Surprise! Click to view back the contents';

	} else {

		listDiv.style.visibility = 'visible';

		togglerContent.textContent = 'Check the box to see what happens'
	}

})



/*-----------------How to create our element from scratch using document.createElement('name of the element') 
and adding it to the page using "NodeParent.appendChild()" e.g. ul.append(listCreated).*/

const newListInput = document.getElementById('new-list-input');
const newListButton = document.querySelector('#new-list-button');

/*let newItem = [];*/

function getListButtons(list) {

	let listButtonsContainer =document.createElement('span'); //new container nested inside the list
	listButtonsContainer.className = 'list-buttons-container';

	let newButtonUp = document.createElement('button');
	newButtonUp.className = 'up-button';
	newButtonUp.textContent = 'Up';
	listButtonsContainer.appendChild(newButtonUp);
	

	let newButtonDown = document.createElement('button');
	newButtonDown.className = 'down-button';
	newButtonDown.textContent = 'Down';
	listButtonsContainer.appendChild(newButtonDown);
	
	let newButtonRemove = document.createElement('button');
	newButtonRemove.className = 'remove-item' //adding new class name to the class
	newButtonRemove.textContent = 'Remove';
	listButtonsContainer.appendChild(newButtonRemove);

	list.appendChild(listButtonsContainer);
}


newListButton.addEventListener('click', () => {

	let newItemList = document.createElement('li');
	
	const unorderedList = document.querySelector('#list-of-fruits');

	newItemList.textContent = newListInput.value;

	getListButtons(newItemList);
	  //adding new button to the new list

	/*for (i = 0 ; i < newItem.length; i++) {

		newItemList.textContent = newItem[i];
	}*/

	/*
	unorderedList.insertAdjacentHTML('beforeend',newItemList)

	// The element won't appear on the page until they are added to the DOM. 
	*

	/*We'll make use of "appendChild()" method on the parent node.
	 Node belongs to the DOM while Element belongs to plain html. But they ar both used interchangeable.*/

	unorderedList.appendChild(newItemList);

	newListInput.value = '';
});


/*if (desciption.textContent.toUpperCase() === 'THE FOLLOWING ARE THE SET OF FRUITS:') {


}*/


/*-------------------Removing element from the page using "Node.removeChild(childElement)"--------------------*/

// const removeItemButton = document.getElementById('remove-last-item-button');


/*for (let i = 0; i < listItem.length; i--) {


	removeItemButton.addEventListener('click', () => {

		 removedList += listItem[i].pop()
});
}--------------------not work*/

/*removeItemButton.addEventListener('click', () => {

	const unorderedList = document.getElementsByTagName('ul')[0];
	const removedItem = document.querySelector('li:last-child');

	unorderedList.removeChild(removedItem);
	

})*/



