from graphics import *
from random import *
from math import sqrt
import time

def Openscene(win,x,y,open1,open2,open3):
        open1_image = Image(Point(x, y),open1)
        open1_image.draw(win)
        update()
        time.sleep(5)
        open1_image.undraw()
        open2_image = Image(Point(x, y),open2)
        open2_image.draw(win)
        update()
        time.sleep(15)
        open2_image.undraw()
        open3_image = Image(Point(x, y),open3)
        open3_image.draw(win)
        update()
        time.sleep(5)
        open3_image.undraw()
        
def main():
    win = GraphWin( 'openning', 800, 500, autoflush=False )
    win.setBackground( 'white' )
    w = 100
    win.setCoords( -w, -w, w, w )
    Openscene(win,0,0,"open1.gif","open2.gif","open3.gif")

main()

    
