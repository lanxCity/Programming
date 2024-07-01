// -----------------Revision from plain JS
/* const myXhr = new XMLHttpRequest();

myXhr.open("GET", "./sample.html");
myXhr.onreadystatechange = function () {
  if (this.readyState === 4) {
    // console.log(myXhr.responseText);
    document.querySelector("#section-heading").innerHTML = myXhr.responseText;
  }
};

ajaxBtn.onclick = (e) => {
  myXhr.send();
  e.target.style.display = "none";
}; */

// --------------------Using jQuery

/* $(document).ready(function () {
  $(ajaxBtn).click(function (e) {
    e.preventDefault();
    $("#section-heading").load("./sample.html");
    $(ajaxBtn).hide();
  });
});
*/
// Trying get method
/* $(document).ready(function () {
  $(viewEmployees).click(function (e) {
    e.preventDefault();
    $.get("./sample.html", (response) => {
      console.log(typeof response);
    });
  });
}); */

// -------------Plain Js for the Employees office status
/* const employeesXhr = new XMLHttpRequest();

employeesXhr.open("GET", "../data/employees.json");

employeesXhr.onreadystatechange = () => {
  if (employeesXhr.readyState === 4) {
    // Creating a list of employees
    const ul = document.createElement("ul");
    ul.setAttribute("id", "employees");
    // Getting the data in JS format
    console.log("hello world");
    const employees = JSON.parse(employeesXhr.responseText);

    employees.forEach((person) => {
      const li = document.createElement("li");
      const span = document.createElement("span");
      // Checking office status
      if (person.inOffice) {
        li.className = "in";
        span.textContent = "IN";
      } else {
        li.className = "out";
        span.textContent = "OUT";
      }
      // Appending
      li.textContent = person.name;
      li.appendChild(span);
      ul.append(li);
    });

    // Appending the whole ul
    document.querySelector(".office-status").appendChild(ul);
  }
};

viewEmployees.onclick = (e) => {
  employeesXhr.send();
  e.target.style.display = "none";
}; */

// Using Jquery for the Employees office status
// 1. using "load"
/* $(document).ready(function () {
  $(".office-status").load(
    "../data/employees.json",
    (response, status, request) => {
      if (status === "success") {
        const ul = document.createElement("ul");
        ul.setAttribute("id", "employees");
        // Getting the data in JS format
        console.log("hello world");
        const employees = JSON.parse(response);

        employees.forEach((person) => {
          const li = document.createElement("li");
          const span = document.createElement("span");
          // Checking office status
          if (person.inOffice) {
            li.className = "in";
            span.textContent = "IN";
          } else {
            li.className = "out";
            span.textContent = "OUT";
          }
          // Appending
          li.textContent = person.name;
          li.appendChild(span);
          ul.append(li);
        });

        // Appending the whole ul
        // NB: It has flaws as it only load the returned data directly in the selector(or on the page). Before I changed it to "innerHTML" from "append"
        document.querySelector(".office-status").innerHTML = ul.outerHTML;
        // End
      }
    }
  );
}); */

// Using "get" (returns the JS Format)
/* $.get("../data/employees.json", (response, status) => {
  if (status === "success") {
    const ul = document.createElement("ul");
    ul.setAttribute("id", "employees");
    // Getting the data in JS format
    console.log("hello world");
    const employees = response;

    employees.forEach((person) => {
      const li = document.createElement("li");
      const span = document.createElement("span");
      // Checking office status
      if (person.inOffice) {
        li.className = "in";
        span.textContent = "IN";
      } else {
        li.className = "out";
        span.textContent = "OUT";
      }
      // Appending
      li.textContent = person.name;
      li.appendChild(span);
      ul.append(li);
    });

    document.querySelector(".office-status").append(ul);
  }
}); */

// 3. getJSON (return the reponse is in JS format)
/* $.getJSON("../data/employees.json").done((data) => {
  const ul = document.createElement("ul");
  ul.setAttribute("id", "employees");

  data.forEach((person) => {
    const li = document.createElement("li");
    const span = document.createElement("span");
    // Checking office status
    if (person.inOffice) {
      li.className = "in";
      span.textContent = "IN";
    } else {
      li.className = "out";
      span.textContent = "OUT";
    }
    // Appending
    li.textContent = person.name;
    li.appendChild(span);
    ul.append(li);
  });

  document.querySelector(".office-status").append(ul);
}); */

/* $(document).ready(function () {
  $("#regForm").submit(function (e) {
    e.preventDefault();

    const formUrl = $(this).attr("action");
    const formData = $(this).serialize();

    console.log("This is form data ", formData);
    $.post(formUrl, formData, function (data, textStatus) {
      if (textStatus) {
        $(".container").html("<p>Thanks for signing up!</p>");
      }
    })
      .done(() => {
        alert("I am done"); //This runs if successful
      })
      .fail(function () {
        $(".container").html("<p>Error! url does not exist.</p>");
      });
  });
}); */

// ----------Fall back, "fail()" method
/* $(document).ready(function () {
  // Click Event
  $("#btn").click(() => {
    // Send request
    $.get("missing.html", function (response, textStatus) {
      if (textStatus === "success") {
        $(".container").html(response);
      }
    }).fail(() => {
      $(".container").html("<p>Sorry! There has been Error</p>");
    });
  });
}); */

//----------- Sending Ajax request to outside source
/* $(document).ready(function () {
  // Start document
  $(".btn").click(function () {
    // Using "this" means the target or button triggering the event instead of using "event" param
    $("#filterList li").removeClass("selected");
    $(this).parent().addClass("selected");

    const flickrApi =
      "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
    const searchContent = $(this).text();
    const flickrOptions = {
      tags: searchContent,
      format: "json",
    };

    $.getJSON(flickrApi, flickrOptions, (data) => {
      // console.log(data.items);

      const ul = document.createElement("ul");
      ul.setAttribute("id", "imgList");

      // Looping through the data
      $.each(data.items, (index, profile) => {
        // creating  element for each obj.

        const li = document.createElement("li");
        const a = document.createElement("a");
        a.setAttribute("href", profile.link);
        const img = document.createElement("img");
        img.setAttribute("src", profile.media.m);

        // Appending
        a.appendChild(img);
        li.appendChild(a);
        ul.appendChild(li);
      });

      $("section#results").html(ul);
      // End getJSON
    });
    // End btn
  });
  // End document
});
 */
