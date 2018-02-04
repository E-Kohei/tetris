from graphics import *
from graphics_helper import *
import time,random


##functions#####################################################################


def getFillColor(GraphicsObject):
    return GraphicsObject.config['fill']


def isColored(shape):
    if getFillColor(shape) != '':
        return True
    else:
        return False


def get_toprow(pixlList):
    i = 0
    while not isColored(pixelList[i]):
        i += 1
    toprow = i - i%15
    return toprow


def get_row(pixelnum):
    return pixelnum - pixelnum%15


def movedown(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4):
    pixelList[b1].setFill('')
    pixelList[b2].setFill('')
    pixelList[b3].setFill('')
    pixelList[b4].setFill('')
    (b1,b2,b3,b4,right,left) = (b1+15,b2+15,b3+15,b4+15,right+15,left+15)
    if bottom1 != sparenum:
        bottom1 += 15
    if bottom2 != sparenum:
        bottom2 += 15
    if bottom3 != sparenum:
        bottom3 += 15
    if bottom4 != sparenum:
        bottom4 += 15
    pixelList[b1].setFill(color)
    pixelList[b2].setFill(color)
    pixelList[b3].setFill(color)
    pixelList[b4].setFill(color)
    return (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)


def moveright(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,toprow):
    if (right+1)%15 != 0 and (get_row(bottom1)<toprow or get_row(bottom3)<toprow):
        pixelList[b1].setFill('')
        pixelList[b2].setFill('')
        pixelList[b3].setFill('')
        pixelList[b4].setFill('')
        (b1,b2,b3,b4,right,left) = (b1+1,b2+1,b3+1,b4+1,right+1,left+1)
        if bottom1 != sparenum:
            bottom1 += 1
        if bottom2 != sparenum:
            bottom2 += 1
        if bottom3 != sparenum:
            bottom3 += 1
        if bottom4 != sparenum:
            bottom4 += 1
        pixelList[b1].setFill(color)
        pixelList[b2].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
    return (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)


def moveleft(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,toprow):
    if left%15 != 0 and (get_row(bottom1)<toprow or get_row(bottom3)<toprow):
        pixelList[b1].setFill('')
        pixelList[b2].setFill('')
        pixelList[b3].setFill('')
        pixelList[b4].setFill('')
        (b1,b2,b3,b4,right,left) = (b1-1,b2-1,b3-1,b4-1,right-1,left-1)
        if bottom1 != sparenum:
            bottom1 -= 1
        if bottom2 != sparenum:
            bottom2 -= 1
        if bottom3 != sparenum:
            bottom3 -= 1
        if bottom4 != sparenum:
            bottom4 -= 1
        pixelList[b1].setFill(color)
        pixelList[b2].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
    return (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)


def turn(blocktype,b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount,toprow):
    if blocktype == 'type1' and (get_row(bottom1)<toprow or get_row(bottom3)<toprow) and \
       [1,left%15,1,(right+1)%15][turncount%4] != 0:
        pixelList[b1].setFill('')
        pixelList[b3].setFill('')
        pixelList[b4].setFill('')
        t = turncount%4
        (b1,b2,b3,b4) = (b1+[16,-14,-16,14][t],b2,b3+[-16,14,16,-14][t],b4+[-14,-16,14,16][t])
        pixelList[b1].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
        (right,left,bottom1,bottom2,bottom3) = \
        ([b4,b1,b2,b3][t],[b2,b3,b4,b1][t],[b1,b1,sparenum,b1][t],[sparenum,b3,b3,b3][t],[b4,b2,b4,b4][t])
        turncount += 1
    elif blocktype == 'type2' and get_row(bottom1)+15 < toprow and \
         [True,(right+1)%15 != 0 and (right+2)%15 != 0 and left%15 != 0][turncount%2]:
        pixelList[b1].setFill('')
        pixelList[b3].setFill('')
        pixelList[b4].setFill('')
        t = turncount%2
        (b1,b2,b3,b4) = (b1+[16,-16][t],b2,b3+[-16,16][t],b4+[-32,32][t])
        pixelList[b1].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
        (right,left,bottom1,bottom2,bottom3,bottom4) = \
        ([b1,b4][t],b1,b1,[sparenum,b2][t],[sparenum,b3][t],[sparenum,b4][t])
        turncount += 1
    elif blocktype == 'type3' and get_row(bottom1)+15 < toprow and \
         [True,[(right+1)%15 != 0,left%15 != 0][reversecount%2]][turncount%2]:
        pixelList[b1].setFill('')
        pixelList[b3].setFill('')
        pixelList[b4].setFill('')
        t = turncount%2
        r = reversecount%2
        (b1,b2,b3,b4) = \
        (b1+[[16,14][r],[-16,-14][r]][t],b2,b3+[[14,16][r],[-14,-16][r]][t],b4+[[-2,2][r],[2,-2][r]][t])
        pixelList[b1].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
        (right,left,bottom1,bottom2,bottom3,bottom4) = \
        ([[b1,b4][r],[b4,b1][r]][t],[[b4,b1][r],[b1,b4][r]][t],b1,[b3,b2][t],[sparenum,b4][t],sparenum)
        turncount += 1
    elif blocktype == 'type4' and (get_row(bottom1)<toprow or get_row(bottom3)<toprow) and \
         [[1,left][reversecount%2]%15 != 0,[left,1][reversecount%2]%15 != 0,[1,right+1][reversecount%2]%15 != 0,[right+1,1][reversecount%2]%15 != 0][turncount%4]:
        pixelList[b1].setFill('')
        pixelList[b3].setFill('')
        pixelList[b4].setFill('')
        t = turncount%4
        r = reversecount%2
        b1 += [[16,14][r],[-14,16][r],[-16,-14][r],[14,-16][r]][t]
        b3 += [[-16,-14][r],[14,-16][r],[16,14][r],[-14,16][r]][t]
        b4 += [-30,-2,30,2][t]
        pixelList[b1].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
        right = [b4,b1,b1,b4][t]
        left = [b1,b4,b4,b1][t]
        bottom1 = [b1,b1,[sparenum,b1][r],[b1,sparenum][r]][t]
        bottom2 = [[sparenum,b2][r],[b2,sparenum][r],[sparenum,b2][r],[b2,sparenum][r]][t]
        bottom3 = [[sparenum,b3][r],[b3,sparenum][r],[b3,sparenum][r],[sparenum,b3][r]][t]
        bottom4 = [[b4,sparenum][r],[sparenum,b4][r],b4,b4][t]
        turncount += 1
    return (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount)


