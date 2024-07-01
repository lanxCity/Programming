// 1. --------------------- For the Employees status
let employeesXhr = new XMLHttpRequest();

employeesXhr.onreadystatechange = () => {
  if (employeesXhr.readyState === 4) {
    if (employeesXhr.status === 200) {
      // Convert the string to JS object using "JSON.parse"
      let employees = JSON.parse(employeesXhr.responseText);
      // Create an unordered list
      let statusUl = document.createElement("ul");
      // looping through the employees array
      employees.forEach((person) => {
        // create list item
        let li = document.createElement("li");
        let span = document.createElement("span");
        // create classes
        if (person.inOffice) {
          span.textContent = "IN";
          li.className = "in";
        } else {
          span.textContent = "OUT";
          li.className = "out";
        }
        // Append the span to the list
        li.appendChild(span);
        li.append(person.name);

        // Attach to the unordered list
        statusUl.appendChild(li);
      });

      document.querySelector(".office-status").appendChild(statusUl);
    }
  }
};

employeesXhr.open("get", "./data/employees.json");
employeesXhr.send();

// 2. ------------------- For the room status
let roomsXhr = new XMLHttpRequest();

roomsXhr.onreadystatechange = () => {
  if (roomsXhr.readyState === 4) {
    if (roomsXhr.status === 200) {
      // Convert the string to JS object using "JSON.parse"
      let rooms = JSON.parse(roomsXhr.responseText);
      // Create an unordered list
      let statusUl = document.createElement("ul");
      // looping through the rooms array
      rooms.forEach((room) => {
        // create list item
        let li = document.createElement("li");
        let span = document.createElement("span");
        // create classes
        if (room.vacant) {
          span.textContent = "EMPTY";
          li.className = "empty";
        } else {
          span.textContent = "FULL";
          li.className = "full";
        }
        // Append the span to the list
        li.appendChild(span);
        li.append(room.roomNum);

        // Attach to the unordered list
        statusUl.appendChild(li);
      });

      document.querySelector(".office-rooms").appendChild(statusUl);
    }
  }
};

roomsXhr.open("get", "./data/rooms.json");
roomsXhr.send();
