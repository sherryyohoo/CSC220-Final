import random
import time
from graphics import *
from os import listdir
from os.path import isfile, join
from back_screen import *

#test function, not called in runLolaRun class
def test():
    win = GraphWin("typeGame", 800, 500)
    g1 = TypeGame(win)
    if g1.display():
        pass #accelerate
    else :
        pass #decelerate
    #some function to quite typing game and redisplay main game

#Typing. Every instance contains a short paragraph to type.
#User will type in an entry. <Enter> when finish.
#if correct, Lola accelerate. If wrong, lola decelerate
class TypeGame():
    
    #constructor of a new typing game
    def __init__(self,win):
        self.win = win
        self.template=self.texttotype("conversation box text/paragraphs/").strip()
        #self.template=open("t1.txt").read()
        self.maxtime=45

    
    #input directory containging all the files, return a list of strings that is the text to type
    def texttotype(self,mypath):
        files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
        #choose a random file in directory
        idx=random.randint(0,len(files)-1)
        f = open(files[idx],'r')
        return f.read()


    #timer display, update the input timeDisplay text
    def displayTime(self,starttime,time,timeDisplay):
        countdown = str((int)(self.maxtime -(time - starttime)))
        #display time in 0:XX format
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
    
    #a display helper that convert a long string to paragraph so that it does not go beyond boundary
    def strToPara(self,str):
        #divide template string into 30-char blocks
        strlist = [str[i*30:(i+1)*30] for i in range(len(str)//30+1)]
        for i in range(1,len(strlist)):
            #replace first occurence of space with enter
            strlist[i] = strlist[i].replace(" ","\n",1)
            #merge processed block into one string
            strlist[0]+=strlist[i]
        return strlist[0]


    #display typing game
    #return a boolean value as result of the game
    def display(self):    
        win = self.win
        #use back screen to mask the main game
        bg=Back_screen(win)
        bg.draw()
        
        #randomly load question box image
        isDominique=random.randint(0,1)
        if isDominique:
            textbox = Image(Point(400,100),"ui/conversation_box_new/question_box_dominique.png")
        else:
            textbox = Image(Point(400,100),"ui/conversation_box_new/question_box_jordan.png")
        textbox.draw(win)

        #display sample text
        texttemplate = Text(Point(400,120),self.strToPara(self.template))
        texttemplate.draw(win)
        
        #display usr input
        usrbox = Image(Point(400,300),"ui/conversation_box_new/conversation_box.png")
        usrbox.draw(win)
        usrInput = Entry(Point(400,300),50)
        usrInput.setFill("white")
        usrInput.draw(win)

        #display countdown timer
        timeDisplay = Text(Point(700,50),"0:00")
        timeDisplay.draw(win)
        currenttime=self.maxtime
        starttime = time.time()

        while True:
            #update time
            if currenttime != self.getRemainingTime(starttime,time.time()):
                self.displayTime(starttime,time.time(),timeDisplay)
                timeDisplay.undraw()
                timeDisplay.draw(win)
                update()
                currenttime = self.getRemainingTime(starttime,time.time())
            
            #listen to <ENTER> for exit typegame
            if win.checkKey()=='Return': # <ENTER>
                break    

            #exit game if time is up
            elif self.timeisup(starttime,time.time()):
                timeDisplay.undraw()
                timeDisplay.draw(win)
                update()
                break

        #evaluate whether the usr input was correct
        usrtext = usrInput.getText()
        if usrtext.strip() == self.template.strip():
            msg = Text(Point(400,475),"Correct! You get the acceleration bonus!")
            result = False
            usrbox.undraw()
            usrbox = Image(Point(400,300),"ui/conversation_box_new/right.png")
            usrbox.draw(win)
            update()

        else:
            msg = Text(Point(400,475),"Wrong! You will be decelerated!")
            result = True
            usrbox.undraw()
            usrbox = Image(Point(400,300),"ui/conversation_box_new/wrong.png")
            usrbox.draw(win)
            update()

        msg.draw(win)
        update()
        time.sleep(3)
        #undraw Everything to go back to main game
        msg.undraw()
        texttemplate.undraw()
        usrInput.undraw()
        usrbox.undraw()
        textbox.undraw()
        timeDisplay.undraw()
        bg.undraw()
        update()
        return result
    





#test()

	
