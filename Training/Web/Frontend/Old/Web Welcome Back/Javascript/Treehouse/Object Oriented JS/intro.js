// Class, properties and methods.
// Javascript Object has properties and methods which represent the states and behaviors of the object respectively.
// 1. ---------------------- Recap of object literal;
/* let car = {
  model: "Toyota",
  tires: 4,
  drive: "auto",
  stillWorking: true,
  hornSound: "Peep...!!!",
  horn: function () {
    return this.hornSound; //the obj.
  },
};

console.log("Car's horning", car.horn());

//let me = () => this; //windows obj
// console.log(me());

console.log(car); */

// 2. ------------------Working With Classes
// This is another way to create object instead of the object literal. And "class syntax" was introduced in ES2015 and it's what developers called "syntactic sugar" .
//JS uses something called "prototype". The syntaxes for creating prototype b4 ES2015 are tedious and complicated. And in that regard, prototype are less common in classes among other programming languages. So as to make OOP JS easier to understand.

// Capitalizing the first letter of a class name and its decoration is a common convention.

/* 
  ____________________The class structure________________

  class ClassName {

   => constructor method: It's a special method that let you outline the properties that the class created would have. So when you create an object from this class, what you are really doing is invoking this constructor method. Like regular method, you can parse in parameters. In nutshell, if class is like a blueprint, then the constructor method is like a factory that create obj based on that blueprint. 

  }

*/

/* class Pets {
  constructor(animal, age, breed, sound) {
    this.animal = animal;
    this.age = age;
    this.breed = breed;
    this.sound = sound;
  }

  speak() {
    console.log(this.sound);
  }
}

const bingo = new Pets("dog", 2, "pug", "woof woof");
const smart = new Pets("cat", 2, "african", "yip yip");

// console.log(bingo.__proto__);
// console.log(Object.isPrototypeOf(Pets));  //Research on this
// console.log(bingo);

bingo.speak(); */

// NB: When adding method inside a class, "function" keyword is not used.

// 3. --------------JS methods, "Setters" And "Getters"
// These methods allow us to create and retrieve, or update an object properties respectively. And it also helps to increase flexibility.

// Getter method is a special method used when you want to have a property that has a dynamic or computed value; the value of the property is computed in the getter method. And even though it doesn't attach to object instance as a property, it can be accessed as a regular property. we use "get" keyword for getters method. And when getter method is called, a prpty value is computed and returned. And this value isn't ever updated or stored anywhere, while Setter methods,on the other hand, receives  value.
// Setters alway receives one parameter. And the parameter is the value of the property we'd like to set. And we use "set" keyword for setters. And it's useful when you want to add some logic to your code or simplify the coding process.

//NB: The name of the property that's going to be set inside both getter and setter methods must not be the same with their respective names. e.g.

/* set ownerName(owner) {
  this.owner = owner
} 

----Rather, we use "backIn" properties to hold the value of owner; use of "_" before the prpty name (_owner).

And once set properties are set, they have been invoked already.

Note that, a ppty value can also be an object.
*/

/* class Pets {
  // ----------------------Constructor
  constructor(animal, age, breed, sound) {
    this.animal = animal;
    this.age = age;
    this.breed = breed;
    this.sound = sound;
  }

  // ---------------------Getter
  get activity() {
    const today = new Date();
    const hours = today.getHours();

    let message;

    if (hours > 8 && hours <= 20) {
      message = `Good day! My ${this.animal} is playing`;

      return message;
    } else {
      message = `Hi buddy! My ${this.animal} is still sleeping`;

      return message;
    }
  }

  // ---------------------Setters
  // Associated getter method for the ownerName
  get owner() {
    return this._owner;
  }

  set owner(owner) {
    /* this._ownerName = owner;
    return this._ownerName; *

    this._owner = owner;
    console.log(`${owner} owns this ${this.animal}.`);
    //returns "undefined"; "ownerName" ppty has not been assigned a value because the value is stored in "backIn" ppty. So, to solve this, we'd create a getter method with same name that would return the value for us.
  }
  /* set ownerName(owner) {
    /* this._ownerName = owner;
    return this._ownerName; *
    
    this.petOwner = owner;
    console.log(`${this.petOwner} owns this ${this.animal}.`);
    //returns "undefined"; "ownerName" method has not been assigned a value because the value is stored in "backIn" ppty. So, to solve this, we'd create a getter method with same name that would return the value for us.
  } *

  //--------------------- Prototype method
  speak() {
    return this.sound;
  }
} */

/* let me = 'sodiq'

me.replace(/[^0-9]/g,"") * //the first arg replaces all non-numeric with the second arg.*/

class Pets {
  // ----------------------Constructor
  constructor(animal, age, breed, sound) {
    this.animal = animal;
    this.age = age;
    this.breed = breed;
    this.sound = sound;
  }

  // ---------------------Getter
  get activity() {
    const today = new Date();
    const hours = today.getHours();

    let message;

    if (hours > 8 && hours <= 20) {
      message = `Good day! My ${this.animal} is playing`;

      return message;
    } else {
      message = `Hi buddy! My ${this.animal} is still sleeping`;

      return message;
    }
  }

  //--------------------- Prototype method
  speak() {
    return this.sound;
  }
}

// Creating owner's class
class Owner {
  // constructor
  constructor(name, address) {
    this.name = name;
    this.address = address;
  }

  get phone() {
    return this._phone;
  }

  set phone(phone) {
    const rawPhoneNum = phone.replace(/[^0-9]/g, "");

    this._phone = rawPhoneNum;
  }
}

const bingo = new Pets("dog", 2, "pug", "woof woof");
const smart = new Pets("cat", 2, "african", "yip yip");

//------------------------ For the owner's class.
bingo.owner = new Owner(
  "Guil",
  '"Lane 4, House 4, Akuru complex, Oluyole Est., Ib.'
);

// bingo.owner.phone = 08046257816;
bingo.owner.phone = "081-46-25-78-16";

/* console.log(bingo.speak());
console.log(bingo.activity);
console.log(bingo.owner); */

// ------------------------------- Quick research--------------
/* class Person {
  constructor(name) {
    // this.setName(name);
    this.setName(name);
  }
  getName() {
    return this.name;
  }
  setName(newName) {
    newName = newName.trim();
    if (newName === "") {
      throw "The name cannot be empty";
    }
    this.name = newName;
  }
}

let person = new Person("Sodiq");
console.log(person.name);

// ------------------
person.setName("Lanx");
console.log(person.getName()); */

/* document.onmousemove = function (event) {
  const display = this.getElementById("display");

  display.value = `Mouse Coordinates: X: ${event.clientX}, Y: ${event.clientY}`;
};
 */
