# AirBnB Clone Project

## Project Description

The AirBnB Clone project is a Python-based command-line application that serves as the foundation for building a simplified version of the AirBnB platform. It includes a command interpreter that allows users to manage AirBnB objects, such as users, states, cities, and places. The project focuses on implementing a parent class for object initialization and serialization/deserialization, creating specific classes for AirBnB objects, and building a file storage engine.

## Command Interpreter

The command interpreter provides a Shell-like interface, allowing users to interact with the application in both interactive and non-interactive modes. It supports various commands for creating, retrieving, updating, and destroying objects.

### How to Use

To start the command interpreter, run the `console.py` script. Ensure you have the required Python version (3.8.5) and dependencies installed.

#### Interactive Mode:

In interactive mode, enter commands at the `(hbnb)` prompt.

```bash
$ ./console.py
(hbnb) help
# Output help information
(hbnb) create User
# Create a new User object
(hbnb) show User 123
# Display information about the User with ID 123
(hbnb) quit
# Exit the command interpreter
