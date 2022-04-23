# Importar librerías
import sys
import pygame

# Iniciar pygame
pygame.init()

# Crear ventana
width = 500
height = 600
surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Mi primer videojuego con pygame')

my_color = (136, 216, 192)
white = (255, 255, 255)
green = (0 , 255, 0)

# Mantener escuchar de eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Agregando un color (necesita actualizar la pantalla)
        surface.fill(my_color)

        # Las figuras se irán dibujando conforme se declaren
        pygame.draw.rect(surface, white, (100, 100, 50, 50))
        pygame.draw.circle(surface, green, (300, 300), 50)
        pygame.draw.line(surface, (0 ,0,0), (100, 100), (300, 300))

        pygame.display.update()