#1.Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados

def contar_frecuencias(cadena):
    # Creamos un diccionario vacío donde guardaremos las letras y sus frecuencias
    frecuencias = {}

    # Recorremos cada carácter de la cadena que el usuario haya pasado
    for caracter in cadena:
        # Ignoramos los espacios en blanco
        if caracter == " ":
            continue  # 'continue' salta a la siguiente iteración

        # Si la letra ya existe como clave en el diccionario
        if caracter in frecuencias:
            # Aumentamos su contador en 1
            frecuencias[caracter] += 1
        else:
            # Si no existe, la agregamos con valor 1
            frecuencias[caracter] = 1
    # Devolvemos el diccionario con los conteos
    return frecuencias
#imprimos resultado
texto = input("introduce una frase: ")
resultado = contar_frecuencias(texto)
print(resultado)


# 2.  Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
#definimos la lista
entrada = input("Introduce números separados por espacios: ")
lista_numeros = entrada.split()              
lista_numeros = [int(numero) for numero in lista_numeros]  
def multiplicar (numero):
    return numero *2
lista_multiplicada = map(multiplicar,lista_numeros)
print(list(lista_multiplicada))


#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo
mi_lista = ["Paris","roma","madrid","london"]
palabra = "i"
for pais in mi_lista :
    if palabra in pais:
        print (pais)
#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
#Valor de las listas
mi_lista1= (1,2,3,4,5)
mi_lista2= mi_lista1 [::-1]
#realizar la resta de las listas y representar el resultado
resultado = list(map(lambda a, b: a - b, mi_lista1,mi_lista2))
print(resultado)

#5.Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
#una tupla que contenga la media y el estado.

#definimos los valores
mi_lista = (4,5,6,7,2,9)
nota_aprobado = 5
#definimos suma de los valores de la lista
def suma_lista (numeros):
    suma=0
    for numero in numeros:
        suma += numero
    return suma
#calculamos el promedio de la lista 
promedio = suma_lista(mi_lista) / len (mi_lista)
#establcemos cuando es suspenso y cuando es aprobado
status = "aprobado" if promedio>nota_aprobado else "suspenso"
mi_lista2 = (promedio,status)
mi_tupla = tuple(mi_lista2)
print(mi_tupla)


#6.Escribe una función que calcule el factorial de un número de manera recursiva
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
numero =int(input("introducir numero: "))
print(factorial_recursivo(numero))



#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
tuple = (2,3,4,5,6)
lista = list (map(str, tuple))
print (lista) 


#8.  Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
#indicando si la división fue exitosa o no

while True:
    try:
        print ("Introduzca dos valores para que sean divididos entre sí.La función será dividir el numero 1 entro el numero 2")
        numero_1 = int (input ("introduzca numero 1: "))
        numero_2 = int (input ("introduzca numero 2: "))
        if numero_2 != 0:
            resultado = numero_1/numero_2
            print (resultado)
            break
        else :
            print ("no es posible dividir entre 0")
    except ValueError:
        print ("no has introducido un valor")

#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

entrada = input("Introduce animales separados por comas y la primera en mayuscula: ")
lista_animales = entrada.split(",")               

animales_prohibidos = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

animales_permitidos = list(filter (lambda animal: animal not in animales_prohibidos,lista_animales))
print (animales_permitidos)


#10.  Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
#excepción personalizada y maneja el error adecuadamente.

while True:
    try: 
        lista_numeros = input("introduzca valores separados por espacio (solo admite numeros enteros, sin decimales) : ")
        numeros = lista_numeros.split ()
        numeros = [int(numero) for numero in numeros]
        if len(numeros) == 0:
            print ("no has introducido valores")
        else: 
            def promedio (numeros):
                suma = 0
                for numero in numeros:
                    suma += numero
                return suma/len(numeros)
            print(promedio(numeros))
    except ValueError:
        print ("no has introducido valores enteros")
#11.  Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
#adecuadamente
while True:
    try: 
        edad = int(input("introduzca su edad: "))
        if 0<edad<120:
            print ("su edad es: "+ str (edad))
            break    
        else: 
           print ("Ha introducido una edad imposible, vuelva a intenarlo") 
    except ValueError:
        print ("no has introducido un valor numerico")

#12.Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map ()
frase = input("introduzca una frase: ")
palabras = frase.split ()
palabras = [str(palabra) for palabra in palabras]
def longitud (palabra) : 
    return len (palabra)
lista_longitud = map (longitud,palabras)
print (list(lista_longitud))

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map ()
palabra = input("introduzca una palabra: ")
def caracteres (palabra):
   letras_unicas = set(palabra)
   resultado =list(map(lambda letra: (letra.upper(), letra.lower()),letras_unicas))
   return resultado
print(caracteres(palabra))
    

