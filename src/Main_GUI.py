'''
Created on Oct 29, 2013

@author: maas
'''
import c0
import m1
import m2
import m3
import Xbox_And_KeyBoard
import Follow_Black_Line
import Go_until
import ir_chat
import tkinter
from tkinter import ttk
import time
import new_create
import Sprint1_m2_walk_under_input
import Sprint2_m2_waypoints
import Sprint3_m2_sing_dance
# import newmp3


class BoxEntries():
    # Using this class to help change variable values
    def __init__(self):
        self.entry_for_port = None
        self.label_for_port = None

        self.entry_for_speed = None
        self.label_for_speed = None

        self.entry_for_angle = None
        self.label_for_angle = None

        self.entry_for_duration = None
        self.label_for_duration = None


def gui(root, rob):
    frame = ttk.Frame(root, padding=(15, 15))
    frame.grid()

    # Menus
    menu = tkinter.Menu(root)
    root['menu'] = menu

    '''
    Disconnect Menu
    '''
    connect_menu = tkinter.Menu(menu, tearoff=0)
    menu.add_cascade(menu=connect_menu, label='Disconnect')
    connect_menu.add_command(label="Disconnect", command=lambda: m1.disconnect(rob))

    '''
    Go/Stop Menu
    '''
    go_menu = tkinter.Menu(menu, tearoff=0)
    menu.add_cascade(menu=go_menu, label='Go/Stop')
    go_menu.add_command(label='Go Until Time', command=lambda: m2.move_forward(rob))
    go_menu.add_command(label='Go Until Stop', command=lambda:m3.move(rob))  # works better, but not great
    go_menu.add_command(label='Stop', command=lambda: m3.stop_please(rob))


    stopper = Sprint3_m2_sing_dance.StopFlag()
    '''
    Robot Features Menu
    '''
    robot_menu = tkinter.Menu(menu, tearoff=0)
    menu.add_cascade(menu=robot_menu, label='Robot')
    robot_menu.add_command(label="Fancy Movement", command=lambda: Sprint1_m2_walk_under_input.main(rob))
    robot_menu.add_command(label="Go to waypoints", command=lambda: Sprint2_m2_waypoints.main(rob))
    robot_menu.add_command(label="Follow Line", command=lambda: Follow_Black_Line.main(rob))
    robot_menu.add_command(label="Go Until", command=lambda: Go_until.main(rob))
    robot_menu.add_command(label="Sing/Dance", command=lambda: Sprint3_m2_sing_dance.main(rob, stopper))
    # robot_menu.add_command(label="Something Special", command=lambda: newmp3.main())
    robot_menu.add_command(label="Send IR Messages", command=lambda: ir_chat.gui_send(rob))
    robot_menu.add_command(label="Recive IR Messages", command=lambda: ir_chat.gui_receve(rob))
    robot_menu.add_command(label="Xbox Control", command=lambda: Xbox_And_KeyBoard.gui(root, rob, stopper))

    # Buttons and Entries
    '''
    Port Number
    '''
    main_frame = ttk.Frame(frame, padding=(69, 20), relief='groove')
    main_frame.grid()

    connect_label = ttk.Label(main_frame, text='Input your port number \nor directly connect to simulator without input')
    connect_label.grid()

    port_label = ttk.Label(main_frame, text='  port of robot=')
    port_label.grid(row=3, column=0, sticky='w')
    entry_port = ttk.Entry(main_frame, width=10)
    entry_port.grid(row=3, column=0, sticky='e')
    rob.port = entry_port


    con_button = ttk.Button(main_frame, text="Connect")
    con_button.grid()
    con_button['command'] = lambda: connect(rob)

    operating_frame = ttk.Frame(frame, padding=(50, 20), relief='ridge')
    operating_frame.grid()
    '''
    Speed
    '''

    speed = BoxEntries()
    speed_entry = ttk.Entry(operating_frame, width=8)
    speed_entry.grid(row=5, column=1, sticky='w')
    BoxEntries.entry_for_speed = speed_entry

    speed_label = ttk.Label(operating_frame, text='Enter a speed in the box:')
    speed_label.grid(row=5, column=0, sticky='w')
    BoxEntries.label_for_speed = speed_label

    speed_button1 = ttk.Button(operating_frame, text='Increase Speed')
    speed_button1.grid()
    speed_button1['command'] = lambda: change_speed(rob, 1)

    speed_button2 = ttk.Button(operating_frame, text='Decrease Speed')
    speed_button2.grid()
    speed_button2['command'] = lambda: change_speed(rob, -1)

    speed_button3 = ttk.Button(operating_frame, text='Set Speed')
    speed_button3.grid()
    speed_button3['command'] = lambda: set_speed(rob, speed)

    '''
    Angle
    '''
    angle = BoxEntries()
    angle_entry = ttk.Entry(operating_frame, width=8)
    angle_entry.grid(row=9, column=1, sticky='w')
    BoxEntries.entry_for_angle = angle_entry

    angle_label = ttk.Label(operating_frame, text="Enter an angle between -180 and 180:")
    angle_label.grid(row=9, column=0, sticky='w')
    BoxEntries.label_for_angle = angle_label

    angle_button1 = ttk.Button(operating_frame, text="Increase Angle")
    angle_button1.grid()
    angle_button1["command"] = lambda: change_angle(rob, 10)

    angle_button2 = ttk.Button(operating_frame, text="Increase Angle")
    angle_button2.grid()
    angle_button2["command"] = lambda: change_angle(rob, -10)

    angle_button3 = ttk.Button(operating_frame, text="Set Angle")
    angle_button3.grid()
    angle_button3["command"] = lambda: set_angle(rob, angle)

    '''
    Duration of Movement
    '''

    duration = BoxEntries()
    duration_entry = ttk.Entry(operating_frame, width=8)
    duration_entry.grid(row=13, column=1, sticky='w')
    BoxEntries.entry_for_duration = duration_entry

    duration_label = ttk.Label(operating_frame, text="Enter total time(sec) for robot to move:")
    duration_label.grid(row=13, column=0, sticky='w')
    BoxEntries.label_for_duration = duration_label

    duration_button1 = ttk.Button(operating_frame, text="Increase Duration")
    duration_button1.grid()
    duration_button1["command"] = lambda:m2.increase_s(rob)

    duration_button2 = ttk.Button(operating_frame, text="Decrease Duration")
    duration_button2.grid()
    duration_button2["command"] = lambda:m2.decrease_s(rob)

    duration_button3 = ttk.Button(operating_frame, text="Set Duration")
    duration_button3.grid()
    duration_button3["command"] = lambda: set_duration(rob, duration)

