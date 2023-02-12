## AirBNB Clone

 This project is a simple copy of the [AirBNB website](https://www.airbnb.com/). It will be built over a period of 4 months until the following features are imlemented (not all features from the actual website will be implemented)
* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them) 

### The Command Interpreter

a.k.a the console, it is very similar to shell except it's a single use function. it is a command-line interface to manage the objects of the project such as:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object
The console should work both in interactive and non-interactive modes.
- In interactive mode:
	
	```
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$
	```

- In non-interactive mode:
	
	```
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	```

#### How to start it
#### How to use it
#### Examples
