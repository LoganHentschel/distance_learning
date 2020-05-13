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
width = 40
height = 60
vel = 5 #velocity; how far the character moves in any direction

# # #
#main loops
run = True
while run:
    pygame.time.delay(100) #creathes a sort of clock; also makes things have a delay so they dont happen instantainiously; 100 miliseconds
# # # # #
    for event in pygame.event.get(): #creates/gets a list of all the events that happen
        if event.type == pygame.QUIT: #if the big red button in the corner is pushed...
            run = False
# # #
#list of...
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    win.fill((0,0,0))

# # #
    #draws rectangle; other shapes have their code on the pygame website 
    #everything in python is a surface, paranthases variables are the surfaces the rectangle is put on, then RGB, then the rect (defining its dimensions)
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height)) 
    pygame.display.update() #gets the rect to actually display on the screen [green rectangle located at 50,50, with a wdith of 40 and aheight of 60]




# # # # # # # 
pygame.quit()