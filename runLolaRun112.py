##CSC 220 Final Project
##Instructor: Jordan Crouser
##Group Members: Nancy Guan;Lucy Yilin Wang, Siyu Lily Qian, Sherry Zhenyao Cai

#import relevant modules 
from graphics import *
from random import *
from math import sqrt
from Questions import *
from TypeGame import *
import time
import itertools
import sys



#---------
# CLASSES
#---------

        
class Timer:
    '''Constructor for the timer class, create a time bar to time the game,
    make the timer move along the time bar to show how much time has passed/left
    for this game
    self: a place-holder for specific instances
    x,y: the location to draw the bar and the timer
    clock: filename of the timer image that will be draw
    win: the window on which the images draw'''
    def __init__(self,x,y,clock,win):
        #create a time bar 
        p1 = Point(x,y-10)
        p2 = Point(x+300,y+10)
        bar1 = Rectangle(p1,p2)
        bar1.setFill("light green")
        bar1.setOutline("light green")
        #set the moving distance of the timer
        #instance variables for speed 
        self.speed = 1.67
        #call image timer and draw the image:timer
        clock_image = Image(Point(x, y),clock)
        #instance variables for clock image
        self.clock_image = clock_image
        #draw timer and time bar 
        bar1.draw(win)
        clock_image.draw(win)

    #move the timer  
    def move_to(self):
        self.clock_image.move(self.speed,0)

class Progress:
    '''Constructor for the Progress class, create a progress bar and make the icon
    move along the bar to show how much journey lola has left for this game
    self: a place-holder for specific instances
    x,y: the location to draw the bar and the icon
    distance: the total distance of Lola's journey (running path)
    lola: filename of the icon image that will be draw
    win: the window on which the images draw'''
        
    def __init__(self,x,y,distance,icon,win):
        #instance variable for distance 
        self.distance = distance
        #create and draw the progress bar 
        p1 = Point(x,y-10)
        p2 = Point(x+300,y+10)
        bar1 = Rectangle(p1,p2)
        bar1.setFill("light blue")
        bar1.setOutline("light blue")
        bar1.draw(win)
        #call and draw the icon image 
        icon_image = Image(Point(x, y),icon)
        self.icon_image = icon_image
        icon_image.draw(win)

    def getx(self):
        #get the current position of the icon image 
        image_position = self.icon_image.getAnchor()
        image_x = image_position.getX()
        #store the value of the current position 
        return(image_x)

        
    def move_to(self,icon_x,progress):
        #icon_x: icon's current x-axis position
        #progress: Lola's progress in the game 
        #calculate where the icon should currently be placed
        #based on Lola's progress in the game over the total distance of the game
        #(the current percentage of Lola's progress in the game)
        #in proportion to the length of the bar 
        icon_curr = (progress/self.distance)*300
        #the length of movement (speed) is the icon's (should be) current position
        #minus the origional icon's position 
        speed =  icon_curr-icon_x
        #round up the number 
        speed = round(speed,2)
        #move the icon through the progress bar
        self.icon_image.move(speed,0)
      



