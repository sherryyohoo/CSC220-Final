from graphics import *
from random import randint
from math import sqrt

class Lola:
    def __init__(self, win, center1, distance1,speed1,jumpHeight1,LolaRadius):
        self.center=center1
        self.x, self.y= center1.getX(), center1.getY()
        self.speed= speed1
        self.distance= distance1
        self.jumpHeight=jumpHeight1
        self.LolaRadius=LolaRadius
        self.Lola=Circle(self.center,LolaRadius)
        self.Lola.draw(win)
                       
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
        self.Lola=Circle(self.center,LolaRadius)
        self.Lola.draw(win)
               
    def land(self):
        self.Lola.undraw(win)
        self.y=self.y-self.jumpHeight
        self.center=Point(self.x, self.y)
        self.Lola=Circle(self.center,LolaRadius)
        self.Lola.draw(win)

        
    def collisionChecker(self,centerOfObject,radiusOfObject):
        #centerOfObject should be the coordinate of the object on the graph
        #return True if collision happened
        x, y= centerOfObject.getX(), centerOfObject.getY()
        d=self.LolaRadius()+radiusOfObject
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
    def __init__(self, win, speed, BgCenter, objRadius, numberOfObjects, backGround,w,
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
            ObjCenter=Point(random.randint(-w,w),random.randint(-w,w))
            self.ObjCenters.append(ObjCenter)
            ObjCircle=Circle(ObjCenter,objRadius)
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
        '''Move BgAndObj by dx,dy, just like move()'''
        for part in self.parts:
            part.move( dx, dy )

        # Must update instance var:
        self.BgX,self.BgY = self.BgX+dx, self.BgY+dy
        self.BgCenter = Point(self.BgX,self.BgY)
        for ObjCenter in self.ObjCenters:
            x,y=ObjCenter.getX(),ObjCenter.getY()
            newX, newY=x+dx, y+dy
            ObjCenter=Point(newX,newY)

 
        
def main():
    win = GraphWin( 'Run, Lola, run', 500, 500, autoflush=False )
    win.setBackground( 'cornflower blue' )
    w = 100
    win.setCoords( -w, -w, w, w )
    
    while True:
        bgAndObj=BgAndObj(....)                       
        bgAndObj.MoveDisp( -1, 0 )

        #Lola pics
        GIF_picture1="XXX1.gif"
        GIF_picture2="XXX2.gif"
        GIF_picture1.draw(win)
        time.sleep(1)
        GIF_picture1.undraw(win)
        GIF_picture2.draw(win)
        time.sleep(1)
        GIF_picture2.undraw(win)

        #lola collides with objects
        #open the game
        #pause while playing the typing game
        #get key
        #jump if space is pressed
        #time bar
        #progress bar 
main()

        
        
        
