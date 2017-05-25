import pygame
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
gameDisplay=pygame.display.set_mode((800,700))

brickImg=pygame.image.load("Ladrillo2.png")
brickAzul=pygame.image.load("LadrilloAzul.png")
brickRojo=pygame.image.load("LadrilloRojo.png")



##l2= [[25,63,1],[25,96,1],[25,129,1],[25,162,1],[25,195,1],[25,228,1],
##    [108,63,1],[108,96,1],[108,129,1],[108,162,1],[108,195,1],[108,228,1],
##    [191,63,1],[191,96,1],[191,129,1],[191,162,1],[191,195,1],[191,228,1],
##    [274,63,1],[274,96,1],[274,129,1],[274,162,1],[274,195,1],[274,228,1],
##    [357,63,1],[357,96,1],[357,129,1],[357,162,1],[357,195,1],[357,228,1],
##    [440,63,1],[440,96,1],[440,129,1],[440,162,1],[440,195,1],[440,228,1],
##    [523,63,1],[523,96,1],[523,129,1],[523,162,1],[523,195,1],[523,228,1],
##    [606,63,1],[606,96,1],[606,129,1],[606,162,1],[606,195,1],[606,228,1],
##    [689,63,1],[689,96,1],[689,129,1],[689,162,1],[689,195,1],[689,228,1]]

##15

##65
##pos x  1=84,2=148,3=212,4=276,5=340,6=404,7=468,8=532,9=596,10=660
##pos x  1==148,2=212,3=276,4=340,5=404,6=468 7=532,8=596

##pos y 40 75 110 145 180 215 250 285 320

##y  35
##x 64

##[110,40,1],[175,40,1],[558,40,1],[622,40,1],
##    [84,75,1],[212,75,1],[276,75,1],[596,75,1],[660,75,1],[724,75,1],

##l2= [       [238,40,1],[302,40,1],                      [430,40,1],[494,40,1],
##        [212,75,1],[276,75,1],[340,75,1],           [404,75,1],[468,75,1],[532,75,1],
##    [148,110,1],[212,110,1],[276,110,1],[340,110,1],[404,110,1],[468,110,1],[532,110,1],[596,110,1],
##    [148,145,1],[212,145,1],[276,145,1],[340,145,1],[404,145,1],[468,145,1],[532,145,1],[596,145,1],
##        [148,180,1],[212,180,1],[276,180,1],[340,180,1],[404,180,1],[468,180,1],[532,180,1],[596,180,1],
##            [212,215,1],[276,215,1],[340,215,1],[404,215,1],[468,215,1],[532,215,1],
##                [276,250,1],[340,250,1],[404,250,1],[468,250,1],
##                        [340,285,1],[404,285,1],
##                            [366,320,1]
##    ]


l2= [                   [238,40,1],[302,40,1],                      [430,40,1],[494,40,1],
                    [212,75,1],[276,75,1],[340,75,1],           [404,75,1],[468,75,1],[532,75,1],
            [148,110,1],[212,110,1],[276,110,1],[340,110,1],[404,110,1],[468,110,1],[532,110,1],[596,110,1],
            [148,145,1],[212,145,1],[276,145,1],[340,145,1],[404,145,1],[468,145,1],[532,145,1],[596,145,1],
            [148,180,1],[212,180,1],[276,180,1],[340,180,1],[404,180,1],[468,180,1],[532,180,1],[596,180,1],[596,180,1],
            [148,215,1],[212,215,1],[276,215,1],[340,215,1],[404,215,1],[468,215,1],[532,215,1],[596,215,1],
                        [212,250,1],[276,250,1],[340,250,1],[404,250,1],[468,250,1],[532,250,1],
                                    [276,285,1],[340,285,1],[404,285,1],[468,285,1],
                                            [340,320,1],[404,320,1],
                                                    [366,355,1]
    ]
l=[[10,40,1],[10,75,1],[10,110,1],[10,145,1],[10,180,1],[10,215,1],
   [75,40,1],[75,75,1],[75,110,1],[75,145,1],[75,180,1],[75,215,1],
   [140,40,1],[140,75,1],[140,110,1],[140,145,1],[140,180,1],[140,215,1],
   [205,40,1],[205,75,1],[205,110,1],[205,145,1],[205,180,1],[205,215,1],
   [270,40,1],[270,75,1],[270,110,1],[270,145,1],[270,180,1],[270,215,1],
   [335,40,1],[335,75,1],[335,110,1],[335,145,1],[335,180,1],[335,215,1],
   [400,40,1],[400,75,1],[400,110,1],[400,145,1],[400,180,1],[400,215,1],
   [465,40,1],[465,75,1],[465,110,1],[465,145,1],[465,180,1],[465,215,1],
   [530,40,1],[530,75,1],[530,110,1],[530,145,1],[530,180,1],[530,215,1],
   [595,40,1],[595,75,1],[595,110,1],[595,145,1],[595,180,1],[595,215,1],
   [660,40,1],[660,75,1],[660,110,1],[660,145,1],[660,180,1],[660,215,1],
   [725,40,1],[725,75,1],[725,110,1],[725,145,1],[725,180,1],[725,215,1]]