class Lola:
    '''Constructor for the Lola class, define Lola's position center,radius,
    speed(include accelerate and decelerate), distance, movement(jump,land) and
    collision checker (check whether Lola collides with the object)
    Lola's speed is also the objects's speed
    self: a place-holder for specific instances
    center1: Lola's position center 
    distance1: Lola's initial distance in the game
    speed1:Lola's initial speed in the game (Also object's initial speed in the game)
    jumpHeight1: the height Lola can jump 
    LolaRadius: Lola's radius from the center 
    win: the window on which the Lola image draw'''
    def __init__(self, win, center, distance,speed,jumpHeight):
        #instance variable for center 
        self.center=center
        #instance variable for position x and y 
        self.x, self.y= center.getX(), center.getY()
        #instance variable for speed 
        self.speed= speed
        #instance variable for distance
        self.distance= distance
        #instance variable for jumpheight 
        self.jumpHeight=jumpHeight
        self.Lola=Image(self.center,"ui/lola/1.gif")

                       
    #following functions changes some values for this object
    #accelerate Lola and the object  
    def accelerate(self,speedValue):
        self.speed= self.speed+speedValue
    #decelerate Lola and the object 
    def decelerate(self,speedValue):
        self.speed= self.speed-speedValue
    #change Lola's distance 
    def changeDistance(self,distance):
        self.distance= self.distance + distance
    #change Lola's center in this journey
    #(not really change Lola image's position,
    #but instead  change Lola's position center in the total distance)
    def changeCenter(self,y):
        newY=y
        self.y=y
        self.Center=Point(self.x,newY)


    #check whether Lola collides with the objects or not 
    def collisionChecker(self,obj):
        #set collision as False 
        collision=False
        #get the object's center 
        objcenter = obj.getCenterForObject()
        #if the object's center, in addition to its Radius, falls in a range defined below
        #collision happened
        #have to correct for margrins in gif picture
        if (objcenter.getY()+obj.getObjRadius())>(self.y-self.Lola.getHeight()/2+13) and (objcenter.getY()-obj.getObjRadius())<(self.y+self.Lola.getHeight()/2-17):
            if ((objcenter.getX()+obj.getObjRadius())>(self.x-self.Lola.getWidth()/2+20) and (objcenter.getX()-obj.getObjRadius())<(self.x+self.Lola.getWidth()/2-20)):
                #return True if collision happened
                collision=True
        #otherwise return False
        return collision 
    
        
    #following functions returns Lola's speed(also object's speed),center, and distance 
    def getSpeed(self):
        return self.speed
    def getCenter(self):
        return self.center
    def getDistance(self):
        return self.distance


class Obj:
    '''Constructor for the Obj class, define objects' position center,
    and if Lola collides with the object, deterime which type of game(typing game or
    question game) should pop up
    self: a place-holder for specific instances
    win: the window on which the images draw'''
    def __init__(self, win):  
        #instance variable for object center 
        self.ObjCenter=Point(800,randint(200,400))
        #instance variable of wheather the collision happens or not  
        self.isCollide = False
        #A condition to determine after collides with object, which type of game will
        #pops up 
        i=randint(0,1)
        if i: 
            self.type = "Questions"
            self.ObjCircle=Image(self.ObjCenter,"ui/signs/question.gif")
            
        else: 
            self.type = "TypeGame"
            self.ObjCircle=Image(self.ObjCenter,"ui/signs/keyboard.gif")

         
        self.objRadius=self.ObjCircle.getWidth()/2

        #draw the object 
        self.ObjCircle.draw(win)

    
    #return the center of each object as a list
    def getCenterForObject(self):
        return self.ObjCenter
    #return the object's radius 
    def getObjRadius(self):
        return self.objRadius
    #return the type of game as questions 
    def isQuestion(self):
        return self.type == "Questions"

    #move all of the objects 
    def MoveObj(self, dx):
        self.ObjCenter = Point(self.ObjCenter.getX()-dx,self.ObjCenter.getY())
        self.ObjCircle.move(-dx,0)    
    #define undraw method 
    def undraw(self):
        self.ObjCircle.undraw()     



#------------------
# HELPER FUNCTION
#------------------

def Openscene(win,x,y,open1,open2,open3):
        '''Helper function of the openning of the game, to introduce game background
        and instructions through showing openning images in sequence
        x,y: the position to draw the image 
        open1,open2,open3: the file names of the images that will be displayed at the
        begining 
        win: the window on which the images draw'''
        
        #call openning images and draw the images
        open1_image = Image(Point(x, y),open1)
        open1_image.draw(win)
        #update the system
        update()
        #freeze the system for 3 seconds 
        time.sleep(3)
        #undraw the first image, call and draw the second image 
        open1_image.undraw()
        open2_image = Image(Point(x, y),open2)
        open2_image.draw(win)
        #update the system
        update()
        #freeze the system for 13 seconds
        time.sleep(13)
        #undraw the second image, call and draw the third image 
        open2_image.undraw()
        open3_image = Image(Point(x, y),open3)
        open3_image.draw(win)
        #update the system
        update()
        #freeze the system for 3 seconds
        time.sleep(3)
        #undraw the third image
        open3_image.undraw()



