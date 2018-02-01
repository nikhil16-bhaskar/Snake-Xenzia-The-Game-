import pygame

pygame.init() #initialize a game
#declaring the colours in RGB in tuples wecan also do it in list.
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600)) #setting surface or display for the game 800 and 600 are lenngth and width pixels in a tuple.
pygame.display.set_caption('Snake Xenzia') #setting the name of the game.which appears at the top.

lead_x=100
lead_y=100
lead_x_change=0
lead_y_change=0
#count=0
clock=pygame.time.Clock()
gameExit = False #variable that decides whrn to exit the game,initially it is false bcoz we want to play.

#main gaming loop
while not gameExit:
    for event in pygame.event.get(): #to get the events which involve mouseclick,buttonclick,quitting etc...
        if event.type == pygame.QUIT: #here type is type of event i.e mouse/buttn click or quit,here when event is equal to QUIT .
            gameExit = True #when event type=QUIT then exit the game.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
                #print("x -ve")
                #count+=1
            elif event.key == pygame.K_RIGHT:
                lead_x_change = +10
                lead_y_change = 0
                #print("x +ve")
                #count+=1
                
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
                #print("x +ve")
                #count+=1
            elif event.key == pygame.K_DOWN:
                lead_y_change = +10
                lead_x_change = 0
                #print("x +ve")
                #count+=1
    lead_x += lead_x_change
    lead_y += lead_y_change
    #if count==50:
        #break
    print("lead_changed")
    gameDisplay.fill(white) #set the background of game ,white
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])# to draw rectangle on gaming screen,so 1st parameter is where do we want to draw it,2nd what colour,3rd a list of[x-cordinate,y-cordinate,height of rect,width of rect].
    
    #(this is more accelerated)gameDisplay.fill(red,rect=[200,200,30,30])#fill is also used to draw shapes.parameters are 1st colour of shape,2nd shapename=[x-cordinate,y-cordinate,height,width].
    
    pygame.display.update()#then update all changes
    clock.tick(20)
   
pygame.quit() # to quit pygame
quit() # to quit python.
