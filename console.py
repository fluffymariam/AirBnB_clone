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

    def emptyline(self):
        '''Pass empty line or on enter'''
        pass
    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

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
        # all User
        parts = arg.split()
        if len(parts) < 1:
            print(storage.all())
        else:
            if parts[0] not in globals():
                print("** class doesn't exist **")
            else:
                for key in storage.all():
                    if parts[0] == key.split('.')[0]:
                        print(storage.all()[key])

    def do_update(self, arg):
        """
        Updates an instance based on class and id with a new attribute value.
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

    def counter(self, arg):
        ''' count how many obj we have'''
        count = 0
        for value in storage.all():
            class_name = value.split(".")[0]
            if class_name == arg:
                count += 1
        return count

    def default(self, arg):
        '''
        handle daynamic commands
        using : <class name>.<method name>(<args>)
        '''
        try:
            names, args = arg.strip(')').split('(')
            class_name, method_name = names.split('.')
            if (method_name == "count"):
                print(self.counter(class_name))
            else:
                fun = "do_{}".format(method_name)
                method_name = getattr(self, fun, None)
                if method_name is not None:
                    if len(args) == 0:
                        method_name(class_name)
                else:
                    args = args.replace('"', "")
                    args = args.replace(" ", "")
                    args = args.replace(",", " ")
                    args = "{} {}".format(class_name, args)
                    method_name(args)
        except Exception:
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