#14.Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la 
# función filter ()
print ("Introduce diversas palabras y una letra. Se eliminarán las palabras que inician por esa letra")
entrada = input("Introduce palabras separados por espacio y la primera en mayuscula: ")
palabras = entrada.split()
letra = input("Introduce una letra en mayuscula: ")
palabra_correcta = filter(lambda palabra: letra not in palabra, palabras)
print (list (palabra_correcta))


#15. Crea una función lambda que  sume 3 a cada número de una lista dada.
lista_numeros = input("introduzca valores separados por espacio (solo admite numeros enteros, sin decimales) : ")
numeros = lista_numeros.split ()
numeros = [int(numero) for numero in numeros]
suma = list (map (lambda numero: numero + 3, numeros))
print (suma)

#16.  Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
#todas las palabras que sean más largas que n. Usa la función filter()
#introducir valores
frase = input("introduzca una frase: ")
numero = int (input( "introduzca numero: "))
#convertirlo a lista
palabras = frase.split ()
palabras = [str(palabra) for palabra in palabras]
def longitud (palabra) : 
    return len (palabra)
lista_longitud = map (longitud,palabras)
#crear un diccionario con las longitudes y las palabras
diccionario = dict(zip(palabras,lista_longitud))

filtrado = dict (filter (lambda item: item[1] > numero,diccionario.items()))
print (filtrado)

#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 
#corresponde al número quinientos setenta y dos 572. Usa la función reduce()
from functools import reduce  # Importamos reduce
def lista_a_numero(digitos):
    # Usamos reduce para convertir la lista en un solo número
    return reduce(lambda acumulado, x: acumulado * 10 + x, digitos)

numeros = [4,5,6,7,8,9]
resultado = lista_a_numero(numeros)
print(resultado)

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
#90. Usa la función filter()
#Definimos los alumnos
alumno_1= {'nombre': 'Javi','edad': '25', 'calificacion': 100 }
alumno_2= {'nombre': 'Pablo','edad': '28', 'calificacion': 95 }
alumno_3= {'nombre': 'Iván','edad': '27', 'calificacion': 80 }
alumno_4= {'nombre': 'Ángel','edad': '28', 'calificacion': 60 }
#creamos una lista con los diccionarios (información de cada alumno)
listado_alumnos = [alumno_1,alumno_2,alumno_3,alumno_4]

#filtramos a los alumnos que no hayan sacado más de 90
filtrado = filter (lambda item:item['calificacion'] >90, listado_alumnos)
#creamos una nueva variable con la la lista de almunos filtrados y lo imprimimos
resultado = list(filtrado)
print (resultado)

#19. Crea una función lambda que filtre los números impares de una lista dada
#Lista 
lista = [1,2,3,4,5,6,7,8,9]
numeros_impares= filter (lambda numero: numero % 2 != 0,lista)
print(list(numeros_impares))


#20.  Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
#Lista 
lista = [1,'hola',2,3,'españa']
numeros = filter (lambda numero: type(numero) ==int, lista)
print(list(numeros))

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda
numero = int (input("introducir un numero:" ))
cubo = lambda numero: numero**3
print (cubo(numero))

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce()
from functools import reduce  # Importamos reduce
def product_numero(digitos):
    # Usamos reduce para multiplicar los numeros entre sí
    return reduce(lambda acumulado, x: acumulado *x, digitos)

numeros = [2,3,2,3,4]
resultado = product_numero(numeros)
print(resultado)

#23. Concatena una lista de palabras. Usa la función reduce()
from functools import reduce  # Importamos reduce
def lista_palabras(palabras):
    # Usamos reduce para multiplicar los numeros entre sí
    return reduce(lambda acumulado, x: acumulado+x, palabras)
frase = ["Hola ", "que tal ", "estas"]
resultado = lista_palabras(frase)
print(resultado)

#24. Cálcula la diferencia total en los valores de una lista. Usa la función reduce()
from functools import reduce  # Importamos reduce
def resta_numero(digitos):
    # Usamos reduce para restar los numeros entre sí
    return reduce(lambda acumulado, x: acumulado -x, digitos)

numeros = [2,7,2,4,4]
resultado = resta_numero(numeros)
print(resultado)

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada. 
frase = input("introducir una frase: ")
print (len(frase))

#26. Crea una función lambda que calcule el resto de l división entre dos números dados
numero_1 = int(input("introducir numero 1: "))
numero_2 = int(input("introducir numero 2:"))
resto = lambda numero_1, numero_2: numero_1%numero_2
print (resto (numero_1,numero_2))

#27. Crea una función que calcule el promedio de una lista de números
lista_numeros = [4,4,5,6,7]

def resultado (lista_numeros):
    suma = 0
    for numeros in lista_numeros:
        suma +=numeros
    return suma/len(lista_numeros)

print (resultado (lista_numeros))

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada







#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.




#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.





#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.







#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.




#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
