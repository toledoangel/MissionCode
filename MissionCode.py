import sys
import pygame
import pygame_menu

ANCHO = 800
ALTO = 600

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("MissionCode")

class Pantalla():


menu = pygame_menu.Menu(height=400,
    theme=pygame_menu.themes.THEME_DARK,
    title='MissionCode',
    width=600)

pantalla_instrucciones = PantallaInstrucciones()

menu.add.button('Pantalla de Instrucciones', mostrar_pantalla_instrucciones)
menu.add.button('Salir', pygame_menu.events.EXIT)

#bucle principal
mostrar_menu = True
pantalla_actual = None

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if pantalla_actual is None:
                mostrar_menu = not mostrar_menu
            else:
                pantalla_actual = None

        if mostrar_menu:
            menu.update(events)
        else:
            if pantalla_actual is not None:
                pantalla_actual.mostrar_pantalla()

    if mostrar_menu:
        pantalla.fill(BLANCO)
        menu.mainloop(pantalla, disable_loop=True)
        menu.update(pygame.event.get())

    pygame.display.flip()



