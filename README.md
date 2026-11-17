# 🚀 Mission Code

MissionCode es un videojuego para niños de 10 a 15 años, el objetivo es que aprendan programación y física de cohetes de forma sencilla y divertida.

La misión del cadete: **despegar un cohete y llevar a su tripulación a Marte**. Para lograrlo hay que programarlo, paso a paso.

## Cómo se juega

Abre `index.html` en cualquier navegador (no necesita internet ni instalar nada) o corre la versión en Python:

```bash
python mision_cohete.py
```

## Los niveles

**1. El algoritmo de despegue.** Un algoritmo es una lista de pasos en orden. El cadete ordena los 7 pasos del lanzamiento (preparación, encendido, verificación, cuenta regresiva, despegue, ascenso y control de vuelo). Si un paso está mal, el programa dice exactamente cuál, igual que en el taller original.

**2. Variables y física.** Con dos variables —aceleración y tiempo— el cadete calcula qué tan alto llegará el cohete con la fórmula real:

```
altura = ½ × aceleración × tiempo²
```

**3. El despegue.** Una cuenta regresiva y la verificación final con condicionales (`if / elif / else`): si la secuencia estaba mal, el cohete explota; si la altura queda entre 113 km y 141.75 km, la tripulación llega a Marte; si la aceleración fue demasiada o muy poca, el cohete se cae.

## Conceptos que enseña

- Algoritmos y orden de pasos
- Variables
- Condicionales (`if`, `elif`, `else`)
- Funciones
- Física: movimiento con aceleración constante

## El origen: un taller de divulgación

Mission Code nació en julio de 2023, en la Ciudad de México, en un taller de divulgación científica realizado con la **Fundación Katya Echazarreta**: durante un mes, una vez por semana, más de 30 niñas, niños y jóvenes por sesión aprendieron a programar trabajando sobre un cuaderno de Google Colab, con su traje de cadetes y una sola misión: despegar el cohete.

Esta versión es ese mismo taller convertido en videojuego, para que cualquier cadete pueda jugarlo desde su casa.

Un proyecto de **Ingesaurio** ([@el_ingesaurio](https://www.instagram.com/el_ingesaurio)) — divulgación de ciencia e ingeniería en español, creado por Angel Toledo Flores.
