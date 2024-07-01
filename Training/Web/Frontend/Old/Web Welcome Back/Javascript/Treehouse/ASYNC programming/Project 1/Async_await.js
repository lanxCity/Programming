// ES2017 introduced "Async-await" to further simplify usage of promises. It involves the use of "async" and "await" keywords and works fundamentally the same as promises under the hood.
// The word "async" is used to mark a defined function an asynchronous function and "await" is used in that function to mark and wait for a promise (either fetch() or a promise func )
/*  
E.g.
async function getJSON(url) {
    const fulfilledResponse = await fetch(url)  //the promise response
    const data = await fulfilledResponse.json()
    return data
}
*/

// ------------------------------------------
/* const astrosUrl = "http://api.open-notify.org/astros.json";
const wikiUrl = "https://en.wikipedia.org/api/rest_v1/page/summary/";
const container = document.querySelector("main");
const myBtn = document.querySelector("#btn");

// ----------Async-await function
// It purpose is to be written as just like function in "sync" code
async function getPeopleInSpace(url) {
  // From the "astros.json"
  const peopleData = await fetch(url).catch('Error fetching data'); //we can also use catch here.
  const peopleJSON = await peopleData.json();

  // From the "wikipedia"
  const profileData = peopleJSON["people"].map(async (person) => {
    const craft = person.craft;
    const personProfile = await fetch(wikiUrl + person.name);
    const personProfileJSON = await personProfile.json();

    // return from the map method
    return { ...personProfileJSON, craft };
  });

  return Promise.all(profileData);
}

// --------------------Generate HTML
function generateHTML(data) {
  data.map((person) => {
    const section = document.createElement("section");
    section.className = "section-astros";
    document.querySelector("#ajax-body").appendChild(section);

    section.innerHTML = `<img src=${person.thumbnail.source} />
      <h2>${person.title}</h2>
      <p>${person.description}</p>
      <p>${person.extract}</p>
      <p><span class = 'space-craft'>${person.craft}</span></p>`;
  });
}

// ------------------------------------Event

/* myBtn.addEventListener("click", async (event) => {
  event.target.textContent = "Loading...";

  //   calling the async-await function
  const astronuats = await getPeopleInSpace(astrosUrl);
  console.log(astronuats);
  generateHTML(astronuats);

  event.target.remove();
}); *

// Combine Async-await and promises.
myBtn.addEventListener("click", (event) => {
  event.target.textContent = "Loading...";

  //   calling the async-await function
  getPeopleInSpace(astrosUrl)
    .then(generateHTML)
    .catch((err) => {
      container.append("Something went wrong...");
      return console.log("Error occured:", err);
    })
    .finally(() => event.target.remove());

  // console.log(getPeopleInSpace(astrosUrl));
}); */

// ------------------------------------------ Simplification for Error purposes.

const astrosUrl = "http://api.open-notify.org/astros.json";
const wikiUrl = "https://en.wikipedia.org/api/rest_v1/page/summary/";
const main = document.querySelector("main");
const myBtn = document.querySelector("#btn");

// A. Fetch data function
async function getJSON(url) {
  /*  const peopleData = await fetch(url).catch((err) => {
    throw err;
  });
  return await peopleData.json(); */

  try {
    const peopleData = await fetch(url);
    return await peopleData.json();
  } catch (err) {
    throw err;
  }

  // End
}

// B. Getting JSONData function
async function getPeopleInSpace(url) {
  // From the "astros.json"

  const peopleJSON = await getJSON(url);

  // From the "wikipedia"
  const profileData = peopleJSON["people"].map(async (person) => {
    const craft = person.craft;
    const personProfileJSON = await getJSON(wikiUrl + person.name);

    // return from the map method
    return { ...personProfileJSON, craft };
  });

  return Promise.all(profileData);
}

// --------------------Generate HTML
function generateHTML(data) {
  data.map((person) => {
    const section = document.createElement("section");
    section.className = "section-astros";
    document.querySelector("#ajax-body").appendChild(section);

    section.innerHTML = `<img src=${person.thumbnail.source} />
      <h2>${person.title}</h2>
      <p>${person.description}</p>
      <p>${person.extract}</p>
      <p><span class = 'space-craft'>${person.craft}</span></p>`;
  });
}

// ------------------------------------Event

/* myBtn.addEventListener("click", async (event) => {
  event.target.textContent = "Loading...";

  //   calling the async-await function
  const astronuats = await getPeopleInSpace(astrosUrl);
  console.log(astronuats);
  generateHTML(astronuats);

  event.target.remove();
}); */

// Combine Async-await and promises.
myBtn.addEventListener("click", (event) => {
  event.target.textContent = "Loading...";

  //   calling the async-await function
  getPeopleInSpace(astrosUrl)
    .then(generateHTML)
    .catch((err) => {
      main.innerHTML = "<h3>Something went wrong...</h3>";
      return console.log("Error occured:", err);
    })
    .finally(() => event.target.remove());

  // console.log(getPeopleInSpace(astrosUrl));
});
