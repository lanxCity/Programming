class Space {
  constructor(column, row) {
    this.x = column;
    this.y = row;
    this.token = null;
    this.id = `space-${column}-${row}`;
    this.diameter = 76;
    this.radius = this.diameter / 2;
  }

  /**
   * Draws SVG space
   */
  drawSVGSpace() {
    const svgSpace = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "circle"
    );
    svgSpace.setAttributeNS(null, "id", this.id);
    svgSpace.setAttributeNS(null, "cx", this.x * this.diameter + this.radius);
    svgSpace.setAttributeNS(null, "cy", this.y * this.diameter + this.radius);
    svgSpace.setAttributeNS(null, "r", this.radius - 8);
    svgSpace.setAttributeNS(null, "fill", "black");
    svgSpace.setAttributeNS(null, "stroke", "none");

    document.getElementById("mask").appendChild(svgSpace);
  }

  /**
   * Updates space to reflect a token has been dropped into it.
   * @param {Object} token - The dropped token
   */
  mark(token) {
    this.token = token;
  }
  // End of the class
}
