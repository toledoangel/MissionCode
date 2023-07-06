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

class Pantalla:

    fondo = pygame.image.load("Imagenes/Mockups/menu-principal.png")

    #Elementos que se repiten en las distintas pantallas
    def __init__(self, fondo):
        self.fondo = pygame.image.load(fondo).convert()
        self.start = pygame.image.load('Imagenes/Animaciones/cohete.png')
        self.boton_start = self.start.get_rect(center=(100,200))


    #Muestra la pantalla
    def mostrar_pantalla(self):
        pantalla.blit(self.fondo, (0, 0))
        pygame.display.flip()


class MenuPrincipal(Pantalla):
    def __init__(self):
        super().__init__("Imagenes/Mockups/instrucciones.png")
        boton_start = self.boton_start
        fuente = pygame.font.SysFont('Arial', 32)
        self.texto_cohete = fuente.render('Programa tu propio cohete', True, BLANCO)


class PantallaDespliegue(Pantalla):
    def __init__(self):
        super().__init__("Imagenes/Mockups/despliegue.png")

class PantallaEligeCohete(Pantalla):
    def __init__(self):
        super().__init__("Imagenes/Mockups/elige-cohete.png")

"""class PantallaInstrucciones(Pantalla):
    def __init__(self):
        super().__init__("Imagenes/Mockups/instrucciones.png")
        #agregar imagenes
        self.imagen_boton_1 = pygame.image.load('ruta_imagen_1.png')
        self.imagen_boton_2 = pygame.image.load('ruta_imagen_2.png')
        self.imagen_boton_3 = pygame.image.load('ruta_imagen_3.png')

        # Cargar imagen de fondo
        self.fondo_instrucciones = pygame.image.load('Imagenes/Mockups/instrucciones.png')

        # Renderizar texto "Elige tu cohete"
        fuente = pygame.font.SysFont('Arial', 32)
        self.texto_cohete = fuente.render('Elige tu cohete', True, BLANCO)

        # Definir posición y tamaño de los botones de imagen
        self.boton_1_rect = self.imagen_boton_1.get_rect(topleft=(100, 200))
        self.boton_2_rect = self.imagen_boton_2.get_rect(topleft=(300, 200))
        self.boton_3_rect = self.imagen_boton_3.get_rect(topleft=(500, 200))

        # Definir posición del botón de inicio
        self.boton_inicio_rect = pygame.Rect(350, 400, 100, 50)

        pantalla.blit(self.fondo_instrucciones, (0, 0))
        pantalla.blit(self.texto_cohete, (ANCHO // 2 - self.texto_cohete.get_width() // 2, 100))
        pantalla.blit(self.imagen_boton_1, self.boton_1_rect)
        pantalla.blit(self.imagen_boton_2, self.boton_2_rect)
        pantalla.blit(self.imagen_boton_3, self.boton_3_rect)
        pygame.draw.rect(pantalla, BLANCO, self.boton_inicio_rect)
        pygame.display.flip()
"""

#def mostrar_pantalla_instrucciones():
 #   global pantalla_actual
    #pantalla_actual = pantalla_instrucciones

def mostrar_pantalla_principal():
    global pantalla_actual
    pantalla_actual = MenuPrincipal()
    #pantalla_principal = MenuPrincipal()


menu = pygame_menu.Menu(height=400,
    theme=pygame_menu.themes.THEME_DARK,
    title='MissionCode',
    width=600)

#instanciar las clases
#pantalla_despliegue = PantallaDespliegue()
#pantalla_elige_cohete = PantallaEligeCohete()
#pantalla_instrucciones = PantallaInstrucciones()




#menu.add.button('Pantalla de Despliegue', mostrar_pantalla_despliegue)
#menu.add.button('Pantalla de Elegir Cohete', mostrar_pantalla_elige_cohete)

#botones del menú principal
#menu.add.button('Pantalla de Instrucciones', mostrar_pantalla_instrucciones)


menu.add.button('Start',mostrar_pantalla_principal)
menu.add.button('Salir', pygame_menu.events.EXIT)


mostrar_menu = True
#realiza el cambio entre pantallas
pantalla_actual = None


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pantalla_actual.mostrar_pantalla_principal()

            mostrar_menu = not mostrar_menu

        if mostrar_menu:
            pantalla.fill(BLANCO)
            menu.update(events)
            menu.mainloop(pantalla, disable_loop=True)
        else:
            if menu.is_enabled():
                if menu.get_selected_widget():
                    pantalla_actual.mostrar_pantalla_principal()
            elif pantalla_actual is not None:
                pantalla_actual.mostrar_pantalla()

        pygame.display.flip()