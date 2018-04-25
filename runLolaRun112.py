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


#------------------
# HELPER FUNCTION
#------------------

def Openscene(win,x,y,open1,open2,open3):
        '''Helper function of the openning of the game, to introduce game background
        and instructions through showing openning images in sequence
        x,y: the position to draw the image 
        open1,open2,open3: the file names of the images that will be displayed at the
        begining 
        window: the window on which the images draw'''
        
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
        p1 = Point(x-100,y-5)
        p2 = Point(x+100,y+5)
        bar1 = Rectangle(p1,p2)
        bar1.setFill("light green")
        bar1.setOutline("light green")
        #set the moving distance of the timer
        #instance variables for speed 
        self.speed = 0.1
        #call image timer and draw the image:timer
        clock_image = Image(Point(x-100, y),clock)
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
        #instance variables for distance 
        self.distance = distance
        #create and draw the progress bar 
        p1 = Point(x-100,y-5)
        p2 = Point(x+100,y+5)
        bar1 = Rectangle(p1,p2)
        bar1.setFill("light blue")
        bar1.setOutline("light blue")
        bar1.draw(win)
        #call and draw the icon image 
        icon_image = Image(Point(x-100, y),icon)
        self.icon_image = icon_image
        icon_image.draw(win)

    def getx(self):
        #get the current position of the icon image 
        image_position = self.icon_image.getAnchor()
        image_x = 100-abs(image_position.getX())
        #store the value of the current position 
        return(image_x)

        
    def move_to(self,icon_x,progress):
        #icon_x: icon's current x-axis position
        #progress: Lola's progress in the game 
        #calculate where the icon should currently be placed
        #based on Lola's progress in the game over the total distance of the game
        #(the current percentage of Lola's progress in the game)
        #in proportion to the length of the bar 
        icon_curr = (progress/self.distance)*200
        #the length of movement (speed) is the icon's (should be) current position
        #minus the origional icon's position 
        speed =  icon_curr-icon_x
        #round up the number 
        speed = round(speed,2)
        #move the icon through the progress bar
        self.icon_image.move(speed,0)
      



class Lola:
    def __init__(self, win, center1, distance1,speed1,jumpHeight1,LolaRadius):
        self.center=center1
        self.x, self.y= center1.getX(), center1.getY()
        self.speed= speed1
        self.distance= distance1
        self.jumpHeight=jumpHeight1
        self.LolaRadius=LolaRadius
                       
     #following functions changes some values for this object
    def accelerate(self,speedValue):
        self.speed= self.speed+speedValue
    def decelerate(self,speedValue):
        self.speed= self.speed-speedValue
    def changeDistance(self,distance):
        self.distance= self.distance + distance
    def changeCenter(self,y):
        newY=y
        self.Center=Point(self.x,newY)

        
    #not sure if the undraw here is going to work or not
    def jump(self):
        self.Lola.undraw(win)
        self.y=self.y+self.jumpHeight
        self.center=Point(self.x, self.y)
        self.Lola=Image(self.center,LolaImage)
        self.Lola.draw(win)
               
    def land(self):
        self.Lola.undraw(win)
        self.y=self.y-self.jumpHeight
        self.center=Point(self.x, self.y)
        self.Lola=Image(self.center,LolaImage)
        self.Lola.draw(win)


    def collisionChecker(self,centerOfObject,radiusOfObject):
        #centerOfObject should be the coordinate of the object on the graph
        #return True if collision happened
        x, y= centerOfObject.getX(), centerOfObject.getY()
        d=self.LolaRadius+radiusOfObject
        seperation=sqrt((self.x-x)**2+(self.y-y)**2)
        if (seperation<d):
            return True
        else:
            return False
        
    #following functions returns values for this object
    def getSpeed(self):
        return self.speed
    def getCenter(self):
        return self.center
    def getDistance(self):
        return self.distance
