#!/usr/bin/python3
""" command interpreter for our Air BnB clone"""


import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ custom command interpreter"""
    
    
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Exit the program """
        return True
    
    def do_EOF(self, arg):
        """Exit the program with an EOF (Ctrl+d)"""
        print()
        return True
    
    def emptyline(self):
        """
        do nothing when on an empty line
        """
        pass
    
    def do_create(self, arg):
        """
        Creates new instace of a base model, saves and prints its id
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                fresh_instance = eval(arg)()
                fresh_instance.save()
                print(fresh_instance.id)
            except NameError:
                print("** class name doesn't exist **")
   
    def do_show(self, arg):
        """
        Prints the string representation of an instance
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[key])
                
    def do_destroy(self, arg):
        """
        deletes an instance based on class name and id
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")
                
    def do_all(self, arg):
        """
        Prints all string reps of instances
        Usage: all [class name]
        """
        args = arg.split()
        all_objs = storage.all()
        if not arg:
            print([str(value) for value in all_objs.values()])
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in all_objs.items() if args[0] in key])
                
                    
    def do_update(self, arg):
        """
        Updates an instance based on class id and name
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        all_objs = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print ("** class does not exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                obj = all_objs[key]
                setattr(obj, args[2], args[3].strip('""'))
                obj.save()
            else:
                print("** no instance found **")
                    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
