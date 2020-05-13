import pygame
pygame.init()
# # # # #
#setting up gaming window; parenthases variables are height/width
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

# # #
#main variables
x = 50
y = 50
wdith = 40
height = 60
velocity = 5

# # #
#main loops
run = True

while run:
    pygame.time.delay(100) #creathes a sort of clock; also makes things have a delay so they dont happen instantainiously; 100 miliseconds

    for event in pygame.event.get(): #creates/gets a list of all the events that happen
        if event.type == pygame.QUIT: #if the big red button in the corner is pushed...
            run = False

pygame.quit()

