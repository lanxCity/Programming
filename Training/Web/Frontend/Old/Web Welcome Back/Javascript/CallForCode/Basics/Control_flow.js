let myName = "LANXCITY";
console.log("hello world");

// ------ it is advisable that the condition of a control flow should be strict (===) as it checks both
// the value and the data type of the comparison. While, on the other hand, the non-strict (==) only checks the value

// The idea of control flow is "Generalisation". Meaning that such program works in various situation.

// ----------------------------Advice on "Generalisation" at (06:28:48/08:54:03)
// When talking about the "if" statement

// Using the comparison operators like <= and >= work the same way as '=='. As the data type is not considered.

// The use of "Logical operators" such as "or ||", "and &&", "not !"

{
	// ----------------------Using "switch" statement

	// The use of "break" in "switch-cases" is compulsory as it breaks out the
	// switch statement once a condition is met. Because if not used, other cases followed would be executed even if
	// such cases are not evaluated to true.

	// let userName = prompt("Enter your name please");

	/*if (userName) {
		var gender = prompt(`Male(M) or Female(F)?`);
		var maritalStatus = prompt("Married(M) or Single(S)");
	}*/

	/*switch (userName.toUpperCase()) {
		case "SODIQ":
			// statements_1
			alert(`Hi ${userName}! Welcome to my website.`);
			break;
		case "LANX":
			alert(`Hi Engr. ${userName}! Welcome to my website.`);
			break;
		default:
			// statements_def
			alert(`Welcome`);
			break;
	}*/

	//------------ To allow numerous things to happened for some cases, we have,

	/*switch (gender.toUpperCase()) {
		case "M":
		case "MALE":
			alert(`Hi Mr. ${userName.toUpperCase()}! Welcome to my website.`);
			break;
		case "F":
		case "FEMALE":
			// -------"if-1" => checking the marital status
			if (maritalStatus.toUpperCase() === "S") {
				alert(`Hi Miss. ${userName.toUpperCase()}! Welcome to my website.`);
			} else if (maritalStatus.toUpperCase() === "M") {
				// getting surname if married
				let surname = prompt("Enter your surname then...");

				//--------"if-2" => confirming the surname is not empty
				if (surname) {
					alert(
						`Hi Mrs. ${surname.toUpperCase()}! Welcome to my website.`
					);
				} else {
					alert(`Hi ${userName.toUpperCase()}! Welcome.`);
				}
				// End if-2
			} else {
				alert(`Hi ${userName.toUpperCase()}! Welcome.`);
			}
			// End if-1
			break;
		default:
			alert("Hi buddy! Welcome.");
			break;
	}*/

	// ----------------------------------------The use of single line "if" statement

	// if (userName) alert(`Hi ${userName.toUpperCase()}!`);

	// ----------------------------------------The use of "Ternary operator"

	/*categorizing operators depends on how many operands this operator works on
	 e.g "!" operator is a unary operator such as "!name", and "+" is a binary. 
	 While ternary takes 3 operands*/

	/*let guessMyName = prompt("I'm a robot. Can you guess my name?");

	// if "guessMyName" is right, "?" then award 10 points else ":" 0 point.
	//this will returns one of the values and we have to store it in a variable "point".
	// Think of the "?" as you are asking a question.

	let point = guessMyName.toUpperCase() === myName ? 10 : 0;

	// conditional statement
	point === 10
		? alert(`Weldone ${userName.toUpperCase()}! You earn ${point} points`)
		: alert(`Sorry, it's ${myName}. You earn ${point} points`);*/

	// -------------------------------------Understanding "Loops"

	/*The concept of "for loop" requires 3 things which are;
	I: Initialisation; C: Condition; U: Update.

	For "while loop", we have;
	V: declare variable === initialisation; C: condition; 

	*/

	// ----------------------The use of "break" and "continue".

	let myMessage = "There is apple inside the apple box";
	let charSearch = "i";

	/*for (let word = 0; word < myMessage.length; word++) {
		if (myMessage[word].toLowerCase() === charSearch) {
			console.log(
				`There is a word "${charSearch}" in the message at index ${word}`
			);
			break;
		}

		// if the "break" is on this line, the loop would run once, and break.
	}*/

	// Example 2

	/*let fruitList = ["APPLE", "ORANGE", "GRAPE"];
	let fruitSearch = "LEMON";

	for (let fruit = 0; fruit < fruitList.length; fruit++) {
		let message;

		if (fruitList[fruit] === fruitSearch) {
			message = `${fruitSearch}" is present in the fruit list.`;
			console.log(message.trim()); //remove any spaces b4 & after string
			break;
		} else if (
			fruitList[fruit] !== fruitSearch &&
			fruit === fruitList.length - 1
		) {
			message = `Sorry, we have no ${fruitSearch} in the list. But the following are fruits we have: ${fruitList}`;
			console.log(message.trim());
		}
	}

	console.log(fruitList);*/

	// The use of "continue"
	/*If you want to do something for every iteration except for very few 
	occurences. Let's say we do not want to print "vowel" in "myMessage", 
	we have; */

	/*for (let word = 0; word < myMessage.length; word++) {
		// excluding the vowel
		if (
			myMessage[word] === "a" ||
			myMessage[word] === "e" ||
			myMessage[word] === "i" ||
			myMessage[word] === "o" ||
			myMessage[word] === "u"
		) {
			continue;
		} //rather than using else statement

		console.log(myMessage[word]);
	}*/

	// ---------------------Nested Loop

	// let orderedList = document.getElementById("ordered-list");

	// for (let i = 0; i < 8; i++) {
	// 	let item = document.createElement("li");

	// 	// let hash = "";
	// 	for (let j = 8; j > i; j--) {
	// 		// hash += "#";
	// 		item.textContent += "#";
	// 	}

	// 	/*hash += "\n";
	//  	console.log(hash);*/

	// 	orderedList.appendChild(item);
	// }
}
