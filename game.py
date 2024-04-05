import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de la Bola")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variables de la bola
ball_radius = 20
ball_color = (255, 0, 0)
ball_pos = [screen_width // 2, screen_height // 2]
ball_speed = [0, 0]  # Velocidad inicial, bola quieta al principio

# Loop del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_speed = [-5, 0]  # Mover hacia la izquierda
            elif event.key == pygame.K_RIGHT:
                ball_speed = [5, 0]  # Mover hacia la derecha
            elif event.key == pygame.K_UP:
                ball_speed = [0, -5]  # Mover hacia arriba
            elif event.key == pygame.K_DOWN:
                ball_speed = [0, 5]  # Mover hacia abajo
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                ball_speed = [0, 0]  # Detener la bola cuando se suelta la tecla

    # Mover la bola solo si la velocidad es diferente de cero
    if ball_speed != [0, 0]:
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

    # Si la bola sale de la pantalla, aparece en el lado opuesto
    if ball_pos[0] - ball_radius > screen_width:
        ball_pos[0] = -ball_radius
    elif ball_pos[0] + ball_radius < 0:
        ball_pos[0] = screen_width + ball_radius
    if ball_pos[1] - ball_radius > screen_height:
        ball_pos[1] = -ball_radius
    elif ball_pos[1] + ball_radius < 0:
        ball_pos[1] = screen_height + ball_radius

    # Llenar la pantalla con color blanco
    screen.fill(WHITE)

    # Dibujar la bola en la pantalla
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(60)