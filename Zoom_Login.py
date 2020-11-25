# Imports 
import pyautogui as pg
import math 
from datetime import datetime

# Set Current Time
now = math.ceil(datetime.now().time()) 


# Precaution
pg.FAILSAFEEXCEPTION = True


# Start Zoom Classes
class Zoom_class:
    def __init__(self, link, time):
        self.link = link
        self.time = time
    def start_class:
        if self.time == now: # Checks to see if Zoom class time equals actual time
            pg.hotkey('winleft')
            pg.typewrite('chrome\n')
            pg.press('enter')
            pg.typewrite(link) # Selects link of class that fits current time
            pg.press('enter')
        else:
            pass 
            
        


ISOM_351 = Zoom_class('', ) # Insert Zoom link and time of Zoom class
OAM_330 = Zoom_class('', )
FIN_320 = Zoom_class('', )
BUS_365 = Zoom_class('', )
BUS_385 = Zoom_class('', )





    
