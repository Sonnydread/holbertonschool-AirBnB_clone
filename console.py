#!/usr/bin/python3
"""Implementation of console 001"""


import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """func to do"""
        return True

    def do_EOF(self, arg):
        """func to do"""
        return True

    def emptyline(self):
        """func to do"""
        pass

    def help_quit(self):
        print("exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
