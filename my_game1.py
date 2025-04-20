import pygame
import random
from pygame import mixer

# Initialize Pygame
pygame.init()
pygame.mixer.init()
#sound effect
catch_sound=pygame.mixer.Sound('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Unnoyon.mp3')
start_sound=pygame.mixer.Sound('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Start_music.mp3')
back_sound=pygame.mixer.Sound('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Back_music.mp3')

# Screen dimensions
background_width = 720
background_height = 1500
screen = pygame.display.set_mode((background_width, background_height))
pygame.display.set_caption("Apple Catch Game")

# Colors
white = (255, 255, 255)
blue = (100, 149, 237)  # Cornflower Blue

# Load Assets
background_img = pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Back3.png')
background = pygame.transform.scale(background_img, (background_width, background_height))

# Apple setup
apple_img = pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Money.png')
apple_width, apple_height = 150, 100
apple = pygame.transform.scale(apple_img, (apple_width, apple_height))
num_of_apples = 15
apple_x=[]
apple_y=[]
y_apple_velocity=[]
apple_rect = [] 

gravity = 0.05
for i in range(num_of_apples):
    apple_x.append(random.randint(50, 550))
    apple_y.append(random.randint(0, 300))
    y_apple_velocity.append(0)
    apple_rect.append(pygame.Rect(0, 0, apple_width, apple_height))  # Create a rect

# Player (Bowl)
bowl_img = pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Hasina3.png')
bowl_width, bowl_height = 200, 300
bowl = pygame.transform.scale(bowl_img, (bowl_width, bowl_height))


bowl_x, bowl_y = 680, 1130
bowl_x_speed = 0
# Load button images
#control button
left_button = pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/left.png')
right_button = pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Right.png')
button_width, button_height = 200, 200
left_button = pygame.transform.scale(left_button, (button_width, button_height))
right_button = pygame.transform.scale(right_button, (button_width, button_height))

left_button_x, left_button_y = 50, 1100
right_button_x, right_button_y = 450, 1100
left_button_rect = pygame.Rect(left_button_x, left_button_y, button_width, button_height)
right_button_rect = pygame.Rect(right_button_x, right_button_y, button_width, button_height)
#score button
score_button=pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Score button.png')
score_button_width=300
score_button_height=50
score_button=pygame.transform.scale(score_button,(score_button_width,score_button_height))
score_button_x=1
score_button_y=10
#hasina button
hasina_button=pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Hasina palayna.png')
button_width=700
button_height=100
hasina_button=pygame.transform.scale(hasina_button,(button_width,button_height))
hasina_button_x=10
hasina_button_y=50
#start screen
start_background = pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Back2.png')
start_background = pygame.transform.scale(start_background, (background_width, background_height))

start_button_img = pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Start.png')
start_button_img = pygame.transform.scale(start_button_img, (400, 200))
start_button_x = 150
start_button_y = 900
start_button_rect = pygame.Rect(start_button_x, start_button_y, 400, 200)
quit_img=pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Exit.png')
quit_img=pygame.transform.scale(quit_img,(400,300))
quit_x=140
quit_y=1000
quit_img_rect=pygame.Rect(quit_x,quit_y,400,300)
# Score
score = 0


# Font (Pygame built-in font)
def draw_text(text, x, y, size=40, color=(0, 0, 0)):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
def draw_write(text,x,y,size=40,color=(0,0,0)):
	font=pygame.font.SysFont(None,size)
	text_surface=font.render(text,True,color)
	screen.blit(text_surface,(x,y))


# Game variables
clock = pygame.time.Clock()
running = True
# game over screen
def game_over_screen():
    global score, apple_x, apple_y, y_apple_velocity

    back_sound.stop()
    restart_img = pygame.image.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/Restart.png')
    restart_img = pygame.transform.scale(restart_img, (300, 150))
    restart_rect = pygame.Rect(210, 900, 300, 150)

    while True:
        screen.blit(background,(0,0))  
        draw_text("Game Over", 180, 600, size=100, color=(255, 0, 0))
        draw_text(f"Final Score: {score}", 200, 750, size=60, color=(255, 255, 255))
        
        screen.blit(restart_img, (210, 900))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    # Reset all variables for restart
                    score = 0
                    for i in range(num_of_apples):
                        apple_x[i] = random.randint(50, 550)
                        apple_y[i] = random.randint(0, 10)
                        y_apple_velocity[i] = 0
                    back_sound.play(-1)
                    return  # Resume game

        pygame.display.update()
        clock.tick(60)

#start loop
def show_start_screen():
    start_sound.play()
    while True:
        
        screen.blit(start_background, (0, 0))
        screen.blit(start_button_img, (start_button_x, start_button_y))
        screen.blit(quit_img,(quit_x,quit_y))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
         

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_img_rect.collidepoint(event.pos):
                	pygame.quit()
                	exit()
                if start_button_rect.collidepoint(event.pos):
                    start_sound.stop()
                    return  # Exit the start screen and start the game

        pygame.display.update()
        clock.tick(60)
show_start_screen()

# Game Loop
back_sound.play(-1)
while running:
    
    screen.fill(blue)
    screen.blit(background, (0, 0))
    bowl_rect = screen.blit(bowl, (bowl_x, bowl_y))
    


    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if left_button_rect.collidepoint(event.pos):
                bowl_x_speed = -10
            elif right_button_rect.collidepoint(event.pos):
                bowl_x_speed = 10
        
        if event.type == pygame.MOUSEBUTTONUP:
            bowl_x_speed = 0

    # Move bowl
    bowl_x += bowl_x_speed
    if bowl_x<=0:
    	bowl_x=0
    elif bowl_x>=600:
    	bowl_x=600
    	
    

    # Update apples
    for i in range(num_of_apples):
        y_apple_velocity[i] += gravity
        apple_y[i] += y_apple_velocity[i]
        apple_rect[i] = screen.blit(apple, (apple_x[i], apple_y[i]))

        # Reset apple if it falls
        if apple_y[i] > 1300:
            game_over_screen()

        # Collision check
        if bowl_rect.colliderect(apple_rect[i]):
            apple_x[i] = random.randint(50, 550)
            apple_y[i] = random.randint(0, 300)
            y_apple_velocity[i] = 0
            score += 1
            catch_sound.play()
    left_button_rect = screen.blit(left_button, (left_button_x, left_button_y))
    right_button_rect = screen.blit(right_button, (right_button_x, right_button_y))
    score_button_rect=screen.blit(score_button,(score_button_x,score_button_y))
    hasina_button_rect=screen.blit(hasina_button,(hasina_button_x,hasina_button_y))
    # Display score
    draw_text(f"Score: {score}", 30, 20, size=50)
    draw_write("Sheikh hasina don't run away.",70,70,size=60)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()