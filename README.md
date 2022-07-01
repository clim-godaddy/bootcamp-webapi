# Bootcamp Web API

Requirements

* [Docker](https://www.docker.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
  * [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) plugin
* [Postman](https://www.postman.com/downloads/)
* [Swagger](https://editor.swagger.io/))


## What is API

Application: User interacting with machine, human to machine
API: Application Programming Interface, machine to machine
Allows communications between software

* Application interacting with OperatingSystem (e.g. open file)
* Shell (bash, zsh) – scripting over OS

Demo/Hands On (part-01)

* Sample clients consuming API
  * Text editor `vscode` viewing/editing files
  * Web Browser viewing local files in Read-Only mode
    * Note `index`/`parent` directory

* Simple Quotes CLI Application
  * `cd part-01`
  * `./quote-day.sh`: Show day-of-week quote
  * `./quote-random.sh`: Show random quote


## Web - HTTP

Now that we have an Application, we want to share with the world
* Web Server: An application serving contents
* Web Client: An application requesting contents

Analogy: A customer (Web Browser) ordering food via the server (Web Server) in a restaurant

* Web Server can serve:
  * static: images, binary contents, files
  * dynamic: current time, transforming input data, reading from database
* [Reponse status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) are organized
  * 1xx: Informational
  * 2xx: Success
  * 3xx: Redirects
  * 4xx: Client errors
  * 5xx: Server errors


Demo/Hands On (part-01)

* Start server
  * `cd part-01`
  * `./start-server.sh`
* Use browser to view files
  * Note `index` page shows a listing of files
* HTTP is a simple protocol (URI, Verbs)
  * Curl
    * `curl localhost:8080/01.txt`
    * `curl –X GET localhost:8080/01.txt`
  * Chrome:
    * Browse to `localhost:8080/01.txt`
    * Inspect Network: View > Developer Tools > Network
    * Note General Section
  * Postman:
    * Settings > ScratchPad
    * Paste `localhost:8080/01.txt` > `Send`
    * Inspect output
* Navigate to a non-existent location: `404 Not Found`


Bonus

* Raw TCP communication
  * `telnet localhost 8080`
  * Type the following
    ```
    GET / <enter> <enter>
    ```


## Web - HTML

HTML (HyperText Markup Language)
* Build engaging content
  * HyperText: text that links to other resources (`index` page)
* Can refer to additional resources
  * Images
  * CSS (styles)
  * Javascript (code running on browser)

Demo/Hands On (part-03)

* Start server
  * `cd part-03`
  * `./start-server.sh`
* Convert `quotes` to html, use some html elements
  * `<blockquote>` or `<q>`
  * Feel free to play with HTML, reload page


## Remote/Web API

* HTML: Only targets Browsers, more for Human consumption.  There are many types of Applications:
  * Browser
  * Desktop Applications
  * Mobile Applications
* These applications can consume HTML content directly
  * Scraping – common as a quick and dirty approach to consumer external data, brittle
* Possible approach: Go back to *raw* data only, continue to use HTTP
  * Text – require parsing to identify quotes, author, etc
  * CSV – comma separate (author, quote)
  * XML (Like HTML, but describe just the data)
  * JSON

Demo/Hands On (part-03)

* Start server
  * `cd part-03`
  * `./start-server.sh`
* Inspect output from `Web - HTML`
  * Chrome: `Right Click` -> `Inspect`
  * Think about how to process/parse necessary data
  * How is it brittle?
  * Compare `.html` vs `.txt`


## Rest API

* Representational state transfer (REST)
  * NOUNs: Resources identified via URI (unique name)
  * VERBs: Re-using HTTP Methods (GET, POST, PUT, DELETE)
  * Media Type (Response): JSON (JavaScript Object Notation) most common
  * Similar to browsing regular website, but getting response in JSON
  * Payload is very small compared to HTML
  * Has a schema, this makes it very easy for any Applications to consume the data

* JSON (JavaScript Object Notation)
  * Most common Media Type (Response)
  * Benefits
    * Human readable, data self documenting with good naming
    * Easy to consume
    * Example
      ```json
      {
        "id": 1,
        "author": "Lao Tzu",
        "quote": "The journey of a thousand miles begins with one step."
      }
      ```

Demo/Hands On (part-05)

* Start server
  * `cd part-05`
  * `./start-server.sh`
* Update quotes to JSON format
* Fetching JSON data from Browser
  * Open Developer Console
    ```javascript
    response = await fetch('./01.json')
    json = await response.json()
    json.author
    json.quote
    ```
* Inspect `01.html`
  * Note how we are using JavaScript to retrieve data

Bonus

* Text
  ```javascript
  txtResponse = await fetch('./01.txt')
  txt = await response.json()
  txtSplit = txt.Split(/\n/)
  txtData = {
    author: txtSplit[1],
    quote: txtSplit[0]
  }
  ```
  Limitation: Quote cannot have new line.
* CSV
  ```javascript
  csvResponse = await fetch('./01.csv')
  csv = await response.json()
  csvSplit = txt.Split(/,/)
  csvData = {
    author: csvSplit[1],
    quote: csvSplit[0]
  }
  ```
  Limitation: Cannot handle quote with commas.


## Rest API - CRUD

Create Read Update Delete
* Common set of operations for resource based API (Remember VERB NOUN)
  * `POST /quotes/`: Create a new quote with data in the body
  * `GET /quotes/<quote-id>`: Get a specific quote
  * `PUT /quotes/<quote-id>`: Create a new quote/Update existing entire quote
  * `DELETE /quotes/<quote-id>`: Delete existing quote
  * `GET /quotes/`: Get a list of all quotes
  * `PATCH /quotes/<quote-id>`: Update existing quote with only fields specified in the body
* Special
  * Search/Filtering
    * List with query params or body params
    * Possibly include `VERB` (e.g. `/search`) in the URI

Demo
  * Cart API


## OpenAPI (Swagger)

REST API Specification [OpenAPIs](https://www.openapis.org/)
* Describe API (Documentation)
  * Endpoints
  * Inputs and Outputs (Schema)
  * Support calling API against endpoints
  * Include examples
* Benefits
  * Validation/Linting on Specification
  * Data Validation
  * Documentation
  * Code Generation (for Design First approach)
  * Tools
    * Design: Graphical Editors
    * Mock Servers
    * Testing
* Two Approaches:
  * Design-First: Preferable, consumer focused
  * Code-First: Generate OpenAPI Spec definition from code
    * less control

Demo/Hands On (part-06)

* Start server
  * `cd part-06`
  * `./start-server.sh`
* Demo Quote OpenAPI (id, author, quote)
  * [Swagger](https://editor.swagger.io/)
    * Load `quotes.json`
    * Set parameters, Execute


## OpenAPI - Design Exercise

We have an API specification for our products resource, now we need the cart item resources defined. Use the [Swagger Editor](https://editor.swagger.io/)

1. Load [./part-07/api.json](./part-07/api.json) into the editor
2. First lets define the Model or Schema
    * what type of data does a shopping cart have in it
3. Create the cartitems/ URLs. Different for resources & collections
4. Define the CRUD operations and a R-Collections
5. Do the [status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) make sense
6. Make sure to save a copy of your spec. You will need it to build your API
