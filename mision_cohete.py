# Mission Code: despega el cohete
# --------------------------------
# Versión en Python del taller de programación con la Fundación Katya
# Echazarreta (Ciudad de México, julio de 2023). Es la esencia del
# cuaderno original de Google Colab que usaron los cadetes, ordenada
# y comentada para que cualquiera pueda correrla y aprender de ella.
#
# Conceptos que se aprenden:
#   1. Algoritmos: una lista de pasos EN ORDEN.
#   2. Variables: valores que guardamos y podemos cambiar.
#   3. Condicionales: si pasa esto... si no, esto otro (if / elif / else).
#   4. Funciones: un cálculo con nombre que podemos reutilizar.
#   5. Física: la altura de un cohete que acelera desde el reposo
#      es altura = 1/2 * aceleración * tiempo^2.

# ---------------------------------------------------------------
# 1. EL ALGORITMO DE DESPEGUE
# Ordena los pasos: ¿qué va primero, qué va después?
# ---------------------------------------------------------------
PASOS_CORRECTOS = {
    "Preparación": 1,            # Revisar y preparar el cohete
    "Encendido del motor": 2,    # Activar el motor
    "Verificación del sistema": 3,  # Comprobar que todo funcione
    "Cuenta regresiva": 4,       # Contar hacia atrás
    "Despegue": 5,               # El cohete se eleva
    "Ascenso": 6,                # Se dirige hacia el espacio
    "Control de vuelo": 7,       # Mantener el rumbo y la estabilidad
}


def revisar_secuencia(orden_del_cadete):
    """Recibe la lista de pasos en el orden del cadete y devuelve
    "0" si todo está bien, o un mensaje con el primer paso mal."""
    for posicion, paso in enumerate(orden_del_cadete, start=1):
        if PASOS_CORRECTOS[paso] != posicion:
            return f"El paso {posicion} de tu algoritmo de despegue es incorrecto"
    print("--- Secuencia de cohete programada exitosamente ---")
    return "0"


# ---------------------------------------------------------------
# 2. VARIABLES Y CONDICIONALES
# El estado del cohete decide qué pasa.
# ---------------------------------------------------------------
estado_cohete = 0

if estado_cohete == 0:
    print("El cohete despega")
elif estado_cohete == 1:
    print("El cohete explota")
else:
    print("El cohete despega pero se cae")


# ---------------------------------------------------------------
# 3. FUNCIONES Y FÍSICA
# altura = 1/2 * aceleración * tiempo^2
# ---------------------------------------------------------------
def calcular_altura(aceleracion, tiempo):
    altura = 0.5 * aceleracion * tiempo ** 2
    return altura


# ---------------------------------------------------------------
# 4. LA VERIFICACIÓN FINAL
# La órbita correcta está entre 113 km y 141.75 km de altura.
# ---------------------------------------------------------------
def verificacion_despegue(altura, error):
    if error != "0":
        print("Despegue fallido: su secuencia de despegue era incorrecta")
        print(error)
    elif 113000 <= altura < 141750:
        print("Despegue exitoso: ¡felicidades! Su tripulación se dirige a Marte")
    elif altura >= 141750:
        print("Despegue fallido: su aceleración fue demasiado alta")
    else:
        print("Despegue fallido: su aceleración fue demasiado pequeña")


# ---------------------------------------------------------------
# EJEMPLO COMPLETO (los valores originales del taller)
# ---------------------------------------------------------------
if __name__ == "__main__":
    mi_orden = [
        "Preparación",
        "Encendido del motor",
        "Verificación del sistema",
        "Cuenta regresiva",
        "Despegue",
        "Ascenso",
        "Control de vuelo",
    ]
    error = revisar_secuencia(mi_orden)

    aceleracion = 28   # m/s^2
    tiempo = 90        # segundos
    altura = calcular_altura(aceleracion, tiempo)
    print(f"Altura calculada: {altura:,.0f} metros")

    verificacion_despegue(altura, error)
