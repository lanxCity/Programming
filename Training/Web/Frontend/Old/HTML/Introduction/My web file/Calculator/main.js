// Declaring variables
const displayScreen = document.getElementById("screen");
const clear = document.getElementById("clear");
const valuesContainer = Array.from(document.querySelectorAll(".value"));
const deleteButton = document.querySelector(".delete");
const equate = document.getElementById("equate");

// -------------------------------------Initialised

// -------Delete button
deleteButton.addEventListener("click", () => {
	if (displayScreen.value) {
		let newScreenValues = displayScreen.value.replace(
			displayScreen.value.charAt(displayScreen.value.length - 1),
			""
		);

		displayScreen.value = newScreenValues;
	}
});

//-------- Clear button
clear.addEventListener("click", () => {
	displayScreen.value = "";
});

// -------Equate

equate.addEventListener("click", () => {
	let resultCalculating;
	try {
		resultCalculating = Function(`
				return ${displayScreen.value}
				`)();
	} catch {
		displayScreen.value = "MATH ERROR";
		resultCalculating = undefined;
	} finally {
		// re-assignment of the answer to the screen

		let answer = resultCalculating;

		if (answer) {
			if (answer.toString().length >= 10) {
				displayScreen.value = answer.toExponential(4);
			} else if (answer.toString().length >= 7) {
				displayScreen.value = answer.toPrecision(4);
			} else {
				displayScreen.value = answer;
			}
		} else {
			setTimeout(() => {
				displayScreen.value = "";
			}, 2000);
		}
	}
});

//--------------- values

valuesContainer.forEach(function (element) {
	element.addEventListener("click", () => {
		displayScreen.value += element.value;
	});
});

//-------------------------------- End
