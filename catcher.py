#Yilin Wang
#Final Exam Task #2: Catcher in the Rye
from math import *
from graphics import *
from random import randint

def IsInside( p, circ ):
    '''Return T if point p inside circle circ, F if not
    '''
    x,y = p.getX( ), p.getY( )
    cent = circ.getCenter( )
    cx,cy = cent.getX( ), cent.getY( )
    r = circ.getRadius( )

    # Pythagorean theorem:
    d = sqrt( (cx-x)**2 + (cy-y)**2 )
    if d <= r:
        return True
    else:
        return False

class grass:
    '''draws the grass'''
    def __init__(self,win,w,r,start):
        Point1=Point(-start,-w)
        Point2=Point(-start+r,-w+25)
        grass=Rectangle(Point1, Point2)
        grass.setFill(color_rgb(205,183,158))
        grass.setOutline(color_rgb(205,183,158))
        grass.draw(win)
        
class child:
    '''class for child'''
    def __init__(self, win,w,centerPoint,childRadius):
        self.childRadius=childRadius
        self.centerPoint=centerPoint
        self.counter = 0 # How many children so far gathered
        self.w=w
        self.disk=Circle(self.centerPoint,childRadius)
        self.disk.setFill('pink')
        self.disk.draw(win)

        smileCircle2=Circle(centerPoint,6)
        smileCircle2.setFill("pink")
        smileCircle2.setOutline("black")
        smileCircle2.draw(win)

        self.x,self.y=centerPoint.getX(),centerPoint.getY()
        smileCircle1=Circle(Point(self.x,self.y+2),6)
        smileCircle1.setFill("pink")
        smileCircle1.setOutline("pink")
        smileCircle1.draw(win)

        self.LchildParts=[self.disk,smileCircle2,smileCircle1]

        
    def MoveChild(self,score):
        '''Move the child'''
        Vspeed=((-1)*(0.5+int(1*(score/3))))
        for i in self.LchildParts:
            i.move(0, Vspeed)
            #Update instance variable:
            center=self.disk.getCenter()
            self.xcent,self.ycent = center.getX(),center.getY()
            xnew,ynew = self.xcent, self.ycent+Vspeed
            self.cx,self.cy = xnew, ynew
            if self.cy<=-self.w-10:
                WrapPoint=Point(randint(-self.w+self.childRadius+10,self.w-self.childRadius-10),self.w-10)
                self.MoveCoinTo(WrapPoint)

    def getXY( self ):
        '''Extract xy coords from the pcent instance var'''
        x,y = self.pcent.getX( ),self.pcent.getY( )
        return x,y
    
    def Undraw(self):
        '''undraws the child'''
        for part in self.LchildParts:
            part.undraw()
            
    def MoveCoinTo( self, p ):
        '''Move center of coin to p'''
        x,y = p.getX( ),p.getY( )
        pcent = self.disk.getCenter( )
        xcoin,ycoin = pcent.getX(),pcent.getY()
        dx = x - xcoin
        dy = y - ycoin
        for part in self.LchildParts:
            part.move( dx, dy )
    
    def Collide( self, a_catcher ):
        '''All the actions for collision are handled here:
           * inside chk
           * move to rand spot
           * update & display counter
        '''
        pcatcher = a_catcher.getCenter( )
        # Use fnc from ClickDisks code:
        if IsInside( pcatcher, self.disk ):
            prand = randPoint(self.w,self.childRadius)
            self.counter += 1
            prand = Point(
                randint( -self.w,self.w ),
                self.w-self.childRadius
                )
            self.MoveCoinTo( prand )
            # Change label in car obj
            # Note: We learned with archery that can use # for text label:
            a_catcher.setLabel( self.counter )
            
    def getScore(self):
        '''return the counter'''
        return self.counter
    
        
class catcher:
    '''creates the catcher'''
    def __init__(self,pcent,win,w,strlabel,length):
        self.pcent=pcent
        xcent,ycent =self.pcent.getX( ),self.pcent.getY( )
        self.win=win 
        p1 = Point( xcent - length/2, ycent - length/5 )
        p2 = Point( xcent + length/2, ycent + length/5 )
        #CatcherBlcok = Rectangle( p1, p2 )
        #CatcherBlock=Rectangle(p1,p2)
        #CatcherBlock.setFill("green")
        gif1=Image(Point(0,0), "lola1.gif")
        gif2=Image(Point(0,0), "lola2.gif")
        gif3=Image(Point(0,0), "lola3.gif")
        gif4=Image(Point(0,0), "lola4.gif")

        '''gif1.draw(win)
        update()
        time.sleep(0.05)
        gif1.undraw()
        gif2.draw(win)
        update()
        time.sleep(0.05)
        gif2.undraw()
        gif3.draw(win)
        update()
        time.sleep(0.05 )
        gif3.undraw()'''
        
        

        # Decision: Make textlabel an instance var:
        '''self.textlabel = Text( pcent, strlabel )
        self.textlabel.setSize( 18 )'''

        self.parts=[ gif1,gif2,gif3,gif4]
        while True: 
            for part in self.parts:
                part.draw(self.win)
                update()
                time.sleep(0.05)
                part.undraw()
            
            
    def getXY( self ):
        '''Extract xy coords from the pcent instance var'''
        x,y = self.pcent.getX( ),self.pcent.getY( )
        print(x,y)
        return x,y

        
    def setLabel( self, newlabel ):
        '''Change the label'''
        self.textlabel.setText( newlabel )

    def MoveCatcherTo( self, Distance):
        '''Move center by distance called Distance'''
        xcent,ycent = self.getXY( )
        x=xcent+Distance
        for part in self.parts:
            part.move( Distance, 0 )
        update( ) # To force all parts to move now
        # We've moved the center, so need to update:
        self.pcent = Point( x, ycent )
        
    def getCenter( self ):
        '''returns the center'''
        return self.pcent
        
def randPoint(w,childRadius):
    '''gives a point with random x value but a constant y value'''
    RandPoint=Point(randint(-w+childRadius+10,w-childRadius-10),w-childRadius)
    return RandPoint
        
def main():
    '''contains the animation loop'''
    win = GraphWin( 'Catcher in the Rye', 500, 500,autoflush=False)
    win.setBackground( "LemonChiffon" )
    w = 100
    win.setCoords( -w, -w, w, w)
    #draws the grass
    for start in range(-w,w,5):
        Grass=grass(win,w,3,start)
        
    #initializes the values
    start=-w
    update(2)    
    childRadius=10
    pcent=Point(w/2,-w+21)
    centerPoint=randPoint(w,childRadius)
    #Child=child(win,w,centerPoint,childRadius)
    score=0
    Catcher=catcher(pcent,win,w,'0',20)
    Distance=6
    #animation loop
    '''while True:  
        Child.MoveChild(score)
        # Check if Child hit the Catcher; actions in class Catcher
        Child.Collide( Catcher )
        score=Child.getScore()
        keyString = win.checkKey()
        if keyString=="Right":
            CatcherCenter=Catcher.getCenter()
            CatcherX=CatcherCenter.getX()
            if not CatcherX>=w-12.5:
                i=1
                Catcher.MoveCatcherTo(i*Distance)
        if keyString=="Left":
            CatcherCenter=Catcher.getCenter()
            CatcherX=CatcherCenter.getX()
            if not CatcherX<=-w+11.5:
                i=-1
                Catcher.MoveCatcherTo(i*Distance)
        if keyString=='period':
            win.close()
            break  '''
main()
