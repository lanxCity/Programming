// ------------Introduction to arrays

/*let stuff = [
		12,
		"sodiq",
		function () {
			console.log(stuff[1]);
		},
	];

	//------------------calling a function from an array
	stuff[2]()*/

// ------------Empty spaces inside an array---------------

/*let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
	numbers.length = 30;
	numbers[35] = 48;*/
/*for (i = 0; i < numbers.length; i++) {
		if (numbers[i]) {
			console.log(numbers[i]); //Filtering the "undefined" values within.
		}
	}*/
// ----------Getting the largest number from an array using "if" or "Math & spread"
// console.log(Math.max(...numbers));
/*let largest = numbers[0]; //assume the first element is the largest

	for (i = 0; i < numbers.length; i++) {
		if (numbers[i] > largest) {
			// largest = numbers[i];
			largest = i;
		}
	}

	console.log(
		largest + " is the index of the largest number in the numbers array"
	);*/

// ----------Average of an array
// creating filtering element
/*function filterArrayElement(arrayElement) {
		let fiteredArray = new Array();

		for (let i = 0; i < arrayElement.length; i++) {
			if (
				arrayElement[i] &&
				arrayElement[i].toString().trim().length !== 0
			) {
				fiteredArray.push(arrayElement[i]);
			}
		}

		return fiteredArray;
	}

	// Counting new the filtered element
	const arrayCounter = function (array) {
		let count = 0;

		for (let i = 0; i < array.length; i++) {
			count++;
		}

		return count;
	};

	// assigning the array filter function to a new variable
	let newArray = filterArrayElement;

	// creating "count" variable to keep track the number elements inside the array.

	let counter = arrayCounter;

	// -----------Average of an array

	let total = 0;

	for (let i = 0; i < newArray(numbers).length; i++) {
		total += newArray(numbers)[i];
	}

	let avrg = total / counter(newArray(numbers));

	console.log(
		`The average = ${total}/ ${counter(newArray(numbers))} = ${avrg}`
	);*/

// -----------Filling array with the user input and "sentinel" value (for loop)
// we can use "Number" to convert a string to number e.g.

/*let highestNum = prompt("Enter any highest number");
	let lowestNum = prompt("Enter any lowest number");

	let division = Number(highestNum) % Number(lowestNum);

	console.log(`The modulo of ${highestNum}/${lowestNum} is ${division}`);*/

/*let grades = new Array();

	while (true) {
		let input = prompt(
			"Enter any grade to create a box for all the grades you entered\n => And press any letter to quit"
		);

		if (!input || !Number(input)) {
			//sentinel values "letters" for break
			break;
		}

		grades.push(Number(input));
		console.log(grades);
	}*/

// -------------Some array methods
// push,pop & unshift,shift etc.

// a. "splice(start: int, deleteCount: int, items...: any)" method

// let grades = [1, 23, 35, 22, 10, 6, 100, 52, 87];

// Removing items

/*let removedGrades = grades.splice(4, 3); // removes 3 items by starting from index 4

	console.log(`The removed grades are [${removedGrades}]`);
	console.log(`The new grades are [${grades}]`);

	// Adding items

	let addingGrades = grades.splice(4, 0, 200, 40, 30, 15); //add items by starting from index 4

	console.log(`The new grades after adding new values are [${grades}]`);

	// replacing items with zeroes
	let zeroReplacement = grades.splice(4, Infinity, 0);
	console.log(grades);

	// b. "sort()" method: this sorts data alphabetically. So it doesn't work for numeric data; not the way you expect.

	grades.push(2, 64, 60, 6, 4, 37);
	grades.sort();
	console.log(grades);

	// So we need a "call back" function and compare the values in the array; passing function as a parameter inside another function

	grades.sort(function (a, b) {
		return a - b;
	});

	console.log(grades);

	// c. The use of "fill(value, start,end)" method: just like splice, it replaces a section of the array values
	/*
		the "end input" of the fill method is usually exclusive unlike the "start input" or index
	*

	grades.fill(-1, 0, grades.length - 1); //replacing all the value with "-1"

	console.log(`The array after the "fill" method is [${grades}]`);*/

// d. The use of "copyWithin()" method to copy a portion from an array to another portion of the same array.

// grades.copyWithin(target-position, start, end)

// Target-positiion: the index to which we want to copy to
// start(default is 0): the element index we want to start to copy (inclusive)
// end(default is array length): the element index we want to stop copy (exclusive)

//---------------------- Some method that does alter the original array.

// e. the use of "concat()" method

// console.log(grades);
/*let gradeA = [72, 75, 82, 90, 93, 78];
	let gradeB = [90, 98, 85, 82];

	console.log(gradeA.concat(gradeB).sort((a, b) => a - b)); //joins two arrays together and doesn't change the original array
	console.log(gradeA.includes(62));
	console.log(gradeA.indexOf(72, 2)); // (valueToSearch, fromWhichIndex)
	console.log(gradeA.join(","));
	console.log(gradeA.slice(1, 5));

	// ---------------------------------f. The use of "for_each" loop: It is only an array method

	// ---revision of the "for" loop

	gradeA.length = 30;

	/*for (let i = 0; i < gradeA.length; i++) {
		// getting rid of the "undefined"

		if (gradeA[i]) console.log(gradeA[i]);
	}*

	let numbering = 1;

	gradeA.forEach(function (element, index) {
		console.log(`${numbering}. ${element} with index of ${index}.`);
		numbering++;
	});
*/

