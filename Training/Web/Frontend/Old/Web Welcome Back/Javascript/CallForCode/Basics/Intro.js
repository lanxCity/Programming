/* ------------------------API: Application Programming Interface.

   REPL: Read,Evaluate,Print,Loop.

   Node.js: For Backend Development.

   Js Framework: Angular, React, Vue, etc. For large scalable web apps. And also, "React Native" is used to build 
   mobile apps (native apps) e.g. for iOS or iPhone OS (an OS developed by apple),android etc.

   The "{}" is called an object literal.

   two types: primitive or value types(string, number, ) & 
   Reference types: (array, object, and function)

   Type of casing to declare javascript variables is called "camelCasing"

   JIT: Just-In-Time compilation; Compile the codes and execute it, unlike e.g. "one-time" compilation.
*/

/*let paragraph = document.getElementById('confirm-label');
let button = document.getElementById('confirm');

button.onclick = function (event) {
   paragraph.textContent = 'Item purchased! Check your mail for confirmation.';
   event.target.style.display = 'none';
}*/

/*button.addEventListener('click', (event) => {
   paragraph.textContent = 'Item purchased! Check your mail for confirmation.';
   event.target.style.display = 'none';

})*/

// let username = prompt('Enter your name please');

// ---------------------Assigning variable as a value to another variable.

/*let name = "Sodiq";

let newName = name;
console.log("Before reassignment, The 'newname' = "+newName);

name = "Lanx"        //It won't affect the "newName" variable.

console.log("After reassignment, The 'newname' doesn't change but still = "+newName)

console.log("While 'name' has changed to "+"'"+name+"'");
*/

/*---------Global and Local variables*/

// 1. Using the "var" keyword to declare variable inside a "function", "function expression" or "IIFE"(Immediate Invoked Function Expression). Using () to wrap the function.

(function () {
   // using the "var" makes the variable to exist only in the function

   var age = 30;
})(); //The outer "()" tells it to be execute.

(function () {
   // using the "var" makes the variable to exist only in the function

   age1 = 50;
})(); //The outer "()" tells it to be execute.

console.log(window.age1); // windows property

/*
   In conclusion, if "var" is not used or the variable is not declared,
   it would looks up to the outer scope (maybe the nesting function) until it found the variable that it has 
   already been declared. But if not, it turns to global scope (the window object)
   and declare itself. 
   Else, it would only be accessible for the outer scope; if the current function is nested.

   a. If we create a global variable, it's basically a prpty of the window object.

   b. Using "let" or "const" makes the variable only exist in the current scope without looking up.

   c. The main reason why is good to use IIFE, instead of declaring variable in the
     global scope, esp. when building complex app where we make use of 
     diff frameworks and libraries, there may be some variables in those libraries
     bearing same variable names as ours. Which is going to be problematic.

     Therefore, it is good to encapsulate all of our codes using IIFE method.

   d. Using "let" is also a global scope, but doesn't stored in a windows object;
      it's stored in declarative environment that you can't see (just like you can't 
      access variable in a function scope from outside the scope).  

   e. Using "let" is great for "block level scoping". Where the variable 
      is restricted within the block that it's defined e.g. "if" or "for".


*/

let age2 = 100;

console.log(window.age2); //undefined

/*{
   //block

   var age3 = 120; //var is not restricted by the bound of the block, but always looks up for function block.  

   let firstName = 'Sodiq';
   const lastName = 'Ramon';

   console.log(`Hi there! I'm ${firstName} ${lastName}.`);

}
*/
console.log(age3);

// We can also nested block

{
   //block

   var age3 = 120; //var is not restricted by the bound of the block, but always looks up for function block.

   let firstName = "Sodiq";
   const lastName = "Ramon";

   {
      let firstName = "Waris";
      const lastName = "Abdulramon";

      console.log(`Hi! This is a nested name is ${firstName} ${lastName}.`);
   }

   console.log(`Hi there! I'm ${firstName} ${lastName}.`);
}
