class Board {
  constructor() {
    this.columns = 7;
    this.rows = 6;
    this.spaces = this.createSpace();
  }

  //   ----------------------------------
  /**
   *Generate 2D array of spaces
   *@return {array} boardSpaces- An array of each spaces on each row on the board.
   */
  //   ----------------------------------

  createSpace() {
    let boardSpaces = [];

    for (let i = 0; i < this.columns; i++) {
      let column = [];

      for (let j = 0; j < this.rows; j++) {
        let newSpace = new Space(i, j);
        column.push(newSpace);
      }

      boardSpaces.push(column);
    }

    return boardSpaces;
  }

  /**
   * Draws associated SVG spaces for all game spaces.
   */
  drawHTMLBoard() {
    for (let column of this.spaces) {
      for (let row of column) {
        row.drawSVGSpace();
      }
    }
  }
  //   End of the Class
}
