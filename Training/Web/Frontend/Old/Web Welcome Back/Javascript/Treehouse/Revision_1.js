// Textbook

/*let message = "Hello World!\
This is Javascript.\n";

let division = "3\\3.";

console.log(message,division);*/

/*for (let numerator = 33; ; numerator-=1) {
	if (numerator % 3 === 1) {
		// statement
	console.log(numerator);
	break;
	}
}*/

/*let triangle = '#'

for (let counter = 1; counter <= 10; counter++) {
	console.log(`${triangle}`);
	triangle += '#'; 
}*/

// Or

/*for (let line = "#"; line.length < 8; line += "#")
  console.log(line);*/

// Using "switch" instead of "if" statement

/*switch (prompt('What is the weather like today?')) {
	case 'sunny':
		alert("It's sunny. I need to go swimming.");
		break;
	case 'rainy':
		alert("It's sunny. I need to go swimming.");
		break;
	case 'cloudy':
		alert("Remove your clothes from the drying wire.");
		break;
	default:
		alert('Have a nice day ahead');
		break;
}*/

/*for (let number=1; number<=100; number++) {

	let output = "";
	if (number % 3 === 0) output += "Fuzz";
	if (number % 5 === 0) output += "Buzz";
	console.log(output || number);
}*/

// creating out of scope functions
/*function chicken() {
	return egg();
}

function egg() {
	return chicken();
}

console.log(chicken() + "came first");*/

/*Designing Chessboard*/

/*for(let chessGrid = " "; chessGrid.lenght<=8; chessGrid++){
	let chessBoard= "";
	if(chessGrid % 2 === 0) chessBoard += "#";
	if (chessGrid % 2 === 1) chessBoard +=" ";
	console.log(chessBoard); 
}*/

let size = 8;
let  board = "";

for (let y = 0; y<size ;y++) {

	for (let x = 0; x<size; x++) {
		if ((x+y) % 2 === 0) {
			board += ' ';
		} else {
			board += "#";
		}
	}

	board += "\n";
}
console.log(board);