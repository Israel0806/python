import pygame
import time
import random


pygame.init()

##pygame.mixer.pre_init() 
##pygame.mixer.init()
##pygame.mixer.init()


negro=(0,0,0)
blanco=(255,255,255)
rojo=(200,0,0)
verde=(0,200,0)
rojo_claro=(255,0,0)
verde_claro=(0,255,0)

ancho=800
altura=700

gameDisplay=pygame.display.set_mode((ancho,altura))
pygame.display.set_caption("Meme Breakout")
clock=pygame.time.Clock()

##opciones para imagenes

ballImg1_1=pygame.image.load("Bola2.png")
ballImg2=pygame.image.load("Bolalvl2.png")
ballImg3=pygame.image.load("Bola3.png")

ballpowerup=pygame.image.load("Powerup.png")

brickBlanco=pygame.image.load("LadrilloBlanco.png")
brickAzul=pygame.image.load("LadrilloAzul.png")
brickRojo=pygame.image.load("LadrilloRojo.png")


barImg=pygame.image.load("Barra.png")
ballImg=pygame.image.load("Bola2def.png")
brickImg=pygame.image.load("Ladrillo2.png")
bar2Img=pygame.image.load("BarraGrande2.png")
fondoImg=pygame.image.load("FondoImg.jpg")
##fondoIntroImg=pygame.image.load("Sample 3 800X700.png")
fondoIntroImg2=pygame.image.load("FondoImg2.jpg")
laserImg=pygame.image.load("Laser.png")
bar3Img=pygame.image.load("BarraPequenia.png")


##pygame.mixer.music.load("Best Future House Music Mix 2016.mp3")
hey=pygame.mixer.Sound("4382__noisecollector__pongblipd-5.wav") 


Barra=False
Barra2=False
pause=False
powerup=[False]
laser=False
score=0

tiempo=0
cont=3
b=132
y3_change=3
radio=12

y3=[]
x3=[]

bolas=[[375,633]]

##l=[[25,63],[25,96],[25,129],[25,162],[25,195],[25,228],[108,63],[108,96],[108,129],[108,162],[108,195],
##   [108,228],[191,63],[191,96],[191,129],[191,162],[191,195],[191,228],[274,63],[274,96],[274,129],[274,162],
##   [274,195],[274,228],[357,63],[357,96],[357,129],[357,162],[357,195],[357,228],[440,63],[440,96],[440,129],
##   [440,162],[440,195],[440,228],[523,63],[523,96],[523,129],[523,162],[523,195],[523,228],[606,63],[606,96],
##   [606,129],[606,162],[606,195],[606,228],[689,63],[689,96],[689,129],[689,162],[689,195],[689,228]]

l=[[10,40,1],[10,75,1],[10,110,1],[10,145,1],[10,180,1],[10,215,1],
   [76,40,1],[76,75,1],[76,110,1],[76,145,1],[76,180,1],[76,215,1],
   [142,40,1],[142,75,1],[142,110,1],[142,145,1],[142,180,1],[142,215,1],
   [207,40,1],[207,75,1],[207,110,1],[207,145,1],[207,180,1],[207,215,1],
   [274,40,1],[274,75,1],[274,110,1],[274,145,1],[274,180,1],[274,215,1],
   [340,40,1],[340,75,1],[340,110,1],[340,145,1],[340,180,1],[340,215,1],
   [406,40,1],[406,75,1],[406,110,1],[406,145,1],[406,180,1],[406,215,1],
   [472,40,1],[472,75,1],[472,110,1],[472,145,1],[472,180,1],[472,215,1],
   [538,40,1],[538,75,1],[538,110,1],[538,145,1],[538,180,1],[538,215,1],
   [604,40,1],[604,75,1],[604,110,1],[604,145,1],[604,180,1],[604,215,1],
   [670,40,1],[670,75,1],[670,110,1],[670,145,1],[670,180,1],[670,215,1],
   [736,40,1],[736,75,1],[736,110,1],[736,145,1],[736,180,1],[736,215,1]]




l2=[                                       [238,40,2],[302,40,2],                      [430,40,2],[494,40,2],
                                        [212,75,2],[276,75,1],[340,75,2],           [404,75,2],[468,75,1],[532,75,2],
                            [148,110,2],[212,110,1],[276,110,1],[340,110,2],[404,110,2],[468,110,1],[532,110,1],[596,110,2],
                            [148,145,2],[212,145,1],[276,145,1],[340,145,1],[404,145,1],[468,145,1],[532,145,1],[596,145,2],
                            [148,180,2],[212,180,1],[276,180,1],[340,180,1],[404,180,1],[468,180,1],[532,180,1],[596,180,2],
                            [148,215,2],[212,215,1],[276,215,1],[340,215,1],[404,215,1],[468,215,1],[532,215,1],[596,215,2],
                                        [212,250,2],[276,250,1],[340,250,1],[404,250,1],[468,250,1],[532,250,2],
                                                    [276,285,2],[340,285,1],[404,285,1],[468,285,2],
                                                                [340,320,2],[404,320,2],
                                                                      [366,355,2]]

l3=[                    [168,45,2],                                               [552,45,2],
                                [232,75,2],                               [488,75,2],
                        [168,104,2],[232,104,2],[296,104,2],[360,104,2],[424,104,2],[488,104,2],[552,104,2],
                [104,136,2],[168,136,2],[232,136,2],[296,136,2],[360,136,2],[424,136,2],[488,136,2],[552,136,2],[616,136,2],
                [104,166,2],[168,166,2],[232,166,2],[296,166,2],[360,166,2],[424,166,2],[488,166,2],[552,166,2],[616,166,2],
                [104,196,2],[168,196,2],[232,196,2],[296,196,2],[360,196,2],[424,196,2],[488,196,2],[552,196,2],[616,196,2],
        [40,226,2],[104,226,2],[168,226,2],[232,226,2],[296,226,2],[360,226,2],[424,226,2],[488,226,2],[552,226,2],[616,226,2],[680,226,2],
        [40,256,2],       [168,256,2],[232,256,2],[296,256,2],[360,256,2],[424,256,2],[488,256,2],[552,256,2],              [680,256,2],
        [40,286,2],       [168,286,2],                                                          [552,286,2]                 ,[680,286,2],
        [40,316,2],        [168,316,2],                                                         [552,316,2]                 ,[680,316,3],
                                    [232,346,2],                                        [488,346,2],
                                    [232,376,2],[296,376,2],                 [424,376,2],[488,376,2]


]

##l2= [[25,63],[25,96],[25,129],[25,162],[25,195],[25,228],
##    [108,63],[108,96],[108,129],[108,162],[108,195],[108,228],
##    [191,63],[191,96],[191,129],[191,162],[191,195],[191,228],
##    [274,63],[274,96],[274,129],[274,162],[274,195],[274,228],
##    [357,63],[357,96],[357,129],[357,162],[357,195],[357,228],
##    [440,63],[440,96],[440,129],[440,162],[440,195],[440,228],
##    [523,63],[523,96],[523,129],[523,162],[523,195],[523,228],
##    [606,63],[606,96],[606,129],[606,162],[606,195],[606,228],
##    [689,63],[689,96],[689,129],[689,162],[689,195],[689,228]]

