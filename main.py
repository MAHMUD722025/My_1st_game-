import asyncio
import random
import pygame

pygame.init()

# Screen
WIDTH, HEIGHT = 720, 1500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hasina Eating Money")
clock = pygame.time.Clock()

# Assets must stay inside the GitHub repository.
def asset(name):
    return name

background = pygame.transform.scale(pygame.image.load(asset("Back3.png")), (WIDTH, HEIGHT))
start_background = pygame.transform.scale(pygame.image.load(asset("Back2.png")), (WIDTH, HEIGHT))
money = pygame.transform.scale(pygame.image.load(asset("Money.png")), (150, 100))
bowl = pygame.transform.scale(pygame.image.load(asset("Hasina3.png")), (200, 300))
left_button = pygame.transform.scale(pygame.image.load(asset("Left.png")), (200, 200))
right_button = pygame.transform.scale(pygame.image.load(asset("Right.png")), (200, 200))
score_button = pygame.transform.scale(pygame.image.load(asset("Score_button.png")), (300, 50))
hasina_button = pygame.transform.scale(pygame.image.load(asset("Hasina palayna.png")), (700, 100))
start_button = pygame.transform.scale(pygame.image.load(asset("Start.png")), (400, 200))
quit_button = pygame.transform.scale(pygame.image.load(asset("Exit.png")), (400, 300))
restart_button = pygame.transform.scale(pygame.image.load(asset("Restart.png")), (300, 150))

left_rect = pygame.Rect(50, 1100, 200, 200)
right_rect = pygame.Rect(450, 1100, 200, 200)
start_rect = pygame.Rect(150, 900, 400, 200)
quit_rect = pygame.Rect(140, 1000, 400, 300)
restart_rect = pygame.Rect(210, 900, 300, 150)

score = 0
num_of_money = 15
gravity = 0.05
money_x = [random.randint(50, 550) for _ in range(num_of_money)]
money_y = [random.randint(0, 300) for _ in range(num_of_money)]
money_velocity = [0 for _ in range(num_of_money)]


def draw_text(text, x, y, size=40, color=(0, 0, 0)):
    font = pygame.font.SysFont(None, size)
    screen.blit(font.render(text, True, color), (x, y))


def reset_game():
    global score
    score = 0
    for i in range(num_of_money):
        money_x[i] = random.randint(50, 550)
        money_y[i] = random.randint(0, 300)
        money_velocity[i] = 0


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

    bowl_x = 600
    bowl_y = 1130
    bowl_speed = 0
    running = True

    while running:
        screen.blit(background, (0, 0))
        bowl_rect = screen.blit(bowl, (bowl_x, bowl_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_rect.collidepoint(event.pos):
                    bowl_speed = -10
                elif right_rect.collidepoint(event.pos):
                    bowl_speed = 10
            elif event.type == pygame.MOUSEBUTTONUP:
                bowl_speed = 0

        bowl_x += bowl_speed
        bowl_x = max(0, min(600, bowl_x))

        missed = False
        for i in range(num_of_money):
            money_velocity[i] += gravity
            money_y[i] += money_velocity[i]
            money_rect = screen.blit(money, (money_x[i], money_y[i]))

            if bowl_rect.colliderect(money_rect):
                money_x[i] = random.randint(50, 550)
                money_y[i] = random.randint(0, 300)
                money_velocity[i] = 0
                score += 1

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
        clock.tick(60)
        await asyncio.sleep(0)

        if missed:
            if not await game_over_screen():
                running = False

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
