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
import m1  # @UnusedImport
import m3  # @UnusedImport
import m4  # @UnusedImport

import tkinter
from tkinter import ttk
import time


def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('Testing functions in module m2:\n')

    root = tkinter.Tk()

    lili = c0.Box_of_Fun_Toys_for_Robots(10, 2, 4, 2)

    m1.gui(root, lili)
    gui(root, lili)
    m3.gui(root, lili)


    root.mainloop()




def gui(root, lili):



    main_frame = ttk.Frame(root, padding=(50, 30), relief='raised')
    main_frame.grid()


    forward_button = ttk.Button(main_frame, text='Forward')
    forward_button.grid()
    forward_button['command'] = lambda: move_forward(lili)

    increase_button = ttk.Button(main_frame, text='Increase-seconds')
    increase_button.grid()
    increase_button['command'] = lambda: increase_s(lili)

    decrease_button = ttk.Button(main_frame, text='Decrease-seconds')
    decrease_button.grid()
    decrease_button['command'] = lambda: decrease_s(lili)
    """ Adds widgets and sets up their callbacks. """

def move_forward(lili):
    speed = lili.get_speed()
    angle = lili.get_angle()
    lili.robot.go(speed, angle)
    time.sleep(lili.time_value)
    lili.robot.stop()
    # print(lili.time_value)

def increase_s(lili):

    lili.time_value = lili.time_value + 1



def decrease_s(lili):
    lili.time_value = lili.time_value - 1



#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
