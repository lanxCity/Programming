// AJAX: Asynchronous JavaScript And XML
//XHR: XML HTTP Request
//initial name:  XMLHTTPRequest Object
// Request of the server is the process of asking server for information
// Response is when the server sent back its answer to the request.
// The web is built upon browsers (clients) send request to web service

// --------------------The process of AJAX
// A => Asynchronous (refers to how the request is sent to the web server )
// J => The language  you use to send Ajax request, process the incoming response, and updating the webpage
// A => and
// X => Extensible markup language (Originally, this was seen as the format the server response should be sent in. But it's not the only format you can receive data in. And it's not the most preferred format any longer.)

// -----In summary, AJAX programming process includes
// 1. Create an XMLHTTPRequest Object: This tells the web browser to get ready for AJAX request and the browser needs to create an object that has all the methods you'd need to send and receive data
// 2. Create a "call back function": The program you want to run when the server returns its response. It is used to process the returned data and update HTML on the page.
// 3. Open a request: Requires two pieces of information; i. The method the browser would use to send a request (post or get) and, ii. the url where the request is sent.
// 4. Send the request

// In nutshell, the first 3 steps gave the browser all the information needed before step 4 takes place.
// they use "var" instead
// AJAX comes with its own set of events

// ---------stage 1
// let formXHref = new XMLHttpRequest();

// --------stage 2
// most important of AJAX events is "onreadystatechange"
// the above event is triggered whenever there is change in ajax request, like "opening new request", "sending the request and receiving response".
// So we create a callback to response to such request; the function is called each time there is change in the state of the ajax request.
// in summary, for the function, we are only interested in the final change of state. That is when the service is back with response. we want to get that response and update our webpage.
// The XMLHttpRequest keeps track of the state using its special property, onreadystatechange. the prpty contains a number including current state of request. And it holds number "4" if request is done and server have sent its response.
// every XMLHttpRequest contents has a property called "responseText". The information that the web service sent back.
// The event handler(callback func) when the event takes place, "onreadystatechange".
/* formXHref.onreadystatechange = () => {
  if (formXHref.readyState > 1 && formXHref.readyState < 4) {
    console.log("Please wait");
  } else if (formXHref.readyState === 4) {
    //   create new element
    let sectionContainer = document.createElement("section");
    sectionContainer.setAttribute("id", "sectionBody");
    sectionContainer.innerHTML = formXHref.responseText;
    //   append the element to the existing container

    document.querySelector(".container").appendChild(sectionContainer);
    // document.body.innerHTML = sectionContainer.outerHTML;
  }
  /* else if (formXHref.readyState === 0) {
    alert("Please wait");
  } *
}; */

// ---------Step 3.
// Use "GET" if you want to send a request for data.
// Such as the result of a data base search
// Use "POST" if you want to send a data, just like a form
// the url is where the request is going. It could point to a file or a server side program on your web server.

// formXHref.open("GET", "./sample.html");

// --------step 4.
// If it's to send info to the server (such users' inputs from the web form, you can parse the "open" method that data from the form) using "post" method.

// But if it's just requesting for files from the server, "GET" is the best option. Such as the result of a database search, receiving set of tweets (using twitter as case study).
// Even typing url on the browser uses "GET" method since it's requesting data from the web server (either a page file, image, etc.); all that's required for a GET request is a url.

/* codeBtn.onclick = (event) => {
  formXHref.send();
  event.target.style.display = "none";
}; */

// For server side program to send a customized information When requesting for data from the server, you need to  send the service information; additional data to url sent to the server is required.
// E.g. http://www.lanxCity.org/customer.py?username=Bogson
// username is the name/property and the "=" sign assign a value "Bogson"  to that property

// The path after the "?" is called query string. It appears after the url and provide a way to send additional info that a web server can use to control the output of its response. Commonly, the data in the query string is used to search a data based information.
// Query string can be made up of one or more "name-value" pairs.

// E.g. http://www.lanxCity.org/customer.py?username=Bogson&password=123456

// While dealing with query string, there are some requirements; you can't just use any sign/char.
// A. In "Get" method, there are special encoding E.g &,"",+,space,etc. have special meaning in url
// & ~= %26, space ~= +, + ~= %2B, etc.
// To learn more, "www.url-encode-decode.com"
// NB: The get downside
// 1. The "get" method is the simplest you can also to send data but it has downside by showing and storing those data on the browser's history
// 2. And there are limited data you can put into the url e.g. IE can only handle url with 2,083 characters long.

// B. Just like "GET", "POSt" method also requires special encoding but also, you need setup special header for the request. And that's an instruction sent to the server telling it what type of data it should expect.
// If you are sending information that includes those char(s), you have to encode them; translate them to set of symbols that are safe.

// ----After, sending an AJAX request, the callback function wait for response from the server. And the web service reply with the text response "responseText"

