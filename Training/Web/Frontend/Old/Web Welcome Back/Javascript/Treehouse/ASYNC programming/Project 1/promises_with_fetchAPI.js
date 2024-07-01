// ES2015: The use of fetchAPI with promises that allows handling of result returned from the server.
// Making network request with "Fetch", and how it makes requesting resources easier.
// A. To make fetch request, we use a global "fetch" method. And it takes one arg; the path to the resources you wanna fetch.
// B. The "fetch" method itself returns a promise

// --------------------------------------
const astrosUrl = "http://api.open-notify.org/astros.json";
const wikiUrl = "https://en.wikipedia.org/api/rest_v1/page/summary/";
const container = document.querySelector(".people");
const myBtn = document.getElementById("btn");

// Function wikiProfile
function getProfile(JSONData) {
  // Start
  const profiles = JSONData["people"].map((profile) => {
    const craft = profile.craft;
    // returning from the map function
    return fetch(wikiUrl + profile.name)
      .then((data) => data.json())
      .then((data) => {
        return { ...data, craft };
      })
      .catch((err) => console.log("Error from wiki:", err));
  });

  return Promise.all(profiles);
}

// Generate the markup for each profile
function generateHTML(data) {
  data.map((person) => {
    const section = document.createElement("section");
    section.className = "section-astros";
    document.querySelector("#ajax-body").appendChild(section);

    section.innerHTML = `<img src=${person.thumbnail.source}
    <h2>${person.title}</h2>
    <p>${person.description}</p>
    <p>${person.extract}</p>
    <p><span class = 'space-craft'>${person.craft}</span></p>`;
  });
}

// ------------------------------------Event
myBtn.onclick = (event) => {
  event.target.textContent = "Loading...";
  // start callback
  fetch(astrosUrl)
    .then((data) => {
      // turn the rslt to normal json data
      return data.json();
    })
    .then(getProfile)
    .then(generateHTML)
    .catch((err) => {
      $(".container").append("<p>Something went wrong...</p>");
      console.log(err);
    });

  document.getElementById("btn").remove();
  // end
};
