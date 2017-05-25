import pygame
import time
import random


pygame.init()

##pygame.mixer.pre_init() 
##pygame.mixer.init()
pygame.mixer.init()


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


barImg=pygame.image.load("C:\Users\Israel\Desktop\Barra.png")
##ballImg=pygame.image.load("C:\Users\Israel\Desktop\Bolarepoio")
ballImg=pygame.image.load("C:\Users\Israel\Desktop\Bola2def")
brickImg=pygame.image.load("C:\Users\Israel\Desktop\Ladrillo.png")
bar2Img=pygame.image.load("C:\Users\Israel\Desktop\BarraGrande2.png")
fondoImg=pygame.image.load("C:\Users\Israel\Desktop\Ejercicios-Python\Proyecto\Sonidos\PrograPics\Fondos\sample1 800x700.jpg")
fondoIntroImg=pygame.image.load("C:\Users\Israel\Desktop\Ejercicios-Python\Proyecto\Sonidos\PrograPics\Fondos\Sample 3 800X700.png")
fondoIntroImg2=pygame.image.load("C:\Users\Israel\Desktop\Ejercicios-Python\Proyecto\Sonidos\PrograPics\Fondos\800x700.jpg")
laserImg=pygame.image.load("C:\Users\Israel\Desktop\Laser.png")


pygame.mixer.music.load("C:\Users\Israel\Desktop\Mixes\Best Future House Music Mix 2016.mp3")
##hey=pygame.mixer.Sound("C:\Users\Israel\Desktop\Ejercicios-Python\Proyecto\Sonidos\hey.waw")
hey=pygame.mixer.Sound("C:\Users\Israel\Desktop\Ejercicios-Python\Proyecto\Sonidos\PrograPics\Audios\pongs\4378__noisecollector__pongblipg4.wav") 
##hey2=pygame.mixer.Sound("C:\Users\Israel\Desktop\Mixes\Best Future House Music Mix 2016.mp3")


Barra=False
pause=False
powerup=False
laser=False


tiempo=0
cont=3
y3=228
x3=606
b=132
y3_change=3


bolas=[[375,633]]

l=[[25,63],[25,96],[25,129],[25,162],[25,195],[25,228],[108,63],[108,96],[108,129],[108,162],[108,195],
   [108,228],[191,63],[191,96],[191,129],[191,162],[191,195],[191,228],[274,63],[274,96],[274,129],[274,162],
   [274,195],[274,228],[357,63],[357,96],[357,129],[357,162],[357,195],[357,228],[440,63],[440,96],[440,129],
   [440,162],[440,195],[440,228],[523,63],[523,96],[523,129],[523,162],[523,195],[523,228],[606,63],[606,96],
   [606,129],[606,162],[606,195],[606,228],[689,63],[689,96],[689,129],[689,162],[689,195],[689,228]]

l2= [[25,63],[25,96],[25,129],[25,162],[25,195],[25,228],
    [108,63],[108,96],[108,129],[108,162],[108,195],[108,228],
    [191,63],[191,96],[191,129],[191,162],[191,195],[191,228],
    [274,63],[274,96],[274,129],[274,162],[274,195],[274,228],
    [357,63],[357,96],[357,129],[357,162],[357,195],[357,228],
    [440,63],[440,96],[440,129],[440,162],[440,195],[440,228],
    [523,63],[523,96],[523,129],[523,162],[523,195],[523,228],
    [606,63],[606,96],[606,129],[606,162],[606,195],[606,228],
    [689,63],[689,96],[689,129],[689,162],[689,195],[689,228]]

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
    l=[[25,63],[25,96],[25,129],[25,162],[25,195],[25,228],[108,63],[108,96],[108,129],[108,162],[108,195],[108,228],[191,63],[191,96],[191,129],[191,162],[191,195],[191,228],[274,63],[274,96],[274,129],[274,162],[274,195],[274,228],[357,63],[357,96],[357,129],[357,162],[357,195],[357,228],[440,63],[440,96],[440,129],[440,162],[440,195],[440,228],[523,63],[523,96],[523,129],[523,162],[523,195],[523,228],[606,63],[606,96],[606,129],[606,162],[606,195],[606,228],[689,63],[689,96],[689,129],[689,162],[689,195],[689,228]]
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
    
def vidas(cont,bolas):
    pos=20
    if len(bolas)==1:
        if bolas[0][1]>567:
            cont=cont-1
        font=pygame.font.SysFont(None,25)
