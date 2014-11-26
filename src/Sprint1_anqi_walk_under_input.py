'''
Created on Oct 31, 2013

@author: zhenga
'''

import c0
import m1
import tkinter
from tkinter import ttk
import time



def main():


    root = tkinter.Tk()
    root.title("Controler Window")

    lili = c0.Box_of_Fun_Toys_for_Robots(None, None, 'sim', None)

    m1.gui(root, lili)
    gui(root, lili)


    root.mainloop()



def gui(root, lili):

    frame_big = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_big.grid()

    main_label = ttk.Label(frame_big, text='Enter your data and choose \n a style to walk~')
    main_label.grid(row=1, column=0)

    frame_0 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_0.grid()

    time_label = ttk.Label(frame_0, text='moving time=')
    time_label.grid(row=2, column=0)
    entry_time = ttk.Entry(frame_0, width=10)
    entry_time.grid(row=2, column=1)
    lili.time_value = entry_time

    speed_label = ttk.Label(frame_0, text='moving speed=')
    speed_label.grid(row=3, column=0)
    entry_speed = ttk.Entry(frame_0, width=10)
    entry_speed.grid(row=3, column=1)
    lili.speed = entry_speed

    angle_label = ttk.Label(frame_0, text='moving angle=')
    angle_label.grid(row=4, column=0)
    entry_degree = ttk.Entry(frame_0, width=10)
    entry_degree.grid(row=4, column=1)
    lili.angle = entry_degree




    frame_1 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_1.grid()

    button_forward = ttk.Button(frame_1, text='Farward')
    button_forward.grid(row=5, column=0)
    button_forward['command'] = lambda: forward_input(lili)


    button_backward = ttk.Button(frame_1, text='Backward')
    button_backward.grid(row=5, column=1)
    button_backward['command'] = lambda: back_ward_input(lili)




    frame_3 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_3.grid()

    button_spinright = ttk.Button(frame_3, text='Spin Right')
    button_spinright.grid(row=6, column=0)
    button_spinright['command'] = lambda: spin_right_input(lili)

    button_spinleft = ttk.Button(frame_3, text='Spin Left')
    button_spinleft.grid(row=6, column=1)
    button_spinleft['command'] = lambda: spin_left_input(lili)



    frame_5 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_5.grid()
    button_curveright = ttk.Button(frame_5, text='Curve Right')
    button_curveright.grid(row=7, column=0)
    button_curveright['command'] = lambda: curve_right_input(lili)

    button_curveleft = ttk.Button(frame_5, text='Curved Left')
    button_curveleft.grid(row=7, column=1)
    button_curveleft['command'] = lambda: curve_left_input(lili)




def forward_input(lili):

    entry1_time = lili.time_value.get()
    entry1_speed = lili.speed.get()

    timu = int(entry1_time)
    spee = int(entry1_speed)

    lili.robot.go(spee, 0)
    time.sleep(timu)
    lili.robot.stop()



def back_ward_input(lili):

    entry2_time = lili.time_value.get()
    entry2_speed = lili.speed.get()

    timu = int(entry2_time)
    spee = int(entry2_speed)

    lili.robot.go(-spee, 0)
    time.sleep(timu)
    lili.robot.stop()


def spin_right_input(lili):

    entry3_time = lili.time_value.get()
    entry3_angle = lili.angle.get()

    timu = int(entry3_time)
    angl = int(entry3_angle)

    lili.robot.go(0, angl)
    time.sleep(timu)
    lili.robot.stop()

def spin_left_input(lili):

    entry4_time = lili.time_value.get()
    entry4_angle = lili.angle.get()

    timu = int(entry4_time)
    angl = int(entry4_angle)

    lili.robot.go(0, -angl)
    time.sleep(timu)
    lili.robot.stop()


def curve_right_input(lili):

    entry5_time = lili.time_value.get()
    entry5_speed = lili.speed.get()
    entry5_angle = lili.angle.get()


    timu = int(entry5_time)
    spee = int(entry5_speed)
    angl = int(entry5_angle)

    lili.robot.go(spee, angl)
    time.sleep(timu)
    lili.robot.stop()

def curve_left_input(lili):

    entry6_time = lili.time_value.get()
    entry6_speed = lili.speed.get()
    entry6_angle = lili.angle.get()

    timu = int(entry6_time)
    spee = int(entry6_speed)
    angl = int(entry6_angle)

    lili.robot.go(spee, -angl)
    time.sleep(timu)
    lili.robot.stop()

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
