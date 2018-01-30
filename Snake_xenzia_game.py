import pygame

pygame.init() #initialize a game
#declaring the colours in RGB in tuples wecan also do it in list.
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600)) #setting surface or display for the game 800 and 600 are lenngth and width pixels in a tuple.
pygame.display.set_caption('Snake Xenzia') #setting the name of the game.which appears at the top.

pygame.display.update() 

gameExit = False #variable that decides whrn to exit the game,initially it is false bcoz we want to play.

#main gaming loop
while not gameExit:
    for event in pygame.event.get(): #to get the events which involve mouseclick,buttonclick,quitting etc...
        if event.type == pygame.QUIT: #here type is type of event i.e mouse/buttn click or quit,here when event is equal to QUIT .
            gameExit = True #when event type=QUIT then exit the game.

    gameDisplay.fill(white) #set the background of game ,white
    pygame.display.update()#then update all changes


pygame.quit() # to quit pygame
quit() # to quit python
