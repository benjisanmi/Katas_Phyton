#1.Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados
    #Creamos la función
    def parametro(cadena_de_texto):
        #eliminamos espacios 
        cadena_de_texto=cadena_de_texto.replace(" ","")
        # Creamos un diccionario vacío para almacenar las frecuencias
        dict = {}
        # Recorremos cada carácter en la cadena de texto
        for letra in cadena_de_texto:
            if letra in dict:
                dict[letra] += 1
            else:
                dict[letra] = 1
        return dict
    #Damos valor a la cadena de texto e imprimimos el diccionario
    cadena = "Cadena de texto como parámetro"
    resultado = parametro(cadena)
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
mi_lista = ("Paris","roma","madrid","london")
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
