def unpause():
    global pause
##    pygame.mixer.music.unpause()
    pause=False

def paused():
##    pygame.mixer.music,pause()
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurface,TextRect=text_objects("Paused",largeText)
    TextRect.center=((ancho/2),(altura/2))
    gameDisplay.blit(TextSurface,TextRect)
     
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                pygame.quit()
                quit()
        #gameDisplay.fill(blanco)
        

        button("Continue",200,450,100,50,verde,verde_claro,"play")
        button("QUIT",500,450,100,50,rojo,rojo_claro,"quit",)                
        pygame.display.update()
        clock.tick(60)

def gameOver():
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurface,TextRect=text_objects("Game Over",largeText)
    TextRect.center=((ancho/2),(altura/2))
    gameDisplay.blit(TextSurface,TextRect)
    l2= [                                       [238,40,2],[302,40,2],                      [430,40,2],[494,40,2],
                                        [212,75,2],[276,75,1],[340,75,2],           [404,75,2],[468,75,1],[532,75,2],
                            [148,110,2],[212,110,1],[276,110,1],[340,110,2],[404,110,2],[468,110,1],[532,110,1],[596,110,2],
                            [148,145,2],[212,145,1],[276,145,1],[340,145,1],[404,145,1],[468,145,1],[532,145,1],[596,145,2],
                            [148,180,2],[212,180,1],[276,180,1],[340,180,1],[404,180,1],[468,180,1],[532,180,1],[596,180,2],
                            [148,215,2],[212,215,1],[276,215,1],[340,215,1],[404,215,1],[468,215,1],[532,215,1],[596,215,2],
                                        [212,250,2],[276,250,1],[340,250,1],[404,250,1],[468,250,1],[532,250,2],
                                                    [276,285,2],[340,285,1],[404,285,1],[468,285,2],
                                                                [340,320,2],[404,320,2],
                                                                      [366,355,2]]
    cont=3
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(blanco)
                

        button("Play Again",200,450,100,50,verde,verde_claro,"play")
        button("QUIT",500,450,100,50,rojo,rojo_claro,"quit",)                
        pygame.display.update()
        clock.tick(60)

def gameOver2():
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurface,TextRect=text_objects("Game Over",largeText)
    TextRect.center=((ancho/2),(altura/2))
    gameDisplay.blit(TextSurface,TextRect)
    l=[[10,40,1],[10,75,1],[10,110,1],[10,145,1],[10,180,1],[10,215,1],
       [76,40,1],[76,75,1],[76,110,1],[76,145,1],[76,180,1],[76,215,1],
       [142,40,1],[142,75,1],[142,110,1],[142,145,1],[142,180,1],[142,215,1],
       [207,40,1],[207,75,1],[207,110,1],[207,145,1],[207,180,1],[207,215,1],
       [274,40,1],[274,75,1],[274,110,1],[274,145,1],[274,180,1],[274,215,1],
       [340,40,1],[340,75,1],[340,110,1],[340,145,1],[340,180,1],[340,215,1],
       [406,40,1],[406,75,1],[406,110,1],[406,145,1],[406,180,1],[406,215,1],
       [472,40,1],[472,75,1],[472,110,1],[472,145,1],[472,180,1],[472,215,1],
       [538,40,1],[538,75,1],[538,110,1],[538,145,1],[538,180,1],[538,215,1],
       [604,40,1],[604,75,1],[604,110,1],[604,145,1],[604,180,1],[604,215,1],
       [670,40,1],[670,75,1],[670,110,1],[670,145,1],[670,180,1],[670,215,1],
       [736,40,1],[736,75,1],[736,110,1],[736,145,1],[736,180,1],[736,215,1]]
    cont=3
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(blanco)
                

        button("Play Again",200,450,100,50,verde,verde_claro,"play")
        button("QUIT",500,450,100,50,rojo,rojo_claro,"quit",)                
        pygame.display.update()
        clock.tick(60)
        

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":

                nivel1()

            elif action=="quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    smallText=pygame.font.Font("freesansbold.ttf",17)
    textSurf,textRect=text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
    
def text_objects(texto,font):
    textSurface=font.render(texto,True,negro)
    return textSurface,textSurface.get_rect()

def message_display(texto):
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurface,TextRect=text_objects(texto,largeText)
    TextRect.center=((ancho/2),(altura/2))
    gameDisplay.blit(TextSurface,TextRect)
    pygame.display.update()
    time.sleep(2)
    nivel1()

def message_display2(texto):
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurface,TextRect=text_objects(texto,largeText)
    TextRect.center=((ancho/2),(altura/2))
    gameDisplay.blit(TextSurface,TextRect)
    pygame.display.update()
    time.sleep(2)
    nivel2()

def message_display3(texto):
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurface,TextRect=text_objects(texto,largeText)
    TextRect.center=((ancho/2),(altura/2))
    gameDisplay.blit(TextSurface,TextRect)
    pygame.display.update()
    time.sleep(2)
    nivel2()    


def message_display4(texto):
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurface,TextRect=text_objects(texto,largeText)
    TextRect.center=((ancho/2),(altura/2))
    gameDisplay.blit(TextSurface,TextRect)
    pygame.display.update()
    time.sleep(2)
    nivel3() 


##def message_display5(texto):
##    largeText=pygame.font.Font("freesansbold.ttf",115)
##    TextSurface,TextRect=text_objects(texto,largeText)
##    TextRect.center=((ancho/2),(altura/2))
##    gameDisplay.blit(TextSurface,TextRect)
##    pygame.display.update()
##    time.sleep(2)
##    nivel3() 

def score1():
    global score
    font=pygame.font.SysFont(None,25)
    text=font.render(" Score: "+str(score),True,blanco)
    gameDisplay.blit(text ,(700,0))

    
def vidas(cont,bolas):
    pos=20
    if len(bolas)==1:
        if bolas[0][1]>665:
            cont=cont-1
        font=pygame.font.SysFont(None,25)
##        text=font.render(" Bolas: "+str(cont),True,negro)
        text=font.render(" Bolas: ",True,negro)
        gameDisplay.blit(text ,(0,0))
        for u in range(0,cont):
            gameDisplay.blit(ballImg2,(pos,5))
            pos+=35

            
def ladrillo(l):

