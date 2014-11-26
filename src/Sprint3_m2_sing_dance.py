'''
Created on Nov 6, 2013

@author: zhenga
'''
import c0
import tkinter
from tkinter import ttk
import time
import Sprint1_m2_walk_under_input
import Sprint2_m2_waypoints
import zellegraphics as zg
import new_create
import Main_GUI
import m1


class StopFlag(object):
    def __init__(self):
        self.stop_sing = False



def main(lili):

    root = tkinter.Tk()
    root.title("Controler Window")
    stopper = StopFlag()

#     lili = c0.Box_of_Fun_Toys_for_Robots(None, None, None, None)
#     Main_GUI.gui(root, lili)

    gui(root, lili, stopper)

    root.mainloop()

def gui(root, lili, stopper):


    main_frame = ttk.Frame(root, padding=(70, 5), relief='raised')
    main_frame.grid()

    instructions = 'Sprint3 Click to play the backgroud music'
    label = ttk.Label(main_frame, text=instructions)
    label.grid()

    button_song0 = ttk.Button(main_frame, text='Sing mix songs together~')
    button_song0.grid()
    button_song0['command'] = lambda: sing_2songs_together(lili, root, stopper)

    button_song1 = ttk.Button(main_frame, text='Sing little star!')
    button_song1.grid()
    button_song1['command'] = lambda: sing_little_star(lili, root, stopper)

    button_song1 = ttk.Button(main_frame, text='Sing Marry Christmas!')
    button_song1.grid()
    button_song1['command'] = lambda: sing_marry(lili, root, stopper)

    button_stop_song = ttk.Button(main_frame, text='Be silient!')
    button_stop_song.grid()
    button_stop_song['command'] = lambda: be_silent(stopper)

    button_start_song = ttk.Button(main_frame, text='Ready for reStart!')
    button_start_song.grid()
    button_start_song['command'] = lambda: start_sing(stopper)

def sing_2songs_together(lili, root, stopper):
    """ Allows robot to sing two song at one time. (dance with light shown)"""
    song_1 = [(96, 30), (96, 30), (103, 30), (103, 30), (105, 30), (105, 30), (103, 30)]
    # song_1+song_1_e:first piece of little little star
    song_1_e = [(101, 30), (101, 30), (100, 30), (100, 30), (98, 30), (98, 30), (96, 30)]
    # song_1+song_1_e:first piece of little little star
    song_9 = [(103, 30), (96, 30), (96, 30), (98, 30), (96, 30), (107, 30), (105, 30)]
    song_9_e = [(105, 30), (105, 30), (86, 30), (98, 15), (100, 15), (98, 15), (96, 15), (107, 30), (91, 30)]
    # song_1:first piece of Marry Christmas
    while True:
        if stopper.stop_sing:
            break
            print('Answer: the mix of little little star and Marry Christmas')
        lili.robot.playSong(song_1)
        lili.robot.setLEDs(25, 70, 1, 0)
        lili.robot.go(40, 49)
        time.sleep(1.5)

        lili.robot.playSong(song_1_e)
        lili.robot.setLEDs(48, 30, 1, 1)
        lili.robot.go(40, 49)
        time.sleep(1.5)

        lili.robot.playSong(song_9)
        lili.robot.setLEDs(100, 80, 1, 0)
        lili.robot.go(30, -60)
        time.sleep(2)
        root.update()

        lili.robot.playSong(song_9_e)
        lili.robot.setLEDs(189, 60, 1, 1)
        lili.robot.go(30, -60)
        time.sleep(2)
        root.update()



def sing_little_star(lili, root, stopper):
    song_1 = [(96, 30), (96, 30), (103, 30), (103, 30), (105, 30), (105, 30), (103, 30), (101, 30), (101, 30), (100, 30), (100, 30), (98, 30), (98, 30), (96, 30)]
    while True:
        if stopper.stop_sing:
            break
        lili.robot.playSong(song_1)
        lili.robot.setLEDs(225, 200, 1, 0)
        lili.robot.go(30, -60)
        time.sleep(1)
        root.update()

def sing_marry(lili, root, stopper):
    song_9 = [(103, 30), (96, 30), (96, 30), (98, 30), (96, 30), (107, 30), (105, 30), (105, 30), (105, 30), (86, 30), (98, 15), (100, 15), (98, 15), (96, 15), (107, 30), (91, 30)]
    while True:
        if stopper.stop_sing:
            break
        lili.robot.playSong(song_9)
        lili.robot.setLEDs(25, 70, 1, 0)
        lili.robot.go(20, 90)
        time.sleep(1)
        root.update()

# def sing_dance(lili, root, stopper):
#
#     song_9 = [(103, 30), (96, 30), (96, 30), (98, 30), (96, 30), (107, 30), (105, 30), (105, 30), (105, 30), (86, 30), (98, 15), (100, 15), (98, 15), (96, 15), (107, 30), (91, 30)]
#     song_1 = [(96, 30), (96, 30), (103, 30), (103, 30), (105, 30), (105, 30), (103, 30)]  # a quick C chord
#     song_1_2 = [(101, 30), (101, 30), (100, 30), (100, 30), (98, 30), (98, 30), (96, 30)]  # a quick C chord
#     song_2 = [(105, 30), (105, 30), (103, 30), (103, 30), (100, 30), (100, 30), (98, 30)]
#     song_2_2 = [(105, 30), (105, 30), (103, 30), (103, 30), (100, 30), (100, 30), (98, 30)]
#     song_3 = [(108, 30), (108, 30), (115, 30), (115, 30), (117, 30), (117, 30), (115, 30)]
#     song_3_2 = [(96, 30), (96, 30), (103, 30), (103, 30), (105, 30), (105, 30), (103, 30)]






def be_silent(stopper):
    """ Set the variable that will stop all the O processes. """
    stopper.stop_sing = True

def start_sing(stopper):
    """ Set the variable that will stop all the O processes. """
    stopper.stop_sing = False



# def be_silent(lili):
#     pass


#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
