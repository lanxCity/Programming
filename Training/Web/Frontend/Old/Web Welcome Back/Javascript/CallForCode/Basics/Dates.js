{
	// ---------------------Introduction to javascript "Date" object
	// A constructor is special function that's going to return an "instanceof" something
	// And we use "new" keyword to create new object from a constructor.
	//And constructor get called when you declare an object using "new"
	// instance of class is typically called an "object"

	//   var valentine = new Date();

	//---this create an instance of a date: a special object to store day,year,hours,etc.
	//if the constructor parameters are empty, there is a default value assign to it.
	// e.g Date() generate from the time laptop time.
	//   console.log(valentine);
	/* 1. If you want to be specific on the date and not date of "right now"; default date, we can pass the info to the constructor about what date we want.

	N.B: the month is "zero base" or indexing method; Jan-Dec ~= 0-11.
	e.g new Date(1990,11,27)

	2. You might also wants to work with "milliseconds" where you have to use UNIX Epoch or time; describing instant in time and defined by number of seconds that have elapsed since Universal Coordinate Time(UTC), Thur,1 Jan 1970.

	e.g new Date(num of ms) or new Date(0) for 1970... or Date.now() for ms since 1970(reference point); if you perse in 1 argument, it's assumed as number of milliseconds

	Date(year,month,day,hrs,mins,s,ms)
	*/

	//   let myDate = new Date(2020, 12);

	//if I should perse in 12 which is ~= 13th month as the month value, it turns it to Jan 2021

	/* let myDate = new Date(1641662150320);
  console.log(myDate);
  console.log(Date.now());*/

	// --------Example 1. (Time taken for a loop to run)

	/* 
	// before the loop

	let initial = Date.now();

	// additional loop
	total = 0;

	for (let i = 0; i < 10000000; i++) {
		total += i;
	}

	//after the loop
	let final = Date.now();
	let timeTaken = final - initial;

	console.log(timeTaken);
	console.log(total);*/

	//---------Example 2. cal. No. of days between two dates

	/*let previousDate = new Date(2021, 11, 31);
	// let currrentDate = Date.now();
	let currentDate = new Date();

	let dayInMilliseconds = 1000 * 60 * 60 * 24;

	let daysBetween = Math.floor(
		(currentDate - previousDate) / dayInMilliseconds
	);

	console.log(
		`There are ${daysBetween} between ${previousDate} and ${currentDate}`
	);*/

	// ----------Example 3.

	/*let grade = [89, 90, 76, 83, 97];
	let userGuess;
	let numbering = 1;
	let correctGuess = 0;*/

	// create a function

	// loop
	/*
	for (let i = 0; i < grade.length; i++) {
		userGuess = prompt(`${numbering}. Guess any number`);

		let timeUp = setTimeout(() => {
			userGuess = undefined;
		}, 10000);

		if (userGuess) {
			if (Number(userGuess) === grade[i]) {
				alert("Correct");
				correctGuess++;
			} else {
				alert(`Sorry, the correct number was ${grade[i]}`);
			}
		} else if (timeUp) {
			alert(
				`You entered no value. But the correct number was ${grade[i]}`
			);
		} else {
			alert(
				`You entered no value. But the correct number was ${grade[i]}`
			);
		}

		numbering++;
	}

	alert(`You got ${correctGuess} out of ${numbering} guesses`);
	*/ //---------------the timer is not working yet

	// ---------------------------Some date methods

	// a. Date.parse(24 May 2001): convert it to ms

	// let Date1 = Date.parse("24 Jan 2000 10:10:10 ");
	// console.log(Date1);

	//b. Date(1995-10-29)

	// let Date2 = new Date("1995-10-29");

	// let Date2 = new Date("24 Jan 2000 10:10:10 ");
	// let Date2 = new Date(2000, 5, 27, 0, 10, 10);
	//It's assumed to be converted to UTC already

	//c. Date.UTC()

	// let Date2 = new Date(Date.UTC(2000, 5, 27, 0, 10, 10));
	// But if the time zone is diff; 10:49pm in USA and you came back to nigeria and wants to convert it, you use "Date.UTC"

	//
	// console.log(Date2);

	// d. Date.now(): get the "ms" of the current local date since 1970
	// let currentDate = Date.now();
	// console.log(currentDate);

	// f. setHours() etc.

	/*let myDate = new Date("2/10/22"); // feb 10 2022
	//let myDate = new Date(22, 1); //return feb 1922

	myDate.setDate(20);

	console.log(myDate);*/

	// g. getTimeZoneOffset(): returns diff btw local and utc time

	let myDate = new Date(); console.log(myDate.getTimezoneOffset()); 
	// returns "-60" instead of "+60", which is num of minute rel to UTC,
	//for "utc +1" 
}