##pos x  1=20,2=84,3=148,4=212,5=276,6=340,7=404,8=468,9=532,10=596,11=660

##pos y 40 75 110 145 180 215 250 285 320

##l3=[[40,40],[168,40],[296,40],[424,40],[552,40],[680,40],
##            [104,75],    
##    [40,110],                                   [680,110],
##    
##    [40,180],                                   [680,180],
##    
##    [40,250],                                   [680,250],
##
##    
##    [40,320],[168,320],[296,320],[424,320],[552,320],[680,320],
        

##l3=[[168,45],                                               [552,45],
##            [232,75],                               [488,75],
##            [168,104],[232,104],[296,104],[360,104],[424,104],[488,104],[552,104],
##    [104,136],[168,136],[232,136],[296,136],[360,136],[424,136],[488,136],[552,136],[616,136],
##    [104,166],[168,166],[232,166],[296,166],[360,166],[424,166],[488,166],[552,166],[616,166],
##    [40,196],[104,196],[168,196],[232,196],[296,196],[360,196],[424,196],[488,196],[552,196],[616,196],[680,196],
##    [40,226]        ,[168,226],[232,226],[296,226],[360,226],[424,226],[488,226],[552,226]      ,[680,226],
##    [40,256],       [168,256],                                                  [552,256]      ,[680,256],
##    [40,286],        [168,286],                                                 [552,286]      ,[680,286],
##                            [232,316],[296,316],                          [424,316],[488,316],
##                            [232,346],[296,346],                          [424,346],[488,346]
##    ]

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
gameDisplay.fill(black)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

##    x=0
##    y=0
##    a=20
##    b=20
##    while x<6:
##        y=0
##        
##        while y<12:
##            pygame.draw.rect(gameDisplay,green,(a,b,62,30))
##            y+=1
####            print (a)
##            a+=64
##            
##        x+=1
####        print (b)
##        a=20
##        b+=35

##            [232,136] [232,166] [424,136] [424,166]

##l2= [                   [238,40,1],[302,40,1],                      [430,40,1],[494,40,1],
##                    [212,75,1],[276,75,1],[340,75,1],           [404,75,1],[468,75,1],[532,75,1],
##            [148,110,1],[212,110,1],[276,110,1],[340,110,1],[404,110,1],[468,110,1],[532,110,1],[596,110,1],
##            [148,145,1],[212,145,1],[276,145,1],[340,145,1],[404,145,1],[468,145,1],[532,145,1],[596,145,1],
##            [148,180,1],[212,180,1],[276,180,1],[340,180,1],[404,180,1],[468,180,1],[532,180,1],[596,180,1],[596,180,1],
##            [148,215,1],[212,215,1],[276,215,1],[340,215,1],[404,215,1],[468,215,1],[532,215,1],[596,215,1],
##                        [212,250,1],[276,250,1],[340,250,1],[404,250,1],[468,250,1],[532,250,1],
##                                    [276,285,1],[340,285,1],[404,285,1],[468,285,1],
##                                            [340,320,1],[404,320,1],
##                                                    [366,355,1]]

    ##    pygame.draw.circle(gameDisplay,(255,0,0),(50,50),12)
##    for x in l2:
##        if (x[0]==238 or x[0]==302 or x[0]==430 or x[0]==494)and x[1]==40:
##            gameDisplay.blit(brickAzul,(x[0],x[1]))               
##        elif (x[0]==212 or x[0]==532 or x[0]==340 or x[0]==404)and x[1]==75:
##            gameDisplay.blit(brickAzul,(x[0],x[1]))
##        elif (x[0]==148 or x[0]==596)and (x[1]==110 or x[1]==145 or x[1]==180 or x[1]==215 ):
##            gameDisplay.blit(brickAzul,(x[0],x[1]))
##        elif (x[0]==212 or x[0]==532)and x[1]==250:
##            gameDisplay.blit(brickAzul,(x[0],x[1]))
##        elif (x[0]==276 or x[0]==468)and x[1]==285:
##            gameDisplay.blit(brickAzul,(x[0],x[1]))
##        elif (x[0]==340 or x[0]==404)and x[1]==320:
##            gameDisplay.blit(brickAzul,(x[0],x[1]))
##        elif x[0]==366 and x[1]==355:
##            gameDisplay.blit(brickAzul,(x[0],x[1]))
##        else:
##            gameDisplay.blit(brickRojo,(x[0],x[1]))



    
    for x in l3:
        if x[0]==232 and (x[1]==136 or x[1]==166):
            gameDisplay.blit(brickRojo,(x[0],x[1]))               
        elif x[0]==488 and (x[1]==136 or x[1]==166):
            gameDisplay.blit(brickRojo,(x[0],x[1]))
        elif x[0]==296 and x[1]==376:
            gameDisplay.blit(brickImg,(x[0],x[1]))
        elif x[0]==424 and x[1]==376:
            gameDisplay.blit(brickImg,(x[0],x[1]))
        else:
##            gameDisplay.blit(brickAzul,(x[0],x[1]))
##      pygame.draw."figura deseada(circle,pixel,rect,polygon)"
##        pygame.draw.circle(gameDisplay,white,(300,500),24)
##        pygame.draw.rect(gameDisplay,green,(250,300,150,20))
    pygame.display.update()