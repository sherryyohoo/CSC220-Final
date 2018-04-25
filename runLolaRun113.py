
from graphics import *
from random import *
from math import sqrt
import time
import itertools
import threading
import sys

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
            
##        # Must update instance var:
##        self.BgX,self.BgY = self.BgX+dx, self.BgY+dy
##        self.BgCenter = Point(self.BgX,self.BgY)
##        for ObjCenter in self.ObjCenters:
##            x,y=ObjCenter.getX(),ObjCenter.getY()
##            newX, newY=x+dx, y+dy
##            ObjCenter=Point(newX,newY)

def main():
    win = GraphWin( 'Run, Lola, run', 800, 500, autoflush=False)
    win.setBackground( 'cornflower blue' )
    w = 100
    win.setCoords( -w, -w, w, w )


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
    while(n<450):
        down=False
        h=-20
        bgAndObj.MoveDisp( -10, 0 )
        status=win.checkKey()
        if status=="space": 
            h=h+50
        elif status=="Down":
            down=True
        if not down:
            lola.changeCenter(h)
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
            
        objectCenters=bgAndObj.getCentersForObjects()
        #print("objectYCenters: ", objectCenters)
        radiusOfObject=bgAndObj.getObjRadius()
        for center in objectCenters:
            #print("Y for obj: ", center.getY(), "X for obj: ", center.getX(),"h", h)
            #lola collides with objects
            if lola.collisionChecker(center,radiusOfObject):
                print("collision")
main()
        
        
