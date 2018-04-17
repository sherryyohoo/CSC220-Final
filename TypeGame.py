#import pygame as pg
import random
#import tkinter as tk
import time
from graphics import *
from os import listdir
from os.path import isfile, join

"""Bugs to fix:
    1. Text display: 第一个词是乱码
    2. A better way to draw countdown timer
    3. Find syntax for <enter>

"""
def test():
    win = GraphWin("typeGame", 600, 600)
    g1 = TypeGame(win)
    g1.display()
    if g1.play():
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
        self.template=open("text2.txt").read()
        self.texttemplate = Text(Point(300,100),self.template)

    
    #input directory containging all the files, return a string that is the text to type
    def texttotype(self,mypath):
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        idx=random.randint(1,len(files))
        text = open(files[idx],'r').read()
        return text


    def displayTime(self,starttime,time,timeDisplay):
        countdown = (int)(10 -(time - starttime))
        text="0:0"+str(countdown)
        timeDisplay.setText(text)

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

    def play(self):
        starttime = time.time()
        while True:
            self.displayTime(starttime,time.time(),timeDisplay)
            timeDisplay.undraw()
            timeDisplay.draw(win)
            if win.checkKey()== '1':
                break
            elif self.timeisup(starttime,time.time()):
                timeDisplay.undraw()
                timeDisplay.draw(win)
                break
        usrtext = usrInput.getText()
        if usrtext == self.template:
            msg = Text(Point(300,500),"Correct! You get the acceleration bonus!")
            result = False
        else:
            msg = Text(Point(300,500),"Wrong! You will be decelerated!")
            result = True
            
        msg.draw(win)
        return result
    

    
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



test()

	
