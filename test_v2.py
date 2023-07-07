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


class Menu_Principal():

    def __init__(self):
        self.fondo = pygame.image.load("Imagenes/Mockups/menufinal.png")
        self.boton_start = pygame.image.load('Imagenes/Animaciones/start.png')
        self.cohete = pygame.image.load('Imagenes/Animaciones/Ariane5pequeño.svg')
        self.boton_start_rect = self.boton_start.get_rect(left=100, centery=ALTO // 2)
        self.fuente = pygame.font.Font(None ,32)

    def draw(self):
        pantalla.blit(self.fondo, (0, 0))
        pantalla.blit(self.boton_start, self.boton_start_rect)
        texto = self.fuente.render("Programa tu propio cohete", True, BLANCO)
        rect_texto = texto.get_rect(center=(200, 100))
        texto_creditos = self.fuente.render("Creditos", True, BLANCO)
        rect_texto_creditos = texto.get_rect(center=(550, 360))
        pantalla.blit(self.cohete, (420, 140))
        pantalla.blit(texto, rect_texto)
        pantalla.blit(texto_creditos, rect_texto_creditos)
        pygame.display.flip()

class EligeCohete:
    def __init__(self):
        self.fondo = pygame.image.load("Imagenes/Mockups/elige-cohete.png")
        self.boton_start = pygame.image.load('Imagenes/Animaciones/start.png')
        self.boton_start_rect = self.boton_start.get_rect(center=(300, 320))
        self.cohete = pygame.image.load('Imagenes/Animaciones/Ariane5pequeño.svg')
        self.cohete_1 = pygame.image.load('Imagenes/Animaciones/Ariane5pequeño.svg')
        self.cohete_2 = pygame.image.load('Imagenes/Animaciones/Ariane5pequeño.svg')
        self.fuente = pygame.font.Font(None, 32)

    def draw(self):
        pantalla.blit(self.fondo, (0, 0))
        pantalla.blit(self.boton_start, self.boton_start_rect)
        texto = self.fuente.render("Elige tu cohete", True, BLANCO)
        rect_texto = texto.get_rect(center=(300, 86))
        pantalla.blit(texto, rect_texto)
        pantalla.blit(self.cohete, (440, 100))
        pantalla.blit(self.cohete_1, (240, 100))
        pantalla.blit(self.cohete_2, (340, 100))
        pygame.display.flip()


class Instrucciones:

    def __init__(self):
        self.fondo = pygame.image.load("Imagenes/Mockups/instrucciones.png")
        self.boton_start = pygame.image.load('Imagenes/Animaciones/start.png')
        self.boton_start_rect = self.boton_start.get_rect(center=(430, 320))
        self.cohete = pygame.image.load('Imagenes/Animaciones/Ariane5pequeño.svg')
        self.fuente = pygame.font.Font(None, 32)

    def draw(self):
        pantalla.blit(self.fondo, (0, 0))
        pantalla.blit(self.boton_start, self.boton_start_rect)
        texto = self.fuente.render("Ordena las instrucciones para el despegue", True, BLANCO)
        rect_texto = texto.get_rect(center=(300, 66))
        pantalla.blit(texto, rect_texto)
        pantalla.blit(self.cohete, (420, 140))
        pygame.display.flip()



menu_principal = Menu_Principal()
elige_cohete = EligeCohete()
instrucciones = Instrucciones()

#inicio
pantalla_actual = menu_principal


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pantalla_actual == menu_principal and menu_principal.boton_start_rect.collidepoint(mouse_pos):
                pantalla_actual = elige_cohete
            elif pantalla_actual == elige_cohete and elige_cohete.boton_start_rect.collidepoint(mouse_pos):
                pantalla_actual = instrucciones #cambia a la siguiente

    if pantalla_actual == menu_principal:
        menu_principal.draw()
    elif pantalla_actual == elige_cohete:
        elige_cohete.draw()
    elif pantalla_actual == instrucciones:
        instrucciones.draw()
































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