##l=[[10,40,1],[10,75,1],[10,110,1],[10,145,1],[10,180,1],[10,215,1],
##   [76,40,1],[76,75,1],[76,110,1],[76,145,1],[76,180,1],[76,215,1],
##   [142,40,1],[142,75,1],[142,110,1],[142,145,1],[142,180,1],[142,215,1],
##   [207,40,1],[207,75,1],[207,110,1],[207,145,1],[207,180,1],[207,215,1],
##   [274,40,1],[274,75,1],[274,110,1],[274,145,1],[274,180,1],[274,215,1],
##   [340,40,1],[340,75,1],[340,110,1],[340,145,1],[340,180,1],[340,215,1],
##   [406,40,1],[406,75,1],[406,110,1],[406,145,1],[406,180,1],[406,215,1],
##   [472,40,1],[472,75,1],[472,110,1],[472,145,1],[472,180,1],[472,215,1],
##   [538,40,1],[538,75,1],[538,110,1],[538,145,1],[538,180,1],[538,215,1],
##   [604,40,1],[604,75,1],[604,110,1],[604,145,1],[604,180,1],[604,215,1],
##   [670,40,1],[670,75,1],[670,110,1],[670,145,1],[670,180,1],[670,215,1],
##   [736,40,1],[736,75,1],[736,110,1],[736,145,1],[736,180,1],[736,215,1]]
    
    for x in l:
        if x[0]==10 or x[0]==76 or x[0]==142 or x[0]==207: 
            gameDisplay.blit(brickAzul,(x[0],x[1]))
            
        if x[0]==274 or x[0]==340 or x[0]==406 or x[0]==472:
            gameDisplay.blit(brickRojo,(x[0],x[1]))
            
        if x[0]==538 or x[0]==604 or x[0]==670 or x[0]==736:
            gameDisplay.blit(brickBlanco,(x[0],x[1]))        
            
def ladrillo2(l):
    for e in l:
        for x in l:
            if (x[0]==238 or x[0]==302 or x[0]==430 or x[0]==494)and x[1]==40:
                if e[2]==2:
                    gameDisplay.blit(brickAzul,(x[0],x[1]))               
            elif (x[0]==212 or x[0]==532 or x[0]==340 or x[0]==404)and x[1]==75:
                    gameDisplay.blit(brickAzul,(x[0],x[1]))               
            elif (x[0]==148 or x[0]==596)and (x[1]==110 or x[1]==145 or x[1]==180 or x[1]==215 ):
                    gameDisplay.blit(brickAzul,(x[0],x[1]))               
            elif (x[0]==212 or x[0]==532)and x[1]==250:
                    gameDisplay.blit(brickAzul,(x[0],x[1]))               
            elif (x[0]==276 or x[0]==468)and x[1]==285:
                gameDisplay.blit(brickAzul,(x[0],x[1]))               
            elif (x[0]==340 or x[0]==404)and x[1]==320:
                    gameDisplay.blit(brickAzul,(x[0],x[1]))               
            elif x[0]==366 and x[1]==355:
                gameDisplay.blit(brickAzul,(x[0],x[1]))               
            else:
                gameDisplay.blit(brickRojo,(x[0],x[1]))

def ladrillo3(l):
    for x in l:
        if x[0]==232 and (x[1]==136 or x[1]==166):
            gameDisplay.blit(brickRojo,(x[0],x[1]))               
        elif x[0]==488 and (x[1]==136 or x[1]==166):
            gameDisplay.blit(brickRojo,(x[0],x[1]))
        elif x[0]==296 and x[1]==376:
            gameDisplay.blit(brickImg,(x[0],x[1]))
        elif x[0]==424 and x[1]==376:
            gameDisplay.blit(brickImg,(x[0],x[1]))
        else:
            gameDisplay.blit(brickAzul,(x[0],x[1]))

def powerUp(i):
    global x3
    global y3
    gameDisplay.blit(ballpowerup,(x3[i],y3[i]))   


##def powerupBarra(cor_x):
##    pygame.draw.rect(gameDisplay,negro,(cor_x,650,233,20))
##    gameDisplay.blit(bar2Img,(cor_x,650))

##def powerupBolas(speed,bolas):
##    bolas.append([375,633])
##    speed.append([5,-5])


##def colision(bolas,speed,l):
##    global powerup
##    global x3
##    global y3
##    global b
##    global radio
##    global score
####    ly=[63, 96, 129, 162, 195, 228]
####    lx=[25, 108, 191, 274, 357, 440, 523, 606, 689]
##    ee=0
##    r=0
##    ii=0
####    while e<len(l):
##    for e in l:
####        for ii in bolas:
##        for ii in range(0,len(bolas)):
####        while i<len(bolas):
####            print bolas
####            if l[e][0]+91>=bolas[ii][0]>=l[e][0]-5:
####                if l[e][1]+40>=bolas[ii][1]>=l[e][1]-5:
##
####            if l[e][1]+40>=bolas[ii][1] and bolas[ii][1]>=l[e][1]:
##            if e[1]+32+radio>=bolas[ii][1]>=e[1]-radio:
##
####                    print ("e",e)
####                    print ("ii",ii)
####                    print ("l[e]",l[e][1]+40)
####                    print ("bolas[ii]",bolas[ii][1])
##    ##                if l[e][0]+88>=bolas[ii][0]>=l[e][0]:
##                    
##                if e[0]+65-radio>=bolas[ii][0]>=e[0]+radio:
##                    score+=10
##
####                    pygame.mixer.Sound.set_volume(1)
####                    time.
####                    pygame.mixer.Sound.play(hey)
##                    hey.play()
####                    pygame.mixer.Sound.set_volume(1.0)
####                    pygame.mixer.Sound.play(hey)
##                    
####                    print "l",l[e][0]
####                    print "bolas",ii," ",bolas[ii][0]
##                    
##                    speed[ii][1]=-speed[ii][1]
##                    
####                    if l[e][0]==689 and l[e][1]==228:
####                    print powerup
##                    
##                    a=random.random()
##                    if a<0.1:
##                        b=random.randrange(0,4)
####                        print a
##                        print (b)
##                        x3.append(e[0]+40)
##                        y3.append(e[1])
##                        powerup.append(True)
##        ##                powerUp()
##                    l.pop(ee)
####                        e=len(l)+1
##
##                elif (e[0]+65+radio>=bolas[ii][0]>=e[0]+83-radio+3) or (e[0]+radio>=bolas[ii][0]>=e[0]-radio+3):
####                    pygame.mixer.Sound.set_volume(1.0)
####                    pygame.mixer.Sound.play(hey)
##                    score+=10
##
##                    hey.play()
####                    print "l",l[e][0]
####                    print "bolas",ii," ",bolas[ii][0]
##                    
##                    speed[ii][0]=-speed[ii][0]
##                    
####                    if l[e][0]==689 and l[e][1]==228:
####                    print powerup
##                    
##                    a=random.random()
##                    if a<0.1:
##                        b=random.randrange(0,4)
####                        print a
##                        print (b)
##                        x3.append(e[0]+40)
##                        y3.append(e[1])
##                        powerup.append(True)
##        ##                powerUp()
##                        
##                    l.pop(ee)
##
##        ee+=1


