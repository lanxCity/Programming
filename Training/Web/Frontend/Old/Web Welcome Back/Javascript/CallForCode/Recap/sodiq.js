// B----------------------Javascript Engine-----------------------

const confirm = document.getElementById("confirm")

function paymentConfirmation() {
	confirm.textContent = "PAYMENT SUCCESSFUL!!! Check Email for Receipt"

	confirmBtn = document.getElementById('confirm-btn')
	confirmBtn.style.display = 'none'
}

// console.log('Helloooooo')
// let name = 56
// console.log(name)

// ----------------------------------The Global and Local  variables----------
// 1. If you create a variable with the "var", such variable is only attached and limited to that
// "function scope" it's been defined in.

// NB: "var" is function level while "let" and "const" are block level. Because using "var" in a code 
// block, excluding funct e.g. "if" and "for", still looks up for function scope or global's.



 // ---------------Operator precedence continued......


// ----------------Number Methods-----------------
// An instance is a variable of a certain data type with the use of its object

// let num = 56        //This is an instance

// let myNum = new Number(34)   //This is an object


/*let myNum = '25343hjghsgdgdg'

console.log(Number(myNum))   //this returns NaN because all the string value must be a number
console.log(Number.parseInt(myNum))
*/

//----------------------------The importance of "parseInt" in converting number from any base to decimal
//The "ParseInt("num_string, radix or base of the num inputed")" convert numbers from different base to decimal 

// let myNum = '11' 

// console.log(`Convert ${myNum} base 10 to base 10: ${Number.parseInt(myNum, 10)}`)
// console.log(`Convert ${myNum} base 2 to base 10: ${Number.parseInt(myNum, 2)}`)
// console.log(`Convert ${myNum} base 8 to base 10: ${Number.parseInt(myNum, 8)}`)
// console.log(`Convert ${myNum} base 16 to base 10: ${Number.parseInt(myNum, 16)}`)


// -------------------------The importance of "toString()" method in coverting numbers from decimal to a certain base
let myNum = Number('11')  //In base 2

console.log(`Convert ${myNum} base 2 to base 8: ${myNum.toString(8)}`)