def reverse_block(blocktype,b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount,toprow):
    if blocktype == 'type3' and get_row(bottom1)+15 < toprow:
        pixelList[b1].setFill('')
        pixelList[b2].setFill('')
        pixelList[b3].setFill('')
        pixelList[b4].setFill('')
        t = turncount%2
        r = reversecount%2
        (b1,b2,b3,b4) = \
        (b1+[[2,-2][r],[-1,1][r]][t],b2+[0,[-1,1][r]][t],b3+[0,[1,-1][r]][t],b4+[[-2,2][r],[1,-1][r]][t])
        pixelList[b1].setFill(color)
        pixelList[b2].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
        (right,left,bottom1,bottom2,bottom3,bottom4) = \
        ([[b1,b4][r],[b3,b2][r]][t],[[b4,b1][r],[b2,b3][r]][t],b1,[b2,sparenum][t],[sparenum,b3][t],[b4,sparenum][t])
        reversecount += 1    
    if blocktype == 'type4' and (get_row(bottom1)<toprow or get_row(bottom3)<toprow) and \
       [[1,left][reversecount%2]%15 != 0,[left,1][reversecount%2]%15 != 0,[1,right+1][reversecount%2]%15 != 0,[right+1,1][reversecount%2]%15 != 0][turncount%4]:
        pixelList[b1].setFill('')
        pixelList[b3].setFill('')
        t = turncount%4
        r = reversecount%2
        b1 += [[-14,14][r],[-16,16][r],[14,-14][r],[16,-16][r]][t]
        b3 += [[14,-14][r],[16,-16][r],[-14,14][r],[-16,16][r]][t]
        pixelList[b1].setFill(color)
        pixelList[b3].setFill(color)
        right = [b4,b4,b1,b1][t]
        left = [b1,b1,b4,b4][t]
        bottom1 = [[sparenum,b1][r],b1,b1,[b1,sparenum][r]][t]
        bottom2 = [[sparenum,b2][r],[b2,sparenum][r],[sparenum,b2][r],[b2,sparenum][r]][t]
        bottom3 = [[b3,sparenum][r],[b3,sparenum][r],[sparenum,b3][r],[sparenum,b3][r]][t]
        bottom4 = [b4,[sparenum,b4][r],[b4,sparenum][r],b4][t]
        reversecount += 1    
    return (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount)
        

