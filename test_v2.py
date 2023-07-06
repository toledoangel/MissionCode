import sys
import pygame
import pygame_menu

#definicion del alto y ancho
ANCHO = 600
ALTO = 400

#colores de fondo
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

#metodos que necesita pygame para iniciar
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("MissionCode")


#para cambiar de pantalla
pantalla_actual = None

class Menu_Principal():

    def __init__(self):
        self.fondo = pygame.image.load("Imagenes/Mockups/menufinal.png")
        self.boton_start = pygame.image.load('Imagenes/Animaciones/cohete.png')

        #self.fondo = self.fondo.convert()

        #super().__init__("Imagenes/Mockups/menu-principal.png")
        """self.boton_start = pygame_menu.widgets.Button(title='',
                                                       image_path='Imagenes/Animaciones/cohete.png',
                                                       image_width=100,
                                                       image_height=100,
                                                       onselect=self.funcion_del_boton)
        """
    def funcion_del_boton(self, boton_start):
        pantalla.blit(self.boton_start, (180, 50))


menu_principal = Menu_Principal()

while True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # pantalla_actual.mostrar_pantalla_principal()
            pantalla_actual = menu_principal



    pantalla.blit(menu_principal.fondo,(0, 0))
    pygame.display.flip()

































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



"""menu = pygame_menu.Menu(height=400,
    theme=pygame_menu.themes.THEME_DARK,
    title='MissionCode',
    width=600)"""

#instanciar las clases
#pantalla_despliegue = PantallaDespliegue()
#pantalla_elige_cohete = PantallaEligeCohete()
#pantalla_instrucciones = PantallaInstrucciones()




#menu.add.button('Pantalla de Despliegue', mostrar_pantalla_despliegue)
#menu.add.button('Pantalla de Elegir Cohete', mostrar_pantalla_elige_cohete)

#botones del menú principal
#menu.add.button('Pantalla de Instrucciones', mostrar_pantalla_instrucciones)


"""menu.add.button('Start',mostrar_pantalla_principal)
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

        pygame.display.flip()"""