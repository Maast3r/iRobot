import pygame
import time

pygame.init()

pygame.mixer.quit()
movie = pygame.movie.Movie('stop.mpg')
res = movie.get_size()
pygame.display.set_mode(res)
overlay = pygame.display.get_surface()
movie.set_display(overlay)
movie.play()
while True:
    time.sleep(1)
