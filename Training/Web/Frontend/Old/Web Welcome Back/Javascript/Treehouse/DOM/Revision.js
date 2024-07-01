// 1.----------The Landscape of JS----
// A. Evolution of Js
// Mocha => Livescript => Javascript => EcmaScript (Ecma Int.) after standardization. And used to refers to the official version of the language.
// Under the Ecma Int., it was standardized under a Technical community called "TC39"
// First Edition of EcmaScript => 1997
// Ecma3.1 => 2008 => Ecma5
// Ecma6 => 2015 (ES2015)
// ------------------------------------------------------------
// B. The diff "flavours" of JS
// i. Vanilla,plain or pure JS: The use of JS without any frameworks or libraries; native, standard-based JS.
// ii. Non-vanilla form of JS (e.g. Type Checking lang and libraries): They help to discover any error in JS before running the code e.g. TypeScript(microsoft), and flow(facebook). Other types of JS are "CoffeeScript" and "Dart" (oop lang by google)

// -------------------------------------------------------------
// C. Common tools and workflow used by JS developers
// i. Js is a dynamic language (aka scripting lang): A lang that executes at runtime (period during which program is running)
// Every browser has its own JS implementation;
// SpiderMonkey was the first JS engine that powers "Netscape navigator", before adopted by "firefox"
// chakra powers IE and Edge
// v8 is the open source engine for chrome
// JS framework (electron) is used to built "VS code" and "atom" text editors

// --------------------------------------------------------------
// D. JS developers workflows
// When starting a new JS project, one of the first things developers do is setup a build system and tools that help manage all of the moving part of the project; everything needed to run the site.
// Build systems include, package managers (npm and yarn), module bundlers (webpack and rollup), compiler (babel and pre-configured), task runners.
// In building complex app, you setup a build system to automate workflow, and install JS library or framework to increase efficiency and build projects faster.
// "React" (by facebook) is one of the JS library.
// "Vue" is a framework that shows similarity with "React"
// "Angular" framework (maintained by google), is a complete JS framework that has more built-in functionality than most JS libraries and frameworks out there.
// Many of top libraries and frameworks provide a tool called "cli" or command line interface. that makes it easier to create applications without configuring any tools.
// perfect code rarely happened at 1st, 2nd, and even 3rd time. Therefore, one of the important steps are "detecting and debugging errors".
// Interactive pages with JS include the following:
// 1. Selecting elements on the page
// 2. Manipulating elements
// 3. Listening to user actions

// -------------------------------Getting started--------
// document, location, alert, console, etc. are properties of windows object
//  "window.document.__proto__" shows document is an instance
// "window.__proto__" shows it's also an instance of windows constructor

// 1. ------------------ Selection of elements
// a. Select element by ID: return single element

/* 
const myHeading = document.getElementById("heading");
const headingColorBtn = document.getElementById("color-btn");
headingColorBtn.addEventListener("click", () => {
  if (colorInput.value) {
    myHeading.style.color = colorInput.value;
  }
}); 
*/

// b. select element by tag name: returns collection of elements with same tag name
/* const myHeading = document.getElementsByTagName("h1")[0];

colorBtn.addEventListener("click", () => {
  if (colorInput.value) {
    myHeading.style.color = colorInput.value;
  }
}); */

/* const fruitList = document.getElementsByTagName("li");
for (let i = 0; i < fruitList.length; i++) {
  fruitList[i].style.color = "red";
} */

// c. Select element by class name: returns collection of elements with same class name

/* const greatFruitList = Array.from(
  document.getElementsByClassName("great-fruit")
);

greatFruitList.forEach((fruit) => {
  fruit.style.color = "blue";
}); */

// d. Select element with "querySelector" and "querySelectorAll"
// These are more flexible as they'll accept ids,classes,tagNames, and more.
// querySelector: returns only the first element of the specified tag.
// querySelectorAll: returns all elements of the same specified tag on the page.
// We can also use pseudo selector to select elements on the page.

/* const fruitListTitle = document.querySelector("[title = label]");

fruitListTitle.setAttribute("id", "fruit-title"); */

// Online resources are MDN (mozilla dev network) and "caniuse.com" to confirm if a certain js method is valid for most browsers.

// 2. --------------- Making changes to a page
// Two DOM element properties used to read and change text on the page
// a. Element.textContent method: This is used to either read or set text value of element.

