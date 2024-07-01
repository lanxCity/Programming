const astrosUrl = "http://api.open-notify.org/astros.json";
const wikiUrl = "https://en.wikipedia.org/api/rest_v1/page/summary/";
const container = document.querySelector(".people");
const myBtn = document.getElementById("btn");

// Mapping or iterate over each result
function getProfile(JSONData) {
  // Hide button
  $("#btn").hide();
  // Start
  JSONData["people"].map((profile) => {
    // make new request for each name
    getJSON(wikiUrl + profile.name, generateHTML);
  });
}

// Generate the markup for each profile
function generateHTML(data) {
  const section = document.createElement("section");
  section.className = "section-astros";

  section.innerHTML = `<img src=${data.thumbnail.source}>
  <h2>${data.title}</h2>
  <p>${data.description}</p>
  <p>${data.extract}</p>`;

  document.querySelector("#ajax-body").innerHTML += section.outerHTML;
  // container.appendChild(section);
  // console.log(data.thumbnail);
}

// Make an AJAX request
function getJSON(url, callbackFunc) {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", url);
  xhr.onload = () => {
    //   console.log(xhr.readyState);

    if (xhr.status === 200) {
      let data = JSON.parse(xhr.responseText);
      return callbackFunc(data);
    } else {
      $("#ajax-body").html(
        "<p>Sorry, An issue occurs. Please, check back&hellip;</p>"
      );
    }
  };
  xhr.send();
}

// Make new request

/* function getProfiles(JSONData) {
  JSONData["people"].map((profile) => {
    console.log(profile);
  });
} */
// ------------------------------------
myBtn.onclick = (event) => {
  event.target.textContent = "Loading...";
  // start callback
  getJSON(astrosUrl, getProfile);

  // end
};

// We want to make a new request for the "wiki url", so we parse second param to the initial function get "getJSON" and assign it a callback func as an argument

// Higher order function is a function that takes one or more functions as arguments or return a func or do both.
