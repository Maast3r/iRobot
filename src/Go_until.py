'''
Created on Nov 8, 2013

@author: maas
'''
import c0
import m1
import m2
import m3
# import Xbox_And_KeyBoard
import Follow_Black_Line
import tkinter
from tkinter import ttk
import time
import new_create

class Entries():
    # Using this class to help change variable values
    def __init__(self, dark, ir):
        self.entry_for_speed = None
        self.label_for_speed = None

        self.entry_for_dark = None
        self.label_for_dark = None
        self.dark = dark

        self.entry_for_ir = None
        self.label_for_ir = None
        self.ir = ir

def main(rob):
    root = tkinter.Tk()
    root.title("Go Until")
    frame = ttk.Frame(root, padding=100)
    frame.grid()

    speed_frame = ttk.Frame(frame, borderwidth=10, relief='ridge')
    speed_frame.grid()
    ir_frame = ttk.Frame(frame, borderwidth=10, relief='groove')
    ir_frame.grid()

    speed = Entries(None, None)
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid()
    Entries.entry_for_speed = speed_entry

    speed_label = ttk.Label(frame, text='Enter a speed in the box.')
    speed_label.grid()
    Entries.label_for_speed = speed_label

    speed_button = ttk.Button(frame, text='Set Speed')
    speed_button.grid()
    speed_button['command'] = lambda: set_speed(rob, speed)

    start_button = ttk.Button(frame, text="Go Until Left Bumper")
    start_button.grid()
    start_button["command"] = lambda: go_until_left(rob)

    start_button2 = ttk.Button(frame, text="Go Until Right Bumper")
    start_button2.grid()
    start_button2["command"] = lambda: go_until_right(rob)

    start_button3 = ttk.Button(frame, text="Go Until Both Bumpers")
    start_button3.grid()
    start_button3["command"] = lambda: go_until_both(rob)

    dark = Entries(None, None)
    dark_entry = ttk.Entry(frame, width=8)
    dark_entry.grid()
    Entries.entry_for_dark = dark_entry
    print(dark_entry)

    dark_label = ttk.Label(frame, text='Enter a darkenss (between 0 and 4096) in the box.')
    dark_label.grid()
    Entries.label_for_dark = dark_label

    dark_button = ttk.Button(frame, text="Set Darkness Level")
    dark_button.grid()
    dark_button["command"] = lambda: set_Dark(rob, dark)

    start_button4 = ttk.Button(frame, text="Go Until Dark")
    start_button4.grid()
    start_button4["command"] = lambda: go_until_dark(rob, Entries.dark)

    # min = 0
    # max = 255
    ir = Entries(None, None)
    ir_entry = ttk.Entry(frame, width=8)
    ir_entry.grid()
    Entries.entry_for_ir = ir_entry
    print(ir_entry)

    ir_label = ttk.Label(frame, text='Enter an IR (between 0 and 255) in the box.')
    ir_label.grid()
    Entries.label_for_ir = ir_label

    ir_button = ttk.Button(frame, text="Set IR")
    ir_button.grid()
    ir_button["command"] = lambda: set_IR(rob, ir)

    start_button5 = ttk.Button(frame, text="Go Until IR")
    start_button5.grid()
    start_button5["command"] = lambda: go_until_IR(rob, Entries.ir)

    start_button6 = ttk.Button(frame, text="Go Until Stuck")
    start_button6.grid()
    start_button6["command"] = lambda: go_until_stuck(rob)

    root.mainloop()

def go_until_left(rob):
    ''''
    Moves robot until front left bumper has been hit
    '''
    speed = rob.get_speed()
    while True:

        rob.robot.go(speed, 0)
        time.sleep(0.01)
        sensor = new_create.Sensors.bumps_and_wheel_drops
        sensor_values = rob.robot.getSensor(sensor)

        left_bumper_state = sensor_values[3]

        if left_bumper_state == 1:
            rob.robot.stop()
            print("Bumped left")
            break

        time.sleep(0.05)

def go_until_right(rob):
    '''
    Moves robot until front  right bumper has been hit
    '''
    speed = rob.get_speed()
    while True:

        rob.robot.go(speed, 0)
        time.sleep(0.01)
        sensor = new_create.Sensors.bumps_and_wheel_drops
        sensor_values = rob.robot.getSensor(sensor)

        right_bumper_state = sensor_values[4]

        if right_bumper_state == 1:
            rob.robot.stop()
            print("Bumped Right")
            break

        time.sleep(0.05)

def go_until_both(rob):
    '''
    Moves robot until both bumpers have been hit
    '''
    speed = rob.get_speed()
    while True:
        rob.robot.go(speed, 0)
        time.sleep(0.01)
        sensor = new_create.Sensors.bumps_and_wheel_drops
        sensor_values = rob.robot.getSensor(sensor)

        left_bumper_state = sensor_values[3]
        right_bumper_state = sensor_values[4]

        if left_bumper_state == 1 and right_bumper_state == 1:
            rob.robot.stop()
            print("Bumped Both")
            break

        time.sleep(0.05)

def go_until_dark(rob, dark):
    '''
    Moves robot until it reaches a dark line
    '''
    speed = rob.get_speed()
    while True:

        rob.robot.go(speed, 0)
        time.sleep(0.01)
        sensordark = rob.robot.getSensor(new_create.Sensors.cliff_front_left_signal)
        sensordark2 = rob.robot.getSensor(new_create.Sensors.cliff_front_right_signal)
        print(sensordark, sensordark2)
        if sensordark < dark or sensordark2 < dark:
            break
    rob.robot.stop()
    print("reached dark line")

def go_until_IR(rob, ir):
    '''
    Moves robot until it hears a user specified ir signal
    '''
    speed = rob.get_speed()
    while True:
        rob.robot.go(speed, 0)
        time.sleep(0.01)
        # rob.robot.startIR()
        irsensor = rob.robot.getSensor(new_create.Sensors.ir_byte)
        if(irsensor == ir):
            rob.robot.stop()
            # rob.robot.stopIR()

def go_until_stuck(rob):
    '''
    Moves robot until it is stuck
    '''
    speed = rob.get_speed()
    angle = 0
    while True:
        time.sleep(.1)
        rob.robot.go(speed, 0)
        time.sleep(.1)
        sensor = new_create.Sensors.bumps_and_wheel_drops
        sensor_values = rob.robot.getSensor(sensor)

        left_bumper_state = sensor_values[3]
        right_bumper_state = sensor_values[4]

        if(left_bumper_state == 1 or right_bumper_state == 1):
            rob.robot.stop()
            rob.robot.go(0, 30)
            time.sleep(1)
            rob.robot.stop()

            angle = angle + 30
            print("Bumped")
        elif(angle == 360):
            rob.robot.stop()
            print("Stuck", angle)
            break

def set_speed(rob, speed):
    # Set speed
    speed_entry = Entries.entry_for_speed
    contents_of_speedentry_box = speed_entry.get()
    rob.speed = int(contents_of_speedentry_box)
    print(rob.speed)

def set_Dark(rob, dark):
    # Set darkness level
    dark_entry = Entries.entry_for_dark
    contents_of_darkentry_box = dark_entry.get()
    Entries.dark = int(contents_of_darkentry_box)
    print(Entries.dark)

def set_IR(rob, ir):
    # Set the ir the robot is listening to
    ir_entry = Entries.entry_for_ir
    contents_of_irentry_box = ir_entry.get()
    Entries.ir = int(contents_of_irentry_box)
    print(Entries.ir)

if __name__ == '__main__':
    main