// For dealing with lot of data, it's a good idea to have a structured data format.

// As identifiers that indicates what the data is, and easy for JS to analyse and use. Two common interchange format are "xml" and "JSON".
// 1. XML is similar to HTML. And like HTML, xml uses tags to structure data. But unlike HTML, xml tags are beyond handful of tags; you could create your own custom tags.
// And it is a very common format for exchanging data between computers. And most servers side language handle xml easily, unlike JS which involves several steps which include analyzing or parsing the xml and going through each of the node for extraction.
/*  E.g. 
<contacts>
  <contact>
    <name>Sodiq</name>
    <phone>08146257816</phone>
  </contact>
  <contact>
    <name>Rasheed</name>
    <phone>08106113235</phone>
  </contact>
  <contact>
    <name>Waris</name>
    <phone>09044957816</phone>
  </contact>
</contacts>
*/
// The advantage of this structured format is that it's easy for the computer to split into usable junks.
// The process of breaking a file up into easily access path is called "Parsing"
// But using ajax to access xml requires alot, unlike other server side language

// For many ajax app, there is a better JS-like data format called "JSON". And it has become the popular way to xchange data using Ajax.
// There is limited to how much you can use ajax to request for data from the server; the term "Same origin policy" which controls how JS can access data from the web server is a factor.

// That is, ajax can communicate from one page to another on the same web server. But not allow to access other web service. e.g. requesting data from another website from my website such as "google map".
// In addition, switching protocols ("http" to "https"), port numbers (http://127.0.0.1:5500/) => 5500, and switching host ("www" to "db") is forbidding.
// www => host
// mysever.com => domain

// NB: You can't open ajax from your local machine (CORS policy); cross-origin resource sharing, external server and domain.
// To circumvent the same origin policy.
// 1. Use of JSON with padding: The ability to link to JS file across domains e.g. copy links for google fonts, icons, etc. or linking to photos of another website e.g. "unsplash"
// CDN : content delivery network
// 2. create a Web proxy: You need server side script(php,ruby, etc.) so that web service can request data from the service at the domain, your server script can access info from another web service. And ajax talks to the script to return the my page.
// 3. CORS: it requires some setup on the service path.

// ------------------Data exchange format, JSON
// A. Call backs and response format
// 1. Callback
// There may be issues while requesting data like server program crashes, server unable to connect to database, etc, and therefore, it's good to check the status of the response.
// So to handle any possible error, we can check for it inside the callback.
// a. the use another prpty of the request object, "status"
// The "status" prpty is a number sent from the server. And "200" means "okay, everything went well"; it's a standard response for successful http request. So other number usually not good.
// status 404: file not found
// status 401: if you are not authorized to access a url because it requires other permission to login to access
// status 500: when server has some kind of error, often the server side program processing the request isn't working.
// The webserver commonly respond to ajax request with a "text-response" (plain text or html); Even though server may respond with xml, html, or Json, to web browsers, those response are just a string of characters.
// Two other text format are xml (reliable data format but difficult to use  with JS) and JSON (javascript-like data format)

let formXHref = new XMLHttpRequest();

formXHref.onreadystatechange = () => {
  let pageContainer = document.querySelector(".container");
  // let pageHead = document.querySelector("#section-heading");
  console.log("hello world");
  if (formXHref.readyState === 4) {
    if (formXHref.status === 200) {
      //   create new element
      let pageBody = document.createElement("section");
      pageBody.setAttribute("id", "sectionBody");
      pageBody.innerHTML = formXHref.responseText;

      //   append the element to the existing container
      pageContainer.appendChild(pageBody);
      // pageContainer.insertBefore(pageBody, pageHead);
      // document.querySelector(".container").appendChild(pageBody);
      // document.body.innerHTML = pageBody.outerHTML;
    } /* else if (formXHref.status === 404) {
      // File not found
      alert("File not found");
    } else if (formXHref.status === 500) {
      // Server has a problem
    } */ else {
      // alert(formXHref.statusText);
      document.body.innerHTML = `<h1>Error! File ${formXHref.statusText}</h1>`;
    }
  }
};

formXHref.open("GET", "./sample.html");

codeBtn.onclick = (event) => {
  formXHref.send();
  event.target.style.display = "none";
};

// JSON: JavaScript Object Notation. It is a way to use JS to pass information around. It use JS array and object to store data.
// Two diff ways to format JSON: use of i.) array notation and, ii.) object notation. But it's common to combine both
// Like JS, JSON object also require "key-value pair";
// Unlike JS, JSON object "key or properties" required to be quote (like python), but must be "double quote" for both "key and value" as "single quote" would not work.
// After writing JSON object, we can verify it using online validator "jsonlint.com" to check if there is mistake or not.
// Since browsers treated all response form the server as plain string (including JSON file), this string needs to converted into JS that the browser understand. And the process is known as "parsing". And all currrent browser can do it using a single command.
