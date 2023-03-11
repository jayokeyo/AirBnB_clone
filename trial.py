#!/usr/bin/python3
import cmd
import sys

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = "HelloWorld: "

    def do_prompt(self, line):
        ''' Modify the command prompt'''
        self.prompt = line + ": "

    def do_greet(self, person):
        '''Greeets the user'''
        if (person):
            print("hello", person)
        else:
            print("hello")

    def help_greet(self):
        print('\n'.join(['Help on command greet',
            'Use: greet [name]', 'Return: hello [name]']))

    def do_introduce(self, line):
        '''Majigambo tupu'''
        print("I am Baba's choice for future president!!!")

    def do_quit(self, line):
        '''Quit from the prompt'''
        sys.exit(0);

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
