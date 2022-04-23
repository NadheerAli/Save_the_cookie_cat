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

# Crear un rectangulo
# Si el rectángulo tendrá alguna interacción, usar la clase Rect. Si solo se quiere dibujar el rectángulo, usar una tupla
my_rect = pygame.Rect(100, 150, 300, 150)
# my_rect = (100, 150, 300, 150)

# Centrar rectángulo
my_rect.center = (width // 2, height // 2)

# Obtiene las coordenadas del rectángulo
# my_rect.x
# my_rect.y

# Mantener escuchar de eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Agregando un color (necesita actualizar la pantalla)
        surface.fill(my_color)
        # Agregar el rectángulo a la pantalla
        pygame.draw.rect(surface, white, my_rect)

        pygame.display.update()