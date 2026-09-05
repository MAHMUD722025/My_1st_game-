import asyncio
import random
import pygame

pygame.init()

WIDTH, HEIGHT = 720, 1500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hasina Eating Money")
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("Back3.png"), (WIDTH, HEIGHT))
start_background = pygame.transform.scale(pygame.image.load("Back2.png"), (WIDTH, HEIGHT))
money = pygame.transform.scale(pygame.image.load("Money.png"), (150, 100))
bowl = pygame.transform.scale(pygame.image.load("Hasina3.png"), (200, 300))
left_button = pygame.transform.scale(pygame.image.load("Left.png"), (200, 200))
right_button = pygame.transform.scale(pygame.image.load("Right.png"), (200, 200))
score_button = pygame.transform.scale(pygame.image.load("Score_button.png"), (300, 50))
hasina_button = pygame.transform.scale(pygame.image.load("Hasina palayna.png"), (700, 100))
start_button = pygame.transform.scale(pygame.image.load("Start.png"), (400, 200))
quit_button = pygame.transform.scale(pygame.image.load("Exit.png"), (400, 300))
restart_button = pygame.transform.scale(pygame.image.load("Restart.png"), (300, 150))

left_rect = pygame.Rect(50, 1100, 200, 200)
right_rect = pygame.Rect(450, 1100, 200, 200)
start_rect = pygame.Rect(150, 900, 400, 200)
quit_rect = pygame.Rect(140, 1000, 400, 300)
restart_rect = pygame.Rect(210, 900, 300, 150)

score = 0
num_of_money = 15
MONEY_FALL_SPEED = 850.0
BOWL_SPEED = 1100.0
money_x = [random.randint(50, 550) for _ in range(num_of_money)]
money_y = [random.randint(0, 300) for _ in range(num_of_money)]


def draw_text(text, x, y, size=40, color=(0, 0, 0)):
    font = pygame.font.SysFont(None, size)
    screen.blit(font.render(text, True, color), (x, y))


def reset_game():
    global score
    score = 0
    for i in range(num_of_money):
        money_x[i] = random.randint(50, 550)
        money_y[i] = random.randint(0, 300)


async def show_start_screen():
    while True:
        screen.blit(start_background, (0, 0))
        screen.blit(start_button, (150, 900))
        screen.blit(quit_button, (140, 1000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos):
                    return False
                if start_rect.collidepoint(event.pos):
                    return True
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)


async def game_over_screen():
    while True:
        screen.blit(background, (0, 0))
        draw_text("Game Over", 180, 600, size=100, color=(255, 0, 0))
        draw_text(f"Final Score: {score}", 200, 750, size=60, color=(255, 255, 255))
        screen.blit(restart_button, (210, 900))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos):
                reset_game()
                return True
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)


async def main():
    global score

    if not await show_start_screen():
        pygame.quit()
        return

    # IMPORTANT for browsers: initialize the audio mixer only AFTER
    # the user has pressed Start, so the browser audio context is unlocked.
    money_sound = None
    try:
        if pygame.mixer.get_init() is None:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
        money_sound = pygame.mixer.Sound("Unnoyon.ogg")
        money_sound.set_volume(0.8)
    except pygame.error:
        money_sound = None

    bowl_x = 600.0
    bowl_y = 1130
    moving_left = False
    moving_right = False
    running = True

    while running:
        dt = clock.tick(60) / 1000.0
        dt = min(dt, 0.05)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_rect.collidepoint(event.pos):
                    moving_left = True
                elif right_rect.collidepoint(event.pos):
                    moving_right = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if left_rect.collidepoint(event.pos):
                    moving_left = False
                if right_rect.collidepoint(event.pos):
                    moving_right = False

        if moving_left:
            bowl_x -= BOWL_SPEED * dt
        if moving_right:
            bowl_x += BOWL_SPEED * dt
        bowl_x = max(0, min(520, bowl_x))

        bowl_rect = screen.blit(bowl, (round(bowl_x), bowl_y))
        missed = False

        for i in range(num_of_money):
            money_y[i] += MONEY_FALL_SPEED * dt
            money_rect = screen.blit(money, (money_x[i], round(money_y[i])))

            if bowl_rect.colliderect(money_rect):
                money_x[i] = random.randint(50, 550)
                money_y[i] = random.randint(0, 300)
                score += 1

                # Play Unnoyon.ogg ONLY when money is caught.
                # Stop the previous copy so the sound never overlaps itself.
                if money_sound is not None:
                    money_sound.stop()
                    money_sound.play()

            if money_y[i] > 1300:
                missed = True
                break

        screen.blit(left_button, (50, 1100))
        screen.blit(right_button, (450, 1100))
        screen.blit(score_button, (1, 10))
        screen.blit(hasina_button, (10, 50))
        draw_text(f"Score: {score}", 30, 20, size=50)
        draw_text("Sheikh hasina don't run away.", 70, 70, size=60)
        pygame.display.update()
        await asyncio.sleep(0)

        if missed:
            if not await game_over_screen():
                running = False

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