def settle(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4):
    while not isColored(pixelList[bottom1+15]) and not isColored(pixelList[bottom2+15]) and\
          not isColored(pixelList[bottom3+15]) and not isColored(pixelList[bottom4+15]):
        (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
        movedown(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)
    return (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)



##graphic#######################################################################


win = GraphWin('',400,350)
win.setBackground("black")


def graphic_key(win):
    # only pixels
    pixelList = []
    for i in range(31):
        for j in range(15):
            pixel = Rectangle(Point(125+10*j,10+10*i),Point(135+10*j, 20+10*i))
            pixelList.append(pixel)

    for pixel in pixelList[:450]:
        pixel.setOutline("blue")

    for pixel in pixelList:
        pixel.draw(win)

    for i in range(16):
        sparepixel = Rectangle(Point(390,i*10),Point(400,i*10+10))
        pixelList.append(sparepixel)

    for pixel in pixelList[450:465]:
        pixel.setFill('black')

    bottomline = Line(Point(125,310),Point(275,310))
    bottomline.setOutline("blue")
    bottomline.draw(win)

    return pixelList


def graphic_button(win):
    # buttons
    moverightbutton = draw_Rectangle(Point(335,235),Point(375,255),win,Fill='green')
    moveleftbutton = draw_Rectangle(Point(225,235),Point(265,255),win,Fill='green')
    turnbutton = draw_Circle(Point(300,245),25,win,Fill='blue')
    reversebutton = draw_Rectangle(Point(270,170),Point(330,210),win,Fill='red')
    settlebutton = draw_Rectangle(Point(290,280),Point(310,320),win,Fill='green')
    buttonList = (moverightbutton,moveleftbutton,turnbutton,reversebutton,settlebutton)

    # texts
    rightvector = write_Text(Point(355,243),"→",win,size=20,color='white')
    righttext = write_Text(Point(355,265),"right",win,face='courier',size=10,color='white')
    leftvector = write_Text(Point(245,243),"←",win,size=20,color='white')
    lefttext = write_Text(Point(245,265),"left",win,face='courier',size=10,color='white')
    turnvector = write_Text(Point(300,245),"↺",win,size=20,color='white')
    turntext = write_Text(Point(300,260),"turn",win,face='courier',size=10,color='white')
    reversevector = write_Text(Point(300,190),"↩",win,size=20,color='white')
    reversetext = write_Text(Point(300,200),"reverse",win,face='courier',size=10,color='white')
    settlevector = write_Text(Point(300,300),"↓",win,size=20,color='white')
    settletext = write_Text(Point(300,330),"settle",win,face='courier',size=10,color='white')
    
    # pixels
    pixelList = []
    for i in range(31):
        for j in range(15):
            pixel = Rectangle(Point(25+10*j,10+10*i),Point(35+10*j,20+10*i))
            pixelList.append(pixel)

    for pixel in pixelList[:450]:
        pixel.setOutline("blue")

    for pixel in pixelList:
        pixel.draw(win)


    for i in range(16):
        sparepixel = Rectangle(Point(390,i*10),Point(400,i*10+10))
        pixelList.append(sparepixel)

    for pixel in pixelList[450:465]:
        pixel.setFill('black')

    bottomline = Line(Point(25,310),Point(175,310))
    bottomline.setOutline("blue")
    bottomline.draw(win)

    return pixelList, buttonList
    
    

sparenum = 465

##main##########################################################################


starttext = write_Text(Point(200,100),"Select how to operate",win,
                       face='courier',size=20,color='white')
starttext2 = write_Text(Point(200,130),"(Click button)",win,face='courier',size=20,color='white')

operate_with_key_button = draw_Rectangle(Point(50,150),Point(150,220),win,Fill='blue')
operate_with_key_text = write_Text(operate_with_key_button.getCenter(),"Key",win,face='courier',size=15,color='white')

operate_with_button_button = draw_Rectangle(Point(250,150),Point(350,220),win,Fill='red')
operate_with_button_text = write_Text(operate_with_button_button.getCenter(),"Button",win,face='courier',size=15,color='white')

while True:   # wait for selection
    click = win.getMouse()
    if isInside_rect(click,operate_with_key_button):
        starttext.undraw()
        starttext2.undraw()
        operate_with_key_button.undraw()
        operate_with_key_text.undraw()
        operate_with_button_button.undraw()
        operate_with_button_text.undraw()
        
        pixelList = graphic_key(win)
        operating_way = 'key'
        break
    elif isInside_rect(click,operate_with_button_button):
        starttext.undraw()
        starttext2.undraw()
        operate_with_key_button.undraw()
        operate_with_key_text.undraw()
        operate_with_button_button.undraw()
        operate_with_button_text.undraw()
        
        pixelList, \
        (moverightbutton,moveleftbutton,turnbutton,reversebutton,settlebutton)\
        = graphic_button(win)
        operating_way = 'button'
        break


blockList = ['type1','type2','type3','type4','type5']
colorList = ["crimson","skyblue","yellow","lightgreen","silver"]
while get_toprow(pixelList) >= 100:
    toprow = get_toprow(pixelList)
    blocktype = blockList[random.randrange(5)]
    color = colorList[random.randrange(5)]
    if blocktype == 'type1':
        (b1,b2,b3,b4) = (6,7,8,22)
        (right,left,bottom1,bottom2,bottom3,bottom4) = \
        (b3,b1,b1,b3,b4,sparenum)
        (turncount,reversecount) = (0,0)
        pixelList[b1].setFill(color)
        pixelList[b2].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
    elif blocktype == 'type2':
        (b1,b2,b3,b4) = (21,22,23,24)
        (right,left,bottom1,bottom2,bottom3,bottom4) = (b4,b1,b1,b2,b3,b4)
        (turncount,reversecount) = (0,0)
        pixelList[b1].setFill(color)
        pixelList[b2].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
    elif blocktype == 'type3':
        (b1,b2,b3,b4) = (21,22,7,8)
        (right,left,bottom1,bottom2,bottom3,bottom4) = \
        (b4,b1,b1,b2,sparenum,b4)
        (turncount,reversecount) = (0,0)
        pixelList[b1].setFill(color)
        pixelList[b2].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
    elif blocktype == 'type4':
        (b1,b2,b3,b4) = (21,22,23,38)
        (right,left,bottom1,bottom2,bottom3,bottom4) = \
        (b3,b1,b1,b2,sparenum,b4)
        (turncount,reversecount) = (0,0)
        pixelList[b1].setFill(color)
        pixelList[b2].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
    elif blocktype == 'type5':
        (b1,b2,b3,b4) = (7,8,22,23)
        (right,left,bottom1,bottom2,bottom3,bottom4) = \
        (b2,b1,b3,b4,sparenum,sparenum)
        (turncount,reversecount) = (0,0)
        pixelList[b1].setFill(color)
        pixelList[b2].setFill(color)
        pixelList[b3].setFill(color)
        pixelList[b4].setFill(color)
    if operating_way == 'key':
        while not isColored(pixelList[bottom1+15]) and not isColored(pixelList[bottom2+15]) and\
              not isColored(pixelList[bottom3+15]) and not isColored(pixelList[bottom4+15]):
            for rep in range(5):
                key = win.checkKey()
                if key == 'Right':
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
                    moveright(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,toprow)
                elif key == 'Left':
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
                    moveleft(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,toprow)
                elif key == 't':
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount) = \
                    turn(blocktype,b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount,toprow)
                elif key == 'r':
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount) = \
                    reverse_block(blocktype,b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount,toprow)
                elif key == 'Down':
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
                    settle(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)
                    break
                time.sleep(0.1)
            if not isColored(pixelList[bottom1+15]) and not isColored(pixelList[bottom2+15]) and\
               not isColored(pixelList[bottom3+15]) and not isColored(pixelList[bottom4+15]):
                (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
                movedown(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)
    else:
        while not isColored(pixelList[bottom1+15]) and not isColored(pixelList[bottom2+15]) and\
              not isColored(pixelList[bottom3+15]) and not isColored(pixelList[bottom4+15]):
            for rep in range(5):
                checkpt = win.checkMouse()
                if checkpt != None:
                    pt = checkpt
                else:
                    pt = Point(1,1)
                if isInside_rect(pt,moverightbutton):
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
                    moveright(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,toprow)
                elif isInside_rect(pt,moveleftbutton):
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
                    moveleft(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,toprow)
                elif isInside_rect(pt,turnbutton):
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount) = \
                    turn(blocktype,b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount,toprow)
                elif isInside_oval(pt,reversebutton):
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount) = \
                    reverse_block(blocktype,b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4,turncount,reversecount,toprow)
                elif isInside_rect(pt,settlebutton):
                    (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
                    settle(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)
                time.sleep(0.1)
            if not isColored(pixelList[bottom1+15]) and not isColored(pixelList[bottom2+15]) and\
               not isColored(pixelList[bottom3+15]) and not isColored(pixelList[bottom4+15]):
                (b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4) = \
                movedown(b1,b2,b3,b4,right,left,bottom1,bottom2,bottom3,bottom4)


    for row in range(30):
        counter = 0
        for pixel in pixelList[row*15:row*15+15]:
            if isColored(pixel):
                counter += 1
        if counter == 15:
            for row2 in range(row,0,-1):
                for pixelnum in range(row2*15,row2*15+15):
                    pixelList[pixelnum].setFill(getFillColor(pixelList[pixelnum-15]))



gameover = Text(Point(200,125),"Game  Over...")
gameover.setSize(36)
gameover.setTextColor('red')
end = Text(Point(200,200),"Click anywhere to quit")
end.setSize(20)
end.setTextColor('white')
gameover.draw(win)
end.draw(win)

win.getMouse()
win.close()
