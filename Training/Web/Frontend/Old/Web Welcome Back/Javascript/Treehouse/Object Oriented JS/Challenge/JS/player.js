// => Create player class with necessary properties.

class Player {
  constructor(id, name, color, active = false) {
    this.id = id;
    this.name = name;
    this.color = color;
    this.active = active;
    this.tokens = this.createToken(21);
    //Spaces are 42, and the game is for two players
  }

  //   ----------------------------------
  /**
   * Creating an array token objects for each player
   *  @param {integer} numOfToken - Number of token objects to be created for each player.
   * @returns {array} tokens - An array consisting of each token object
   */
  //   -----------------------------
  createToken(numOfToken) {
    const tokens = [];

    //   creating object for each token and store them in a tokens array.
    for (let i = 0; i < numOfToken; i++) {
      let token = new Token(this, i);

      tokens.push(token);
    }

    return tokens;
  }

  // -------------------------------------
  /**
   * Gets all tokens that haven't been dropped.
   * @return {array}  Array of unused tokens.
   */
  get unusedTokens() {
    return this.tokens.filter((token) => !token.dropped);
    // "filter" method returns an array elements that passed the callback test.
  }

  /**
   * Gets the active token by returning the first token in the array of unused tokens.
   * @return {Object} First token object in the array of unused tokens.
   */
  get activeToken() {
    return this.unusedTokens[0];

    //NB: getter and setter are accessed as normal object.
  }

  /**
   * Check if a player has any undropped tokens left
   * @return {Boolean}
   */
  checkTokens() {
    return this.unusedTokens.length == 0 ? false : true;
  }

  //   End of class
}
