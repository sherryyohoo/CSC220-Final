#import pygame as pgimport random
import time,random
from graphics import *
from os import listdir
from os.path import isfile, join

"""Bugs to fix:
        up & down很卡
"""
def test():
    win = GraphWin("Questions", 500, 500)
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
        f=self.randomQ("CSC220-Final/conversation box text/questions/")
        #f=open("question1.txt")
        lines = [ line for line in f]
        self.question = lines[0]
        self.options = lines[1:5]
        self.answer = lines[5].strip()
        self.maxtime = 20

        

    
    #input directory containging all the files, return a file containg the question
    def randomQ(self,mypath):
        files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
        idx=random.randint(0,len(files)-1)
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
        if time-starttime>self.maxtime:
            return True
        else:
            return False
    

    def display(self):
        #code to gradually fading out of main game
        win = self.win
        #win.setBackground("white")
        #qustionBox
        idx=random.randint(0,1)
        if idx:
            questionbox = Image(Point(250,100),"CSC220-Final/ui/conversation_box_new/question_box_dominique.png")
        else:
            questionbox = Image(Point(250,100),"CSC220-Final/ui/conversation_box_new/question_box_jordan.png")
        questionbox.draw(win)
        questiontext = Text(Point(250,100),self.question)
        questiontext.draw(win)
        answerbox = Image(Point(250,300),"CSC220-Final/ui/conversation_box_new/conversation_box.png")
        answerbox.draw(win)
        #option box 

        self.optionlist = [Option(win,self.options[i],Point(250,250+50*i)) for i in range(4)]
        for opt in self.optionlist:
            opt.draw()

        marker =  1

        timeDisplay = Text(Point(450,50),"0:00")
        timeDisplay.draw(win)
        currenttime=self.maxtime
        starttime = time.time()

        while True:
            if win.checkKey()== 'Return': #<Enter>
                break
 
            if win.checkKey()=='Down':#keys.Down:
                #deselect previous mark
                self.optionlist[marker-1].isSelected=False
                if marker == 4:
                    marker =1
                else:
                    marker+=1
                #redraw option box for marker, show it in different color
                self.optionlist[marker-1].isSelected=True
                for opt in self.optionlist:
                    opt.undraw()
                    opt.draw()

            if win.checkKey()=='Up':#keys.Up:
                self.optionlist[marker-1].isSelected=False
                if marker <= 1:
                    marker =4
                else:
                    marker-=1
                #redraw option box for marker, show it in different color
                self.optionlist[marker-1].isSelected=True
                for opt in self.optionlist:
                    opt.undraw()
                    opt.draw()
            
            if currenttime != self.getRemainingTime(starttime,time.time()):
                self.displayTime(starttime,time.time(),timeDisplay)
                timeDisplay.undraw()
                timeDisplay.draw(win)
                currenttime = self.getRemainingTime(starttime,time.time())
            if self.timeisup(starttime,time.time()):
                timeDisplay.undraw()
                timeDisplay.draw(win)
                break   

        #if correct
        if str(marker) == self.answer:
            msg = Text(Point(250,475),"Correct! You get the acceleration bonus!")
            result = False
            for opt in self.optionlist:
                opt.undraw()
            answerbox.undraw()
            answerbox = Image(Point(250,300),"CSC220-Final/ui/conversation_box_new/right.png")
            answerbox.draw(win)
            for opt in self.optionlist:
                opt.draw()
        #if incorrect
        else:
            msg = Text(Point(250,475),"Wrong! You will be decelerated!")
            result = True
            for opt in self.optionlist:
                opt.undraw()
            answerbox.undraw()
            answerbox = Image(Point(250,300),"CSC220-Final/ui/conversation_box_new/wrong.png")
            answerbox.draw(win)
            for opt in self.optionlist:
                opt.draw()
            self.optionlist[int(self.answer)-1].undraw()
            self.optionlist[int(self.answer)-1].drawWrong()
        msg.draw(win)
        time.sleep(3)
        msg.undraw()
        timeDisplay.undraw()
        for opt in self.optionlist:
            opt.undraw()
        questiontext.undraw()
        answerbox.undraw()
        questionbox.undraw()

        return result
    


class Option():
    def __init__(self,win,text,position):
        self.win=win
        self.text=Text(position,text)
        self.text.setSize(10)
        self.isSelected=False
        self.position=position
        #self.optionbox


    def draw(self):
        if self.isSelected:
            self.optionbox = Image(self.position,"CSC220-Final/ui/conversation_box_new/button_right.png")
        else:
            self.optionbox = Image(self.position,"CSC220-Final/ui/conversation_box_new/button_normal.png")
        self.optionbox.draw(self.win)
        self.text.draw(self.win)

    def drawWrong(self):
        self.optionbox = Image(self.position,"CSC220-Final/ui/conversation_box_new/button_wrong.png")
        self.optionbox.draw(self.win)
        self.text.draw(self.win)

    def undraw(self):
        self.optionbox.undraw()
        self.text.undraw()


test()

	