/* const heading = document.querySelector("#heading");
// console.log(heading.childNodes[0].nodeValue);
// console.log(heading.textContent); */
const toggleBtn = document.querySelector("#toggle-list");
const listSection = document.querySelector("#list-of-items");
const listTitle = document.querySelector("p#list-title");
const listTitleInput = document.querySelector("#title-input");
const listTitleBtn = document.querySelector("#title-btn");
const listUl = document.getElementById("fruit-list");
const ulExistingChildren = listUl.children;
const addItemInput = document.getElementById("add-item-input");
const addItemBtn = document.getElementById("add-item-btn");
// const removeItemBtn = document.getElementById("remove-item-btn");

// --------------toggle button
toggleBtn.addEventListener("click", (event) => {
  if (event.target.checked) {
    listUl.style.transform = "scale(0)";
    setTimeout(() => {
      listUl.style.display = "none";
    }, 600);
  } else {
    listUl.style.display = "block";
    setTimeout(() => {
      listUl.style.transform = "scale(1)";
    }, 200);
  }
});

// -----------list title button
listTitleBtn.addEventListener("click", () => {
  if (
    listTitleInput.value &&
    listTitleInput.value.toLowerCase() !== "default"
  ) {
    listTitle.textContent = listTitleInput.value + ":";
    listTitleInput.value = "";
  } else if (listTitleInput.value.toLowerCase() === "default") {
    let defaultContent = "list of best fruits for breaking while fasting";

    listTitle.textContent = defaultContent + ":";
    listTitleInput.value = "";
  }
});

// --------------Add item button
addItemBtn.addEventListener("click", () => {
  const newItem = document.createElement("li");
  if (addItemInput.value) {
    // newItem.textContent = addItemInput.value;
    let newListValue = document.createTextNode(addItemInput.value);
    newItem.appendChild(newListValue);
    // Clearing the input field
    addItemInput.value = "";
    // calling the buttons function on new items
    createButtons(newItem);
    listUl.appendChild(newItem);
  }
});

// The existing item on the page
// NB: "forEach" can't be used because it's just a collection and not an array
for (let i = 0; i < ulExistingChildren.length; i++) {
  // if (ulExistingChildren[i].tagName === "LI")
  createButtons(ulExistingChildren[i]);
}
// --------------Remove item button
/* removeItemBtn.addEventListener("click", () => {
  const lastChild = document.querySelector("li:last-child");
  if (listUl.lastElementChild) {
    listUl.removeChild(lastChild);
  }
}); */

// b. Element.innerHTML
// This also does same thing as "innerContent", but much powerful as it doesn't limit to text altering. It could be used to alter whole elements on a page.

/*titleBtn.addEventListener("click", () => {
  if (titleInput.value) listTitle.innerHTML = titleInput.value + ":";
}); */

// c. --------------HTML Attributes
// "attributes" like "href" or form "action" attributes are properties of the element object

/* listTitle.title = "List Description";

console.log(listTitle.attributes); */

/* toggleBtn.addEventListener("click", (event) => {
  if (event.target.checked) {
    setTimeout(() => {
      listSection.style.display = "none";
      ul.style.transitionDelay = "1s";
    }, 1000);
  } else {
    section.style.display = "block";
  }
}); */

// ------------------------------------------------
// NB: Best practices is to stick to a certain method to grab elements on a page
// ------------------------------------------------------

// d. --------------Creating new element on a page
// we use "document.createElement('elementName')"
// e. ---------------adding element to a Node
// we use "Node.appendChild(element)"
// "Node belongs to Dom" while "Element belongs to plain HTML"

// 3. Listening and Responding to user's actions
// "EventTarget.addEventListener"  Event always target element on a page. the "Event target" may be an element, document itself, a window, or any object that supports events such as (XMLHttpRequest)
// a. Using the first item of "ul" as an example
// const listItems = document.getElementsByTagName("li")[0];
// const listItems = document.getElementsByTagName("li");

// The setback of the loop is that the event wouldn't be attached to new items added. And that's why we have the word "Event bubbling"

/* for (let i = 0; i < listItems.length; i++) {
  listItems[i].addEventListener("mouseover", () => {
    // listItems.style.textTransform = "uppercase";
    // OR
    listItems[i].textContent = listItems[i].textContent.toUpperCase();
  });

  listItems[i].addEventListener("mouseout", () => {
    // listItems.style.textTransform = "lowercase";
    listItems[i].textContent = listItems[i].textContent.toLowerCase();
  });
} */

