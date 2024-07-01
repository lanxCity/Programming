// An object programming involves the use of constructor function to create an object of a certain thing.
// That is, instead of having to create object for each entity, the constructor does the job when it's required.
// And along with the function, "this" function is used to refer to the new object creating.
// The constructor function does not have a return but rather, the function is invoked and preceded by "new" keyword to create a new object instance.
// There is another way of doing this, and it's known as "factory function".
// That is, having another function inside a function you're creating new object and return that function.

// ------------------------------Revision-------------------
/*function profile() {
	this.name = "Lanx";
	this.age = 25;
}

let person = new profile();

console.log(person);*/

// ---------------------------------- Creating a constructor function-------
// A. -----------------Normal Constructor

/*function FormSubmitBtn(name) {
	// The function attached all the value to windows object

	this.name = username.value;
	this.age = Number(userAge.value);
	this.FavoriteMeal = userFood.value;
}*/

// ----------Try this myself

// Without the "onclick" function from the HTML file

/*function Profile() {
	this.name = username.value;
	this.age = Number(userAge.value);
	this.FavoriteMeal = userFood.value;
}

const submitBtn = document.getElementById("submitBtn");

let user;

submitBtn.addEventListener("click", (event) => {
	event.target.style.opacity = ".5";
	user = new Profile();
});*/

// B. -----------Factory Function (It doesn't require the use of "this")

/* let user;

function newProfile(name, interest) {
	let person = {
		username: name,
		userInterest: interest,
	};

	return person;
}

user = newProfile("Sodiq", ["Football", "Eating"]);

console.log(user);*/

// Try this myself with "onclick" function

/*let user;

function profileSubmitBtn() {
	let profile = function () {
		this.name = username.value;
		this.age = userAge.value;
		this.food = userFood.value;
		console.log(this);
	};

	user = new profile();
}*/

// -------------------------------Creating prototype methods for constructor functions: The idea of "Inheritance"

// 1. Creating a method on the instances of an object or function constructor

/* function Profile(username, userAge) {
  this.name = username;
  this.age = userAge;
  /*this.message = function () {
		console.log(this.name, this.age);
	};*
}

Profile.prototype.greetings = function () {
  let message = `Hi ${this.name} of ${this.age} years old! Nice having you on board`;

  return message;
}; */

// NB: It is advisable to return from a function and perform necessary action on it such as log it from outside, or use it somewhere else.
// Note: creating methods inside of the constructor is not advisable. As another copy of the object constructor is being created repeatedly on every new instances.
// Leading to wastage of memory if numerous methods are created inside the constructor.
// Therefore, it is advisable to attach every methods for that constructor on the parent (or prototype).
// E.g. A function is treated as object, where object is the prototype. therefore, those methods are attached directly to object or ancestor internally.
// to avoid copies as we keep creating new object.
// Therefore, those objects created by the constructor would be assigned that constructor prototype; having only one object (or methods)
// that numerous objects referenced as their prototype. It's going to prevent the duplication of the method at each object created.
// If a certain method is not found in a prototype, "undefined" is returned

// ----There is a default prototype that a thing is going to inherit from while looking up for a certain method inside prototypes.
// It is called "object.prototype". For any new object created, they automatically inherit from "object.prototype".
// And it makes some certain methods available for new object created such as "toString()" and "valueOf()" methods.

/* let user = new Profile("Sodiq", 25);

console.log(user.greetings()); */

// --------------------------------Prototype and Inheritance
// Inheritance allows one object to take part of another object and inherit them as its own.
// And this is done in javascript by what is known as a "prototype".
// Prototype is one object that another object can inherit from.
// Try "object.prototype === object.getPrototype(user)" on the console. And should return true

// let x = new Object();
// console.log(Object.prototype === Object.getPrototypeOf(x));  //this is true because x inherits the object prototype

// console.log(Profile.prototype === Profile.getPrototypeOf(user));  // Error!!! getPrototype is not a method of function "Profile"

// console.log(Profile.prototype === Object.getPrototypeOf(user)); //true

// -------------------------Setting an object prototype using "object.setPrototypeOf"
// That is, manually set prototype for an object.

