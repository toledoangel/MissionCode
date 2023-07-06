import pygame
import pygame_menu

#inicializacion de pygame
pygame.init()
#dimensiones de la pantalla
pantalla = pygame.display.set_mode((700,400))
pygame.display.set_caption("Pygame")

class Game:
    screen = None

    def __init__(self, width, height, pantallas):

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fondo = pygame.image.load("Animaciones\Ariane5pequeño.svg")
        self.pantallas = pantallas
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.blit(self.fondo,(0,0))
            pygame.display.flip()

        self.clock.tick(60)


            # Capturar otros eventos (teclado, ratón, etc.)
            # ...
        #pygame.display.flip() mostrar los cambios
        #self.clock.tick(60)

        # Actualizar el estado del juego
        # ...

        #bucles que inicializan las diferentes clases

    #tipos de letra


#clases por pantallas

""" 1. Cuando explota
    2. CUando empieza, se cae y explota
    3. Cuando si funciona
"""

"""
menu
"""
def menu_principal():
    Game(700, 400, "Menu principal")

def elige_cohete():
    Game(700, 400, "Elige Cohete")

def instrucciones():
    Game(700, 400, "Instrucciones")




"""
menu que nos manda a cada pantalla, investigar lo de los temas
"""
menu = pygame_menu.Menu(height=400,
    theme=pygame_menu.themes.THEME_DARK,
    title='Cohete',
    width=600)



menu.add.button('Menu Principal', menu_principal)
menu.add.button('Elige tu cohete',elige_cohete)
menu.add.button('Instrucciones', instrucciones)
menu.add.button('Quit', pygame_menu.events.EXIT)



if __name__ == '__main__':
    menu.mainloop(pantalla)