def animate(win,lola,status):
    '''Helper function of Lola's animation, to swap Lola's gif
       Lola: pass in Lola's class 
       status: pass in space or Down, decide whether Lola should jump or crouches 
       win: the window on which the images draw'''
    #determine Lola's jump height 
    h=350
    #set up down as False: Lola does not crouch 
    down=False
    #if pass in space, Lola jumps 
    if status=="space": 
        h=h-75
    #if pass in Down, Lola crouches
    elif status=="Down":
        down=True
    #If Lola does not crouches
    #Draw and Swap Lola's gif images 
    if not down:
        lola.changeCenter(h)
        gif1=Image(Point(400,h), "ui/lola/1.gif")
        gif1.draw(win)
        #update the system 
        update()
        #freeze the system to swap image through draw and undraw  
        time.sleep(0.05)
        gif1.undraw()
        gif2=Image(Point(400,h), "ui/lola/2.gif")
        gif2.draw(win)
        update()
        time.sleep(0.05)
        gif2.undraw()
        gif3=Image(Point(400,h), "ui/lola/3.gif")
        gif3.draw(win)
        update()
        time.sleep(0.05)
        gif3.undraw()
        gif4=Image(Point(400,h), "ui/lola/4.gif")
        gif4.draw(win)
        update()
        time.sleep(0.05)
        gif4.undraw()
        gif5=Image(Point(400,h), "ui/lola/5.gif")
        gif5.draw(win)
        update()
        time.sleep(0.05)
        gif5.undraw()
        gif6=Image(Point(400,h), "ui/lola/6.gif")
        gif6.draw(win)
        update()
        time.sleep(0.05)
        gif6.undraw()
        gif7=Image(Point(400,h), "ui/lola/7.gif")
        gif7.draw(win)
        update()
        time.sleep(0.05)
        gif7.undraw()
        gif8=Image(Point(400,h), "ui/lola/8.gif")
        gif8.draw(win)
        update()
        time.sleep(0.05)
        gif8.undraw()
        gif9=Image(Point(400,h), "ui/lola/9.gif")
        gif9.draw(win)
        update()
        time.sleep(0.05)
        gif9.undraw()
        gif10=Image(Point(400,h), "ui/lola/10.gif")
        gif10.draw(win)
        update()
        time.sleep(0.05)
        gif10.undraw()
        gif11=Image(Point(400,h), "ui/lola/11.gif")
        gif11.draw(win)
        update()
        time.sleep(0.05)
        gif11.undraw()
    #if Lola crouches
    #change the height of Lola
    #swap other gif images to show the movement of Lola 
    if down:
        h=h+25
        #change Lola's center 
        lola.changeCenter(h)
        gif1=Image(Point(400,h), "ui/lola/1.gif")
        gif1.draw(win)
        #update the system 
        update()
        #freeze the system to swap image through draw and undraw  
        time.sleep(0.05)
        gif1.undraw()
        gif2=Image(Point(400,h), "ui/lola/2.gif")
        gif2.draw(win)
        update()
        time.sleep(0.05)
        gif2.undraw()
        gif3=Image(Point(400,h), "ui/lola/3.gif")
        gif3.draw(win)
        update()
        time.sleep(0.05)
        gif3.undraw()
        gif4=Image(Point(400,h), "ui/lola/4.gif")
        gif4.draw(win)
        update()
        time.sleep(0.05)
        gif4.undraw()
        gif5=Image(Point(400,h), "ui/lola/5.gif")
        gif5.draw(win)
        update()
        time.sleep(0.05)
        gif5.undraw()
        gif6=Image(Point(400,h), "ui/lola/6.gif")
        gif6.draw(win)
        update()
        time.sleep(0.05)
        gif6.undraw()
        gif7=Image(Point(400,h), "ui/lola/7.gif")
        gif7.draw(win)
        update()
        time.sleep(0.05)
        gif7.undraw()
        gif8=Image(Point(400,h), "ui/lola/8.gif")
        gif8.draw(win)
        update()
        time.sleep(0.05)
        gif8.undraw()
        gif9=Image(Point(400,h), "ui/lola/9.gif")
        gif9.draw(win)
        update()
        time.sleep(0.05)
        gif9.undraw()
        gif10=Image(Point(400,h), "ui/lola/10.gif")
        gif10.draw(win)
        update()
        time.sleep(0.05)
        gif10.undraw()
        gif11=Image(Point(400,h), "ui/lola/11.gif")
        gif11.draw(win)
        update()
        time.sleep(0.05)
        gif11.undraw()

        
