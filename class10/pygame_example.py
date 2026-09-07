import pygame
import random

pygame.init()

# 視窗
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Simple Pygame")

clock = pygame.time.Clock()

# 玩家
player = pygame.image(100, 100, 50, 50)
speed = 5

# 目標
target = pygame.Rect(
    random.randint(0, WIDTH - 40),
    random.randint(0, HEIGHT - 40),
    40,
    40
)

score = 0
font = pygame.font.Font(None, 36)

running = True

while running:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 鍵盤控制
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed

    if keys[pygame.K_RIGHT]:
        player.x += speed

    if keys[pygame.K_UP]:
        player.y -= speed

    if keys[pygame.K_DOWN]:
        player.y += speed

    # 不讓玩家跑出畫面
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    if player.top < 0:
        player.top = 0

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT

    # 碰撞
    if player.colliderect(target):
        score += 1
        target.x = random.randint(0, WIDTH - target.width)
        target.y = random.randint(0, HEIGHT - target.height)

    # 畫面
    screen.fill((240, 240, 240))

    pygame.draw.rect(screen, (50, 100, 255), player)
    pygame.draw.rect(screen, (255, 70, 70), target)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # 60 FPS
    clock.tick(60)

pygame.quit()