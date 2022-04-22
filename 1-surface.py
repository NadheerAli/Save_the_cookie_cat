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

# Mantener escuchar de eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()