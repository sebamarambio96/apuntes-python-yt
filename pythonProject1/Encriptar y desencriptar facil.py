

def encriptar(texto):
    print('el texto a encriptar es: ' + texto)
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    print('Texto encriptado: ' + textoFinal)
def desencriptar(texto):
    print('El texto a desencriptar es: ' + texto)
    textoFinal = ''
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador += 1
    print('Texto desencriptado: ' + textoFinal)

seguirTrabajando = True
while seguirTrabajando:
    peticion = input('Que proceso desea que ejecute: ')
    if peticion == "Terminar":
        seguirTrabajando = False
    if peticion == "terminar":
        seguirTrabajando = False
    if peticion == "Apagar":
        seguirTrabajando = False

    if peticion == "Encriptar":
        encriptar(input('Introduzca el texto a encriptar: '))
    if peticion == "encriptar":
        encriptar(input('Introduzca el texto a encriptar: '))

    if peticion == "Desencriptar":
        desencriptar(input('Introduzca el texto a desencriptar: '))
    if peticion == "desencriptar":
        desencriptar(input('Introduzca el texto a desencriptar: '))

#archivo = open('texto.txt', 'a')
#archivo.write('Prueba de guardado en el archivo')
#archivo.close()

#archivo = open('texto.txt', 'r')
#print(archivo.read())