def colision(bolas,speed,l):
    global powerup
    global x3
    global y3
    global b
    global radio
    global score
##    ly=[63, 96, 129, 162, 195, 228]
##    lx=[25, 108, 191, 274, 357, 440, 523, 606, 689]
    ee=0
    r=0
    ii=0

    for e in l:
        for ii in range(0,len(bolas)):
            if e[1]+30>=bolas[ii][1]>=e[1]:
                if e[0]+65-radio>=bolas[ii][0]>=e[0]+radio:
                    if l[ee][2]!=3:
                        l[ee][2]-=1
                    hey.play()
                    speed[ii][1]=-speed[ii][1]
                    a=random.random()
                    if a<0.1:
                        b=random.randrange(0,4)
                        x3.append(e[0]+40)
                        y3.append(e[1])
                        powerup.append(True)
                    if l[ee][2]==0:
                        score+=10
                        l.pop(ee)
                elif (e[0]+65+radio>=bolas[ii][0]>=e[0]+83-radio+3) or (e[0]+radio>=bolas[ii][0]>=e[0]-radio+3):
                    print ("1  ",l[ee][2])
                    l[ee][2]-=1
                    print ("2  ",l[ee][2])
                    hey.play()
                    speed[ii][0]=-speed[ii][0]
                    a=random.random()
                    if a<0.1:
                        b=random.randrange(0,4)
                        x3.append(e[0]+40)
                        y3.append(e[1])
                        powerup.append(True)
                    if l[ee][2]==0:
                        score+=10
                        l.pop(ee)
        ee+=1
        
def bola(bola):
    for i in range(0,len(bolas)):
##        pygame.draw.circle(gameDisplay,verde,(bolas[i][0],bolas[i][1]),12)
##        gameDisplay.blit(ballImg,(bolas[i][0]-12,bolas[i][1]-15))
        gameDisplay.blit(ballImg1_1,(bolas[i][0]-12,bolas[i][1]-15))        

def bola2(bola):
    for i in range(0,len(bolas)):
##        pygame.draw.circle(gameDisplay,verde,(bolas[i][0],bolas[i][1]),12)
##        gameDisplay.blit(ballImg,(bolas[i][0]-12,bolas[i][1]-15))
        gameDisplay.blit(ballImg3,(bolas[i][0]-12,bolas[i][1]-15))

def bola3(bola):
    for i in range(0,len(bolas)):
        gameDisplay.blit(ballImg,(bolas[i][0]-12,bolas[i][1]-15))
 
def barra(cor_x):
    if Barra2==True:
        gameDisplay.blit(bar3Img,(cor_x,650))
    elif Barra==False:
##        pygame.draw.rect(gameDisplay,negro,(cor_x,650,150,20))
        gameDisplay.blit(barImg,(cor_x,650))
    elif Barra==True:
##        pygame.draw.rect(gameDisplay,negro,(cor_x,650,233,20))
        gameDisplay.blit(bar2Img,(cor_x,650))

        
def intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
##        gameDisplay.blit(fondoIntroImg,(0,0))
        gameDisplay.blit(fondoIntroImg2,(0,0))
##        largeText=pygame.font.Font("freesansbold.ttf",90)
##        TextSurface,TextRect=text_objects("Meme Breakout",largeText)
##        TextRect.center=((ancho/2),(altura/2)-30)
##        gameDisplay.blit(TextSurface,TextRect)
        button("PLAY",200,450,100,50,verde,verde_claro,"play")
        button("QUIT",500,450,100,50,rojo,rojo_claro,"quit",)                
        pygame.display.update()
        clock.tick(60)

def nivel2():
##    pygame.mixer.music.play(-1)
    global pause
    global cont
    global speed2
    global x3
    global y3
    global Barra
    global Barra2
    global tiempo
    global bolas
    global lasers
    global l2
    global laser
    global powerup
    global b
    global radio
    global score
    tiempo=0
    tiempo2=0
    tiempo3=0
    temp=False
    temp2=False
    temp3=False
    cont2=0
    x_change=0
##    y3_change=0
    lasers=[515,515]
    cor_x=300
##    x2=375
##    y2=633
    speed=[[5,-5]]
    quit=False
    while not quit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                pygame.mixer.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        gameDisplay.blit(fondoImg,(0,0))

        
        
        
        if Barra2==True:
            if cor_x>ancho-100:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0
        elif Barra==False:
            if cor_x>ancho-150:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0
        elif Barra==True:
            if cor_x>ancho-250:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0


        cor_x+=x_change
        bola2(bolas)
        barra(cor_x)
        vidas(cont,bolas)
        colision(bolas,speed,l2)
        ladrillo2(l2)
        score1()
        
        ##codigo bola
                         
        i=0
        while i<len(bolas):
##        for i in range(0,len(bolas)):
            bolas[i][0]+=speed[i][0]
            bolas[i][1]+=speed[i][1]
            if bolas[i][0]<radio or bolas[i][0]>ancho-radio:
                speed[i][0]=-speed[i][0]
                bolas[i][0]+=speed[i][0]
            if bolas[i][1]<radio or bolas[i][1]>670:
                speed[i][1]=-speed[i][1]
                bolas[i][1]+=speed[i][1]
            
            
    ##      codigo bola toca barra
##            print speed
                
            if Barra2==True:
                if bolas[i][1]==638:
                    if cor_x-5<=bolas[i][0]<=cor_x+10:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+10<bolas[i][0]<=cor_x+20:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+20<bolas[i][0]<=cor_x+30:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+30<bolas[i][0]<=cor_x+40:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+40<bolas[i][0]<=cor_x+50:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+50<bolas[i][0]<=cor_x+60:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+60<bolas[i][0]<=cor_x+70:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+70<bolas[i][0]<=cor_x+80:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                    if cor_x+80<bolas[i][0]<=cor_x+90:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+90<bolas[i][0]<=cor_x+105:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                        
            elif Barra==False:
                if  bolas[i][1]==638:
##                    cor_x+155>=bolas[i][0]>=cor_x-5 
                    if cor_x-5<=bolas[i][0]<=cor_x+15:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+15<bolas[i][0]<=cor_x+30:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+30<bolas[i][0]<=cor_x+45:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+45<bolas[i][0]<=cor_x+60:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+60<bolas[i][0]<=cor_x+75:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+75<bolas[i][0]<=cor_x+90:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+90<bolas[i][0]<=cor_x+105:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+105<bolas[i][0]<=cor_x+120:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+120<bolas[i][0]<=cor_x+135:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+135<bolas[i][0]<=cor_x+155:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
            elif Barra==True:
                if  bolas[i][1]==638: 
                    if cor_x-5<=bolas[i][0]<=cor_x+25:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+25<bolas[i][0]<=cor_x+50:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+50<bolas[i][0]<=cor_x+75:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+75<bolas[i][0]<=cor_x+100:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+100<bolas[i][0]<=cor_x+125:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+125<bolas[i][0]<=cor_x+150:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                    if cor_x+150<bolas[i][0]<=cor_x+175:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+175<bolas[i][0]<=cor_x+200:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+200<bolas[i][0]<=cor_x+225:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+225<bolas[i][0]<=cor_x+243:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()

                                  
    ##        x=0
    ##        pos_x=25
    ##        pos_y=30
    ##        print powerup



