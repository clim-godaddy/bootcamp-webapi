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

