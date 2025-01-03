meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado",
}

print("¡Bienvenido al diccionario de palabras modernas!")
print("Escribe una palabra en MAYÚSCULAS para conocer su significado.\n")

for _ in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict:
        print(meme_dict[word])  
    else:
        print("Lo siento, esa palabra no está en nuestro diccionario. ¡Intenta con otra!")

    print()
