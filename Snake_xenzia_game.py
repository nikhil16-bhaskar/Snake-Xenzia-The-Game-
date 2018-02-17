import pygame
import time
import random

pygame.init() #initialize a game
#declaring the colours in RGB in tuples wecan also do it in list.
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width=800
display_height=600
gameDisplay = pygame.display.set_mode((display_width,display_height)) #setting surface or display for the game 800 and 600 are lenngth and width pixels in a tuple.
pygame.display.set_caption('Snake Xenzia') #setting the name of the game.which appears at the top.

 
#count=0
FPS=30
block_size=10
clock=pygame.time.Clock() #it is used to set the fps(frames per second) of the game.


font=pygame.font.SysFont(None,25)
def Snake(block_size,snakeList):
    for Xny in snakeList:
        pygame.draw.rect(gameDisplay,green,[Xny[0],Xny[1],block_size,block_size])

    
def message_to_screen(msg,colour):
    screen_text=font.render(msg,True,colour)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])


#main gaming loop
def gameLoop():
    gameExit = False #variable that decides whrn to exit the game,initially it is false bcoz we want to play.
    gameOver= False
    lead_x=display_width/2 #starting x co-ordinates of block.
    lead_y=display_width/2 #starting y co-ordinates of block.
    lead_x_change=0 #change in x co-ordinate from starting point 
    lead_y_change=0 #change in y co-ordinate from starting point
    randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
    randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
    snakeList=[]
    snakeLength=1
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)           
            message_to_screen("you lost!,press c to play again or q to quit.",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_c:
                        gameLoop()
                    if event.key==pygame.K_q:
                        gameExit = True
                        gameOver = False
                    
                    
        for event in pygame.event.get(): #to get the events which involve mouseclick,buttonclick,quitting etc...
            if event.type == pygame.QUIT: #here type is type of event i.e mouse/buttn click or quit,here when event is equal to QUIT .
                gameExit = True #when event type=QUIT then exit the game.
            if event.type == pygame.KEYDOWN: # when event type is keydown(when any key is pressed)
                if event.key == pygame.K_LEFT: #if left key is pressed
                    lead_x_change = -block_size #change lead_x_change by -10 cordinates on x axis.
                    lead_y_change = 0 # change lead_y_change to zero,so that at a time only x cordiante changes making y constant.
                    #print("x -ve")
                    #count+=1
                elif event.key == pygame.K_RIGHT: #if right key is pressed 
                    lead_x_change = block_size #change lead_x_change by -10 cordinates on x axis.
                    lead_y_change = 0 # change lead_y_change to zero,so that at a time only x cordiante changes making y constant.
                    #print("x +ve")
                    #count+=1
                    
                elif event.key == pygame.K_UP:# when up key is pressed.
                    lead_y_change = -block_size #change lead_y_change by -10 cordinates on y axis.
                    lead_x_change = 0 # change lead_x_change to zero,so that at a time only y cordiante changes making x constant
                    #print("x +ve")
                    #count+=1
                elif event.key == pygame.K_DOWN: # when down key is pressed.
                    lead_y_change = block_size #change lead_y_change by 10 cordinates on y axis.
                    lead_x_change = 0 # change lead_x_change to zero,so that at a time only y cordiante changes making x constant
                    #print("x +ve")
                    #count+=1
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver=True
        lead_x += lead_x_change #add lead_x and lead_x_change so that original place of block changes by lead_x_change.
        lead_y += lead_y_change #add lead_y and lead_y_change so that original place of block changes by lead_y_change.
         #if count==50:
            #break
        #print("lead_changed")
        gameDisplay.fill(white) #set the background of game ,white
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,block_size,block_size])

        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver=True
            
        Snake(block_size,snakeList)
        # to draw rectangle on gaming screen,so 1st parameter is where do we want to draw it,2nd what colour,3rd a list of[x-cordinate,y-cordinate,height of rect,width of rect].
        
        #(this is more accelerated)gameDisplay.fill(red,rect=[200,200,30,30])#fill is also used to draw shapes.parameters are 1st colour of shape,2nd shapename=[x-cordinate,y-cordinate,height,width].
        
        pygame.display.update()#then update all changes

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
            randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
            snakeLength+=1
        clock.tick(FPS)#we have set fps=20

    
    pygame.quit() # to quit pygame
    quit() # to quit python.

gameLoop()    