##        text=font.render(" Bolas: "+str(cont),True,negro)
        text=font.render(" Bolas: ",True,negro)
        gameDisplay.blit(text ,(0,0))
        for u in range(0,cont):
            gameDisplay.blit(ballImg,(pos,5))
            pos+=35

            
def ladrillo(l):
    x=0
    while x<len(l):
        gameDisplay.blit(brickImg,(l[x][0],l[x][1]))        
        x+=1
    
    
def powerUp():
    global x3
    global y3
    gameDisplay.blit(ballImg,(x3,y3))   


##def powerupBarra(cor_x):
##    pygame.draw.rect(gameDisplay,negro,(cor_x,650,233,20))
##    gameDisplay.blit(bar2Img,(cor_x,650))

##def powerupBolas(speed,bolas):
##    bolas.append([375,633])
##    speed.append([5,-5])


def colision(bolas,speed,l):
    global powerup
    global x3
    global y3
    global b
##    ly=[63, 96, 129, 162, 195, 228]
##    lx=[25, 108, 191, 274, 357, 440, 523, 606, 689]
    e=0
    r=0
##    i=0
    while e<len(l):
        for ii in range(0,len(bolas)):
##        while i<len(bolas):
##            print bolas
##            if l[e][0]+91>=bolas[ii][0]>=l[e][0]-5:
##                if l[e][1]+40>=bolas[ii][1]>=l[e][1]-5:
            
            if l[e][1]+40>=bolas[ii][1]>=l[e][1]-5:
                if l[e][0]+88>=bolas[ii][0]>=l[e][0]:

##                  sonido de bola
                
##                    pygame.mixer.Sound.set_volume(1)
                    hey.play()
##                    pygame.mixer.Sound.play(hey)
##                    print "l",l[e][0]
##                    print "bolas",ii," ",bolas[ii][0]
                    
                    speed[ii][1]=-speed[ii][1]
                    
##                    if l[e][0]==689 and l[e][1]==228:
##                    print powerup
                    
                    a=random.random()
                    if a<0.5:
                        b=random.randrange(0,3)
                        print a
                        print b
                        x3=l[e][0]+40
                        y3=l[e][1]-10
                        powerup=True
        ##                powerUp()
                    l.pop(e)
##            i+=1


##          choque de lado(bola) no resuelto
                    
##                if l[e][0]+5>=bolas[ii][0]>=l[e][0]-5 or l[e][0]+85>=bolas[ii][0]>=l[e][0]+80:
##                    speed[0]=-speed[0]
##                    print "x2",x2
##                    print "l",l[e][0]

        e+=1
        

def bola(bola):
    for i in range(0,len(bolas)):
        pygame.draw.circle(gameDisplay,verde,(bolas[i][0],bolas[i][1]),12)
        gameDisplay.blit(ballImg,(bolas[i][0]-12,bolas[i][1]-15))
    
def barra(cor_x):
    if Barra==False:
        pygame.draw.rect(gameDisplay,negro,(cor_x,650,150,20))
        gameDisplay.blit(barImg,(cor_x,650))
    if Barra==True:
        pygame.draw.rect(gameDisplay,negro,(cor_x,650,233,20))
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
    global tiempo
    global bolas
    global lasers
    global l2
    global laser
    global powerup
    global b
    tiempo=0
    tiempo2=0
    temp=False
    temp2=False
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

        radio=12
        
        
        if Barra==False:
            if cor_x>ancho-156:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0
        if Barra==True:
            if cor_x>ancho-236:
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
        
        ##codigo bola
        
##        i=0
##        while i<len(bolas):
        for i in range(0,len(bolas)):
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
            if Barra==False:
                if cor_x+155>=bolas[i][0]>=cor_x-5 and bolas[i][1]==638:
                    
                    speed[i][1]=-speed[i][1]
                    
            if Barra==True:
                if cor_x+238>=bolas[i][0]>=cor_x-5 and bolas[i][1]==638:
                    speed[i][1]=-speed[i][1]
    ##        x=0
    ##        pos_x=25
    ##        pos_y=30
            colision(bolas,speed,l2)
            ladrillo(l2)
    ##        print powerup


                
            if powerup==True:
                global y3_change
                y3+=y3_change
                powerUp()
            if y3>638:
                powerup=False
