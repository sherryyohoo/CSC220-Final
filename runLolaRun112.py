from graphics import *
from random import *
from math import sqrt
from Questions import *
from TypeGame import *
import time
import itertools
import threading
import sys

def Openscene(win,x,y,open1,open2,open3):
        open1_image = Image(Point(x, y),open1)
        open1_image.draw(win)
        update()
        time.sleep(5)
        open1_image.undraw()
        open2_image = Image(Point(x, y),open2)
        open2_image.draw(win)
        update()
        time.sleep(15)
        open2_image.undraw()
        open3_image = Image(Point(x, y),open3)
        open3_image.draw(win)
        update()
        time.sleep(5)
        open3_image.undraw()
        
class Timer:
    def __init__(self,x,y,clock,win):
        p1 = Point(x-100,y-5)
        p2 = Point(x+100,y+5)
        bar1 = Rectangle(p1,p2)
        bar1.setFill("light green")
        bar1.setOutline("light green")
        self.speed = 0.1
        #call image timer and draw the image:timer
        clock_filename = clock 
        clock_image = Image(Point(x-100, y),clock_filename )
        self.clock_image = clock_image
        bar1.draw(win)
        clock_image.draw(win)
      
    def move_to(self):
        self.clock_image.move(self.speed,0)

class Progress:
    def __init__(self,x,y,distance,lola,win):
        self.distance = distance
        p1 = Point(x-100,y-5)
        p2 = Point(x+100,y+5)
        bar1 = Rectangle(p1,p2)
        bar1.setFill("light blue")
        bar1.setOutline("light blue")
        bar1.draw(win)
        lola_image = Image(Point(x-100, y),lola)
        self.lola_image = lola_image
        lola_image.draw(win)

    def getx(self):
        image_position = self.lola_image.getAnchor()
        image_x = 100-abs(image_position.getX())
        return(image_x)

        
    def move_to(self,x,progress):
        lola_curr = (progress/self.distance)*200
        speed =  lola_curr-x
        speed = round(speed,2)
        self.lola_image.move(speed,0)
      



class Lola:
    def __init__(self, win, center1, distance1,speed1,jumpHeight1,LolaRadius):
        self.center=center1
        self.x, self.y= center1.getX(), center1.getY()
        self.speed= speed1
        self.distance= distance1
        self.jumpHeight=jumpHeight1
        self.LolaRadius=LolaRadius
                       
    #following functions changes some values for this object
    def accelerate(self):
        self.speed += self.speed
    def decelerate(self):
        self.speed -= self.speed
    def changeDistance(self,distance):
        self.distance= self.distance + distance

        
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
            ObjCenter=Point(newX,newY)

def main():
    win = GraphWin( 'Run, Lola, run', 800, 500, autoflush=False)
    win.setBackground( 'cornflower blue' )
    w = 100
    win.setCoords( -w, -w, w, w )
    #Openinng 
    Openscene(win,0,0,"open1.gif","open2.gif","open3.gif")
    
    initialSpeed=10
    BgCenter=Point(0,0)
    objRadius=4
    numberOfObjects=10
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
    timer = Timer(0,90,"timer.png",win)
    progress = Progress(0,80,totalDistance,"german.png",win)
    
    while(t>0 and lola.getDistance()<totalDistance):
        h=-20
        bgAndObj.MoveDisp( -10, 0 )
        status=win.checkKey()
        if status=="space": 
            h=h+20
        gif1=Image(Point(0,h), "lola1.gif")
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
        gif4.undraw()
        t=t-1
        timer.move_to()
        x = progress.getx()
        progress.move_to(x,distance1)
        #collision checker and enters game
        
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
                


##    while (n<450):
##            gif[0].draw(win)
##            time.sleep(1)
##            gif[0].undraw()
##        keyString=win.checkKey()
##        objectCenters=bgAndObj.getCentersForObjects()
##        radiusOfObject=bgAndObj.getObjRadius()
##        if keyString=="space":
##            for center in objectCenters: 
##            #lola collides with objects
##                if lola.collisionChecker(center,radiusOfObject):
##                    print("collision")
##                    #open game
##                        #if score, accelerate
##                        #if not score, decelerate
##        #time bar
##        #progress bar
##        n=n+1
main()

        
        
