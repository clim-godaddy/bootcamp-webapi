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
