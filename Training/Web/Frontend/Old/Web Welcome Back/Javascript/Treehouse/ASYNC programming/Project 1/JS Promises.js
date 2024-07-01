//----------------------------------- Intro----------------
// Since creating diff callback functions along with the XMLHttpRequest Api can be a little complex to use and manage compared to modern fetching API (JS introducing ES15 and ES17). Creating func in its separate func can be confusing where one have to read through each to know the purpose of a certain func.
// "Promises" in JS introduces a more straight forward alternative for executing, composing, and managing Async code. And also make it easier to handle errors in program.
// It offers an elegant and human readable ways to manage "Async" code. And give more control over "Async" program.
//What is promise?
// Promise represents eventual completion of "Async" operation; a value that may not be available yet like, requested from the server.

// -----------------------------
// A. Diff btw "callback" and "promises"
// B. Promise state: A promise will always be in 3 possible state. i.)Pending, ii.)Fulfilled, and iii.) Rejected.
/* 
Pending state is the default state;
Fulfilled state is that the operation completed successfully;
Rejected state means the operation failed.
*/

// C. Working with "Promises"
/* 
=>Create a promise instance using Promise() constructor
=>Define what should happen when the promise is fulfilled or rejected
=>Call one of the methods provided by the promise API to either consume value of a fulfilled promised or provide a rejection reason for a rejected promise 
*/

// The promise constructor takes one callback, and the callback accept two args; resolve, if the promise is fulfilled,and reject, if the promise is rejected.

// resolve() returns a "promise object" that is resolved with a given value to the instance and changes the status of the promise.
//While reject() returns a "promise object" that is rejected with a given reason to the instance.
// And both of these functions are provided by the constructor.
//  In summary, the above function will return a promise "object"; the state of the promise like pending, resolve, or rejected.

// ---------Example 1. Breakfast promise
/* const breakfastPromise = new Promise((resolve, reject) => {
  // "resolve" changes the status of promise from pending to fulfilled. And we can parse it a value which then become the fulfillment value of the promise.
  // So when the Async task complete successfully, It's going to return a promise object with a value parse inside "resolve" func

  // And then we need to get or consume the value out of the promise object. So, to do that, the promise API provides methods that can be call on the promise, and the most common two are "then()" and "catch()".
  // "then()" can be called to handle both fulfilled and rejected promises. And accepts 2 func as its args; fulfilled and rejected promises. But in the following example, we'll use "then" for fulfilled and "catch" for rejected.
  // The third method, which is a newer method, is the "finally()" method. Any program inside it runs either their is an error or not.
  // resolve();

  setTimeout(function () {
    // This runs after 5s...
    // resolve("Your order is ready!!!");
    return resolve("Hello world");
  }, 5000);
}); */

// console.log(breakfastPromise);
/* breakfastPromise
  .then((value) => console.log(value))
  .catch((err) => console.log(err)); */

// Recap: A promise is the eventual value or a result of an Async operation

// -----------------------Using "Promises" for Astronauts program------------------------------

/* const astrosUrl = "http://api.open-notify.org/astros.json";
const wikiUrl = "https://en.wikipedia.org/api/rest_v1/page/summary/";
const container = document.querySelector(".people");
const myBtn = document.getElementById("btn");

// Mapping or iterate over each result
function getProfile(JSONData) {
  // Hide button
  // $("#btn").hide();
  // Start

  const profiles = JSONData["people"].map((profile) => {
    // make new request for each name
    return getJSON(wikiUrl + profile.name);
  });

  // The following returns an array of multiple resolved promise object. And what we need is a single resolved promise, and then parse to "generateHTML" func.
  // Therefore, there is an efficient way to fire-off and keep track of multiple Async operation with "Promise.all()" method.
  // The method is used for when a program needs to wait for more than one promise to resolved.
  // return console.log(profiles);
  return Promise.all(profiles);
}

// Generate the markup for each profile
function generateHTML(data) {
  data.map((person) => {
    const section = document.createElement("section");
    section.className = "section-astros";

    section.innerHTML = `<img src=${person.thumbnail.source}>
    <h2>${person.title}</h2>
    <p>${person.description}</p>
    <p>${person.extract}</p>`;

    document.querySelector("#ajax-body").innerHTML += section.outerHTML;
  });
}

// Make an AJAX request
function getJSON(url) {
  return new Promise((resolve, reject) => {
    // Start "promise"
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.onload = () => {
      if (xhr.status === 200) {
        let data = JSON.parse(xhr.responseText);
        resolve(data);
      } else {
        reject(xhr.statusText);
      }
    };

    // There may be error in network connectivity, so, we have "onerror" ppty
    xhr.onerror = () => {
      console.log(Error("A network error occurred"));
      $("#btn").text("Try again!");
    };
    xhr.send();
    // End Promise
  });
}
// ------------------------------------Event
myBtn.onclick = (event) => {
  event.target.textContent = "Loading...";
  // start callback
  getJSON(astrosUrl)
    .then(getProfile)
    .then(generateHTML)
    .catch((err) => {
      console.log(err);
    })
    .finally(() => {
      console.log("Done!!!");
    });

  // end
}; */

/* const astrosUrl = "http://api.open-notify.org/astros.json";
const wikiUrl = "https://en.wikipedia.org/api/rest_v1/page/summary/";
const container = document.querySelector(".people");
const myBtn = document.getElementById("btn");

// Function wikiProfile
function getProfile(JSONData) {
  // Start

  const profiles = JSONData["people"].map((profile) => {
    // make new request for each name
    return getJSON(wikiUrl + profile.name);
  });

  return Promise.all(profiles);
}

// Generate the markup for each profile
function generateHTML(data) {
  // Hide button
  document.getElementById("btn").remove();
  // data.map((person) => {
  data.forEach((person) => {
    const section = document.createElement("section");
    section.className = "section-astros";
    document.querySelector("#ajax-body").appendChild(section);

    section.innerHTML = `<img src=${person.thumbnail.source}
    <h2>${person.title}</h2>
    <p>${person.description}</p>
    <p>${person.extract}</p>`;
  });
}

// Make an AJAX request
function getJSON(url) {
  return new Promise((resolve, reject) => {
    // Start "promise"
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.onload = () => {
      if (xhr.status === 200) {
        let data = JSON.parse(xhr.responseText);
        resolve(data);
      } else {
        reject(xhr.statusText);
      }
    };

    xhr.onerror = () => {
      $("#btn").text("Try again!");
      console.log(Error("A network error occurred"));
    };
    xhr.send();
    // End Promise
  });
}
// ------------------------------------Event
myBtn.onclick = (event) => {
  event.target.textContent = "Loading...";
  // start callback
  getJSON(astrosUrl)
    .then(getProfile)
    .then(generateHTML)
    .catch((err) => {
      $(".container").append("<p>Something went wrong...</p>");
      console.log(err);
    })
    .finally(() => {
      console.log("Done!!!");
    });

  // end
};

*/
