'''
Created on Nov 4, 2013

@author: zhenga
'''



import c0
import tkinter
from tkinter import ttk
import time
import math
import new_create
import zellegraphics as zg



class Position_Data():
    def __init__(self):
        self.mouse_position_x = None
        self.mouse_position_y = None


# # Read this before grading please: It will not work if you just push'run buttom',Because I made change on this
#### to allow my team to call it from Main_GUI.
# ## If you want to run this individualy, 1.delet 'lili' parameter in main().
#### 2.unhash(=delet#sign) line35    3. unhash connect part in gui()    4.unhash connect function.
####and this sprint will
# ## work perfectly~~

def main(lili):


    position_data = Position_Data()
    root = tkinter.Tk()
#     lili = c0.Box_of_Fun_Toys_for_Robots(None, None, None, None)
    distance_to = [0, 0]  # vecter distance to move everytime
    B = [zg.Point(0, 0)]  # a point list containing all position(x,y)
    gui(root, lili, position_data, distance_to, B)

#     Sprint1_m2_walk_under_input.gui(root, lili)
    root.mainloop()

def gui(root, lili, position_data, distance_to, B):

    main_frame = ttk.Frame(root, padding=5, relief='raised')
    main_frame.grid()

#     connect_label = ttk.Label(main_frame, text='Input your port# or directly\n connect to simulator without input')
#     connect_label.grid()
#
#     port_label = ttk.Label(main_frame, text='  port of robot=')
#     port_label.grid()
#     entry_port = ttk.Entry(main_frame, width=10)
#     entry_port.grid()
#     lili.port = entry_port
#
#
#     con_button = ttk.Button(main_frame, text="Connect")
#     con_button.grid()
#     con_button['command'] = lambda: connect(lili)

    instructions = 'Sprint2 Click the mouse button to get position,\n'
    instructions = instructions + 'for the robot to go'
    label = ttk.Label(main_frame, text=instructions)
    label.grid()

    go_button = ttk.Button(main_frame, text="Go Those Points")
    go_button.grid()
    go_button['command'] = lambda: go_all_points(lili, distance_to, B)

    canvas = tkinter.Canvas(main_frame, background='pink', width=400, height=400)
    canvas.grid()

    canvas.bind('<Button-1>', lambda event: left_mouse_click(event, lili, distance_to, B))

# def connect(lili):
#     if lili.port.get() == '':
#         lili.robot = new_create.Create('sim')
#     else:
#         entry0_port = lili.port.get()
#         poooo = int(entry0_port)
#         lili.robot = new_create.Create(poooo)

def left_mouse_click(event, lili, distance_to, B):
    canvas = event.widget
    canvas.create_oval(event.x - 5, event.y - 5,
                        event.x + 5, event.y + 5,
                      fill='yellow', width=0)

    B.append(zg.Point(event.x, event.y))
    print(B)


def go_all_points(lili, distance_to, B):

    for k in range(1, len(B)):
        if B[k].x > B[k - 1].x and B[k].y > B[k - 1].y:  # Quardratic 4
            print(B)
            distance_to[0] = B[k].x - B[k - 1].x
            distance_to[1] = B[k].y - B[k - 1].y

            lili.robot.go(0, (-math.atan(distance_to[1] / distance_to[0]) * 180 / math.pi) / 3)
            time.sleep(3)
            lili.robot.go(math.sqrt(distance_to[0] * distance_to[0] + distance_to[1] * distance_to[1]) / 3, 0)
            time.sleep(3)
            lili.robot.go(0, (math.atan(distance_to[1] / distance_to[0]) * 180 / math.pi) / 3)
            time.sleep(3)
            lili.robot.stop()

            print(B, '4')

        elif B[k].x > B[k - 1].x and B[k].y < B[k - 1].y:  # Quardratic 1
            print(B)
            distance_to[0] = B[k].x - B[k - 1].x
            distance_to[1] = B[k - 1].y - B[k].y

            lili.robot.go(0, (math.atan(distance_to[1] / distance_to[0]) * 180 / math.pi) / 3)
            time.sleep(3)
            lili.robot.go(math.sqrt(distance_to[0] * distance_to[0] + distance_to[1] * distance_to[1]) / 3, 0)
            time.sleep(3)
            lili.robot.go(0, (-math.atan(distance_to[1] / distance_to[0]) * 180 / math.pi) / 3)
            time.sleep(3)
            lili.robot.stop()

            print(B, '1')

        elif B[k].x < B[k - 1].x and B[k].y > B[k - 1].y:  # Quardratic 3
            print(B)
            distance_to[0] = B[k - 1].x - B[k].x
            distance_to[1] = B[k].y - B[k - 1].y

            lili.robot.go(0, -(math.atan(distance_to[0] / distance_to[1]) * 180 / math.pi + 90) / 3)
            time.sleep(3)
            lili.robot.go(math.sqrt(distance_to[0] * distance_to[0] + distance_to[1] * distance_to[1]) / 3, 0)
            time.sleep(3)
            lili.robot.go(0, (math.atan(distance_to[0] / distance_to[1]) * 180 / math.pi + 90) / 3)
            time.sleep(3)
            lili.robot.stop()

            print(B, '3')

        elif B[k].x < B[k - 1].x and B[k].y < B[k - 1].y:  # Quardratic 2
            print(B)
            distance_to[0] = B[k - 1].x - B[k].x
            distance_to[1] = B[k - 1].y - B[k].y

            lili.robot.go(0, (math.atan(distance_to[0] / distance_to[1]) * 180 / math.pi + 90) / 3)
            time.sleep(3)
            lili.robot.go(math.sqrt(distance_to[0] * distance_to[0] + distance_to[1] * distance_to[1]) / 3, 0)
            time.sleep(3)
            lili.robot.go(0, -(math.atan(distance_to[0] / distance_to[1]) * 180 / math.pi + 90) / 3)
            time.sleep(3)
            lili.robot.stop()

            print(B, '2')







#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
