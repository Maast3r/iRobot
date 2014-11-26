'''
Created on Oct 28, 2013

@author: doolansr
'''
import c0
import m1
import m2
import m3
import Xbox_And_KeyBoard
import Main_GUI
import Go_until
import tkinter
from tkinter import ttk
import time
import new_create


def main():

    rob = c0.Box_of_Fun_Toys_for_Robots(0, 0, 'sim', 0)

    root = tkinter.Tk()
    root.title("Master")

    # Xbox_And_KeyBoard.main()

    Main_GUI.gui(root, rob)

    root.mainloop()



if __name__ == '__main__':
    main()
