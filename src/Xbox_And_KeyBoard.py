'''
Created on Oct 28, 2013

@author: doolansr
'''
'''using joy to key
and grabing the inputs from:
start
joy.cpl'''
import c0
import m1
import m2
import m3
import Main_GUI
import tkinter
from tkinter import ttk

def main():
    root = tkinter.Tk()
    print(' ')
    box_of_toys = c0.Box_of_Fun_Toys_for_Robots
    gui(root, box_of_toys)

    root.mainloop()
def gui(root, box_of_toys):
    'imports key board and x-box compatablity'
    # connect start
    root.bind_all('<Key-z>', lambda event: m1.connect(box_of_toys))
    # Disconnect select
    root.bind_all('<Key-p>', lambda event:m1.disconnect(box_of_toys))
    # increase time RB
    root.bind_all('<Key-r>', lambda event:m2.increase_s(box_of_toys))
    # go move a

    root.bind_all('<Key-a>', lambda event: m3.Go_move(box_of_toys))

    # decrease speed
    root.bind_all('<Key-a>', lambda event: m2.move_forward(box_of_toys))
    # decrease speed LB

    root.bind_all('<Key-l>', lambda event: m2.decrease_s(box_of_toys))
    # stop b
    root.bind_all('<Key-b.', lambda event: m3.stop_please(box_of_toys))

    # decrease speed
    root.bind_all('<Key-l>', lambda event: m2.decrease_s(box_of_toys))
    # stop b
    root.bind_all('<Key-b>', lambda event: m3.stop_please(box_of_toys))
    # stop

    # right turn
    root.bind_all('<Key-s>'), lambda event: Main_GUI.change_angle(box_of_toys, 60)
    # left turn
    root.bind_all('<Key-d>'), lambda event:Main_GUI.change_angle(box_of_toys, -60)




#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
