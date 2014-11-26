"""
The  **** Stop! In the Name of Love! **** Python Capstone Project.

CSSE 120 - Introduction to Software Development (Robotics).
Fall term, 2013-2014.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is:
   PUT-YOUR-NAME-HERE
Most of the code in this project by that author appears in this module
OR in other modules whose name begins with
    m1_... or c1_... for person 1,  m2_... or c2_... for person 2, etc.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import c0  # @UnusedImport
import m2  # @UnusedImport
import m3  # @UnusedImport
import m4  # @UnusedImport

import tkinter
from tkinter import ttk
import new_create
import time

def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('Testing functions in module m1:\n')
    root = tkinter.Tk()
    root.title("Project")
    lili = c0.Box_of_Fun_Toys_for_Robots(20, 2, 'sim', 8)

    gui(root, lili)
    m2.gui(root, lili)
    m3.gui(root, lili)

    root.mainloop()


def gui(root, lili):
    """ Adds widgets and sets up their callbacks. """


    main_frame = ttk.Frame(root, padding=5, relief='raised')
    main_frame.grid()

    con_button = ttk.Button(main_frame, text="Connect")
    con_button.grid()
    con_button['command'] = lambda: connect(lili)

    discon_button = ttk.Button(main_frame, text="Disconnect")
    discon_button.grid()
    discon_button['command'] = lambda: disconnect(lili)

def connect(lili):
    port = lili.get_port()
    lili.robot = new_create.Create(port)

def disconnect(lili):
    lili.robot.shutdown()



#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
