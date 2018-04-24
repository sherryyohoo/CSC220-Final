#import pygame as pg
import random
#import tkinter as tk
import time
from graphics import *
from os import listdir
from os.path import isfile, join
from back_screen import *


def test():
    win = GraphWin("typeGame", 800, 500)
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
        self.template=self.texttotype("conversation box text/paragraphs/")
        #self.template=open("t1.txt").read()
        self.maxtime=20

    
    #input directory containging all the files, return a string that is the text to type
    def texttotype(self,mypath):
        files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
        idx=random.randint(0,len(files)-1)
        f = open(files[idx],'r')
        return f.read()


    #timer display
    def displayTime(self,starttime,time,timeDisplay):
        countdown = str((int)(self.maxtime -(time - starttime)))
        if len(countdown)==1:
            text="0:0"+countdown
        else:
            text="0:"+countdown
        timeDisplay.setText(text)

    #get countdown seconds in int
    def getRemainingTime(self,starttime,time):
        return (int)(self.maxtime -(time - starttime))

    #return boolean of whether time is up
    def timeisup(self,starttime,time):
        if time-starttime>self.maxtime:
            return True
        else:
            return False
    

    def display(self):
        
        win = self.win
        #win.setBackground("white")
        #use back screen to mask the main game
        bg=Back_screen(win)
        bg.draw()
        #display sample text
        isDominique=random.randint(0,1)
        if isDominique:
            textbox = Image(Point(400,100),"ui/conversation_box_new/question_box_dominique.png")
        else:
            textbox = Image(Point(400,100),"ui/conversation_box_new/question_box_jordan.png")
        textbox.draw(win)
        texttemplate = Text(Point(400,100),self.template)
        texttemplate.draw(win)
        #display usr input
        
        
        usrbox = Image(Point(400,300),"ui/conversation_box_new/conversation_box.png")
        usrbox.draw(win)
        usrInput = Entry(Point(400,300),50)
        usrInput.setFill("white")
        usrInput.draw(win)
        timeDisplay = Text(Point(450,50),"0:00")
        timeDisplay.draw(win)
        currenttime=self.maxtime
        starttime = time.time()
        while True:
            #update time
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
            msg = Text(Point(400,475),"Correct! You get the acceleration bonus!")
            result = False
            usrbox.undraw()
            usrbox = Image(Point(400,300),"ui/conversation_box_new/right.png")
            usrbox.draw(win)
        else:
            msg = Text(Point(400,475),"Wrong! You will be decelerated!")
            result = True
            usrbox.undraw()
            usrbox = Image(Point(400,300),"ui/conversation_box_new/wrong.png")
            usrbox.draw(win)
            
        msg.draw(win)
        time.sleep(3)
        #undraw Everything to go back to main game
        msg.undraw()
        texttemplate.undraw()
        usrInput.undraw()
        usrbox.undraw()
        textbox.undraw()
        timeDisplay.undraw()
        bg.undraw()
        return result
    





test()

	
