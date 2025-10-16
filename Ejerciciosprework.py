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
mi_lista = (1,2,3,4,5)
#definimos la función para multiplicar *2 e imprimirla
def multiplicar (numero):
    return numero*2
lista_actualizada = map(multiplicar, mi_lista)
print(list(lista_actualizada))

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo
mi_lista = ("Paris","roma","madrid","london")
palabra = "i"
for pais in mi_lista :
    if palabra in pais:
        print (pais)
#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

mi_lista1= (1,2,3,4,5)
mi_lista2= mi_lista1 [::-1]

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


#6. 
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
numero =int(input("introducir numero: "))
print(factorial_recursivo(numero))








#7
 
