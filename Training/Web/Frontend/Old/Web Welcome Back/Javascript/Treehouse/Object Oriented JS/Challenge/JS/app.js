// ===>                  Introduction
/* 
=> Analysis of the project: This is all about what the project entails and what we really need. And in this case, each part of the game (or classes) such as, Game, players, token, board, and spaces. 

=> Building Constructor methods and generating objects: Properties and methods needed, etc.
*/

// --------------------------------------------------

const game = new Game();

// -------- Adding event to the "start game" button
document.getElementById("begin-game").addEventListener("click", function () {
  this.style.display = "none";

  game.startGame();
  document.getElementById("play-area").style.opacity = 1;
});

// ---------- Adding event to document once the game start
document.addEventListener("keydown", function (event) {
  game.handleKeydown(event);
});
