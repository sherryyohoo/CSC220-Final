from graphics import *

class Black_screen():
    def __init__(self,width,height,win):
        p1 = Point(0,height)
        p2 = Point(width,0)
        screen = Image(Point(p1,p2),"ui/settings/office.gif")
        self.screen = screen
        self.win = win
    
    def draw(self):
        self.screen.draw(self.win)
    def undraw(self):
        self.screen.undraw()
    
"""

def main():
    width = 1000
    height = 600
    win = GraphWin('blackscreen', width, height,autoflush = False)
    win.setBackground('white')
    blackscreen = black_screen(width,height,win)
    blackscreen.draw()
    #Some condition
    
     #blackscreen.undraw()
   

main()
    
    """  
    
