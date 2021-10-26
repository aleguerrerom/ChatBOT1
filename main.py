from nltk.chat.util import Chat, reflections

# lista de reflecciones
reflections = {
    "yo":"tu",
    "hola":"hey",
    "yo soy": "tu eres"
}

###Arreglo de pares
pairs = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas?",]
    ],
    [
        r"cual es tu nombre",
        ["Mi nombre es Chatbot!!!",]
    ],
    [
        r"como estas|como vas",
        ["Bien, y tu?", "Pura vida"]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal", "Buenas"]
    ],
    [
        r"Que (.*) quieres?",
        ["Nada Gracias","Comer" ]
    ],
    [
        r"(.*) fuiste creado?",
        ["Fui creado hoy", ]
    ],
    [
        r"Finalizar|Fin|FIN|FINALIZAR|fin|finalizar",
        ["Chao", "Fue un gusto hablar contigo","Adios"]
    ],
]


## Funcion para pedir numero entero para el menu
def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            print("Elige una opcion: ")
            print("1. Opcion Preguntas")
            print("2. Salir")
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

#funcion de chateo
def chatear():
        salir = False
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                print("Hola Bienvenid@!!")
                chat = Chat(pairs, reflections)
                chat.converse()
            elif opcion == 2:
                    option = input("Deseas Salir S/N?")
                    if option == 'S' or option == 's':
                        salir = True
                        print("Has salido del Chat")
                        exit()
                    else:
                        salir = False
                        pedirNumeroEntero()
            else:
                print("Introduce un numero entre 1 y 2")


if __name__ == "__main__":
    chatear()

chatear()