/* let gradeA = [72, 75, 82, 90, 93, 78];
gradeA.length = 30; */

/*for (let i = 0; i < gradeA.length; i++) {
	console.log(gradeA[i]);
}*/ //This does not eradicates empty elements "undefined"

// The following both eradicate any empty elements
/*
for (item in gradeA) {
	console.log(gradeA[item]);
}

//The "forEach" callback function takes up to three args; (element,index,the array itself if needed).  

gradeA.forEach((element) => console.log(element));
*/

/* let grades = [
  [25, 20, 60, 56],
  [25, 20, 60, 56],
  [25, 20, 60, 56],
  [25, 20, 60, 56],
  [25, 20, 56, 56],
  [25, 20, 62, 56],
  [25, 20, 65, 56],
]; */

/*for (let row = 0; row < grades.length; row += 1) {
	for (let col = 0; col < grades[row].length; col++) {
		console.log(grades[row][col]);
	}

	console.log("~~~~~~~~~~~~~~~~~~");
}*/

/*for (row in grades) {
	for (col in grades[row]) {
		console.log(grades[row][col]);
	}

	console.log("~~~~~~~~~~~~~~~~~~~~~");
}*/

/*grades.forEach((row) => {
	row.forEach((col) => {
		console.log(col);
	});
	console.log("~~~~~~~~~~~~~~~~~~~~~~~");
});*/

// ------------------------------Online Quiz------------
// A. Reversing an array
/* let years = [1993, 1991, 2001, 1991, 1950, 2000, 1990, 2016, 2022, 2025, 1900];

years.sort((a, b) => b - a);
console.log(years); */

// B. Smallest element in an array
/* let myList = [-1, 12, 4, 5, 2, 11, -3];
function smallestNumber(list) {
  let smallest = list[0];

  list.forEach((num) => {
    if (smallest >= num) smallest = num;
  });

  return smallest;
}

console.log(smallestNumber(myList)); */

// C. Find duplicate of values
/* let myStringList = [
  "bcd",
  "abd",
  "jude",
  "bcd",
  "oiu",
  "gzw",
  "oiu",
  "bnm",
  "iop",
  "qwp",
  "jude",
]; */

/* function findDuplicates(list) {
	let newList = [];
	let duplicateList = [];
  
	list.forEach((value) => {
	  if (!newList.includes(value)) {
		newList.push(value);
	  } else {
		duplicateList.push(value);
	  }
	});
  
	if (duplicateList.length) return duplicateList;
  
	return "No duplicates!";
  }
  
  console.log(findDuplicates(myStringList)); */
// The array "entries()" method
//create new "[key, value]" array of each element in the original element. let [0,1] = [10,20]
// Using the "next().value" method access the values one after the other and if it's exceeded, "undefined" is returned;
// Given me = [10,3,6,7,8]
// 1st element => [0,10] or [index,element]
// 2nd element => [1,3]

// let newMe = myStringList.entries();
/*console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value);
console.log(newMe.next().value); */

/* for (let [index, element] of newMe) {
  console.log(`Index ${index}: ${element}`);
} */

// ----------------------------jhdjhsdfjjjjjjjjjjjjjjjjjjjjjjjj

/* let years = [1993, 1991, 2001, 1991, 1950, 2000, 1990, 2016, 2022, 2025, 1900];

function sortData(list) {
  let listToObject = list.entries();
  let newList = [];
  let smallest = list[0];
  let smallestExist = false;

  do {
    list.forEach((i) => {
      if (smallest > i) smallest = i;

      //if list is not empty
      if (newList.length) {
        newList.forEach((j) => {
          if (j === smallest) {
            smallestExist = true;
          }
        });

        if (!smallestExist && list.indexOf(i) === list.length - 1) {
          smallestExist = false;
          smallest = i;
        }
      }
    });

    if (!list.length || !smallestExist) {
      for (let [occurrences, element] of listToObject) {
        if (element === smallest) {
          for (let i = 0; i < occurrences; i++) {
            newList.push(smallest);
          }
        }
      }
    }
  } while (newList.length !== list.length);

  return newList
}

sortData(years); */ // Not working yet (infinite loop)

// Find duplicate
/* let myList = [1, 3, 4, 5, 4, 32, 1, 3, 4, 2, 1, 4];
function duplicate(arr) {
  let newArr = [];
  let dupNum = [];
  for (let i = 0; i < arr.length; i++) {
    num = arr[i];
    let numExist = false;
    if (!newArr.length) {
      newArr.push(num);
    } else {
      for (let j = 0; j < newArr.length; j++) {
        if (newArr[j] === num) {
          numExist = true;
          break;
        } else {
          numExist = false;
          if (j === newArr.length - 1 && numExist === false) {
            newArr.push(num);
            break;
          }
        }
      }
    }
    if (numExist) {
      if (!dupNum.length) {
        dupNum.push(num);
      } else {
        for (let k = 0; k < dupNum.length; k++) {
          if (dupNum[k] === num) {
            break;
          } else {
            if (k === dupNum.length - 1) {
              dupNum.push(num);
            }
          }
        }
      }
    }
  }
  console.log(newArr);
  return dupNum;
}

console.log(duplicate(myList));
 */