##            condicion powerupImg
                    
            j=0
            while(j<len(y3)):
##            for j in range(0,len(y3)):  
                if powerup[j]==True:
##                    print "x3",len(x3)
##                    print "y3",len(y3)
##                    print "powerup",j," ",powerup[j]
                    global y3_change
                    y3[j]+=y3_change
                    powerUp(j)
                if y3[j]>638:
                    powerup[j]=False
                    y3.pop(j)
                    x3.pop(j)
                    powerup.pop(j)
                j+=1
##            y3_change=0


                
    ##      powerups
                
            if temp==True:
                tiempo+=30

            if temp3==True:
                tiempo3+=30
                
##            codigo laser part2
                
            if temp2==True:
                tiempo2+=30
                
            if laser==True:
                laser_pos=0
                lasers_change=-8
##                pygame.draw.rect(gameDisplay,verde,(xx,lasers[0],20,150))
                gameDisplay.blit(laserImg,(xx,lasers[0]))
##                pygame.draw.rect(gameDisplay,verde,(xx+150,lasers[1],20,150))
                if Barra2==True:
                    gameDisplay.blit(laserImg,(xx+96,lasers[1]))
                elif Barra==False:
                    gameDisplay.blit(laserImg,(xx+150,lasers[1]))
                elif Barra==True:
                    gameDisplay.blit(laserImg,(xx+230,lasers[1]))
                lasers[0]+=lasers_change
                lasers[1]+=lasers_change
                temp2=True
##                print "laser1",laser
                for ee in l2:
##                while ee<len(l):
##                    if l[ee][0]+85>=xx>=l[ee][0]-5 and l[ee][1]+40>=lasers[0]>=l[ee][1]-5:
                    if ee[0]+85>=xx>=ee[0]-5:
                        if ee[1]+40>=lasers[0]>=ee[1]-5:
                            lasers[0]=50000
                            l2.pop(laser_pos)
                            score+=20
##                    if l[ee][0]+85>=xx+150>=l[ee][0]-5 and l[ee][1]+40>=lasers[1]>=l[ee][1]-5:
                    if ee[1]+40>=lasers[1]>=ee[1]-5:
                        if ee[0]+85>=xx+150>=ee[0]-5:
                            lasers[1]=50000
                            l2.pop(laser_pos)
                            score+=20
                    laser_pos+=1
            lasers_change=0

##            tiempo laser
            
            if tiempo2>2000:
                cont2+=1
                tiempo2=0
                xx=cor_x
                lasers[0]=515
                lasers[1]=515
            if cont2>6:
                laser=False
                tiempo2=0
                cont2=0
##                lasers[0]=515
##                lasers[1]=515
##                print "laser0",laser

                
##          tiempo barra
                
            if tiempo>10000:
                Barra=False
                tiempo=0
                temp=False


            if tiempo3>10000:
                Barra2=False
                tiempo3=0
                temp3=False
                
##          powerupcondicion
                
##            print "y3",y3
##            print "cor_x",cor_x," ",cor_x+150
##            print "b",b
                
            j=0
            while j<len(x3):

##            for j in range(0,len(y3)):
##                print y3[j]
                if cor_x<=x3[j]<=cor_x+150 and 630<=y3[j]<=636:
##                    print "j", j
                    x3.pop(j)
                    y3.pop(j)
                    powerup.pop(j)
    
##                    print "repoio"
    ##              barrapowerup
                    if b==0:
                        tiempo=0
                        Barra=True
                        temp=True
                        Barra2=False
    ##            bolapowerup
                    if b==1: 
                        bolas.append([375,633])
                        speed.append([5,-5])
    ##            laserpowerup
                    if b==2:
                        tiempo2=0
                        laser=True
                        lasers[0]=515
                        lasers[1]=515
                        xx=cor_x
##                barrapequeñapowerup
                    if b==3:
                        tiempo3=0
                        Barra=False
                        Barra2=True
                        temp3=True
                            
                j+=1


##      codigo bola perdida
##            print (bolas[0][1]) 
            if len(bolas)==1:    
                if bolas[0][1]>665:
##                    bolas.pop(i)
                    cont-=1
##                    bolas=[[375,633]]
                    if cont==0:
                        l=[[10,40,1],[10,75,1],[10,110,1],[10,145,1],[10,180,1],[10,215,1],
                       [76,40,1],[76,75,1],[76,110,1],[76,145,1],[76,180,1],[76,215,1],
                       [142,40,1],[142,75,1],[142,110,1],[142,145,1],[142,180,1],[142,215,1],
                       [207,40,1],[207,75,1],[207,110,1],[207,145,1],[207,180,1],[207,215,1],
                       [274,40,1],[274,75,1],[274,110,1],[274,145,1],[274,180,1],[274,215,1],
                       [340,40,1],[340,75,1],[340,110,1],[340,145,1],[340,180,1],[340,215,1],
                       [406,40,1],[406,75,1],[406,110,1],[406,145,1],[406,180,1],[406,215,1],
                       [472,40,1],[472,75,1],[472,110,1],[472,145,1],[472,180,1],[472,215,1],
                       [538,40,1],[538,75,1],[538,110,1],[538,145,1],[538,180,1],[538,215,1],
                       [604,40,1],[604,75,1],[604,110,1],[604,145,1],[604,180,1],[604,215,1],
                       [670,40,1],[670,75,1],[670,110,1],[670,145,1],[670,180,1],[670,215,1],
                       [736,40,1],[736,75,1],[736,110,1],[736,145,1],[736,180,1],[736,215,1]]
                        cont=3
                        bolas=[[375,633]]
                        speed=[[5,-5]]
                        laser=False
                        Barra=False
                        score=0
                        gameOver()
                    bolas=[[375,633]]
                    speed=[[5,-5]]
                    laser=False
                    Barra=False
                    Barra2=False
                    powerup=[False]
                    y3=[]
                    x3=[]
                    message_display3("-1 bola")
            elif bolas[i][1]>665:
                    bolas.pop(i)
                    speed.pop(i)
##            if bolas[i][1]>665:
##                    bolas.pop(i)
##                    speed.pop(i)
##            if len(bolas)==0:
##                message_display("-1 bola")
                    
            i+=1

            if len(l2)==0:
                bolas=[[375,633]]
                speed=[[5,-5]]
                laser=False
                Barra=False
                Barra2=False
                powerup=[False]
                y3=[]
                x3=[]
                message_display4("Good Job")
                
            pygame.display.update()
            clock.tick(60)

    
