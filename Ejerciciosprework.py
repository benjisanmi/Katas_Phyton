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
mi_lista1= [1,2,3,4,5]
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
def primer_elemento_repetido(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None # Devuelve None si no hay elementos repetidos
lista=input("Introducir los elementos separados por espacios: ")
mi_lista = lista.split()
print(primer_elemento_repetido(mi_lista))

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.
contraseña = input ("Introducir contraseña: ")
cadena = str(contraseña)
nueva_cadena =""

for letra in cadena [0:-4]:
    nueva_cadena += "#"
contraseña_oculta = nueva_cadena+ cadena[-4:]
print (contraseña_oculta)



#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.
palabra_1=input("Introducir palabra: ")
palabra1 = list(palabra_1)
palabra_2=input ("Introducir otra palabra: ")
palabra2 = list(palabra_2)

palabra1_ordenada = sorted(palabra1)
palabra2_ordenada = sorted(palabra2)
if palabra1_ordenada == palabra2_ordenada:
    print ("Son palabras anagramas")
else:
    print ("No son palabras anagramas")

#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.
nombres = input ("Introduzca nombres. La primera en mayuscula y separados por espacios: ")
lista_nombres = nombres.split()

nombre_buscado = input ("Intoduzca el nombre buscado. La primera en mayúscula: ")

if nombre_buscado in lista_nombres:
    print ("Nombre encontrado")
else:
    print ("No encontrado")

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.
empleado_buscado = input ("Introducir nombre: ")

empleados = ["Javier San Miguel", 'Juan Gutierrez', 'Arturo Noguero', 'Fernando Iglesias', 'Javier San Juan']
empleos = {"Javier San Miguel": "Data science", 'Juan Gutierrez': "RRHH", 'Arturo Noguero': "PMO", 'Fernando Iglesias':'Becario', 'Javier San Juan': 'Contable'}
if empleado_buscado in empleados:
    print (empleos[empleado_buscado])
else:
    print ("No trabaja aquí")

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista_1= input ('Introducir primeros valores (separado por espacios): ')
lista1_integer=lista_1.split()
mi_lista1= [int(x) for x in lista1_integer]
lista_2= input ("Introducir segunda lista de valores(separado por espacios): ")
lista2_integer= lista_2.split()
mi_lista2 = [int(x) for x in lista2_integer]
#realizar la suma de las listas y representar el resultado
resultado = list(map(lambda a, b: a + b, mi_lista1,mi_lista2))
print (resultado)

#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.
class Arbol:
    def __init__(self):
        # 1. Inicializar el tronco con longitud 1 y lista vacía de ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # 2. Aumentar longitud del tronco en una unidad
        self.tronco += 1

    def nueva_rama(self):
        # 3. Agregar una nueva rama de longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # 4. Aumentar en una unidad la longitud de todas las ramas
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        # 5. Eliminar una rama en una posición específica (índice base 1 para mayor claridad)
        if 1 <= posicion <= len(self.ramas):
            self.ramas.pop(posicion - 1)
        else:
            print("Posición inválida. No existe esa rama.")

    def info_arbol(self):
        # 6. Devolver información del árbol
        info = f"Longitud del tronco: {self.tronco}\n"
        info += f"Número de ramas: {len(self.ramas)}\n"
        info += f"Longitudes de ramas: {self.ramas if self.ramas else 'Sin ramas'}"
        return info

# --- Caso de uso ---
if __name__ == "__main__":
    # 1. Crear un árbol
    arbol = Arbol()

    # 2. Hacer crecer el tronco una unidad
    arbol.crecer_tronco()

    # 3. Añadir una nueva rama
    arbol.nueva_rama()

    # 4. Hacer crecer todas las ramas una unidad
    arbol.crecer_ramas()

    # 5. Añadir dos nuevas ramas
    arbol.nueva_rama()
    arbol.nueva_rama()

    # 6. Retirar la rama situada en la posición 2
    arbol.quitar_rama(2)

    # 7. Obtener información del árbol
    print(arbol.info_arbol())



#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
#agregar dinero al saldo.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        # Inicializar usuario con nombre, saldo y cuenta corriente (True/False)
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        # Retirar dinero del saldo. Lanza error si no es posible.
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        # Transferir dinero desde otro usuario al usuario actual
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if not otro_usuario.cuenta_corriente:
            raise ValueError(f"{otro_usuario.nombre} no tiene cuenta corriente.")
        if otro_usuario.saldo < cantidad:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        # Realizar transferencia
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} ha transferido {cantidad} a {self.nombre}.")
        print(f"Saldo de {otro_usuario.nombre}: {otro_usuario.saldo}")
        print(f"Saldo de {self.nombre}: {self.saldo}")

    def agregar_dinero(self, cantidad):
        # Agregar dinero al saldo
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}")

    def __str__(self):
        # Información legible del usuario
        tipo_cuenta = "Sí" if self.cuenta_corriente else "No"
        return f"Usuario: {self.nombre} | Saldo: {self.saldo} | Cuenta corriente: {tipo_cuenta}"