##            y3_change=0
                
    ##      powerups
                
            if temp==True:
                tiempo+=30


                
##            codigo laser2
            if temp2==True:
                tiempo2+=30
                
            if laser==True:
                ee=0
                lasers_change=-8
##                pygame.draw.rect(gameDisplay,verde,(xx,lasers[0],20,150))
                gameDisplay.blit(laserImg,(xx,lasers[0]))
##                pygame.draw.rect(gameDisplay,verde,(xx+150,lasers[1],20,150))
                gameDisplay.blit(laserImg,(xx+150,lasers[1]))
                lasers[0]+=lasers_change
                lasers[1]+=lasers_change
                temp2=not temp2
##                print "laser1",laser
                while ee<len(l2):
                    if l2[ee][0]+85>=xx>=l[ee][0]-5 and l2[ee][1]+40>=lasers[0]>=l2[ee][1]-5:
                        lasers[0]=50000
                        l2.pop(ee)
                    if l2[ee][0]+85>=xx+150>=l[ee][0]-5 and l[ee][1]+40>=lasers[1]>=l2[ee][1]-5:
                        lasers[1]=50000
                        l2.pop(ee)
                    ee+=1
            lasers_change=0
            
            if tiempo2>1000:
                cont2+=1
                tiempo2=0
                xx=cor_x
                lasers[0]=515
                lasers[1]=515
            if cont2>6:
                laser=False
                tiempo2=0
##                print "laser0",laser

                
##          tiempo barra
                
            if tiempo>10000:
                Barra=False
                tiempo=0
                temp=not temp
                
##          powerupcondicion
                
##            print "y3",y3
##            print "cor_x",cor_x," ",cor_x+150
##            print "b",b
            if cor_x<=x3<=cor_x+150 and y3==635:
##                print "b",b
##              barrapowerup
                if b==0:
                    Barra=not Barra
                    temp=not temp
##            bolapowerup
                if b==1: 
                    bolas.append([375,633])
                    speed.append([5,-5])
##            laserpowerup
                if b==2:
                    laser=not laser
                    xx=cor_x

##      codigo bola perdida
                    
            if len(bolas)==1:    
                if bolas[0][1]>665:
##                    bolas.pop(i)
                    cont-=1
##                    bolas=[[375,633]]
                    if cont==0:
                        l2=[[25,63],[25,96],[25,129],[25,162],[25,195],[25,228],[108,63],[108,96],[108,129],[108,162],[108,195],[108,228],[191,63],[191,96],[191,129],[191,162],[191,195],[191,228],[274,63],[274,96],[274,129],[274,162],[274,195],[274,228],[357,63],[357,96],[357,129],[357,162],[357,195],[357,228],[440,63],[440,96],[440,129],[440,162],[440,195],[440,228],[523,63],[523,96],[523,129],[523,162],[523,195],[523,228],[606,63],[606,96],[606,129],[606,162],[606,195],[606,228],[689,63],[689,96],[689,129],[689,162],[689,195],[689,228]]
                        cont=3
                        bolas=[[375,633]]
                        speed=[[5,-5]]
                        laser=False
                        Barra=False
                        gameOver()
                    bolas=[[375,633]]
                    speed=[[5,-5]]
                    laser=False
                    Barra=False
                    message_display("-1 bola")
            if bolas[i][1]>665:
                    bolas.pop(i)
                    speed.pop(i)
##            if len(bolas)==0:
##                message_display("-1 bola")
                    
##            i+=1








            
        
##        if cont==0:
##            gameOver()

##      codigo bola -1
            

                    
##      fin level1
            
        if len(l)==0:
            message_display2("Good Job")
		
        pygame.display.update()
        clock.tick(60)
    
   
##def nivel3():


def nivel1():
##    pygame.mixer.music.play(-1)
    global pause
    global cont
    global speed2
    global x3
    global y3
    global Barra
    global tiempo
    global bolas
    global lasers
    global l
    global laser
    global powerup
    global b
    tiempo=0
    tiempo2=0
    temp=False
    temp2=False
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

        radio=12
        
        
        if Barra==False:
            if cor_x>ancho-156:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        x_change=0
            if cor_x<6:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=0
        if Barra==True:
            if cor_x>ancho-236:
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
        
        ##codigo bola
        
