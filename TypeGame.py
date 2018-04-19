#import pygame as pg
import random
#import tkinter as tk
import time
from graphics import *
from os import listdir
from os.path import isfile, join


def test():
    win = GraphWin("typeGame", 600, 600)
    g1 = TypeGame(win)
    if g1.display():
        pass #accelerate
    else :
        pass #decelerate
    #some function to quite typing game and redisplay main game

#typing game
class TypeGame():
    
    
    #set up display and load text
    def __init__(self,win):
        self.win = win
        
        #self.template=texttotype("pathway to directory containing text")
        self.template=open("t1.txt").read()
        self.texttemplate = Text(Point(300,100),self.template)
        self.maxtime=45

    
    #input directory containging all the files, return a string that is the text to type
    def texttotype(self,mypath):
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        idx=random.randint(1,len(files))
        text = open(files[idx],'r').read()
        return text


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
        self.texttemplate.draw(win)
        usrInput = Entry(Point(300,300),50)
        usrInput.setFill("white")
        usrInput.draw(win)
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
                
            if win.checkKey()=='Return': # <ENTER>
                break                              
            elif self.timeisup(starttime,time.time()):
                timeDisplay.undraw()
                timeDisplay.draw(win)
                break
        usrtext = usrInput.getText()
        if usrtext.strip() == self.template.strip():
            msg = Text(Point(300,500),"Correct! You get the acceleration bonus!")
            result = False
        else:
            msg = Text(Point(300,500),"Wrong! You will be decelerated!")
            result = True
            
        msg.draw(win)
        return result
    





test()

	


