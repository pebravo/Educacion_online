print('=====Venta de cursos EDUCATE-ONLINE=====')
print('\n')
bandera = True
contador = 0
contador1 = 0
contador2 = 0
contador3 = 0
descuento1 = 0
descuento2 = 0
descuento3 = 0
nodescuento1 = 0
nodescuento2 = 0
nodescuento3 = 0
while bandera == True:
    print('==================================')
    print('||\t EDUCATE-ONLINE\t\t||')
    print('==================================')
    print('\n')
    print('==================================')
    print('||Los cursos que se encuentran  ||')
    print('||a la venta son los siguientes:||')
    print('==================================')
    print('||  Asignatura\t\tSemestre||')
    print('==================================')
    print('||1.- Programación\t$250.000||')
    print('||2.- Base de datos\t$310.000||')
    print('||3.- Robótica\t\t$280.000||')
    print('==================================')
    numero = int(input('¿Qué curso desea comprar?: (Seleccione el numero)'))
    if numero in (1,2,3):
            if numero == 1:
                contador1 = contador + 1
                nombre = input('Ingrese nombre completo :')
                rut = input('Ingrese rut :')
                opcion = input('Tiene cupón ? :')
                if opcion == 'si':
                    cupon = input('Ingrese cupón :')
                    if cupon == 'educateonline':
                       descuento1 = descuento1 + 1 
                else:
                    nodescuento1 = nodescuento1 + 1                 
            elif numero == 2:
                contador2 = contador2 + 1  
                nombre = input('Ingrese nombre completo :')
                rut = input('Ingrese rut :') 
                opcion = input('Tiene cupón :')
                if opcion == 'si':
                   cupon = input('Ingrese cupón :')
                   if cupon == 'educateonline':
                        descuento2 = descuento2 + 1
                else:
                    
                        nodescuento2 = nodescuento2 + 1      
            elif numero == 3:  
                contador3 += 1
                nombre = input('Ingrese nombre completo :')
                rut = input('Ingrese rut :') 
                opcion = input('Tiene cupón ? :')
                if opcion == 'si':
                    cupon = input('ingrese cupón :')
                    if cupon == 'educateonline':
                        descuento3 = descuento + 1
                else:
                        nodescuento3 = nodescuento3 + 1

    else:
        print('Numero no existe, reintente')
        contador = contador + 1
    if contador == 3:
        print('Se solicita el fin del programa, 3 intentos fallidos.')
    respuesta = input('¿desea continuar?:')
    if respuesta == 'no':
        bandera = False
        print ('Total de cursos comprados son :', contador1+contador2+contador3)
        print ('Total de cursos comprados con descuento son :', descuento1+descuento2+descuento3)
        print ('Total de cursos comprados sin descuento:', nodescuento1+nodescuento2+nodescuento3)
        print ('Total de cursos comprados de programación :', contador1)
        print ('Total de cursos comprados de base de datos :', contador2)
        print ('Total de cursos comprados de robótica :', contador3)