def connect(rob):
    if rob.port.get() == '':
        rob.robot = new_create.Create('sim')
    else:
        entry0_port = rob.port.get()
        poooo = int(entry0_port)
        rob.robot = new_create.Create(poooo)


def set_port(rob, port):
    port_entry = BoxEntries.entry_for_port
    contents_of_portentry_box = port_entry.get()
    rob.port = contents_of_portentry_box
    print(rob.port)

def change_speed(rob, amount):
    speed = rob.get_speed()
    rob.speed = speed + amount
    print(rob.speed)

def set_speed(rob, speed):
    speed_entry = BoxEntries.entry_for_speed
    contents_of_speedentry_box = speed_entry.get()
    rob.speed = int(contents_of_speedentry_box)
    print(rob.speed)

def change_angle(rob, amount):
    angle = rob.get_angle()
    rob.angle = angle + amount
    print(rob.angle)

def set_angle(rob, angle):
    angle_entry = BoxEntries.entry_for_angle
    contents_of_angleentry_box = angle_entry.get()
    rob.angle = int(contents_of_angleentry_box)
    print(rob.angle)

def set_duration(rob, duration):
    duration_entry = BoxEntries.entry_for_duration
    contents_of_durationentry_box = duration_entry.get()
    rob.time_value = int(contents_of_durationentry_box)
    print(rob.time_value)

def stop_in_the_name(rob):
    m3.stop_please(rob)


if __name__ == '__main__':
    pass
