# Weapon Detection System with UI
## A machine learning model for weapon detection.

> [click here to download weight file](https://drive.google.com/file/d/10uJEsUpQI3EmD98iwrwzbD4e19Ps-LHZ/view?usp=sharing)


INCASE PLAYSOUND givs error update following code :
import pygame
def play_sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
play_sound('alarm.wav')
