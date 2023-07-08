#!/usr/bin/python3
"""Implementation of console 001"""


import cmd
import json
from models.place import Place
from models.state import State
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Comand interpreteiton"""
    prompt = '(hbnb)'
    cls = ["BaseModel", "State", "City", "User", "Place", "Amenity", "Review"]

    def do_create(self, arg):
        """functions to operate"""
        if not arg:
            print("** class name missing **")
        elif arg in self.cls:
            new = eval(arg)()
            eval(arg).save(new)
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """functions to operate"""
        if not arg:
            all_objs = storage.all()
            lis = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                lis.append(str(obj))
            print(lis)
        elif arg in self.cls:
            all_objs = storage.all()
            lis = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if arg == obj.__class__.__name__:
                    lis.append(str(obj))
            if len(lis) > 0:
                print(lis)
            else:
                print("** class doesn't exist **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """functions to operate"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[1]:
                all_objs = storage.all()
                for key in all_objs.keys():
                    o = all_objs[key]
                    if o.id == args[1] and o.__class__.__name__ == args[0]:
                        print(o)
                        break
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """functions to operate"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                for key in all_objs.keys():
                    o = all_objs[key]
                    if o.id == args[1] and o.__class__.__name__ == args[0]:
                        del all_objs[key]
                        storage.save()
                        break
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """functions to operate"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                all_objs = storage.all()
                for key in all_objs.keys():
                    o = all_objs[key]
                    if o.id == args[1] and o.__class__.__name__ == args[0]:
                        setattr(o, args[2], args[3].strip('"'))
                        break
                else:
                    print("** no instance found **")

    def do_quit(self, arg):
        """func to do"""
        return True

    def do_EOF(self, line):
        """func to do"""
        return True

    def emptyline(self):
        """func to do"""
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
