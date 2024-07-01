// The DOM, Document Object Model, is the structure representation of a page
// Consider DOM as boxes which are related to each other. And each box is known as a node.
// And a node can have child nodes, and it's considered as the parent node.
// So those child nodes are known as siblings
// NB: We can relatively reference "node" using its parent. So It's a relative way of traversing through the structure of web page
// The purpose of nodes is rather than grabbing ech structure by Class or ID, we can grab by traversing through the structure.

// A.---------------------Working with DOM children
// The following is nt actually the sophisticated of dealing with a certain element on a page.

/* const myDocument = document.childNodes;

// console.log(myDocument); //returns [doctype html, html]

// Traversing down the child (from chrome)
let myList = document.childNodes[1].childNodes[2].childNodes[11];
console.log(myList)

// console.log(myList)
// console.log(myList.childNodes)
// console.log(myList.parentNode) // ~= myList.parentElement
// In addition, we can also use "nextSiblings", "previousSiblings", etc. */

// B.--------------------Getting Element by Tag names and Class names
// These returns the HTMLCollection of certain tag names or classes
// They are not actually an array but "ArrayLike" and we can use "Array.from()" method to make it an array
/* let myList = document.getElementsByTagName('li')
// console.log(myList)
let myListArray = Array.from(myList) 
console.log(myListArray)



let myListImptnt = document.getElementsByClassName('important')
console.log(myListImptnt)
*/

// C.-------------------------Node types And Node Names
// Each node inside the DOM has both name and type.
// i. Node type
//  The read-only nodeType property of a Node interface is an integer that identifies what the node is. It distinguishes different kind of nodes from each other, such as elements, text and comments.
// All elements on the page are of "node type 1" while the actual text is 3
// NB: the text inside an element is also stored as an array-like because it is treated as childNodes

// let myList = document.getElementsByTagName("li");
/* 
console.log(myList);
console.log(myList[0].childNodes[0].nodeType);  // element "a" is also nodeType of 1
console.log(myList[0].childNodes[0].childNodes[0].nodeType) // 3 
*/

// ii. Node name
/* 
console.log(myList[0].nodeName); //returns "LI"
console.log(myList[0].childNodes[0].nodeName) //returns "A"
console.log(myList[0].childNodes[0].childNodes[0].nodeName) //returns "#text" */

// D.--------------------Text node (childNode Explained)
// The children node of a text type node is the actual text
// The text node of node type always have "nodeValue"

let myParagraph = document.getElementsByTagName("p");
console.log(myParagraph);

// E. -------------------Modifying nodeValue
// The text node usually has a property called "nodeValue". Therefore, you can change the "nodeValue" of text nodes but not its the element node as it remains "null". E.g.
// console.log(myParagraph[0].childNodes[0])

// console.log(myParagraph[0].nodeValue = 'Changing the value on the page') // the element value does not change
// console.log(myParagraph[0].childNodes[0].nodeValue = 'Changing the value on the page ')

// F. Practice with "EventListener"

let myList = document.getElementsByTagName("ul")[0];
/*myList.onmouseover = () => {
  myList.childNodes[3].childNodes[0].nodeValue = "Changed Item";
};*/

let myBtn = document.getElementById("my-btn");
/*myBtn.onmouseenter = () => {
  myList.style.display = "none";
  myBtn.childNodes[0].nodeValue = "Surprised!";
};

myBtn.onmouseout = () => {
  setTimeout(() => {
    myList.style.display = "block";
    myBtn.childNodes[0].nodeValue = "Hover over me";
  }, 500);
}; */

// G. Working with Attributes in the DOM And adding element to page
// Some elements have attributes rather than "nodeValue" such as "input", "img", etc.

let username = document.getElementById("username");
console.log(username.attributes);
console.log(username.hasAttribute("pattern"));
console.log(username.getAttribute("placeholder"));

myBtn.onclick = () => {
  let newNode = document.createElement("li");
  if (username.value) {
    let newNodeValue = document.createTextNode(username.value);
    newNode.appendChild(newNodeValue);
    myList.appendChild(newNode);
  }
};
