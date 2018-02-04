from graphics import *


def getOutlineColor(GraphicsObject):
    return GraphicsObject.config['outline']


def getFillColor(GraphicsObject):
    return GraphicsObject.config['fill']


def isBetween(val,end1,end2):
    '''Return True if val is between the ends.'''
    return min(end1,end2) <= val <= max(end1,end2)


def isInside_rect(point,rect):
    '''Return True if the point is inside the Rectangle, rect.'''
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(),pt1.getX(),pt2.getX()) and \
           isBetween(point.getY(),pt1.getY(),pt2.getY())


def isInside_circle(point,circle):
    '''Return True if the point is inside the Circle, circle.'''
    radius = circle.getRadius()
    distance_square = (point.getX()-circle.getCenter().getX())**2+(point.getY()-circle.getCenter().getY())**2
    return distance_square < radius**2


def isInside_oval(point,oval):
    '''Return True if the point is inside the Oval, oval'''
    dx = point.getX()-oval.getCenter().getX()
    dy = point.getY()-oval.getCenter().getY()
    a = abs(oval.getP1().getX()-oval.getP2().getX())/2
    b = abs(oval.getP1().getY()-oval.getP2().getY())/2
    return (dx**2/a**2)+(dy**2/b**2) < 1

def write_Text(point,text,win,face='helvetica',size=12,style='normal',color='black'):
    t = Text(point,text)
    t.setFace(face)
    t.setSize(size)
    t.setStyle(style)
    t.setTextColor(color)
    t.draw(win)
    return t

def draw_Rectangle(p1,p2,win,Fill=None,Outline=None,Width=None):
    rec = Rectangle(p1,p2)
    rec.setFill(Fill)
    rec.setOutline(Outline)
    rec.setWidth(Width)
    rec.draw(win)
    return rec

def draw_Circle(center,radius,win,Fill=None,Outline=None,Width=None):
    c = Circle(center,radius)
    c.setFill(Fill)
    c.setOutline(Outline)
    c.setWidth(Width)
    c.draw(win)
    return c

def draw_Oval(p1,p2,win,Fil=None,Outline=None,Width=None):
    oval = Oval(p1,p2)
    oval.setFill(Fill)
    oval.setOutline(Outline)
    oval.setWidth(Width)
    oval.draw(win)
    return oval

