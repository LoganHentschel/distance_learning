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
# #
clock = pygame.time.Clock()
#
score = 0
# #
bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('struck.wav')
#
background_music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

# # # # #
# # # # #
#This is optional; for small/simple games you don't have to make these classes, but for bigger, more complex games... its much more recomended
#classes!
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
        self.right = True
        self.walk_count = 0
        self.standing = True
        #
        self.hitbox = (self.x + 20, self.y, 28, 60)
    #
    def draw(self, win):
        if self.walk_count+1 >= 27:
            self.walk_count = 0
        #
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(walkRight[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))
        self.hitbox = (self.x + 17, self.y+11, 29, 52)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    
    def hit(self):
        self.x = 60
        self.y = 410
        self.walk_count = 0
        #
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5 points', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        #
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
# #
class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        #
        self.walk_count = 0
        self.vel = 3
        self.path = (self.x, self.end)
        #
        self.hitbox = (self.x + 17, self.y+2, 31, 57)
        self.health = 10
        self.visable = True
    #
    def draw(self, win):
        self.move()
        if self.visable:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0
            #
            if self.vel > 0: #right
                win.blit(self.walkRight[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
            else:
                win.blit(self.walkLeft[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
            #
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20,50,10)) #red health bar
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20,50-(5 * (10-self.health)),10)) #green health bar
            self.hitbox = (self.x + 17, self.y+2, 31, 57)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    #
    def move(self):
        if self.vel > 0: #moving right
            if self.x + self.vel < self.path[1]: #move forward
                self.x += self.vel
            else: #change directions
                self.vel = self.vel * -1
                self.walk_count = 0
        else: #moving left
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
    #
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visable = False
        print('hit')


# #
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing #the velocity/speed of the bullet
        #
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y,), self.radius)

# # # # #
# # # # #
#functions!
def  redrawGameWindow():
    win.blit(bg, (0,0))
    #
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (370, 10))
    #
    character.draw(win)
    goblin.draw(win)

    #
    for bullet in bullets:
        bullet.draw(win)
    # #
    pygame.display.update() 

# # # # #
#main loop
font = pygame.font.SysFont('comicsans', 30, True) #last two variables are ture/false for bold & italics

#
character = player(200,410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
#
# :o it's shoopdawoop
shootLoop = 0
#
bullets = []
#
run = True
#
while run:
    clock.tick(27)
    #
    if character.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and character.hitbox[1] + character.hitbox[3] > goblin.hitbox[1]:
        if character.hitbox[0] + character.hitbox[2] > goblin.hitbox[0] and character.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            character.hit()
            score -= 5

    #
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop> 3:
        shootLoop = 0
# # #
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    #
    for bullet in bullets:
        #check if object (bullet) is 1. above the bottom of the rectangle & 2. below the top of the rectangle
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        #
        if bullet .x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    # #
    keys = pygame.key.get_pressed()
    #
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if character.left:
            facing = -1
        else:
            facing = 1
        #
        if len(bullets) < 5:
            bullets.append(projectile(round(character.x + character.width //2), round(character.y + character.height //2), 6, (0,0,0), facing))
        #
        shootLoop = 1
    # #
    if keys[pygame.K_LEFT] and (character.x > character.vel):
        character.x -= character.vel
        character.left = True 
        character.Right = False
        character.standing = False
    elif keys[pygame.K_RIGHT] and character.x < (screenwidth-character.width): #-character.vel / -vel
        character.x += character.vel
        character.right = True
        character.left = False
        character.standing = False
    else:
        #character.standing = True #having this here creates a bug??? o_o weird
        character.walk_count = 0
        # #
    if not (character.isJump):
        if keys[pygame.K_UP]:
            character.isJump = True
            #character.right = False
            #character.left = False
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