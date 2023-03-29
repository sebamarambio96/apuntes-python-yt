diccionario = {
    "1": "UNO",
    "2": "DOS",
    "3": "TRES",
    "4": "CUATRO"
}

texto = input("Ingrese un número")

textoFinal = ''
for letra in texto:
    textoFinal += diccionario[letra] + ' '

print(textoFinal)


