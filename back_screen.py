from graphics import *

class Back_screen():
    def __init__(self,win):
        p1 = Point(0,win.getHeight())
        p2 = Point(win.getWidth(),0)
        screen = Rectangle(p1,p2)
        screen.setFill('cornflower blue')
        self.screen = screen
        self.win = win
    
    def draw(self):
        self.screen.draw(self.win)
    def undraw(self):
        self.screen.undraw()
    


    
    
    