// NB: Prototype is not directly attached to instances but their constructor;
// "person.prototype" returns undefined. Unless you look up one scope by using dunder "_proto_"

/* let user = {    // shift+alt+A  for block comment
  active: true,
};

let person = {
  name: "Sodiq",
  age: 25,
};

// Therefore, "person" can access properties of its new prototype, user
// setPrototypeOf(objectToChangeItsProto, newProtoObj or Array)

let newProto = Object.setPrototypeOf(person, user); */

// -------------------------------Override in prototypal inheritance
// Override a particular value in the prototype of an object.

/* let userActive = {
  active: false,
};

let admin = {
  name: "Sodiq",
  major: "Mechanical Engineering",
  level: "Professor",
};

let student1 = {
  name: "Alabi",
  major: "Civil Engineering",
  level: 500,
};

let adminActiveProto = Object.setPrototypeOf(admin, userActive);
let studentActiveProto = Object.setPrototypeOf(student1, userActive);

// Override a value in prototype, userActive for a student object

student1.active = true; //this create new prpty inside the obj student

console.log("Is admin active:", admin.active);
console.log("Is student active:", student1.active); */

// ------------------Instance properties VS Prototype properties: Best practices

// ----When to use prpty on the prototype VS when to use it on the object
// When there are similarity in the properties of users, then using those prpty inside constructor
// is advisable.
// But where there are differences, setting those prpty on prototype is advisable

// -----------Revision

/* function newProfile(name, contact, sex, age) {
  this.name = name;
  this.contact = contact;
  this.sex = sex;
  this.age = age;
}

// creating a newProfile prototype func
newProfile.prototype.status = function () {
  return "Student";
};

// end
let me = new newProfile("Lanx", 8146257816, "Male", 25);
let you = new newProfile("Kareemot", 9031740783, "Female", 21);

// overriding proto property, "status"
me.status = function () {
  return "Teacher";
};

console.log(me); */
// --------------------End

// ----------------------------Polymorphisms
// In JS, An object can be treated as its type or its parent's or ancestor's
// And in JS, we often have a collection of similar items. E.g. In the above,
// think of "userActive" as an array with elements "admin" and "student1".
// Polymorphism means Ability to call the same method on different objects
//  and each object responds in different way

// 1. ------- Example

// Creating prototype for new objects
/* let profileProto = {
  occupation: ["Lecturer", "Student"],
  // For Lecturers
  lecturerTitle: "Prof.",
  courses: ["Hydraulics", "Hydrology", "Design of structure"],
  // For student
  level: 500,

  //   greetings for students
  greetings: function () {
    return `${this.name} says hi to everyone!`;
  },
};

// Profile constructor
function NewProfile(name, gender) {
  this.name = name;
  this.gender = gender;
  this.department = "Agricultural And Environmental Engineering";
}

let lecturer = new NewProfile("Sodiq", "Male");
let student = new NewProfile("Kareemot", "Female");

// Setting new prototype for instances
let lecturerProto = Object.setPrototypeOf(lecturer, profileProto);
let studentProto = Object.setPrototypeOf(student, profileProto);

// Creating Polymorphisms
let users = [lecturer, student];

users.forEach((user) => {
  // Overriding for lecturers
  if (user === lecturer) {
    user.occupation = user.occupation[0];
    user.title = user.lecturerTitle;
    user.courses = user.courses;
    user.greetings = function () {
      let message = `${this.title} ${this.name} says hi to everyone! I teaches `;

      this.courses.forEach((course) => {
        message += course;
        if (
          this.courses.indexOf(course) !== this.courses.length - 2 &&
          this.courses.indexOf(course) !== this.courses.length - 1
        ) {
          message += ", ";
        } else if (this.courses.indexOf(course) === this.courses.length - 2) {
          message += " and ";
        } else {
          message += ".";
        }
      });
      return message;
    };
  } else {
    user.occupation = user.occupation[1];
    user.level = 500;
  }

  console.log(user.greetings());
}); */

// 2. -----------Example: Prototype of a function
// This means as an object constructor, the transferring of its prototype to any object instances by a function.
// If you check the "function.prototype", the prototype still points back to the function;
// function => prototype (an object with constructor prpty); Object.constructor => function, and circle continues
// person instanceof greetings == greetings.prototype.isPrototypeOf(person)

