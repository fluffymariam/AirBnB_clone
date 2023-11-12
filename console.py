#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
import models

class HBNBCommand(cmd.Cmd):
    """
    This class defines the command interpreter for the program.
    """

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def do_quit(self, arg):
        """
        Exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl-D)
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

    def help_quit(self):
        """
        Print help message for quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Print help message for EOF command
        """
        print("Exit the program on EOF (Ctrl-D)")

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print its id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string of an instance based on class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string rep ll instances or instances of a specific class.
        Usage: all [class name]
        """
        args = arg.split()
        obj_list = []
        if not arg:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        for obj in storage.all().values():
            if obj.__class__.__name__ == args[0]:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on clae and id with a new attribute value.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                obj = storage.all()[key]
                setattr(obj, args[2], args[3][1:-1])
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
