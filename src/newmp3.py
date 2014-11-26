'''
Created on Nov 7, 2013

@author: maas
'''

import zellegraphics as zg
from zellegraphics import *
import time
import pygame


def main():
    '''
    Plays Stop in the Name of Love from an mp3 file using the pygame library
    '''
    screenHeight = 10
    screenWidth = 250
    window = zg.GraphWin("Music", screenWidth, screenHeight)
    pygame.init()
    pygame.mixer.music.load("stop in the name of love.ogg")
    pygame.mixer.music.play(-1)
    window.closeOnMouseClick()

if __name__ == '__main__':
    main()
