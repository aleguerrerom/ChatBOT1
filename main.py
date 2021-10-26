from nltk.chat.util import Chat, reflections

mis_reflecciones = {
    "ir":"fui",
    "hola":"hey"
}

###Array
preguntas = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas?",]
    ],
    [
        r"cual es tu nombre",
        ["Mi nombre es Chatbot!!!",]
    ],
    [
        r"como estas",
        ["Bien, y tu?",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]
    ],
    [
        r"Que (.*) quieres?",
        ["Nada Gracias", ]
    ],
    [
        r"(.*) fuiste creado?",
        ["Fui creado hoy", ]
    ],
    [
        r"Finalizar|Fin|FIN|FINALIZAR|fin|finalizar",
        ["Chao", "Fue un gusto hablar contigo" ]
    ],
]

def chatear():
        print("Hola Bienvenid@!!")
        chat = Chat(preguntas, mis_reflecciones)
        chat.converse()

if __name__ == "__main__":
    chatear()

while True:
    if preguntas !
    chatear()