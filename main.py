nombre = input('¿Cómo te llamas?')
print('Hola ' + nombre)

edad = int(input('¿Cuantos años tienes?'))
masDe12 = edad >= 12
respuestaHijoDelDueño = input('¿Eres hijo de dueño?')
esHijoDelDueño = respuestaHijoDelDueño == 'si'
puedePasar = masDe12 or esHijoDelDueño
if puedePasar:
    print('Usted puede pasar a la montaña rusa')
else:
    print('Usted no puede pasar a la montaña rusa')


