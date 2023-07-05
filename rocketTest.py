import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configurar la pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Videojuego de Cohetes")

# Cargar las imágenes del cohete
cohete_imagen = pygame.image.load("Recursos\cohete.png")

# Obtener el rectángulo del cohete y su posición inicial
cohete_rect = cohete_imagen.get_rect()
cohete_rect.centerx = 30 // 2
cohete_rect.bottom = 30 // 2

# Variables para la animación
velocidad_cohete = 5
cohete_subiendo = False

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el cohete
    if cohete_subiendo:
        cohete_rect.y -= velocidad_cohete
    else:
        cohete_rect.y += velocidad_cohete

    # Cambiar la dirección del cohete cuando alcanza los límites de la pantalla
    if cohete_rect.top <= 0:
        cohete_subiendo = False
    elif cohete_rect.bottom >= alto_pantalla:
        cohete_subiendo = True

    # Dibujar en la pantalla
    pantalla.fill(NEGRO)
    pantalla.blit(cohete_imagen, cohete_rect)

    # Actualizar la pantalla
    pygame.display.flip()
