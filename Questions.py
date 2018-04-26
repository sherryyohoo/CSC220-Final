import time,random
from graphics import *
from os import listdir
from os.path import isfile, join
from back_screen import *

"""Bugs to fix:
        up & down not very smooth
        collision checker did not get coin on lower side
"""

#test function, not called in runLolaRun class
def test():
    win = GraphWin("Questions", 800, 500)
    g1 = Questions(win)
    if g1.display():
        pass #accelerate
    else :
        pass #decelerate
    #some function to quite typing game and redisplay main game

#Qustion class. Every instance contains a multiple choice question.
#User use Up and Down key to contol selection
#if correct, Lola accelerate. If wrong, lola decelerate
class Questions():
       
    #contructor 
    def __init__(self,win):
        self.win = win
        # pick a random question
        f=self.randomQ("conversation box text/questions/")
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

    #a display helper that convert a long string to paragraph so that it does not go beyond boundary
    def strToPara(self,str):
        #divide template string into 30-char blocks
        strlist = [str[i*30:(i+1)*30] for i in range(len(str)//30+1)]
        for i in range(1,len(strlist)):
            #replace first occurence of space with enter
            strlist[i] = strlist[i].replace(" ","\n",1)
            strlist[0]+=strlist[i]
        return strlist[0]

    #timer display, update the input timeDisplay text
    def displayTime(self,starttime,time,timeDisplay):
        countdown = str((int)(self.maxtime -(time - starttime)))
        if len(countdown)==1:
            text="0:0"+countdown
        else:
            text="0:"+countdown
        timeDisplay.setText(text)

    #get countdown time as seconds in int
    def getRemainingTime(self,starttime,time):
        return (int)(self.maxtime -(time - starttime))

    #return boolean of whether time is up
    def timeisup(self,starttime,time):
        if time-starttime>self.maxtime:
            return True
        else:
            return False
    
    #display question
    #return a boolean value as result of the game
    def display(self):
        win = self.win
        #use back screen to mask the main game
        bg=Back_screen(win)
        bg.draw()

        #randomly load question box image
        isDominique=random.randint(0,1)
        if isDominique:
            questionbox = Image(Point(400,100),"ui/conversation_box_new/question_box_dominique.png")
        else:
            questionbox = Image(Point(400,100),"ui/conversation_box_new/question_box_jordan.png")
        questionbox.draw(win)

        #display question
        questiontext = Text(Point(400,100),self.strToPara(self.question))
        questiontext.draw(win)

        #display answer options
        answerbox = Image(Point(400,300),"ui/conversation_box_new/conversation_box.png")
        answerbox.draw(win)
        self.optionlist = [Option(win,self.options[i],Point(400,250+50*i)) for i in range(4)]
        for opt in self.optionlist:
            opt.draw()

        #store current selection
        marker =  0

        #display countdown timer
        timeDisplay = Text(Point(700,50),"0:00")
        timeDisplay.draw(win)
        currenttime=self.maxtime
        starttime = time.time()

        while True:
            #Press <Enter> to exit quesiton game
            if win.checkKey()== 'Return': #<Enter>
                break
            #Press keys.Down to go down in selection
            elif win.checkKey()=='Down':
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
                    update()

            #Press keys.Up to go up in selection
            elif win.checkKey()=='Up':
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
                    update()
            
            #update time
            if currenttime != self.getRemainingTime(starttime,time.time()):
                self.displayTime(starttime,time.time(),timeDisplay)
                timeDisplay.undraw()
                timeDisplay.draw(win)
                update()
                currenttime = self.getRemainingTime(starttime,time.time())

            #exit if time is up
            if self.timeisup(starttime,time.time()):
                timeDisplay.setText("0:00")
                timeDisplay.undraw()
                timeDisplay.draw(win)
                update()
                break   

        #if correct, show message and update display
        if str(marker) == self.answer:
            msg = Text(Point(400,475),"Correct! You get the acceleration bonus!")
            result = False
            for opt in self.optionlist:
                opt.undraw()
            answerbox.undraw()
            answerbox = Image(Point(400,300),"ui/conversation_box_new/right.png")
            answerbox.draw(win)
            for opt in self.optionlist:
                opt.draw()
        #if incorrect, show message, show correct answer in blue and update display
        else:
            msg = Text(Point(400,475),"Wrong! You will be decelerated!")
            result = True
            for opt in self.optionlist:
                opt.undraw()
            answerbox.undraw()
            answerbox = Image(Point(400,300),"ui/conversation_box_new/wrong.png")
            answerbox.draw(win)
            for opt in self.optionlist:
                opt.draw()
            self.optionlist[int(self.answer)-1].undraw()
            self.optionlist[int(self.answer)-1].drawWrong()

        msg.draw(win)
        update()
        time.sleep(3)

        #undraw Everything to go back to main game
        msg.undraw()
        timeDisplay.undraw()
        for opt in self.optionlist:
            opt.undraw()
        questiontext.undraw()
        answerbox.undraw()
        questionbox.undraw()
        bg.undraw()
        update()
        return result
    

#helper class for each multiple choice option
class Option():
    #Constructor
    def __init__(self,win,text,position):
        self.win=win
        self.text=Text(position,text)
        self.text.setSize(10)
        self.isSelected=False
        self.position=position
        #self.optionbox

    #draw box and text according to selection
    def draw(self):
        if self.isSelected:
            self.optionbox = Image(self.position,"ui/conversation_box_new/button_right.png")
        else:
            self.optionbox = Image(self.position,"ui/conversation_box_new/button_normal.png")
        self.optionbox.draw(self.win)
        self.text.draw(self.win)

    #draw box as blue if it is the correct answer that was not selected by user
    def drawWrong(self):
        self.optionbox = Image(self.position,"ui/conversation_box_new/button_wrong.png")
        self.optionbox.draw(self.win)
        self.text.draw(self.win)

    #undraw text and box
    def undraw(self):
        self.optionbox.undraw()
        self.text.undraw()


#test()

	
