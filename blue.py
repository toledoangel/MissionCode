"""
        self.rectangulos = [
            pygame.Rect(20, 50, 150, 15),
            pygame.Rect(20, 90, 150, 15),
            pygame.Rect(20, 130, 150, 15),
            pygame.Rect(20, 170, 150, 15),
            pygame.Rect(20, 210, 150, 15),
            pygame.Rect(20, 250, 150, 15),
            pygame.Rect(20, 290, 150, 15),
            pygame.Rect(20, 330, 150, 15),
            pygame.Rect(20, 370, 150, 15),
            pygame.Rect(20, 410, 150, 15)
        ]

        self.orden_inicial = list(range(1, len(self.rectangulos) + 1))
        self.orden_actual = self.orden_inicial.copy()

        self.rectangulo_seleccionado = None
        self.offset_arrastre = (0, 0)

        def draw(self):
            self.pantalla.blit(self.fondo, (0, 0))
            self.pantalla.blit(self.boton_start, self.boton_start_rect)
            texto = self.fuente.render("Ordena las instrucciones para el despegue", True, BLANCO)
            rect_texto = texto.get_rect(center=(300, 66))
            self.pantalla.blit(texto, rect_texto)
            self.pantalla.blit(self.cohete, (420, 140))

            for rect in self.rectangulos:
                pygame.draw.rect(self.pantalla, BLANCO, rect)

            pygame.display.flip()

        def validar_orden(self):
            if self.orden_actual == self.orden_inicial:
                return True
            else:
                return False

    #  def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, rect in enumerate(self.rectangulos):
                        if rect.collidepoint(event.pos):
                            self.rectangulo_seleccionado = rect
                            self.offset_arrastre = self.rectangulo_seleccionado.x - event.pos[
                                0], self.rectangulo_seleccionado.y - event.pos[1]
                            break

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for i, rect in enumerate(self.rectangulos):
                        if rect.collidepoint(event.pos) and rect != self.rectangulo_seleccionado:
                            indice_seleccionado = self.rectangulos.index(self.rectangulo_seleccionado)
                            indice_soltado = self.rectangulos.index(rect)
                            self.rectangulos[indice_seleccionado], self.rectangulos[indice_soltado] = self.rectangulos[
                                indice_soltado], self.rectangulos[indice_seleccionado]
                            break

                    self.rectangulo_seleccionado = None

                    orden_actual = [self.rectangulos.index(rect) + 1 for rect in self.rectangulos]
                    if orden_actual == self.orden_inicial:
                        print("Orden correcto")
                        # Redireccionar al usuario a la siguiente pantalla
                        # ...
                    else:
                        print("Orden incorrecto")

            elif event.type == pygame.MOUSEMOTION:
                if self.rectangulo_seleccionado is not None:
                    self.rectangulo_seleccionado.x = event.pos[0] + self.offset_arrastre[0]
                    self.rectangulo_seleccionado.y = event.pos[1] + self.offset_arrastre[1]
"""