# --- Caso de uso ---
if __name__ == "__main__":
    # Crear dos usuarios
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    print(alicia)
    print(bob)

    # Agregar 20 unidades de saldo a Bob
    bob.agregar_dinero(20)

    # Transferir 80 unidades desde Bob a Alicia
    alicia.transferir_dinero(bob, 80)

    # Retirar 50 unidades del saldo de Alicia
    alicia.retirar_dinero(50)

    # Estado final
    print("\nEstado final de los usuarios:")
    print(alicia)
    print(bob)








#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , 
#reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
#de la función procesar_texto .
def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra_limpia = palabra.strip(".,!?").lower()
        conteo[palabra_limpia] = conteo.get(palabra_limpia, 0) + 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Debe proporcionar la palabra original y la nueva para reemplazar.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Debe proporcionar la palabra que se desea eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Use 'contar', 'reemplazar' o 'eliminar'.")


# --- Programa principal interactivo ---
if __name__ == "__main__":
    texto_usuario = input("Introduce una frase o texto: ")

    print("\n¿Qué operación deseas realizar?(IMPORTANTE: Introducir numero de la operacion que quieres realizar 1,2 o 3)")
    print("1. Contar palabras")
    print("2. Reemplazar una palabra")
    print("3. Eliminar una palabra")

    opcion = input("Selecciona una opción (introducir numero de la opción 1, 2 o 3): ")

    if opcion == "1":
        resultado = procesar_texto(texto_usuario, "contar")
        print("\nResultado del conteo de palabras:")
        for palabra, cantidad in resultado.items():
            print(f"{palabra}: {cantidad}")

    elif opcion == "2":
        palabra_original = input("Introduce la palabra que quieres reemplazar: ")
        palabra_nueva = input("Introduce la nueva palabra: ")
        resultado = procesar_texto(texto_usuario, "reemplazar", palabra_original, palabra_nueva)
        print("\nTexto resultante:")
        print(resultado)

    elif opcion == "3":
        palabra_a_eliminar = input("Introduce la palabra que deseas eliminar: ")
        resultado = procesar_texto(texto_usuario, "eliminar", palabra_a_eliminar)
        print("\nTexto resultante:")
        print(resultado)

    else:
        print("Opción no válida. Inténtalo de nuevo.")

#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario
hora = input ("Introducir hora en HH:MM:SS: " )
tiempo = hora.split (":")
tiempo_int = [int (x) for x in tiempo]
if 6<tiempo_int[0]<21:
    print ("es de día")
else:
    print ("es de noche")


#39.Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numércos. 
nota = int(input ("Introducir su nota numérica: "))
if nota <=69:
    print ("Insuficiente")
else:
    if nota <=79:
        print ("Bien")
    else: 
        if nota<=89:
            print ("muy bien")
        else:
            if nota <=100:
                print ("excelente")
            else:
                print ("No puede haber una calificación mayor de 100")
    
#40. . Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o 
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

figura = input ("Introducir figura para calcular el área: ")
import math
def calcular_area (figura):
    if figura == "rectangulo":
        base = int (input ("Introducir valor de la base: "))
        altura = int (input ("Introducir valor de la altura: "))
        print (base * altura)
    elif figura == "circulo":
        base = int (input("Introducir radio del círculo: "))
        altura = math.pi
        print (math.pi * (base ** 2))
    elif figura == "triangulo":
        base = int (input ("Introducir valor de la base: "))
        altura = int (input ("Introducir valor de la altura: "))
        print (0.5 * base * altura)
    datos = (base,altura)
    print (datos)
figura = input ("Introducir figura para calcular el área: ")
print (calcular_area (figura))

#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#monto final de una compra en una tienda en línea, después de aplicar un descuento.

precio_original = int (input("Introducir precio original: "))
descuento = input ("¿Tienes decuento? ")
if descuento =="si":
    valor_descuento = int(input("Introducir valor del descuento: "))
    if valor_descuento > 0:
        precio_final = precio_original - valor_descuento
        print (f"El valor del producto con el descuento es: {precio_final}, si no hubiese costado {precio_original}")
    else:
        print (f"El valor del descuento no es válido, tiene que ser mayor que 0. Por lo tanto el valor es: {precio_original}")
    
else: 
    print (f"Al no tener descuento el precio sigue siendo el mismo. El valor es {precio_original}")












