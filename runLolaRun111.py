from graphics import *
from random import *
from math import sqrt
import time
import itertools
import threading
import sys




##
##
##t= threading.Thread(target=animate)
##t.start()
        
class Lola:
    def __init__(self, win, center1, distance1,speed1,jumpHeight1,LolaRadius):
        self.center=center1
        self.x, self.y= center1.getX(), center1.getY()
        self.speed= speed1
        self.distance= distance1
        self.jumpHeight=jumpHeight1
        self.LolaRadius=LolaRadius
        #self.thread = threading.Thread(target = self.animate)
                       
    #following functions changes some values for this object
    def accelerate(self,speedValue):
        self.speed= self.speed+speedValue
    def decelerate(self,speedValue):
        self.speed= self.speed-speedValue
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
    
    def animate(self):
        win = GraphWin( 'Run, Lola, run', 600, 500, autoflush=False )
        win.setBackground( 'cornflower blue' )
        w = 100
        win.setCoords( -w, -w, w, w )
        while True:
            #bgAndObj.MoveDisp( -10, 0 )
            gif1=Image(Point(0,-20), "lola1.gif")
            gif1.draw(win)
            update()
            time.sleep(1)
            gif1.undraw()
            gif2=Image(Point(0,-20), "lola2.gif")
            gif2.draw(win)
            update()
            time.sleep(1)
            gif2.undraw()
            gif3=Image(Point(0,-20), "lola3.gif")
            gif3.draw(win)
            update()
            time.sleep(1)
            gif3.undraw()
            gif4=Image(Point(0,-20), "lola4.gif")
            gif4.draw(win)
            update()
            time.sleep(1)
            gif4.undraw()

    
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


def heightchange():
    increase = True
    
    while 1:
        if increase:
            height +=1
        else:
            height -=1
        

        
def main():
    win = GraphWin( 'Run, Lola, run', 600, 500, autoflush=False )
    win.setBackground( 'cornflower blue' )
    w = 100
    win.setCoords( -w, -w, w, w )


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
    global height = -20
    heightthread = threading.Thread(target = self.heightchange)
    heightthread.start()
    
    while(n<450):
        bgAndObj.MoveDisp( -10, 0 )
        gif1=Image(Point(0,height), "lola1.gif")
        gif1.draw(win)
        update()
        time.sleep(0.1)
        gif1.undraw()
        gif2=Image(Point(0,height), "lola2.gif")
        gif2.draw(win)
        update()
        time.sleep(0.1)
        gif2.undraw()
        gif3=Image(Point(0,height), "lola3.gif")
        gif3.draw(win)
        update()
        time.sleep(0.1)
        gif3.undraw()
        gif4=Image(Point(0,height), "lola4.gif")
        gif4.draw(win)
        update()
        time.sleep(0.1)
        gif4.undraw()
        n=n+1
##t= threading.Thread(target=animate)
##t.start()
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
##done = False
###here is the animation
##def animate():
##    for c in itertools.cycle(['|', '/', '-', '\\']):
##        if done:
##            break
##        sys.stdout.write('\rloading ' + c)
##        sys.stdout.flush()
##        time.sleep(0.1)
##    sys.stdout.write('\rDone!     ')
##
##t = threading.Thread(target=animate)
##t.start()
##
###long process here
##time.sleep(10)
##done = True
        
        
        