// ------------------------Event bubbling
// The event bubbling: This is attaching an event to the ancestral of children element.
// That is, listen for event from the ancestral element.

/* listSection.addEventListener("mouseover", (event) => {
  // listItems.style.textTransform = "uppercase";
  // OR
  // listItems.textContent = listItems.textContent.toUpperCase();
  if (event.target.tagName === "LI") {
    event.target.textContent = event.target.textContent.toUpperCase();
  }
});

listSection.addEventListener("mouseout", (event) => {
  // listItems.style.textTransform = "lowercase";
  // listItems.textContent = listItems.textContent.toLowerCase();

  if (event.target.tagName === "LI") {
    //Case sensitive
    event.target.textContent = event.target.textContent.toLowerCase();
  }
});
 */

// ---------------------Traversing the DOM--------------
// 1. "parentNode" property

/* listSection.addEventListener("click", (event) => {
  if (event.target.className === "remove") {
    // listUl.removeChild(event.target);
    // instead of grabbing the parent node using "id" or any means, we can just traverse

    let removeBtn = event.target;
    let span = removeBtn.parentNode;
    let li = span.parentNode;
    let ul = li.parentNode;
    ul.removeChild(li);
  }
}); */

// --------------------OR
/* listUl.addEventListener("click", (event) => {
  if (event.target.tagName === "BUTTON") {
    // listUl.removeChild(event.target);
    // instead of grabbing the parent node using "id" or any means, we can just traverse

    let removeBtn = event.target;
    let span = removeBtn.parentNode;
    let li = span.parentNode;
    let ul = li.parentNode;
    ul.removeChild(li);
  }
}); */
listUl.onclick = (event) => {
  if (event.target.tagName === "BUTTON") {
    // The "up" button
    if (event.target.className === "up") {
      // The use of "insertBefore()" method that insert a node before a reference node
      let upBtn = event.target;
      let span = upBtn.parentNode;
      let li = span.parentNode;
      // for previous list item
      let previousLi = li.previousElementSibling;
      // for their parent
      let ul = li.parentNode;

      if (previousLi) {
        ul.insertBefore(li, previousLi);
      }
    }

    // The down button
    if (event.target.className === "down") {
      // The use of "insertBefore()" method that insert a node before a reference node
      let downBtn = event.target;
      let span = downBtn.parentNode;
      let li = span.parentNode;
      // for previous list item
      let nextLi = li.nextElementSibling;
      // for their parent
      let ul = li.parentNode;

      // NB: There is "insertAfter" method
      if (nextLi) {
        // swap the argument other way round (not in the right order)
        ul.insertBefore(nextLi, li);
      }
    }

    // The remove button
    if (event.target.className === "remove") {
      // listUl.removeChild(event.target);
      // instead of grabbing the parent node using "id" or any means, we can just traverse

      let removeBtn = event.target;
      let span = removeBtn.parentNode;
      let li = span.parentNode;
      let ul = li.parentNode;
      ul.removeChild(li);
    }
  }
};

// 2. Reference to siblings
// a. previousSibling and previousElementSibling properties
// b. nextSibling and nextElementSibling properties
// Just like "element.childNodes", "previousSibling" either also points to the default "#text" node or to the element on the page.
// Therefore, using "previousElementSibling" is very straight and points directly to the element on the page.

// 3. The use of "children" property
// We noticed if some items are added to the list, those buttons are not added to them.
// Therefore, we clean up all buttons inside "HTML file" and decided to create a function that will those buttons to both existing items and newly added items. Therefore we are not creating those buttons when we only wants to add the new item

function createButtons(li) {
  // For all buttons container
  let span = document.createElement("span");
  span.setAttribute("class", "buttons");
  // For the up button
  let upBtn = document.createElement("button");
  upBtn.setAttribute("class", "up");
  upBtn.textContent = "Up";
  // For the down button
  let downBtn = document.createElement("button");
  downBtn.setAttribute("class", "down");
  downBtn.textContent = "Down";
  // For the remove button
  let removeBtn = document.createElement("button");
  removeBtn.setAttribute("class", "remove");
  removeBtn.textContent = "Remove";

  // Adding those buttons to the container
  span.appendChild(upBtn);
  span.appendChild(downBtn);
  span.appendChild(removeBtn);

  // Adding the container to the list
  li.appendChild(span);
}

// 4. The "firsElementChild" and "lastElement" properties
// Also have counterparts "firstChild" and "lastChild"