#------
# MAIN
#------
def main():
    #construct the width, height,and background color of the window
    win = GraphWin( 'Run, Lola, run', 800, 500, autoflush=False)
    win.setBackground( 'cornflower blue' )

    #call openscene function to set up the openning of the game 
    openning = Openscene(win,400,250,"ui/opening/open1.gif","ui/opening/open2.gif","ui/opening/open3.gif")
    
    #display background picture
    BgCenter=Point(400,250)
    BgPicName="ui/settings/setting1.gif"
    BgImage=Image(BgCenter,BgPicName)
    BgImage.draw(win)
    
    #set up object radius and objects list 
    objRadius=5
    objs=[]
    
    #set Lola's initial values in the game  
    lolacenter=Point(400,400)
    distance=0
    speed=10
    jumpHeight=25
    #call Lola class and pass in these values 
    lola=Lola(win, lolacenter, distance,speed,jumpHeight)

    #set up the total time of the game 
    t = 90 #this represent # of t *sleep time seconds
    
    #set up the total distance of the game 
    totalDistance = 2000
    
    #Call the timer class to initialize the time bar 
    timer = Timer(0,20,"ui/signs/timer.gif",win)
    
    #Call Progress class to initialize the progress bar 
    progress = Progress(0,60,totalDistance,"ui/signs/german.gif",win)

    #keep track of question and text that has already appeared
    usedQuestions = []
    usedText = []
    #max number of question and text in directory
    mypath = "conversation box text/paragraphs/"
    maxq = len([join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))])
    mypath = "conversation box text/questions/"
    maxt = len([join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))])

    

    #while loop to start the game
    #while loop will stop when time expires or Lola reach the end of the path 
    while(t>0 and lola.getDistance()<totalDistance):
        #print(lola.getDistance())
        # An object appear every 10 t 
        if t % 10 == 0:
            #print("Object should appear")
            obj=Obj(win)
            #append object to the object list 
            objs.append(obj)
        #move objects according to speed of Lola
        for ball in objs:
            ball.MoveObj(lola.getSpeed())
            #if the object is outside the window, remove and undraw it 
            if ball.getCenterForObject().getX()<0:
                objs.remove(ball)
                ball.undraw()
             
        #animate lola: space to jump, down to squat(crouch)
        #check whether space or down has been pressed 
        status=win.checkKey()
        #call animate function to animate Lola 
        animate(win,lola,status)

        #minus time t for 0.5 for each loop 
        t=t-0.5
        #call the move_to method in Timer class to move the timer for each loop 
        timer.move_to()
        #track the icon's position 
        icon_x = progress.getx()
        #call the move_to method in Progress class to move the icon for each loop
        progress.move_to(icon_x,lola.getDistance())

        #collision checker and enters game
        for ball2 in objs:
            #print("Y for obj: ", center.getY(), "X for obj: ", center.getX(),"h", h)
            #if lola collides with objects
            if lola.collisionChecker(ball2):
                #assign the type of game and enter the game
                #by calling Questions or TypeGame (they are py files and should be
                #placed in the same folder as this file) 
                if ball2.isQuestion():
                    g =Questions(win)
                    #change a question is it has appeared before
                    while g.getQuestion() in usedQuestions:
                        g = Questions(win)
                        #avoid stuck in infintely loop if run out of questions
                        if len(usedQuestions) ==  maxq:
                            break
                    usedQuestions.append(g.getQuestion())
                else: 
                    g = TypeGame(win)
                    #change text is it has appeared before
                    while g.getText() in usedText:
                        g = TypeGame(win)
                        #avoid stuck in infintely loop if run out of questions
                        if len(usedText) ==  maxt:
                            break
                    usedText.append(g.getText())
                #if win the game: Lola accerelate 
                if g.display(): 
                    lola.accelerate(g.getAcceleration())
                #if lose the game: Lola decelerate 
                else: 
                    lola.decelerate(1)
                #after collision, remove and undraw the objects 
                objs.remove(ball2)
                ball2.undraw()
                   
        #update Lola's distance
        lola.changeDistance(lola.getSpeed())

    #determine whether the player win the game or not
    #when the time expires(the while loop stop), if Lola's current distance is larger or
    #equal to the total distance, then player win the game
    if lola.getDistance()>=totalDistance:
         win_image = Image(Point(400, 300),"ui/signs/win.gif")
         win_image.draw(win)
    #otherwise, player lose the game 
    else:
        lose_image = Image(Point(400,300),"ui/signs/lose.gif")
        lose_image.draw(win)
                       

main()