/* function greetings() {
  return "Hello world";
}

let person = new greetings(); //Object.getPrototypeOf(person) returns the func proto

console.log(Object.getPrototypeOf(person));
console.log(person.__proto__); */

// -----------------------------------Check for property in an object using "in"
/* 
let person = {
  name: "Sodiq",
  age: 25,
  gender: "Male",
  contact: 8146257816,
};

console.log("address" in person);
console.log("gender" in person);

if ("matric_number" in person) {
  console.log("Matric Number exist already");
} else {
  person.matric_number = 200268;
}

for (i in person) {
  console.log(person[i]);
  console.log(person.i); // this returns undefined bcos i is not defined inside the object; "in" also deals with index and not the prop itself
} */

// ----------------------------The "hasOwnProperty" method
// This is used similar to "in" but it would only check the object itself only excluding it prototype

/* console.log("level" in lecturer); //this returns "true" bcos there is "level" ppty inside the lecturer proto
console.log(lecturer.level !== undefined); //this returns "true" bcos there is "level" ppty inside the lecturer proto

console.log(lecturer.hasOwnProperty("level")); //this returns false as it only check inside the obj it's attached to.
 */
// -----------------------------Getting an array of property names from an object

/* let lecturerPpty = []

for (let ppty in lecturer) {
  if (lecturer.hasOwnProperty(ppty)) {
    lecturerPpty.push(ppty)
  }
}

console.log(lecturerPpty) */

// ----------------------A. Converting "Object literal" to a constructor
// Just create constructors for both teacher and student separately and assign them to instances of teacher and student
// ----------------------B. Setting prototypes with constructors.
// Instead of creating diff constructor for student and teacher,and changing their prototype to "ProfileProto".
// And whatever their varied properties would be attached to their prototype or prototype ancestor
// That is, e.g. "ProfileProto.prototype.greetings = func"
// I'm using a single for both along with polymorphism.
// The process of all these prototype is called "Inheritance"
// Creating prototype for new objects

function ProfileProto() {
  this.occupation = ["Lecturer", "Student"];

  // For Lecturers
  this.lecturerTitle = "Prof.";
  this.courses = ["Hydraulics", "Hydrology", "Design of structure"];

  // For student
  this.level = 500;
}

// Profile constructor
function NewProfile(name, gender) {
  this.name = name;
  this.gender = gender;
  this.department = "Agricultural And Environmental Engineering";
}

//Changing the prototype of the constructor
NewProfile.prototype = new ProfileProto();

// Greetings

// Creating Profile
let lecturer = new NewProfile("Sodiq", "Male");
let student = new NewProfile("Kareemot", "Female");

/* // Setting new prototype for instances (Not used in this case. Since the instance constructor proto has been changed)
let lecturerProto = Object.setPrototypeOf(lecturer, profileProto);
let studentProto = Object.setPrototypeOf(student, profileProto); 
*/

// Creating Polymorphisms
let users = [lecturer, student];

users.forEach((user) => {
  // Overriding for lecturers
  if (user === lecturer) {
    user.occupation = user.occupation[0];
    user.title = user.lecturerTitle;
    user.courses = user.courses;
    NewProfile.prototype.greetings = function () {
      let message = `${this.title} ${this.name} says hi to everyone! I teaches `;

      this.courses.forEach((course) => {
        message += course;
        if (
          this.courses.indexOf(course) !== this.courses.length - 2 &&
          this.courses.indexOf(course) !== this.courses.length - 1
        ) {
          message += ", ";
        } else if (this.courses.indexOf(course) === this.courses.length - 2) {
          message += " and ";
        } else {
          message += ".";
        }
      });
      return message;
    };
  } else {
    user.occupation = user.occupation[1];
    user.level = user.level;
    NewProfile.prototype.greetings = function () {
      return `${this.name} says hi to everyone!`;
    };
  }

  console.log(user.greetings());
});
//
// ----------------------"InstanceOf" operator
// This is used to see if an object is of a particular type.
/* console.log(lecturer instanceof NewProfile); //true
console.log(lecturer instanceof ProfileProto); //true */