class BgAndObj:
    def __init__(self, win, speed, BgCenter, objRadius, numberOfObjects,w,
                 BgPicName):
        #w stands for the setting for the coordinate
        #BgPicName is supposed to be the name of the Image
        self.speed=speed
        self.BgX, self.BgY=BgCenter.getX(),BgCenter.getY()
        self.BgCenter=BgCenter
        self.objRadius=objRadius
        self.ObjCenters=[]
        self.BgImage=Image(BgCenter,BgPicName)
        self.parts=[]
        self.BgImage.draw(win)
        #using random function to distributes those objects
        for i in range(numberOfObjects):
            #generate object centers
            ObjCenter=Point(randint(-w,w),randint(-w,w))
            self.ObjCenters.append(ObjCenter)
            ObjCircle=Image(ObjCenter,"coin.gif")
            #put object generated in self.parts
            self.parts.append(ObjCircle)
        #draw object
        for part in self.parts:
            part.draw(win)
        
    def getBgCenter(self):
        return self.BgCenter
    def getObjRadius(self):
        return self.objRadius
    def getSpeed(self):
        return self.speed
    
    #return the center of each object as a list
    def getCentersForObjects(self):
        return self.ObjCenters

    #move background and all of the objects 
    def MoveDisp( self, dx, dy ):
        if self.BgX <= -450:           
            for i in range(0,len(self.parts)):
                self.parts[i].move(450, dy)
                dx=450
        else:
            for i in range(0,len(self.parts)):
                self.parts[i].move( dx, dy )
                
        for i in range(0,len(self.parts)):
            objCenter=self.parts[i].getAnchor()
            objX,objY=objCenter.getX(), objCenter.getY()
            objX=objX+dx
            objY=objY+dy
            newCenter=Point(objX,objY)
            self.ObjCenters[i]=newCenter
            self.BgX=self.BgX+dx
    
'''class BgAndObj:
    def __init__(self, win, speed, BgCenter, objRadius, numberOfObjects,w,
                 BgPicName):
        #w stands for the setting for the coordinate
        #BgPicName is supposed to be the name of the Image
        self.speed=speed
        self.BgX, self.BgY=BgCenter.getX(),BgCenter.getY()
        self.BgCenter=BgCenter
        self.objRadius=objRadius
        self.ObjCenters=[]
        self.BgImage=Image(BgCenter,BgPicName)
        self.parts=[]
        self.parts.append(self.BgImage)
        #using random function to distributes those objects
        for i in range(numberOfObjects):
            #generate object centers
            ObjCenter=Point(randint(-w,w),randint(-w,w))
            self.ObjCenters.append(ObjCenter)
            ObjCircle=Circle(ObjCenter,3)
            #put object generated in self.parts
            self.parts.append(ObjCircle)
        #draw object
        for part in self.parts:
            part.draw(win)
        
    def getBgCenter(self):
        return self.BgCenter
    def getObjRadius(self):
        return self.objRadius
    def getSpeed(self):
        return self.speed
    
    #return the center of each object as a list
    def getCentersForObjects(self):
        return self.ObjCenters

    #move background and all of the objects 
    def MoveDisp( self, dx, dy ):
        if self.BgX <= -25:           
            for i in range(1,len(self.parts)):
                self.parts[i].move( 25, dy )
            self.BgX=0
        elif self.BgX > -25:
            for i in range(1,len(self.parts)):
                self.parts[i].move( dx, dy )

        # Must update instance var:
        self.BgX,self.BgY = self.BgX+dx, self.BgY+dy
        self.BgCenter = Point(self.BgX,self.BgY)
        for ObjCenter in self.ObjCenters:
            x,y=ObjCenter.getX(),ObjCenter.getY()
            newX, newY=x+dx, y+dy
            ObjCenter=Point(newX,newY)'''

