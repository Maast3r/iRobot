'''
Created on Nov 1, 2013

@author: maas
'''
import c0
import m1
import m2
import m3
# import Xbox_And_KeyBoard
import tkinter
from tkinter import ttk
import time
import new_create
import math

class Distance():
    # Using this class to help change variable values
    def __init__(self, distance):
        self.entry_for_distance = None
        self.label_for_distance = None
        self.t_distance = distance


def main(rob):
    root = tkinter.Tk()
    root.title("Follow Black Line")

    frame = ttk.Frame(root, padding=30)
    frame.grid()
    distance = Distance(0)
    distance_entry = ttk.Entry(frame, width=8)
    distance_entry.grid()
    Distance.entry_for_distance = distance_entry

    distance_label = ttk.Label(frame, text="Enter the distance (cm) of black line you would like the robot to follow.")
    distance_label.grid()
    Distance.label_for_distance = distance_label

    distance_button = ttk.Button(frame, text="Set Distance")
    distance_button.grid()
    distance_button["command"] = lambda: set_distance(rob, distance)

    start_button = ttk.Button(frame, text="Start")
    start_button.grid()
    start_button["command"] = lambda: pid(rob, Distance.t_distance)

    root.mainloop()

def pid(rob, t_distance):
    '''
    Calculates all the information needed for PID control, and then runs the robot accordingly.
    '''
    # Max darkness is 4096
    darkness = 1500

    Kp = .01
    Ki = .01
    Kd = .01
    integral = []
    Integral = 0
    last_error = 0
    derivative = []
    Derivative = 0
    total_distance = 0
    while True:
        leftdarksensor = rob.robot.getSensor(new_create.Sensors.cliff_front_left_signal)
        rightdarksensor = rob.robot.getSensor(new_create.Sensors.cliff_front_right_signal)
        distancesensor = rob.robot.getSensor(new_create.Sensors.distance)
        total_distance = distancesensor + total_distance

        error = darkness - leftdarksensor
        integral.append(error)
        derivative.append(error - last_error)

        proportion = (90 / darkness) * error  # calculate the proportion
        for k in integral:
            Integral = Integral + k
        Integral = Integral * (1 / 60)  # calculate the integral
        for j in derivative:
            Derivative = Derivative + k
        Derivative = Derivative * (1 / 60)  # calculate the derivative

        turn = Kp * proportion + Ki * Integral + Kd * Derivative

        last_error = error

        rob.robot.go(10, turn)
        time.sleep(1 / 60)
        if(total_distance / 10 >= t_distance):  # Stops the robot after he goes the user's specified distance
            print(total_distance)
            break
    rob.robot.stop()
    print(leftdarksensor, rightdarksensor)


def set_distance(rob, distance):
    distance_entry = Distance.entry_for_distance
    contents_of_distanceentry_box = distance_entry.get()
    Distance.t_distance = int(contents_of_distanceentry_box)
    print(Distance.t_distance)

if __name__ == '__main__':
    main