##        i=0
##        while i<len(bolas):
        for i in range(0,len(bolas)):
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
            if Barra==False:
                if cor_x+155>=bolas[i][0]>=cor_x-5 and bolas[i][1]==638:
                    
                    speed[i][1]=-speed[i][1]
                    
            if Barra==True:
                if cor_x+238>=bolas[i][0]>=cor_x-5 and bolas[i][1]==638:
                    speed[i][1]=-speed[i][1]
    ##        x=0
    ##        pos_x=25
    ##        pos_y=30
            colision(bolas,speed,l)
            ladrillo(l)
    ##        print powerup


                
            if powerup==True:
                global y3_change
                y3+=y3_change
                powerUp()
            if y3>638:
                powerup=False
##            y3_change=0
                
    ##      powerups
                
            if temp==True:
                tiempo+=30


                
##            codigo laser2
            if temp2==True:
                tiempo2+=30
                
            if laser==True:
                ee=0
                lasers_change=-8
##                pygame.draw.rect(gameDisplay,verde,(xx,lasers[0],20,150))
                gameDisplay.blit(laserImg,(xx,lasers[0]))
##                pygame.draw.rect(gameDisplay,verde,(xx+150,lasers[1],20,150))
                gameDisplay.blit(laserImg,(xx+150,lasers[1]))
                lasers[0]+=lasers_change
                lasers[1]+=lasers_change
                temp2=not temp2
##                print "laser1",laser
                while ee<len(l):
                    if l[ee][0]+85>=xx>=l[ee][0]-5 and l[ee][1]+40>=lasers[0]>=l[ee][1]-5:
                        lasers[0]=50000
                        l.pop(ee)
                    if l[ee][0]+85>=xx+150>=l[ee][0]-5 and l[ee][1]+40>=lasers[1]>=l[ee][1]-5:
                        lasers[1]=50000
                        l.pop(ee)
                    ee+=1
            lasers_change=0
            
            if tiempo2>1000:
                cont2+=1
                tiempo2=0
                xx=cor_x
                lasers[0]=515
                lasers[1]=515
            if cont2>6:
                laser=False
                tiempo2=0
##                print "laser0",laser

                
##          tiempo barra
                
            if tiempo>10000:
                Barra=False
                tiempo=0
                temp=not temp
                
##          powerupcondicion
                
##            print "y3",y3
##            print "cor_x",cor_x," ",cor_x+150
##            print "b",b
            if cor_x<=x3<=cor_x+150 and y3==635:
##                print "b",b
##              barrapowerup
                if b==0:
                    Barra=not Barra
                    temp=not temp
##            bolapowerup
                if b==1: 
                    bolas.append([375,633])
                    speed.append([5,-5])
##            laserpowerup
                if b==2:
                    laser=not laser
                    xx=cor_x

##      codigo bola perdida
                    
            if len(bolas)==1:    
                if bolas[0][1]>665:
##                    bolas.pop(i)
                    cont-=1
##                    bolas=[[375,633]]
                    if cont==0:
                        l=[[25,63],[25,96],[25,129],[25,162],[25,195],[25,228],[108,63],[108,96],[108,129],[108,162],[108,195],[108,228],[191,63],[191,96],[191,129],[191,162],[191,195],[191,228],[274,63],[274,96],[274,129],[274,162],[274,195],[274,228],[357,63],[357,96],[357,129],[357,162],[357,195],[357,228],[440,63],[440,96],[440,129],[440,162],[440,195],[440,228],[523,63],[523,96],[523,129],[523,162],[523,195],[523,228],[606,63],[606,96],[606,129],[606,162],[606,195],[606,228],[689,63],[689,96],[689,129],[689,162],[689,195],[689,228]]
                        cont=3
                        bolas=[[375,633]]
                        speed=[[5,-5]]
                        laser=False
                        Barra=False
                        gameOver()
                    bolas=[[375,633]]
                    speed=[[5,-5]]
                    laser=False
                    Barra=False
                    message_display("-1 bola")
            if bolas[i][1]>665:
                    bolas.pop(i)
                    speed.pop(i)
##            if len(bolas)==0:
##                message_display("-1 bola")
                    
##            i+=1








            
        
##        if cont==0:
##            gameOver()

##      codigo bola -1
            

                    
##      fin level1
            
        if len(l)==0:
            message_display2("Good Job")
		
        pygame.display.update()
        clock.tick(60)
    
        
intro()
nivel1()
##nivel2()
##nivel3()
pygame.quit()
quit()

