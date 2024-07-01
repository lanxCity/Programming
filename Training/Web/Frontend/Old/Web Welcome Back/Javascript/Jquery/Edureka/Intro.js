// --------------------------Revision----------------------------

/* var docLoc = document.location;
var docCharset = document.characterSet;
var docTitle = document.title;

var main = document.getElementById("main-container");

var mainStyle = {
  width: "100%",
  overflow: "auto",
  border: "1px solid red",
};
console.log(main.style);

Object.assign(main.style, mainStyle);

main.innerHTML = docLoc + "<hr />";
main.innerHTML += docCharset + "<hr />";
main.innerHTML += docTitle; */

/* let main = document.querySelector("main");

main.addEventListener("click", (event) => {
  if (event.target.tagName === "LI") {
    const li = event.target;
    const ul = li.parentNode;
    const mainEl = ul.parentNode;

    const prevLi = li.previousElementSibling;

    ul.insertBefore(li, prevLi);
  }
}); */

// -------------------------------Intro: ready() func

// ====> When page has been load completely
console.log("Hey!!! I'm on line 39");

$(document).ready(function () {
  console.log("Document is ready!!! (From line 42)");

  // ====> Selectors
  // $("main").text("This is from jQuery!!!");
  // $("#main").text("This is from jQuery!!!");
  // $(".main-container").text("This is from jQuery!!!");
  // console.log($(".main-container").text("This is from jQuery!!!"));

  //---returns the element itself; every action is being perform on the element one after the other.

  // -===> Function chaining: Some functions or action in jQuery
  /*  $(".box")
    .css("width", "150px")
    .css("height", "150px")
    .css("background", "red")
    .fadeOut(1000); */

  /* $(".box")
    .css({ width: "150px", height: "150px", background: "red" })
    .slideUp(2000); */

  /*  $(".box")
    .css({ width: "150px", height: "150px", background: "red" })
    .slideDown(); //SlideDown means to show. And this does nothing. Since it's showing already */

  /*   $(".box")
    .css({ width: "150px", height: "150px", background: "red" })
    .slideToggle(2000, "linear");  //swing is the default */

  // --------------------------------------------------------------
  /* let counter = 0;
  (function toggleBox() {
    $(".box")
      .css({ width: "150px", height: "150px", background: "red" })
      .slideToggle(1000, "linear");
    counter++;
    setTimeout(() => {
      toggleBox();
    }, 2000);
  })(); */

  // -------------------------------------
  /*  var counter = 0;
  var img = [
    "Desert",
    "Jellyfish",
    "Koala",
    "Tulips",
    "Lighthouse",
    "Chrysanthemum",
    "Penguins",
    "Hydrangeas",
  ]; */

  /*  (function imgDisplay(images) {
    if (counter === images.length) counter = 0;

    $(".box img")
      .attr("src", `./images/${images[counter]}.jpg`)
      .slideToggle(1000);
    counter++;

    setTimeout(() => {
      $(".box img").slideToggle(1000);

      setTimeout(imgDisplay, 1000, images);
    }, 3000);
  })(img); */

  // ------------------------------
  // -------------------------------
  // End document
});

console.log("Hey!!! I'm on line 45");

function me() {
  for (let i = 0; i < 10; i++) {}
}