#------
# MAIN
#------
def main():
    #construct the width, height,and background color of the window
    win = GraphWin( 'Run, Lola, run', 800, 500, autoflush=False)
    win.setBackground( 'cornflower blue' )
    #set up the coordinates of the window 
    w = 100
    win.setCoords( -w, -w, w, w )
    #Call the Openscene function to begin the game with the openning scenes 
    Openscene(win,0,0,"open1.gif","open2.gif","open3.gif")
    #set up Lola's initial speed, background center,object radius, number of objects,
    #background picture names
    initialSpeed=10
    BgCenter=Point(0,0)
    objRadius=5
    numberOfObjects=2
    BgPicName=""
    number=0
    BgCenter=Point(0,0)
    BgPicName="setting1.gif"
    speed=2
    n=0
    center1=Point(0,0)
    distance1=0
    speed1=4
    jumpHeight1=25
    LolaRadius=70
    bgAndObj=BgAndObj(win, speed, BgCenter, objRadius, numberOfObjects,w,
                 BgPicName)
    bgAndObj.MoveDisp( -1, 0 )
    lola=Lola(win, center1, distance1,speed1,jumpHeight1,LolaRadius)
    t = 200 #this represent #*sleep time seconds
    totalDistance = 200 #To be determined
    #Call the timer class to initialize the time bar 
    timer = Timer(0,90,"timer.png",win)
    #Call Progress class to initialize the progress bar 
    progress = Progress(0,80,totalDistance,"german.png",win)

    #while loop to start the game
    #make lola runs 
    while(t>0 and lola.getDistance()<totalDistance):
        down=False 
        h=-20
        bgAndObj.MoveDisp( -10, 0 )
        status=win.checkKey()
        if status=="space": 
            h=h+20
        elif status=="Down":
                down=True
        if not down:
            lola.changeCenter(h)
            gif1=Image(Point(0,h), "lola1.gif")
            gif1.draw(win)
            update()
            time.sleep(0.15)
            gif1.undraw()
            gif2=Image(Point(0,h), "lola2.gif")
            gif2.draw(win)
            update()
            time.sleep(0.15)
            gif2.undraw()
            gif3=Image(Point(0,h), "lola3.gif")
            gif3.draw(win)
            update()
            time.sleep(0.1)
            gif3.undraw()
            gif4=Image(Point(0,h), "lola4.gif")
            gif4.draw(win)
            update()
            time.sleep(0.1)
            gif4.undraw()
        if down:
            h=-25
            lola.changeCenter(h)
            gif1=Image(Point(0,h), "lolaaa3.gif")
            gif1.draw(win)
            update()
            time.sleep(0.1)
            gif1.undraw()
            gif2=Image(Point(0,h), "lolaaa2.gif")
            gif2.draw(win)
            update()
            time.sleep(0.1)
            gif2.undraw()
            gif3=Image(Point(0,h), "lolaaa1.gif")
            gif3.draw(win)
            update()
            time.sleep(0.1)
            gif3.undraw()
            gif2.draw(win)
            update()
            time.sleep(0.1)
            gif2.undraw()
            gif1.draw(win)
            update()
            time.sleep(0.1)
            gif1.undraw()
                
        '''gif1=Image(Point(0,h), "lola1.gif")
        gif1.draw(win)
        update()
        time.sleep(0.1)
        gif1.undraw()
        gif2=Image(Point(0,h), "lola2.gif")
        gif2.draw(win)
        update()
        time.sleep(0.1)
        gif2.undraw()
        gif3=Image(Point(0,h), "lola3.gif")
        gif3.draw(win)
        update()
        time.sleep(0.1)
        gif3.undraw()
        gif4=Image(Point(0,h), "lola4.gif")
        gif4.draw(win)
        update()
        time.sleep(0.1)
        gif4.undraw()'''
        t=t-1
        #call the move_to method in Timer class to move the timer for each loop 
        timer.move_to()
        #track the icon's position 
        icon_x = progress.getx()
        #call the move_to method in Progress class to move the icon for each loop
        progress.move_to(icon_x,distance1)
        #collision checker and enters game
        objectCenters=bgAndObj.getCentersForObjects()
        #print("objectYCenters: ", objectCenters)
        radiusOfObject=bgAndObj.getObjRadius()
        for center in objectCenters:
            #print("Y for obj: ", center.getY(), "X for obj: ", center.getX(),"h", h)
            #lola collides with objects
            if lola.collisionChecker(center,radiusOfObject):
                print("collision")
        
        #if collide with TypeGame Object
        if lola.collisionChecker(center,radiusOfObject):
                g = TypeGame(win)
                if g.display():
                        lola.accelerate()
                else:
                        lola.decelerate()
        #if collide with Questions Object
        if lola.collisionChecker(center,radiusOfObject):
                g = Questions(win)
                if g.display():
                        lola.accelerate()
                else:
                        lola.decelerate()

        #update distance
        lola.changeDistance(lola.getSpeed())
        
                

main()

        
        
