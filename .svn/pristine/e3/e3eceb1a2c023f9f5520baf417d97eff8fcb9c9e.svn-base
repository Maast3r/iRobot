'''
Created on Nov 4, 2013

@author: zhenga
'''



import c0

import tkinter
from tkinter import ttk
import time
import math
import Sprint1_m2_walk_under_input


class Pen_Data():
    def __init__(self):
        self.mouse_position_x = None
        self.mouse_position_y = None



def main():

    pen_data = Pen_Data()

    root = tkinter.Tk()

    lili = c0.Box_of_Fun_Toys_for_Robots(None, None, None, None)


    A = [0, 0, 0]
    gui(root, lili, pen_data, A)
    Sprint1_m2_walk_under_input.gui(root, lili)

    root.mainloop()

def gui(root, lili, pen_data, A):

    main_frame = ttk.Frame(root, padding=5, relief='raised')
    main_frame.grid()

    instructions = 'Click the left mouse button to get position,\n'
    instructions = instructions + 'for the robot to go'
    label = ttk.Label(main_frame, text=instructions)
    label.grid()

    canvas = tkinter.Canvas(main_frame, background='pink', width=500, height=500)
    canvas.grid()

    canvas.bind('<Button-1>', lambda event: left_mouse_click(event, lili, A))

    button = ttk.Button(main_frame, text='Flip pen color')
    button.grid()


def left_mouse_click(event, lili, A):
    canvas = event.widget
    canvas.create_oval(event.x - 5, event.y - 5,
                        event.x + 5, event.y + 5,
                      fill='yellow', width=0)

    if event.x > A[0] and event.y > A[1]:  # Quardratic 4
        A[0] = A[0] + event.x
        A[1] = A[1] + event.y

        lili.robot.go(0, -math.atan(A[1] / A[0]) * 180 / math.pi)
        time.sleep(1)
        lili.robot.go(math.sqrt((A[0]) ^ 2 + (A[1]) ^ 2), 0)
        time.sleep(1)
        lili.robot.go(0, math.atan(A[1] / A[0]) * 180 / math.pi)
        time.sleep(1)

        lili.robot.stop()
        print(A, '4')

    elif event.x > A[0] and event.y < A[1]:  # Quardratic 1
        A[0] = A[0] + event.x
        A[1] = A[1] + event.y

        lili.robot.go(0, math.atan(A[1] / A[0]) * 180 / math.pi)
        time.sleep(1)
        lili.robot.go(math.sqrt((A[0]) ^ 2 + (A[1]) ^ 2), 0)
        time.sleep(1)
        lili.robot.go(0, -math.atan(A[1] / A[0]) * 180 / math.pi)
        time.sleep(1)
        lili.robot.stop()
        print(A, '1')

    elif event.x < A[0] and event.y > A[1]:  # Quardratic 3
        A[0] = A[0] + event.x
        A[1] = A[1] + event.y

        lili.robot.go(0, -math.atan(A[1] / A[0]) * 180 / math.pi + 90)
        time.sleep(1)
        lili.robot.go(math.sqrt((A[0]) ^ 2 + (A[1]) ^ 2), 0)
        time.sleep(1)
        lili.robot.go(0, math.atan(A[1] / A[0]) * 180 / math.pi + 90)
        time.sleep(1)
        lili.robot.stop()
        print(A, '3')
    elif event.x < A[0] and event.y < A[1]:  # Quardratic 2
        A[0] = A[0] + event.x
        A[1] = A[1] + event.y

        lili.robot.go(0, math.atan(A[1] / A[0]) * 180 / math.pi + 90)
        time.sleep(1)
        lili.robot.go(math.sqrt((A[0]) ^ 2 + (A[1]) ^ 2), 0)
        time.sleep(1)
        lili.robot.go(0, -(math.atan(A[1] / A[0]) * 180 / math.pi + 90))
        time.sleep(1)
        lili.robot.stop()
        print(A, '2')











#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
