import pygame 
import random
import pygame.mixer
pygame.init()
pygame.mixer.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Define the Screen
W = 800
L = 600

win = pygame.display.set_mode((W, L))
text_title = "Catch the Ball"
pygame.display.set_caption(text_title)

# Define the sound
YesSound = pygame.mixer.Sound("E:\\Abhijit@E)\\Projects\\Catch the boll\\Gain.mp3")

# Define the text
textAct = font.render("Catch The ball", True, (200, 0, 0))
text = textAct.get_rect()
text.x = 300
text.y = 200


textAct2 = font.render("Start", True, (255, 255, 255))
text2 = textAct2.get_rect()
text2.x = 350
text2.y = 310

textAct3 = font.render("Next Level", True, (255, 255, 255))
text3 = textAct3.get_rect()
text3.x = 350
text3.y = 310

textAct4 = font.render("YOU WIN :D", True, (255, 215, 0))
text4 = textAct4.get_rect()
text4.x = 350
text4.y = 310



# Define the Game
Waterimg = pygame.image.load("E:\\Abhijit@E)\\Projects\\Catch the boll\\Water.png")
Water = Waterimg.get_rect()
Water.x = 300
Water.y = 300

Waterholderimg = pygame.image.load("E:\\Abhijit@E)\\Projects\\Catch the boll\\Bucket.png")
Waterholder = Waterholderimg.get_rect()
Waterholder.x = 400
Waterholder.y = 500

droplitimg = pygame.image.load("E:\\Abhijit@E)\\Projects\\Catch the boll\\Droplit.png")
droplit = droplitimg.get_rect()
xboi = random.randint(100, 800)
droplit.x = xboi
droplit.y = 50

# Defineing Collision
def check_collision(Waterholder, droplet):
    return Waterholder.colliderect(droplet)

# Define Points

# Define the Start Box
Box_col = (0, 0, 0)
Box = pygame.Rect(270, 300, 250, 50)

# Define The level - 2 box
Box2_col = (0, 0, 0)
Box2 = pygame.Rect(270, 300, 250, 50)
# Define The Variables
BG = (0, 255, 255)
Start_screen_Dont_see = False
GameStart = False
player_speed = 20
droplit_speed = 1
time = 120
# Define the Points
points = 0
points_col = (0, 0, 0)
def update_point_text():
    global points_text, points_rect
    points_text = font.render("Points:" + str(points), True,  points_col)   
    points_rect = points_text.get_rect()
    points_rect.x = 0
    points_rect.y = 0

update_point_text()
# while loop

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Box.collidepoint(event.pos):
                Start_screen_Dont_see = True
       
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            Waterholder.x += player_speed
        if key[pygame.K_a]:
            Waterholder.x -= player_speed
        

        # BUNDARIES

    win.fill(BG)
    if Start_screen_Dont_see == False: 
        pygame.draw.rect(win, Box_col, Box)
        win.blit(textAct2, text2)
        win.blit(textAct, text)
        win.blit(Waterimg, Water)
        GameStart = True

    elif GameStart:
        droplit.y += droplit_speed
        win.blit(Waterholderimg, Waterholder)
        win.blit(droplitimg, droplit)
        win.blit(points_text, points_rect)
        time -= 1
        if droplit.y > L:
            droplit.x = random.randint(100, 800)
            droplit.y = 0

        if check_collision(Waterholder, droplit):
            droplit.x = random.randint(100, 800)
            droplit.y = 0
            YesSound.play()
            points += 1
            update_point_text()
        if points == 10:
            droplit_speed = float(1.5)
        if Waterholder.x > W:
            Waterholder.x -= W
        elif Waterholder.x > W:
            Waterholder.x += W
        if points == 20:
            droplit_speed = 3
        if points == 100:
            win.blit(textAct4, text4)
            droplit_speed = 0
            Dontsee =True
            
        
               
    pygame.display.update()

pygame.quit()
