import pygame as pg
import random
import tkinter as tk
import time
from graphics import *
from os import listdir
from os.path import isfile, join


#typing game
def typegame():
    win = GraphWin("typeGame", 600, 600)
    win.setBackground("white")

    #setup countdown timer
    timer=TimeCounter(10)
    #timer.mainloop()
    #text=texttotype("pathway to directory containing text")
    template=open("text2.txt").read()
    texttemplate = Text(Point(300,100),template)
    
    

    texttemplate.draw(win)
    usrInput = Entry(Point(300,300),50)
    usrInput.setFill("white")
    usrInput.draw(win)
    timeDisplay = Text(Point(500,0),"0:00")
    starttime = time.time()
    while win.checkKey is not None:
        displaytime(starttime,time.time(),timeDisplay)
        if win.checkKey()== '1':
            break
        elif timeisup(starttime,time.time()):
            break
    usrtext = usrInput.getText()
    if usrtext == template:
        msg = Text(Point(300,500),"Correct! You get the bonus!")
    else:
        msg = Text(Point(300,500),"Wrong! You will be punished!")
    msg.draw(win)
    



#input directory containging all the files, return a string that is the text to type
def texttotype(mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    idx=random.randint(1,len(files))
    text = open(files[idx],'r').read()
    return text


def displayTime(starttime,time,timeDisplay):
    countdown = (int)(time - starttime)
    text="0:"+str(countdown)
    timeDisplay.setText(text)

def timeisup(starttime,time):
    if time-startime<=0:
        return True
    else:
        return False
    
    
class TimeCounter():
        def __init__(self,remaining):
                self.starttime = time.time()
                self.remaining = remaining
                self.countdown()
                
        def countdown(self, remaining = None):
                if remaining is not None:
                    self.remaining = remaining
                while True:
                    self.remaining = self.remaining - 1
                    self.after(1000, self.countdown)

        def getTime(self):
            if self.remaining <= 0:
                return "time's up!"
            else:
                return "0:",str(remaining)

        def timeisup(self):
            if self.remaning <=0:
                return True
            else:
                return False



    
typegame()

	
