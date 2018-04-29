from graphics import *

class Back_screen():
    def __init__(self,win):

        p1 = Point(win.getWidth()/2,win.getHeight()/2)
        '''
        p2 = Point(win.getWidth(),0)
        screen = Rectangle(p1,p2)
        screen.setFill('cornflower blue')'''
        self.screen=Image(p1,"ui/settings/office.gif")
        self.win = win
    
    def draw(self):
        self.screen.draw(self.win)
    def undraw(self):
        self.screen.undraw()
    


    
    
    
