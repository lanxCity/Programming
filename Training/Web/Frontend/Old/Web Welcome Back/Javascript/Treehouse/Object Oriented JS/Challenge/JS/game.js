class Game {
  constructor() {
    this.board = new Board();
    this.players = this.createPlayers();
    this.ready = false;
  }

  // -----------------------------------------
  /**
   * Returns active player.
   * @return  {Object}    player - The active player.
   */
  get activePlayer() {
    return this.players.find((player) => player.active);

    // "find" method returns a unique and the first element that passed the callback test.
  }

  /**
   * Creating an array of all players.
   * @returns {array} players- An array of all the players.
   */
  createPlayers() {
    // Creating each player object from Player class
    const players = [
      new Player(1, "Player 1", "red", true),
      new Player(2, "Abdul", "blue"),
    ];

    return players;
  }

  /**
   * Begins game.
   */
  startGame() {
    // Check if one of those players is ready.

    this.board.drawHTMLBoard();
    this.activePlayer.activeToken.drawHTMLToken();
    this.ready = true;
  }

  // ------------------------------------
  /**
   * Handle required key pressed once the game is ready
   * @param {object} e - keydown event object
   */

  handleKeydown(e) {
    if (this.ready) {
      if (e.key === "ArrowLeft") {
        this.activePlayer.activeToken.moveLeft();
      }
      if (e.key === "ArrowRight") {
        this.activePlayer.activeToken.moveRight(this.board.columns);
      }
      if (e.key === "ArrowDown") {
        this.playToken();
      }
    }
  }

  /**
   * Finds Space object to drop Token into, drops Token
   */
  playToken() {
    let spaces = this.board.spaces;
    let activeToken = this.activePlayer.activeToken;
    let targetColumn = spaces[activeToken.columnLocation];
    let targetSpace = null;

    for (let space of targetColumn) {
      if (space.token === null) {
        targetSpace = space;
      }
    }

    if (targetSpace !== null) {
      game.ready = false;
      activeToken.dropToken(
        targetSpace,
        this.updateGameState(activeToken, targetSpace) //I did it myself..................................................
      );
    }
  }

  /**
   * Updates game state after token is dropped.
   * @param   {Object}    token - The token that's being dropped.
   * @param   {Object}    target - Targeted space for dropped token.
   */
  updateGameState(token, target) {
    target.mark(token);

    if (!this.checkForWin(target)) {
      this.switchPlayers();

      if (this.activePlayer.checkTokens()) {
        this.activePlayer.activeToken.drawHTMLToken();
        this.ready = true;
      } else {
        this.gameOver("No more tokens");
      }
    } else {
      this.gameOver(`${target.owner.name} wins!`);
    }
  }

  /**
   * Checks if there a winner on the board after each token drop.
   * @param   {Object}    target - Targeted space for dropped token.
   * @return  {boolean}   Boolean value indicating whether the game has been won (true) or not (false)
   */
  checkForWin(target) {
    const owner = target.token.owner;
    let win = false;

    // vertical
    for (let x = 0; x < this.board.columns; x++) {
      for (let y = 0; y < this.board.rows - 3; y++) {
        if (
          this.board.spaces[x][y].owner === owner &&
          this.board.spaces[x][y + 1].owner === owner &&
          this.board.spaces[x][y + 2].owner === owner &&
          this.board.spaces[x][y + 3].owner === owner
        ) {
          win = true;
        }
      }
    }

    // horizontal
    for (let x = 0; x < this.board.columns - 3; x++) {
      for (let y = 0; y < this.board.rows; y++) {
        if (
          this.board.spaces[x][y].owner === owner &&
          this.board.spaces[x + 1][y].owner === owner &&
          this.board.spaces[x + 2][y].owner === owner &&
          this.board.spaces[x + 3][y].owner === owner
        ) {
          win = true;
        }
      }
    }

    // diagonal
    for (let x = 3; x < this.board.columns; x++) {
      for (let y = 0; y < this.board.rows - 3; y++) {
        if (
          this.board.spaces[x][y].owner === owner &&
          this.board.spaces[x - 1][y + 1].owner === owner &&
          this.board.spaces[x - 2][y + 2].owner === owner &&
          this.board.spaces[x - 3][y + 3].owner === owner
        ) {
          win = true;
        }
      }
    }

    // diagonal
    for (let x = 3; x < this.board.columns; x++) {
      for (let y = 3; y < this.board.rows; y++) {
        if (
          this.board.spaces[x][y].owner === owner &&
          this.board.spaces[x - 1][y - 1].owner === owner &&
          this.board.spaces[x - 2][y - 2].owner === owner &&
          this.board.spaces[x - 3][y - 3].owner === owner
        ) {
          win = true;
        }
      }
    }

    return win;
  }

  switchPlayers() {
    for (let player of this.players) {
      player.active = player.active === true ? false : true;
    }
  }

  /**
   * Displays winner info.
   * @param   {String}    message - Game over message.
   */
  gameOver(message) {
    document.getElementById("game-over").style.display = "block";
    document.getElementById("game-over").textContent = message;
  }
  //   End of class
}
