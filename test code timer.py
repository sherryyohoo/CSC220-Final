import time 
from graphics import *
import math 

class Timer:
    def __init__(self,x,y,clock,win):
        p1 = Point(x-100,y-25)
        p2 = Point(x+100,y+25)
        bar1 = Rectangle(p1,p2)
        bar1.setFill("black")
        self.speed = 1
        #call image timer and draw the image:timer
        clock_filename = clock 
        clock_image = Image(Point(x-100, y),clock_filename )
        self.clock_image = clock_image
        bar1.draw(win)
        clock_image.draw(win)
      
    def move_to(self):
        self.clock_image.move(self.speed,0)

class Progress:
    def _init_(self,x,y,distance,lola,win):
        self.distance = distance
        p1 = Point(x-100,y-25)
        p2 = Point(x+100,y+25)
        bar1 = Rectangle(p1,p2)
        bar1.setFill("black")
        bar1.draw(win)
        lola_filename = lola
        lola_image = Image(Point(x-100, y),lola_filename)
        self.lola_image = lola_image
        lola_image.draw(win)
        self.progress_center = self.lola_image.getCenter()
        self.progress_x = self.progress_center.getX()
    
        
    def move_to(self,lola_position):
        lola_curr = (lola_position/self.distance)*200
        speed =  lola_curr- self.progress_x 
        self.lola_image.move(speed,0)

    
        
        
        
def main():
    #construct the width, height,and background color of the window
    width = 1000
    height = 600
    win = GraphWin('timer', width, height,autoflush = False)
    win.setBackground('white')
    
    timer = Timer(800,200,"timer.png",win)
    #progress = Progress(800,500,100,"timer.png",win)
    #error message:object take no parameter 
   

    #this is a while loop focus on the move of the clock  
    t = 100 #this represent #*sleep time seconds 
    while t>0:
       time.sleep(1)
       t = t-1
       update()
       timer.move_to()
    
        
    
       
    
    
    



    
    
        

main()
