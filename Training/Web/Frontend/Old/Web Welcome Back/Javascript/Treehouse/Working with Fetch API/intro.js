const select = document.getElementById("breeds");
const card = document.querySelector(".card");
const form = document.getElementById("user-form");

// -------Fetching Data
function fetchData(url) {
  return fetch(url)
    .then(checkStatus)
    .then((res) => res.json())
    .catch((err) => {
      card.innerHTML =
        "<p id = 'err-paragraph'>Unable to display image... <br>Could be network error or server connection</p>";
      throw `Something went wrong... ${err}`;
    });
}

// ----------------------
// Using promise.all() to fetch data sequentially. And this method returns an array of data or none; all response must be true
Promise.all([
  fetchData("https://dog.ceo/api/breeds/list"),
  fetchData("https://dog.ceo/api/breeds/image/random"),
]).then((data) => {
  // Accessing each data
  const breedOptions = data[0].message;
  const breedImage = data[1].message;

  // calling respective functions
  selectOptions(breedOptions);
  generateImg(breedImage);
});

/* 
fetchData("https://dog.ceo/api/breeds/list").then((data) =>
  selectOptions(data.message)
);

fetchData("https://dog.ceo/api/breeds/image/random").then((data) =>
  generateImg(data.message)
); */

// ----------------------------------------------------

// Check response status

function checkStatus(response) {
  if (response.ok) {
    return Promise.resolve(response);
  } else {
    return Promise.reject(new Error(response.statusText));
  }
}

//   --------Generate image
function selectOptions(data) {
  data.forEach((breed) => {
    const option = `<option value="${breed}">${breed}</option>`;
    select.innerHTML += option;
  });
}

function generateImg(source) {
  const html = `
        <img src="${source}" alt="${select.value}" />
        <p>Click to view more ${select.value}s</p>`;

  card.innerHTML = html;
}

// --------------------Selected breed
function fetchBreedImg() {
  const breed = select.value;
  const img = card.querySelector("img");
  const p = card.querySelector("p");

  // Disable select field
  select.disabled = true;
  p.textContent = `Please wait...`;
  // Fetching data
  fetchData(`https://dog.ceo/api/breed/${breed}/images/random`).then((data) => {
    select.disabled = false;
    // return generateImg(data.message);
    img.src = data.message;
    img.alt = breed;
    p.textContent = `Click to view more ${breed}s`;
  });
}

select.addEventListener("change", fetchBreedImg);
card.addEventListener("click", fetchBreedImg);
form.addEventListener("submit", postData);

// ---------------------------------------------
// The default http method for making "fetch" request is "GET" method. And others include "head","post"(to submit data),"delete"(to delete data), or "put"(to update data).
// E.g. for post data-comment on the page, we want to use post method on "fetch"; it requires additional arg(s) inside the fetch().
function postData(event) {
  event.preventDefault();
  const userName = document.getElementById("name").value;
  const userComment = document.getElementById("comment").value;

  // We can call the "fetchData" func but we'd use the "fetch" func.
  // The 'application/json' is the media type for each json response. And the below communicate to the server that the data has been encoded with json.
  // In post request, values are sent to the server in the body of the request. So first, the form data needs to be "stringify" or transform to the json string.
  // // or {userName:userName, userComment: userComment}

  /*  fetch("https://jsonplaceholder.typicode.com/comments", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ userName, userComment }),
  })
    .then(checkStatus)
    .then((res) => res.json())
    .then((data) => console.log(data)); */

  const config = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ userName, userComment }),
  };

  fetch("https://jsonplaceholder.typicode.com/comments", config)
    .then(checkStatus)
    .then((res) => res.json())
    .then((data) => console.log(data)); // The data sent means the request is successful.
}
