import pygame
pygame.init()
# # # # # # #
# # # # # # # 
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
#
screenwidth = 500
screenheight = 500
# #
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

# # # # #
# # # # #
#This is optional; for small/simple games you don't have to make these classes, but for bigger, more complex games... its much more recomended
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #
        self.vel = 5
        self.isJump = False
        self.JumpCount = 10
        #
        self.left = False
        self.right = False
        self.walk_count = 0
# #
    def draw(self, win):
        if self.walk_count+1 >= 27:
            self.walk_count = 0
        #
        if self.left:
            win.blit(walkLeft[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        elif self.right:
            win.blit(walkRight[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        else:
            win.blit(char, (self.x,self.y))
# # # # #
# # # # #
#functions!
def  redrawGameWindow():
    win.blit(bg, (0,0))
    character.draw(win)
    pygame.display.update() 

# # # # #
#main loop
character = player(300,410, 64, 64)
run = True
#
while run:
    clock.tick(27)
# # #
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    # #
    keys = pygame.key.get_pressed()
    #
    if keys[pygame.K_LEFT] and character.x > character.vel:
        character.x -= character.vel
        character.left = True 
        character.Right = False
    elif keys[pygame.K_RIGHT] and character.x < (screenwidth-character.width): #-character.vel / -vel
        character.x += character.vel
        character.right = True
        character.left = False
    else:
        character.right = False
        character.left = False
        character.walk_count = 0
        # #
    if not (character.isJump) :
        if keys[pygame.K_SPACE]:
            character.isJump = True
            character.right = False
            character.left = False
            character.walk_count = 0
    else:
        if character.JumpCount >= -10:
            neg = 1
            if character.JumpCount < 0:
                neg = -1
            character.y -= (character.JumpCount**2)/2*neg
            character.JumpCount -= 1
        else:
            character.isJump = False
            character.JumpCount = 10
    redrawGameWindow()

# # # # # # #
# # # # # # #
pygame.quit()