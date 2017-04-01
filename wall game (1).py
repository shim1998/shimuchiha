import os
import random
import pygame
import sys
from Tkinter import *
class Player(object):

    def __init__(self,x,y):
        self.rect = pygame.Rect(x, y, 12, 12)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):


        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

        for destruct in destruction:
            if self.rect.colliderect(destruct.rect):
                if dx > 0:
                    top = Tk()
                    L1 = Label(top,text="You Lose")
                    L1.pack()
                    top.mainloop()
                    print "You lose"
                    pygame.quit()
                    sys.exit()
                if dx < 0:
                    top = Tk()
                    L1 = Label(top,text="You Lose")
                    L1.pack()
                    top.mainloop()
                    print "You lose"
                    pygame.quit()
                    sys.exit()
                if dy > 0:
                    top = Tk()
                    L1 = Label(top,text="You Lose")
                    L1.pack()
                    top.mainloop()
                    print "You lose"
                    pygame.quit()
                    sys.exit()
                if dy < 0:
                    top = Tk()
                    L1 = Label(top,text="You Lose")
                    L1.pack()
                    top.mainloop()
                    print "You lose"
                    pygame.quit()
                    sys.exit()
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Destruction(object):

    def __init__(self,pos):
        destruction.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()


pygame.display.set_caption("DUO")
screen = pygame.display.set_mode((1000, 256))
font = pygame.font.SysFont('Calibri', 25, True, False)
font2= pygame.font.SysFont('Calibri', 50, True, False)
clock = pygame.time.Clock()
walls = []
destruction=[]
points=[]
player = Player(16,16)
player2 = Player(336,16)
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                   W                   W",
"W                   W                   W",
"WXXXXXXXXXXXXXXXXXX W XXXXXXXXXXXXXXXXXXW",
"W                   W                   W",
"W                   W                   W",
"WXXXXXXXXXX XXXXXXXXWXXX XXXXXXXXXXXXXXXW",
"W                   W                   W",
"W                   W                   W",
"W XXXXXXXXXXXXXXXXXXW XXXXXXXXXX DDDDDDDW",
"W                   W                   W",
"W                   W                   W",
"WXXXXXXXXXXXXXWWXXX WXXXXXXXXXXXXXX WWWWW",
"W                   W                   W",
"WE                  WF                  W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]
# Parse the level string above. W = wall, E = exit, F=exit
x = y = 0
for row in level:
    for col in row:
        if col == "X":
            a=random.randint(0,10)
            if a%2==0 and not a%3==0:
                Wall((x,y))
            if a%2!=0:
                Destruction((x,y))
            if a%2==0 and a%3==0:
                pass
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        if col == "F":
            end_rect2 = pygame.Rect(x, y, 16, 16)
        if col == "D":
            Destruction((x,y))
        x += 16
    y += 16
    x = 0
x=""
running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
        player2.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
        player2.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
        player2.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
        player2.move(0, 2)
    if player.rect.colliderect(end_rect) and player2.rect.colliderect(end_rect2):
        top = Tk()
        L1 = Label(top,text="You Win")
        L1.pack()
        top.mainloop()
        print "You win"
        pygame.time.wait(1000)
        pygame.quit()
        sys.exit()

    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for destruct in destruction:
        pygame.draw.rect(screen,(255,0,255),destruct.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect2)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.draw.rect(screen, (255, 200, 0), player2.rect)
    text=font2.render("INSTRUCTIONS", True, (255,255,255))
    screen.blit(text, [680, 10])
    text2=font.render("1.Use arrow keys to navigate", True,(255,255,255))
    screen.blit(text2,[670,70])
    text3=font.render("the yellow blocks through ",True,(255,255,255))
    screen.blit(text3,[690,100])
    text4=font.render("the maze!!",True,(255,255,255))
    screen.blit(text4,[690,130])
    text5=font.render("2.Don't touch the pink wall",True,(255,255,255))
    screen.blit(text5,[670,160])
    text6=font.render("3.Use the white wall to stop",True,(255,255,255))
    screen.blit(text6,[670,190])
    text7=font.render("one of the yellow block",True,(255,255,255))
    screen.blit(text7,[690,220])
    pygame.display.flip()