"""" Ejemplo de arbol binario adaptado a Python3
originalmente escrito en Python (2), tomado del libro 
        "Aprenda a Pensar como Un Programador"
"""
# https://argentinaenpython.com/quiero-aprender-python/aprenda-a-pensar-como-un-programador-con-python.pdf

class Arbol:
    def __init__(self, carga, izquierda=None, derecha=None):
        self.carga = carga
        self.izq = izquierda
        self.der = derecha
    def __str__(self):
        return str(self.carga)

# Función para cargar su memoria:
def recuerdo(casoBase="un perro"):
    try:
        import pickle
        arch = open("memoria.pck", "rb")
        aprendidos = pickle.load(arch)
        arch.close()
        return aprendidos
    except:
        return Arbol(casoBase)

# Funcion para memorizar
def recordar(que):
    import pickle
    import os
    if os.path.isfile("memoria.pck"):
        os.remove("memoria.pck")
    arch= open("memoria.pck", "wb")
    pickle.dump(que, arch)
    arch.close()

def animal():

    global raiz

    # Titulo:
    print("\n |=|=|=| ADIVINA EL ANIMAL |=|=|=|")

    # Bucle, hasta que el usuario decida que no está listo:
    while 1:
        print("\n")
        if not esperoUnSi("Pensá en un animal! ¿listo? "): break

        # RECORRIDO DEL ARBOL!:
        arbol = raiz                        # Se almacena el CASO BASE en $arbol (referencia de "raiz" type:Arbol())
        while arbol.izq != None:      # Mientras la rama izq contenga un arbol:
                                            #   (Al iniciar no se cumple, porque $arbol es una "hoja").
            indicador = arbol.carga + "? "  # Almaceno la carga de este y lo planteo como interrogante.
            if esperoUnSi(indicador):       # Hago la pregunta:
                arbol = arbol.der       # If contesta "si", se almacena la rama derecha en $arbol.
            else:                           # If contesta "no", se almacena la rama izquierda en $arbol.
                arbol = arbol.izq

        # Intenta adivinar:
        adivina = arbol.carga               # <Al salir del bucle, (porque alcanza una "hoja"), ya no puede preguntar,
                                            #   y almacena un animal en $adivina>.
        indicador = "Es " + adivina + "? "  # Se formula la pregunta y se almacena en $indicador (variable auxiliar).
        if esperoUnSi(indicador):           # If responde "si" :
            print("\njaja ADIVINE!!!, y estoy aprendiendo \n... vamos denuevo")
            continue                        # Y reinicia el "bucle principal".

        # Si falla:
        print("\n Uhh...")

        # Obtener informacion nueva:
        indicador = "...en que animal estabas pensando? "          # Cambia la pregunta (Se puede simplificar).
        animal = input(indicador)                               # $animal contiene el "nuevo animal".
        indicador = "Que pregunta distinguiría a %s de %s? "    # Otra vez, se puede simplificar: input("Str" % etc.)
        pregunta = input(indicador % (animal,adivina))          # <Que pregunta distinguiría a "este nuevo animal"
                                                                #   de "el animal que yo dije">, retorna la pregunta!

        # Añadir informacion nueva al arbol:
        arbol.carga = pregunta                                          # Se asigna la pregunta a la carga.
        indicador = "Si el animal fuera %s, cual seria la respuesta? "  # Se relaciona la pregunta con el animal:
        if esperoUnSi(indicador % animal):                      # If contesta "si" se asigna el CASO BASE a la rama
            arbol.izq = Arbol(adivina)                    # izq. y el "nuevo animal" a la rama der.
            arbol.der = Arbol(animal)                       # <En el caso contrario el nuevo animal
        else:                                                   #   se convierte en CASO BASE>
            arbol.izq = Arbol(animal)                     # <NOTA: en este proceso se entiende que el CASO BASE
            arbol.der = Arbol(adivina)                      #   es la opción por descarte cuando termina la "rama">

        print("...a ver dame otra oportunidad")
        # Reinicia el bucle principal.

# Función para preguntar:
def esperoUnSi(preg):
    rsp = input(preg).lower()
    while (rsp[:1] != "n" and rsp[:1] != "s" and rsp[:2] != 'ok'
           and rsp[:5] != 'bueno' and rsp[:4] != 'dale'
           and rsp[:4] != "bien"):
        
        rsp = input("necesito una respuesta ").lower()     
    return (rsp[:1] == 's' or rsp[:2] == 'ok' or rsp[:5] == 'bueno'
            or rsp[:4] == 'dale' or rsp[:4] == "bien")

if __name__ == '__main__':

    # Importamos su memoría.
    #   Si no la hay crea un CASO BASE definido en la función:
    raiz = recuerdo()

    # Ejecutamos el programa:
    animal()

    # Preguntamos si quiere recordar lo aprendido:
    indicador = "\nQueres que recuerde lo que me enseñaste? "
    if esperoUnSi(indicador):
        recordar(raiz)

"""
CONCLUSIONES:

1) Excepto el CASO BASE al principio, todos los animales son hojas, y las preguntas son cargas.
2) $arbol es una referencia de $raiz. Y se utiliza para estructurar el Arbol() ($raiz).
    Creando Arboles, asignandolos a ramas, y cargandolos.
3) Al no haber asignacioines a los nodos, solo puedo seguir el recorrido
    del arbol, o utilizar la "notación del punto" para apuntar a una "hoja".

NOTA PARA FUTUROS ANALISIS:

A) Prestar mucha atencion a las asignaciones y las referencias.
B) Recordar que cuando tengamos Casos Base (y a veces otras situaciones), se puede leer
    mejor el programa de atrás hacia delante.
"""
