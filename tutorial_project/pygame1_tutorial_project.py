import pygame
pygame.init()
# # # # #
#setting up gaming window; parenthases variables are height/width
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
#
screenwidth = 500
screenheight = 500
# #
#puts all the image sprites into python - pasted because many images is tedious 
#**It is possible to simply flip the images in reguards to right & left; both are separate in this case
#use ' pygame.path.join ('folder_name', sprite_name') ' to get images from different directories [ or 'folder/'sprite name' ?]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
#omg theres so many whyyyy... lukcily only had to paste it this time lol. going to be soo tedious when I have to do it myself
# # #
#main variables
x = 50
y = 50
width = 64
height = 64
vel = 5 #velocity; how far the character moves in any direction
#
#jump variables
isJump = False
JumpCount = 10
#
#animaion variables
left = False
right = False
walk_count = 0

# # # # 
#functions!
def  redrawGameWindow():
    global walk_count

    win.blit(bg, (0,0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height)) 
    pygame.display.update() 

# # # # # # # 
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
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < (screenwidth-width): #'-vel' ?
        x += vel
    if not  (isJump) :
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -10:
            neg = 1
            if JumpCount < 0:
                neg = -1
            y -= (JumpCount**2)/2*neg
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10
            
# # #
#Call functions at end!
redrawGameWindow()

# # # # # # #
pygame.quit()