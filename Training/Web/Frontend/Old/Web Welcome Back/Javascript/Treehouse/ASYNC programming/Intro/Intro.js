// Introduction to Synchronous JS
// This is when each task is executed one after the other.

/*  function wait() {
        let btn = document.getElementById('btn')
        // Set initial time
        let start = new Date().getTime();

        // console.log("Starting..................");
        // Creating loop
        while (new Date().getTime() - start < 2000) {
          console.log("Running!!!!!!!!!");
        }
        // End  loop
        console.log("Finished!!!!!!!!!");
    }

    $("#btn-1").click(wait); */

/* let btn = document.getElementById("btn-1");
function wait() {
  // The usage of "while loop with date" is called "bolcking"; blocking next code from running and all the activities of the browser (include the input field) for certain amount of time.
  console.log("Starting...");
  let start = new Date().getTime();
  while (new Date().getTime() - start < 10000);
  console.log("Finished!!!!!!!!!");
}

btn.addEventListener("click", wait); */

/* function wait() {
  console.log("Starting...");
  setTimeout(() => {
    console.log("Finished!!!!!!!!!");
  }, 8000);
}

$("#btn-1").click(wait); */

// --------------------connecting to outside server "Syn way"
/* function getJSON(url) {
  const myXhr = new XMLHttpRequest();

  myXhr.onreadystatechange = function () {
    if (myXhr.readyState === 4 && myXhr.status === 200) {
      let myData = JSON.parse(myXhr.responseText);

      myData.map((element) => {
        if (element.albumId === 1) console.log(element);
      });
    }
  };
  myXhr.open("GET", url, false);
  //the "false" is optional either you want the request to be "Async" or not. But "async" is default unless you set it to false.
  myXhr.send(null);
}

getJSON("https://jsonplaceholder.typicode.com/photos");
console.log("Done!"); */

// --------------------connecting to outside server "ASync way"
/* function getJSON(url) {
  const myXhr = new XMLHttpRequest();

  myXhr.onreadystatechange = function () {
    if (myXhr.readyState === 4 && myXhr.status === 200) {
      let myData = JSON.parse(myXhr.responseText);

      myData.map((element) => {
        if (element.albumId === 1) console.log(element);
      });
    }
  };
  myXhr.open("GET", url);
  //the "false" is optional either you want the request to be "Async" or not. But "async" is default unless you set it to false.
  myXhr.send();
}

getJSON("https://jsonplaceholder.typicode.com/photos");
console.log("Done!"); */

// Using jQuery
/* $(document).ready(function () {
  // Beginning
  $("#btn-1").click(function () {
    $.getJSON(
      "https://jsonplaceholder.typicode.com/photos",
      (myData, status) => {
        if (status === "success") {
          myData.map((element) => {
            if (element.albumId === 1) console.log(element);
          });
        }
        // End getJason func
      }
    );
    console.log("Done!");
    //   End func "onclick btn-1"
  });
}); */

// Async code is typically structured differently than "synchronous" counterpart. Because one of the fundamental ways tot structure "Async program" is with "Callback function".
