## Automated music for work 
import pyautogui as pg
import random

# Precaution
pg.FAILSAFEEXCPETION = True
pg.PAUSE = 1.0

# Music
Street_Fighter_Mas = 'https://www.youtube.com/watch?v=LdyabrdFMC8'
Blood_on_the_Radio = 'https://www.youtube.com/watch?v=5WKmOS_cW1w'
Vintage = 'https://www.youtube.com/watch?v=cVxIqlzdx98'
Beginnings = 'https://www.youtube.com/watch?v=7kQ1llzPiB4'
Bossa_uh = 'https://www.youtube.com/watch?v=FSnuF1FPSIU'
Accordian = 'https://www.youtube.com/watch?v=4KmEc6zFmgo'
Iron_Man = 'https://www.youtube.com/watch?v=F01UTYg79KY'
My_Favorite_Things = 'https://www.youtube.com/watch?v=rqpriUFsMQQ'
Mambo = 'https://www.youtube.com/watch?v=K0KyKOTLqrQ'
Another_Star = 'https://www.youtube.com/watch?v=TJU_HGZFjgo'
Honda = 'https://www.youtube.com/watch?v=v96sokSHeT4'
Mercy = 'https://www.youtube.com/watch?v=CShUISLYLGY'
Skiptracing = 'https://www.youtube.com/watch?v=iLk4QIOjL1s'

Music = [Street_Fighter_Mas, Blood_on_the_Radio, Vintage, Beginnings, Bossa_uh, Accordian, Iron_Man, My_Favorite_Things, Mambo, Another_Star, Honda, Mercy, Skiptracing]
Music_choice = random.randrange(len(Music)) 

# Open Youtube vid
def play_music():
    pg.hotkey('winleft')
    pg.typewrite('chrome\n')
    pg.press('enter')
    pg.typewrite(Music[Music_choice])
    pg.press('enter')
    pg.hotkey('winleft', 'down')

play_music()


# Turn volume on if off
pg.hotkey('volumeup')

