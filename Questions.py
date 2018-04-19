#import pygame as pgimport random
import time
from graphics import *
from os import listdir
from os.path import isfile, join

"""Bugs to fix:


"""
def test():
    win = GraphWin("Questions", 600, 600)
    g1 = Questions(win)
    if g1.display():
        pass #accelerate
    else :
        pass #decelerate
    #some function to quite typing game and redisplay main game

#typing game
class Questions():
    
    
    #set up display and load text
    def __init__(self,win):
        self.win = win
        #f=randomQ("pathway to directory containing text")
        f=open("question1.txt")
        lines = [ line for line in f]
        self.question = lines[0]
        self.options = lines[1:5]
        self.answer = lines[5].strip()
        self.maxtime = 20

        

    
    #input directory containging all the files, return a file containg the question
    def randomQ(self,mypath):
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        idx=random.randint(1,len(files))
        f = open(files[idx],'r')
        return f


    def displayTime(self,starttime,time,timeDisplay):
        countdown = str((int)(self.maxtime -(time - starttime)))
        if len(countdown)==1:
            text="0:0"+countdown
        else:
            text="0:"+countdown
        timeDisplay.setText(text)

    def getRemainingTime(self,starttime,time):
        return (int)(self.maxtime -(time - starttime))

    def timeisup(self,starttime,time):
        if time-starttime>10:
            return True
        else:
            return False
    

    def display(self):
        #code to gradually fading out of main game
        win = self.win
        win.setBackground("white")
        #qustionBox
        self.questiontext = Text(Point(300,100),self.question)
        self.questiontext.draw(win)
        #option box 

        textA = Text(Point(300,200),self.options[0])
        textA.draw(win)
        textB = Text(Point(300,250),self.options[1])
        textB.draw(win)
        textC = Text(Point(300,300),self.options[2])
        textC.draw(win)
        textD = Text(Point(300,350),self.options[3])
        textD.draw(win)
        
        marker =  0

        timeDisplay = Text(Point(500,50),"0:00")
        timeDisplay.draw(win)
        currenttime=self.maxtime
        starttime = time.time()

        while True:
            if currenttime != self.getRemainingTime(starttime,time.time()):
                self.displayTime(starttime,time.time(),timeDisplay)
                timeDisplay.undraw()
                timeDisplay.draw(win)
                currenttime = self.getRemainingTime(starttime,time.time())
            if self.timeisup(starttime,time.time()):
                timeDisplay.undraw()
                timeDisplay.draw(win)
                break

            if win.checkKey()== 'c': #<Enter>
                break
 
            if win.checkKey()=='a':#keys.Down:
                if marker == 4:
                    marker =1
                else:
                    marker+=1
                #redraw option box for marker, show it in different color
            if win.checkKey()=='b':#keys.Up:
                if marker <= 1:
                    marker =4
                else:
                    marker-=1
                #redraw option box for marker, show it in different color

        if str(marker) == self.answer:
            msg = Text(Point(300,500),"Correct! You get the acceleration bonus!")
            result = False
        else:
            msg = Text(Point(300,500),"Wrong! You will be decelerated!")
            result = True
            
        msg.draw(win)
        return result
    





test()

	