def nivel3():
##    pygame.mixer.music.play(-1)
    global pause
    global cont
    global speed2
    global x3
    global y3
    global Barra
    global Barra2
    global tiempo
    global bolas
    global lasers
    global l3
    global laser
    global powerup
    global b
    global radio
    global score
    tiempo=0
    tiempo2=0
    tiempo3=0
    temp=False
    temp2=False
    temp3=False
    cont2=0
    x_change=0
##    y3_change=0
    lasers=[515,515]
    cor_x=300
##    x2=375
##    y2=633
    speed=[[5,-5]]
    quit=False
    while not quit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                pygame.mixer.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        gameDisplay.blit(fondoImg,(0,0))

        
        
        
        if Barra2==True:
            if cor_x>ancho-96:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0
        elif Barra==False:
            if cor_x>ancho-156:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0
        elif Barra==True:
            if cor_x>ancho-236:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0


        cor_x+=x_change
        bola3(bolas)
        barra(cor_x)
        vidas(cont,bolas)
        colision(bolas,speed,l3)
        ladrillo3(l3)
        score1()
        
        ##codigo bola
                         
        i=0
        while i<len(bolas):
##        for i in range(0,len(bolas)):
            bolas[i][0]+=speed[i][0]
            bolas[i][1]+=speed[i][1]
            if bolas[i][0]<radio or bolas[i][0]>ancho-radio:
                speed[i][0]=-speed[i][0]
                bolas[i][0]+=speed[i][0]
            if bolas[i][1]<radio or bolas[i][1]>670:
                speed[i][1]=-speed[i][1]
                bolas[i][1]+=speed[i][1]
            
            
    ##      codigo bola toca barra
##            print speed
                
            if Barra2==True:
                if bolas[i][1]==638:
                    if cor_x-5<=bolas[i][0]<=cor_x+10:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+10<bolas[i][0]<=cor_x+20:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+20<bolas[i][0]<=cor_x+30:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+30<bolas[i][0]<=cor_x+40:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+40<bolas[i][0]<=cor_x+50:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+50<bolas[i][0]<=cor_x+60:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+60<bolas[i][0]<=cor_x+70:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+70<bolas[i][0]<=cor_x+80:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                    if cor_x+80<bolas[i][0]<=cor_x+90:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+90<bolas[i][0]<=cor_x+105:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                        
            elif Barra==False:
                if  bolas[i][1]==638:
##                    cor_x+155>=bolas[i][0]>=cor_x-5 
                    if cor_x-5<=bolas[i][0]<=cor_x+15:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+15<bolas[i][0]<=cor_x+30:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+30<bolas[i][0]<=cor_x+45:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+45<bolas[i][0]<=cor_x+60:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+60<bolas[i][0]<=cor_x+75:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+75<bolas[i][0]<=cor_x+90:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+90<bolas[i][0]<=cor_x+105:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+105<bolas[i][0]<=cor_x+120:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+120<bolas[i][0]<=cor_x+135:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+135<bolas[i][0]<=cor_x+155:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
            elif Barra==True:
                if  bolas[i][1]==638: 
                    if cor_x-5<=bolas[i][0]<=cor_x+25:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+25<bolas[i][0]<=cor_x+50:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+50<bolas[i][0]<=cor_x+75:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+75<bolas[i][0]<=cor_x+100:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+100<bolas[i][0]<=cor_x+125:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+125<bolas[i][0]<=cor_x+150:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                    if cor_x+150<bolas[i][0]<=cor_x+175:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+175<bolas[i][0]<=cor_x+200:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+200<bolas[i][0]<=cor_x+225:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+225<bolas[i][0]<=cor_x+243:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()

                                  
    ##        x=0
    ##        pos_x=25
    ##        pos_y=30
    ##        print powerup



##            condicion powerupImg
                    
            j=0
            while(j<len(y3)):
##            for j in range(0,len(y3)):  
                if powerup[j]==True:
##                    print "x3",len(x3)
##                    print "y3",len(y3)
##                    print "powerup",j," ",powerup[j]
                    global y3_change
                    y3[j]+=y3_change
                    powerUp(j)
                if y3[j]>638:
                    powerup[j]=False
                    y3.pop(j)
                    x3.pop(j)
                    powerup.pop(j)
                j+=1
##            y3_change=0


                
    ##      powerups
                
            if temp==True:
                tiempo+=30

            if temp3==True:
                tiempo3+=30
                
##            codigo laser part2
                
            if temp2==True:
                tiempo2+=30
                
            if laser==True:
                laser_pos=0
                lasers_change=-8
##                pygame.draw.rect(gameDisplay,verde,(xx,lasers[0],20,150))
                gameDisplay.blit(laserImg,(xx,lasers[0]))
##                pygame.draw.rect(gameDisplay,verde,(xx+150,lasers[1],20,150))
                if Barra2==True:
                    gameDisplay.blit(laserImg,(xx+96,lasers[1]))
                elif Barra==False:
                    gameDisplay.blit(laserImg,(xx+150,lasers[1]))
                elif Barra==True:
                    gameDisplay.blit(laserImg,(xx+230,lasers[1]))
                lasers[0]+=lasers_change
                lasers[1]+=lasers_change
                temp2=True
##                print "laser1",laser
                for ee in l3:
##                while ee<len(l):
##                    if l[ee][0]+85>=xx>=l[ee][0]-5 and l[ee][1]+40>=lasers[0]>=l[ee][1]-5:
                    if ee[0]+85>=xx>=ee[0]-5:
                        if ee[1]+40>=lasers[0]>=ee[1]-5:
                            lasers[0]=50000
                            l3.pop(laser_pos)
                            score+=20
##                    if l[ee][0]+85>=xx+150>=l[ee][0]-5 and l[ee][1]+40>=lasers[1]>=l[ee][1]-5:
                    if ee[1]+40>=lasers[1]>=ee[1]-5:
                        if ee[0]+85>=xx+150>=ee[0]-5:
                            lasers[1]=50000
                            l3.pop(laser_pos)
                            score+=20
                    laser_pos+=1
            lasers_change=0

##            tiempo laser
            
            if tiempo2>2000:
                cont2+=1
                tiempo2=0
                xx=cor_x
                lasers[0]=515
                lasers[1]=515
            if cont2>6:
                laser=False
                tiempo2=0
                cont2=0
##                lasers[0]=515
##                lasers[1]=515
##                print "laser0",laser

                
##          tiempo barra
                
            if tiempo>10000:
                Barra=False
                tiempo=0
                temp=False


            if tiempo3>10000:
                Barra2=False
                tiempo3=0
                temp3=False
                
##          powerupcondicion
                
##            print "y3",y3
##            print "cor_x",cor_x," ",cor_x+150
##            print "b",b
                
            j=0
            while j<len(x3):

##            for j in range(0,len(y3)):
##                print y3[j]
                if cor_x<=x3[j]<=cor_x+150 and 630<=y3[j]<=636:
##                    print "j", j
                    x3.pop(j)
                    y3.pop(j)
                    powerup.pop(j)
    
##                    print "repoio"
    ##              barrapowerup
                    if b==0:
                        tiempo=0
                        Barra=True
                        temp=True
                        Barra2=False
    ##            bolapowerup
                    if b==1: 
                        bolas.append([375,633])
                        speed.append([5,-5])
    ##            laserpowerup
                    if b==2:
                        tiempo2=0
                        laser=True
                        lasers[0]=515
                        lasers[1]=515
                        xx=cor_x
##                barrapequeñapowerup
                    if b==3:
                        tiempo3=0
                        Barra=False
                        Barra2=True
                        temp3=True
                            
                j+=1


##      codigo bola perdida
##            print (bolas[0][1]) 
            if len(bolas)==1:    
                if bolas[0][1]>665:
##                    bolas.pop(i)
                    cont-=1
##                    bolas=[[375,633]]
                    if cont==0:
                        l3=[                    [168,45],                                               [552,45],
                                                        [232,75],                               [488,75],
                                                [168,104],[232,104],[296,104],[360,104],[424,104],[488,104],[552,104],
                                        [104,136],[168,136],[232,136],[296,136],[360,136],[424,136],[488,136],[552,136],[616,136],
                                        [104,166],[168,166],[232,166],[296,166],[360,166],[424,166],[488,166],[552,166],[616,166],
                                        [104,196],[168,196],[232,196],[296,196],[360,196],[424,196],[488,196],[552,196],[616,196],
                                [40,226],[104,226],[168,226],[232,226],[296,226],[360,226],[424,226],[488,226],[552,226],[616,226],[680,226],
                                [40,256],       [168,256],[232,256],[296,256],[360,256],[424,256],[488,256],[552,256],              [680,256],
                                [40,286],       [168,286],                                                          [552,286]      ,[680,286],
                                [40,316],        [168,316],                                                         [552,316]      ,[680,316],
                                                        [232,346],                                      [488,346],
                                                        [232,376],[296,376],                          [424,376],[488,376]

                            ]
                        cont=3
                        bolas=[[375,633]]
                        speed=[[5,-5]]
                        laser=False
                        Barra=False
                        score=0
                        gameOver()
                    bolas=[[375,633]]
                    speed=[[5,-5]]
                    laser=False
                    Barra=False
                    Barra2=False
                    powerup=[False]
                    y3=[]
                    x3=[]
                    message_display4("-1 bola")
            elif bolas[i][1]>665:
                    bolas.pop(i)
                    speed.pop(i)
##            if bolas[i][1]>665:
##                    bolas.pop(i)
##                    speed.pop(i)
##            if len(bolas)==0:
##                message_display("-1 bola")
                    
            i+=1

            if len(l3)==0:
                bolas=[[375,633]]
                speed=[[5,-5]]
                laser=False
                Barra=False
                Barra2=False
                powerup=[False]
                y3=[]
                x3=[]
                message_display2("Good Job")

	    
            pygame.display.update()
            clock.tick(120)

    

def nivel1():
##    pygame.mixer.music.play(-1)
    global pause
    global cont
    global speed2
    global x3
    global y3
    global Barra
    global Barra2
    global tiempo
    global bolas
    global lasers
    global l
    global laser
    global powerup
    global b
    global radio
    global score
    tiempo=0
    tiempo2=0
    tiempo3=0
    temp=False
    temp2=False
    temp3=False
    cont2=0
    x_change=0
##    y3_change=0
    lasers=[515,515]
    cor_x=300
##    x2=375
##    y2=633
    speed=[[5,-5]]
    quit=False
    while not quit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                pygame.mixer.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        gameDisplay.blit(fondoImg,(0,0))

        
        
        
        if Barra2==True:
            if cor_x>ancho-96:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0
        elif Barra==False:
            if cor_x>ancho-156:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0
        elif Barra==True:
            if cor_x>ancho-250:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0


        cor_x+=x_change
        bola(bolas)
        barra(cor_x)
        vidas(cont,bolas)
        colision(bolas,speed,l)
        ladrillo(l)
        score1()
        
        ##codigo bola
                         
        i=0
        while i<len(bolas):
##        for i in range(0,len(bolas)):
            bolas[i][0]+=speed[i][0]
            bolas[i][1]+=speed[i][1]
            if bolas[i][0]<radio or bolas[i][0]>ancho-radio:
                speed[i][0]=-speed[i][0]
                bolas[i][0]+=speed[i][0]
            if bolas[i][1]<radio or bolas[i][1]>670:
                speed[i][1]=-speed[i][1]
                bolas[i][1]+=speed[i][1]
            
            
    ##      codigo bola toca barra
##            print speed
                
            if Barra2==True:
                if bolas[i][1]==638:
                    if cor_x-5<=bolas[i][0]<=cor_x+10:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+10<bolas[i][0]<=cor_x+20:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+20<bolas[i][0]<=cor_x+30:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+30<bolas[i][0]<=cor_x+40:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+40<bolas[i][0]<=cor_x+50:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+50<bolas[i][0]<=cor_x+60:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+60<bolas[i][0]<=cor_x+70:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+70<bolas[i][0]<=cor_x+80:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                    if cor_x+80<bolas[i][0]<=cor_x+90:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+90<bolas[i][0]<=cor_x+105:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                        
            elif Barra==False:
                if  bolas[i][1]==638:
##                    cor_x+155>=bolas[i][0]>=cor_x-5 
                    if cor_x-5<=bolas[i][0]<=cor_x+15:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+15<bolas[i][0]<=cor_x+30:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+30<bolas[i][0]<=cor_x+45:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+45<bolas[i][0]<=cor_x+60:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+60<bolas[i][0]<=cor_x+75:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+75<bolas[i][0]<=cor_x+90:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+90<bolas[i][0]<=cor_x+105:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+105<bolas[i][0]<=cor_x+120:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+120<bolas[i][0]<=cor_x+135:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+135<bolas[i][0]<=cor_x+155:
                        speed[i][1]=2
                        speed[i][1]=-speed[i][1]
                        hey.play()
            elif Barra==True:
                if  bolas[i][1]==638: 
                    if cor_x-5<=bolas[i][0]<=cor_x+25:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+25<bolas[i][0]<=cor_x+50:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+50<bolas[i][0]<=cor_x+75:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+75<bolas[i][0]<=cor_x+100:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+100<bolas[i][0]<=cor_x+125:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+125<bolas[i][0]<=cor_x+150:
                        speed[i][1]=5
                        speed[i][1]=-speed[i][1]
                    if cor_x+150<bolas[i][0]<=cor_x+175:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+175<bolas[i][0]<=cor_x+200:
                        speed[i][1]=4
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+200<bolas[i][0]<=cor_x+225:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()
                    if cor_x+225<bolas[i][0]<=cor_x+243:
                        speed[i][1]=3
                        speed[i][1]=-speed[i][1]
                        hey.play()

                                  
    ##        x=0
    ##        pos_x=25
    ##        pos_y=30	    
