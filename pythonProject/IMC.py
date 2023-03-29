def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

def pedirelIMC():
    peso = int(input('ingrese su peso en kg'))
    alturaEnCM = int(input('Ingrese su altura en '))
    alturaEnMetros = alturaEnCM / 100
    imc = calcularIMC(peso, alturaEnMetros)

    print('Su IMC es de ' + str(imc))

    if imc < 20:
        print('Estado de delgadez')
    if imc >= 19 and imc < 26:
        print('Peso normal')
    if imc >= 26 and imc < 30:
        print('Estado de sobrepeso')
    if imc >= 30:
        print('Estado de obesidad')

print('Calcular el IMC de la primer persona')
pedirelIMC()
print('Calcular el IMC de la segunda persona')
pedirelIMC()
print('Calcular el IMC de la tercer persona')
pedirelIMC()
