'''
Created on Oct 31, 2013

@author: zhenga
'''

import c0
import m1
import m2
import m3
import tkinter
from tkinter import ttk
import time

class All_Deta_Lili():
    def __init__(self):
        self.entry_for_time = None
        self.entry_for_speed = None
        self.entry_for_degree = None
        self.label_above = None


def main():


    root = tkinter.Tk()
    root.title("Controler Window")

    lili = c0.Box_of_Fun_Toys_for_Robots(None, None, 'sim', None)

    m1.gui(root, lili)
    gui(root, lili)


    root.mainloop()



def gui(root, lili):

    main_label = ttk.Label(root, text='Enter your data or walk with defaut style~')
    main_label.grid()



    frame_1 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_1.grid()

    button_forward = ttk.Button(frame_1, text='Farward')
    button_forward.grid()


    entry1_time = ttk.Entry(frame_1, width=15)
    entry1_time.grid()
    lili.time_value = entry1_time


    entry1_speed = ttk.Entry(frame_1, width=15)
    entry1_speed.grid()
    lili.speed = entry1_speed

    button_forward['command'] = lambda: forward_input(lili)




    frame_2 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_2.grid()
    button_backward = ttk.Button(frame_2, text='Backward')
    button_backward.grid()

    entry2_time = ttk.Entry(frame_2, width=15)
    entry2_time.grid()
    lili.time_value = entry2_time

    entry2_speed = ttk.Entry(frame_2, width=15)
    entry2_speed.grid()
    lili.speed = entry2_speed

    button_backward['command'] = lambda: back_ward_input(lili)



    frame_3 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_3.grid()
    button_spinright = ttk.Button(frame_3, text='Spin Right')
    button_spinright.grid()

    entry3_time = ttk.Entry(frame_3, width=15)
    entry3_time.grid()
    lili.time_value = entry3_time

    entry3_degree = ttk.Entry(frame_3, width=15)
    entry3_degree.grid()
    lili.angle = entry3_degree

    button_spinright['command'] = lambda: spin_right_input(lili)



    frame_4 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_4.grid()
    button_spinleft = ttk.Button(frame_4, text='Spin Left')
    button_spinleft.grid()

    entry4_time = ttk.Entry(frame_4, width=15)
    entry4_time.grid()
    lili.time_value = entry4_time

    entry4_degree = ttk.Entry(frame_4, width=15)
    entry4_degree.grid()
    lili.angle = entry4_degree

    button_spinleft['command'] = lambda: forward_input(lili)



    frame_5 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_5.grid()
    button_curveright = ttk.Button(frame_5, text='Curve Right Moving')
    button_curveright.grid()

    entry5_time = ttk.Entry(frame_5, width=15)
    entry5_time.grid()
    lili.time_value = entry5_time

    entry5_speed = ttk.Entry(frame_5, width=15)
    entry5_speed.grid()
    lili.speed = entry5_speed

    entry5_degree = ttk.Entry(frame_5, width=15)
    entry5_degree.grid()
    lili.angle = entry5_degree

    button_curveright['command'] = lambda: curve_right_input(lili)


    frame_6 = ttk.Frame(root, padding=(50, 30), relief='raised')
    frame_6.grid()
    button_curveleft = ttk.Button(frame_6, text='Curved Left Moving')
    button_curveleft.grid()

    entry6_time = ttk.Entry(frame_6, width=15)
    entry6_time.grid()
    lili.time_value = entry6_time

    entry6_speed = ttk.Entry(frame_6, width=15)
    entry6_speed.grid()
    lili.speed = entry6_speed

    entry6_degree = ttk.Entry(frame_6, width=15)
    entry6_degree.grid()
    lili.angle = entry6_degree

    button_curveleft['command'] = lambda: curve_left_input(lili)




def forward_input(lili):

    entry1_time = lili.time_value
    entry1_speed = lili.speed
    contents_of_entry_box = entry1_time.get()
    contents_of_entry_box_2 = entry1_speed.get()

    timu = int(contents_of_entry_box)
    spee = int(contents_of_entry_box_2)

    lili.robot.go(spee, 0)
    time.sleep(timu)
    lili.robot.stop()



def back_ward_input(lili):

    entry2_time = lili.time_value
    entry2_speed = lili.speed
    contents2_of_entry_box = entry2_time.get()
    contents2_of_entry_box_2 = entry2_speed.get()

    timu = int(contents2_of_entry_box)
    spee = int(contents2_of_entry_box_2)

    lili.robot.go(spee, 0)
    time.sleep(timu)
    lili.robot.stop()

def spin_right_input(lili):

    entry3_time = lili.time_value
    entry3_angle = lili.angle
    contents3_of_entry_box = entry3_time.get()
    contents3_of_entry_box_2 = entry3_angle.get()

    timu = int(contents3_of_entry_box)
    angl = int(contents3_of_entry_box_2)

    lili.robot.go(0, angl)
    time.sleep(timu)
    lili.robot.stop()

def spin_left_input(lili):

    entry4_time = lili.time_value
    entry4_angle = lili.angle
    contents4_of_entry_box = entry4_time.get()
    contents4_of_entry_box_2 = entry4_angle.get()

    timu = int(contents4_of_entry_box)
    angl = int(contents4_of_entry_box_2)

    lili.robot.go(0, angl)
    time.sleep(timu)
    lili.robot.stop()


def curve_right_input(lili):

    entry5_time = lili.time_value
    entry5_speed = lili.speed
    contents5_of_entry_box = entry5_time.get()
    contents5_of_entry_box_2 = entry5_speed.get()

    entry1_angle = lili.angle
    contents5_of_entry_box_3 = entry1_angle.get()

    timu = int(contents5_of_entry_box)
    spee = int(contents5_of_entry_box_2)
    angl = int(contents5_of_entry_box_3)

    lili.robot.go(spee, angl)
    time.sleep(timu)
    lili.robot.stop()

def curve_left_input(lili):

    entry6_time = lili.time_value
    entry6_speed = lili.speed
    contents6_of_entry_box = entry6_time.get()
    contents6_of_entry_box_2 = entry6_speed.get()

    entry1_angle = lili.angle
    contents6_of_entry_box_3 = entry1_angle.get()

    timu = int(contents6_of_entry_box)
    spee = int(contents6_of_entry_box_2)
    angl = int(contents6_of_entry_box_3)

    lili.robot.go(spee, angl)
    time.sleep(timu)
    lili.robot.stop()

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
