import pygame

pygame.init()

width, height = 550,650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

# Ball properties
ball_radius = 20
ball_color = (255, 0, 0)
ball_x = width // 2
ball_y = height // 6
ball_speed_y = 0
gravity = 0.5
bounce_factor = -0.75

# Ground properties
ground_color = (0, 0, 0)
ground_rect = pygame.Rect(10, 620, 530, 10)

clock = pygame.time.Clock()
fps = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #apply gravity
    ball_speed_y += gravity
    ball_y += ball_speed_y
    
    if ball_y + ball_radius >= ground_rect.top:
        ball_y = ground_rect.top - ball_radius
        ball_speed_y *= bounce_factor
    
    screen.fill((255,255,255))
    pygame.draw.circle(screen, ball_color, (ball_x, int(ball_y)), ball_radius)
    pygame.draw.rect(screen, ground_color, ground_rect)
    pygame.display.flip()
    clock.tick(fps)
    
pygame.quit()
quit()