##        pygame.display.update()
##        clock.tick(60)
    ##        print powerup



##            condicion powerupImg
                    
            j=0
            while(j<len(y3)):
##            for j in range(0,len(y3)):  
                if powerup[j]==True:
##                    print "x3",len(x3)
##                    print "y3",len(y3)
##                    print "powerup",j," ",powerup[j]
                    global y3_change
                    y3[j]+=y3_change
                    powerUp(j)
                if y3[j]>638:
                    powerup[j]=False
                    y3.pop(j)
                    x3.pop(j)
                    powerup.pop(j)
                j+=1
##            y3_change=0


                
    ##      powerups
                
            if temp==True:
                tiempo+=30

            if temp3==True:
                tiempo3+=30
                
##            codigo laser part2
                
            if temp2==True:
                tiempo2+=30
                
            if laser==True:
                laser_pos=0
                lasers_change=-8
##                pygame.draw.rect(gameDisplay,verde,(xx,lasers[0],20,150))
                gameDisplay.blit(laserImg,(xx,lasers[0]))
##                pygame.draw.rect(gameDisplay,verde,(xx+150,lasers[1],20,150))
                if Barra2==True:
                    gameDisplay.blit(laserImg,(xx+96,lasers[1]))
                elif Barra==False:
                    gameDisplay.blit(laserImg,(xx+150,lasers[1]))
                elif Barra==True:
                    gameDisplay.blit(laserImg,(xx+230,lasers[1]))
                lasers[0]+=lasers_change
                lasers[1]+=lasers_change
                temp2=True
##                print "laser1",laser
                for ee in l:
##                while ee<len(l):
##                    if l[ee][0]+85>=xx>=l[ee][0]-5 and l[ee][1]+40>=lasers[0]>=l[ee][1]-5:
                    if ee[0]+85>=xx>=ee[0]-5:
                        if ee[1]+40>=lasers[0]>=ee[1]-5:
                            lasers[0]=50000
                            l.pop(laser_pos)
                            score+=20
##                    if l[ee][0]+85>=xx+150>=l[ee][0]-5 and l[ee][1]+40>=lasers[1]>=l[ee][1]-5:
                    if ee[1]+40>=lasers[1]>=ee[1]-5:
                        if ee[0]+85>=xx+150>=ee[0]-5:
                            lasers[1]=50000
                            l.pop(laser_pos)
                            score+=20
                    laser_pos+=1
            lasers_change=0

##            tiempo laser
            
            if tiempo2>2000:
                cont2+=1
                tiempo2=0
                xx=cor_x
                lasers[0]=515
                lasers[1]=515
            if cont2>6:
                laser=False
                tiempo2=0
                cont2=0
##                lasers[0]=515
##                lasers[1]=515
##                print "laser0",laser

                
##          tiempo barra
                
            if tiempo>10000:
                Barra=False
                tiempo=0
                temp=False


            if tiempo3>10000:
                Barra2=False
                tiempo3=0
                temp3=False
                
##          powerupcondicion
                
##            print "y3",y3
##            print "cor_x",cor_x," ",cor_x+150
##            print "b",b
                
            j=0
            while j<len(x3):

##            for j in range(0,len(y3)):
##                print y3[j]
                if cor_x<=x3[j]<=cor_x+150 and 630<=y3[j]<=636:
##                    print "j", j
                    x3.pop(j)
                    y3.pop(j)
                    powerup.pop(j)
    
##                    print "repoio"
    ##              barrapowerup
                    if b==0:
                        tiempo=0
                        Barra=True
                        temp=True
                        Barra2=False
    ##            bolapowerup
                    if b==1: 
                        bolas.append([375,633])
                        speed.append([5,-5])
    ##            laserpowerup
                    if b==2:
                        tiempo2=0
                        laser=True
                        lasers[0]=515
                        lasers[1]=515
                        xx=cor_x
##                barrapequeñapowerup
                    if b==3:
                        tiempo3=0
                        Barra=False
                        Barra2=True
                        temp3=True
                            
                j+=1


##      codigo bola perdida
##            print (bolas[0][1]) 
            if len(bolas)==1:    
                if bolas[0][1]>665:
##                    bolas.pop(i)
                    cont-=1
##                    bolas=[[375,633]]
                    if cont==0:
                        l=[[10,40,1],[10,75,1],[10,110,1],[10,145,1],[10,180,1],[10,215,1],
                          [76,40,1],[76,75,1],[76,110,1],[76,145,1],[76,180,1],[76,215,1],
                          [142,40,1],[142,75,1],[142,110,1],[142,145,1],[142,180,1],[142,215,1],
                          [207,40,1],[207,75,1],[207,110,1],[207,145,1],[207,180,1],[207,215,1],
                          [274,40,1],[274,75,1],[274,110,1],[274,145,1],[274,180,1],[274,215,1],
                          [340,40,1],[340,75,1],[340,110,1],[340,145,1],[340,180,1],[340,215,1],
                          [406,40,1],[406,75,1],[406,110,1],[406,145,1],[406,180,1],[406,215,1],
                          [472,40,1],[472,75,1],[472,110,1],[472,145,1],[472,180,1],[472,215,1],
                          [538,40,1],[538,75,1],[538,110,1],[538,145,1],[538,180,1],[538,215,1],
                          [604,40,1],[604,75,1],[604,110,1],[604,145,1],[604,180,1],[604,215,1],
                          [670,40,1],[670,75,1],[670,110,1],[670,145,1],[670,180,1],[670,215,1],
                          [736,40,1],[736,75,1],[736,110,1],[736,145,1],[736,180,1],[736,215,1]]
                        cont=3
                        bolas=[[375,633]]
                        speed=[[5,-5]]
                        laser=False
                        Barra=False
                        score=0
                        gameOver()
                    bolas=[[375,633]]
                    speed=[[5,-5]]
                    laser=False
                    Barra=False
                    Barra2=False
                    powerup=[False]
                    y3=[]
                    x3=[]
                    message_display("-1 bola")
            elif bolas[i][1]>665:
                    bolas.pop(i)
                    speed.pop(i)
##            if bolas[i][1]>665:
##                    bolas.pop(i)
##                    speed.pop(i)
##            if len(bolas)==0:
##                message_display("-1 bola")
                    
            i+=1





            
        
##        if cont==0:
##            gameOver()


            

                    
##      fin level1
            
        if len(l)==0:
            bolas=[[375,633]]
            speed=[[5,-5]]
            laser=False
            Barra=False
            Barra2=False
            powerup=[False]
            y3=[]
            x3=[]
            message_display("GG IZI")
	    
        pygame.display.update()
        clock.tick(60)
    
        
##intro()
##nivel1()
##nivel2()
nivel3()
pygame.quit()
quit()

