//--------- The multidimensional array

{
  let grades = [
    [70, 72, 75, 82, 90, 84],
    [82, 77, 71, 92, 62, 84, 88, 96],
    [90, 72, 77, 62, 71, 98],
  ];

  //-------- Using the "for" loop
  /*for (let i = 0; i < grades.length; i++) {
		for (let j = 0; j < grades[i].length; j++) {
			console.log(grades[i][j]);
		}

		console.log("~~~~~~~");
	}*

  // Using the "for_each" loop

  grades.forEach(function (grade) {
    // accessing the element

    grade.forEach(function (score) {
      console.log(score);
    });

    if (grades.indexOf(grade) !== grades.length - 1) {
      console.log("~~~~~~~~~~~~~~");
    }
  });*/

  // ------------ "labels" for "break" and "continue"

  /*
	"label" allows you to label the outer loop and use a "break" and "continue" to go 
	the outer loop instead of the current nested loop they (break & continue) 
	are currently in.
	And using "label" means labeling the outer loop with a name
  */

  // Revision

  /*for (let grade = 0; grade < grades.length; grade++) {
		let largest = grades[grade][0];

		for (let score = 0; score <= grades[grade].length; score++) {
			// first checking each box all through
			if (grades[grade][score] > largest) {
				largest = grades[grade][score];
			}
			// the inner loop
			console.log(grades[grade][score]);
		}

		console.log(`${largest} is the largest number in grade ${grade + 1}`);

		// the outer loop
		console.log(`End of grade ${grade + 1}`);
	}*/

  /*for (let grade = 0; grade < grades.length; grade++) {
		let scoreToFind = 62;

		for (let score = 0; score <= grades[grade].length; score++) {
			// first checking each box all through
			if (grades[grade][score] === scoreToFind) {
				console.log(`${scoreToFind} exist in this grade of scores`);

				// the "continue" stops the other codes within this loop and continue with the nxt iteration of the loop again; 62 wouldn't be printed like other scores
				// while "break" breaks out of the loop entirely and continue with other grades
				// ------------

				// continue;
				break;
			}
			// the inner loop
			console.log(grades[grade][score]);
		}

		// the outer loop
		console.log(`End of grade ${grade + 1}`);
	}*/

  // -----labeling
  outerLoop: for (let grade = 0; grade < grades.length; grade++) {
    let scoreToFind = 62;

    for (let score = 0; score <= grades[grade].length; score++) {
      // first checking each box all through
      if (grades[grade][score] === scoreToFind) {
        console.log(`${scoreToFind} exist in this grade of scores`);
        // continue outerLoop    =~ "break" out of this loop but, unlike "continue label", just that the codes within the labelled loop would run
        break outerLoop; // breaks of all the loop entirely
      }
      // the inner loop
      console.log(grades[grade][score]);
    }

    // the outer loop
    console.log(`End of grade ${grade + 1}`); // this code is ignored with continue outerLoop but not ignored wth a break of inner loop.
  }

  // -------------------------------------------End of main block
}
