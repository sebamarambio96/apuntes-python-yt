def encriptar(texto):
    print('el texto a encriptar es: ' + texto)
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    return textoFinal
    print('Texto encriptado: ' + textoFinal)

def encriptarArchivo():
    archivo = open('texto.txt', 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open('texto.txt', 'w')
    archivo.write(textoEncriptado)
    archivo.close()

