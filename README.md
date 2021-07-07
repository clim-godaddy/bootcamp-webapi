# Bootcamp Web API


## What is API

Allows communications between software

* Application interacting with OperatingSystem (e.g. open file)
* Shell (bash, zsh) – scripting over OS

Hands On

* Interact with Shell
  * Show information (`date`, `whoami`, `cat <file>`, `less`)
  * Navigate (`cd`, `ls`)
* Interact with other programs
  * `git`
* Build simple Quotes API
  * Create `quotes` directory
  * Create `quote` file `07.txt` to complete quote for days of the week
  * Script to show random quote, day-of-week quote


## Web - HTTP

Now that we have an Application, we can share with the world
* Web Server: An application serving contents (IP address, e.g. 208.109.192.70)
  * Analogy: A customer ordering food via the server in a restaurant
* DNS: We need a name for our server to make it easier for others to find instead of IP
* Web Server can serve both static & dynamic contents
* Reponse statuc codes are organized (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
  * 1xx: Informational
  * 2xx: Success
  * 3xx: Redirects
  * 4xx: Client errors
  * 5xx: Server errors


Hands On

* Host a local server serving the files from previous session
  * `python -m http.server 8080 --directory quotes`
* Use browser to view files
  * Note `index` page shows a listing of files (similar to `ls`)
* HTTP is a simple protocol
  * `telnet localhost 8080`
  * Type the following
    ```
    GET / <enter> <enter>
    ```
* `telnet` establishes a connection to the server
  * Run echo server
    * `python echo_server.py`
    * Review implementation
  * Communicate with server via `telnet`
    * `telnet localhost 1234`
    * Type some text
    * Quit: `Ctrl+]` -> `quit`


## Web - HTML

HTML (HyperText Markup Language)
* Build engaging content
  * HyperText: text that links to other resources (`index` page)
* Can refer to additional resources
  * Images
  * CSS (styles)
  * Javascript (code running on browser)

Hands On

* Convert files to html, use some html elements
  * `<blockquote>` or `<q>`
  * Play with HTML


## Remote/Web API

* HTML: Only targets Browsers, there are many types of Applications
  * Browser
  * Desktop Applications
  * Mobile Applications
* Consume HTML content directly
  * Scraping – common as a quick and dirty approach to consumer external data, brittle
* Possible approach: Go back to data only, continue to use HTTP
  * Text – require parsing to identify quotes, author, etc
  * CSV – comma separate (author, quote)
  * XML (Like HTML, but describe just the data)
  * JSON
* RPC (Remote procedure call)
  * XML-RPC, SOAP, CORBA

Hands On

* Inspect output from `Web - HTML`
  * Think about how to process/parse necessary data
  * How is it brittle?


## Rest API

* Representational state transfer (REST)
  * NOUNs: Resources identified via URI
  * VERBs: Re-using HTTP Methods (GET, POST, PUT, DELETE)
  * Media Type (Response): JSON (JavaScript Object Notation) most common, Yaml, XML
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

Hands On
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


## Rest API - CRUD

Create Read Update Delete
* Common set of operations for resource based API
  * `POST /quotes/`: Create a new quote with data in the body
  * `GET /quotes/<quote-id>`: Get a specific quote
  * `PUT /quotes/<quote-id>`: Create a new quote/Update existing entire quote
  * `DELETE /quotes/<quote-id>`: Delete existing quote
  * `GET /quotes/`: Get a list of all quotes
  * `PATCH /quotes/<quote-id>`: Update existing quote with only fields specified in the body
* Example:
  * https://quotes.rest/
* Special
  * Search/Filtering
    * List with query params or body params
    * Possibly include `VERB` (e.g. `/search`) in the URI

Hands On
* Play with API


## OpenAPI (Swagger)

REST API Specification (https://www.openapis.org/)
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
  * Code-First: Generate Swagger definition from code

Hands On
* Inspect Example Endpoint OpenAPI (https://quotes.rest/)
* Design a simple Quote OpenAPI (id, author, quote)
  * Swagger (https://editor.swagger.io/)
  * Postman (https://www.postman.com/)
    * Download & Install Postman
