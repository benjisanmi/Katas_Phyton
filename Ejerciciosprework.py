# Ejercicio 1: 
# Escribe una expresión en Python que combine el string "Python" y el string "Rocks" 
# en una sola cadena sin ningún espacio entre ellas.

cadena = "Python" + "Rocks"  # Usamos el operador '+' para unir los dos strings
print(cadena)  # Imprimimos el resultado: 'PythonRocks'

# Ejercicio 2:
# Reutiliza en un nuevo fichero el código anterior para que la salida sea 'Python Rocks' 
# (con un espacio entre las palabras). Se puede hacer hasta de tres maneras diferentes, 
# prueba todas las que se te ocurran.

cadena = " ".join(["Python", "Rocks"])
print(cadena)  # Imprime 'Python Rocks'

# Ejercicio 3:
# Crea un string que incluya tu nombre y edad usando concatenación de diferentes strings. 
# Es decir, un string con tu nombre, otro con tu edad y diferentes string para el resto de la frase. 
# Por ejemplo, si tu nombre es Ana y tienes 25 años, la cadena debe ser:
# Vamos a construir un string con el nombre y la edad usando concatenación
nombre = "Ana"
edad = "25"
frase = "Mi nombre es " + nombre + " y tengo " + edad + " años."
print(frase)  # Imprime: 'Mi nombre es Ana y tengo 25 años.'

# Ejercicio 4:
# Utiliza la repetición de strings para crear un nuevo string que repita la palabra "Hola" cinco veces,
# separadas por espacios.
cadena = "Hola " * 5  # Usamos el operador '*' para repetir la palabra
cadena = cadena.strip()  # Eliminamos el espacio final innecesario
print(cadena)  # Imprime: 'Hola Hola Hola Hola Hola'

# Ejercicio 5:
# Reemplaza todos los espacios en el string 'Que la Fuerza te acompañe' por guiones bajos (_) mediante un método.
frase = "Que la Fuerza te acompañe"
frase_modificada = frase.replace(" ", "_")  # Usamos el método 'replace' para cambiar los espacios
print(frase_modificada)  # Imprime: 'Que_la_Fuerza_te_acompañe'

# Ejercicio 6: 
# Crea una variable llamada greeting y asígnale el valor 'Hola'. 
# Luego, crea otra variable llamada name y asígnale el nombre de tu personaje favorito de Star Wars. 
# Finalmente, imprime la concatenación de estas dos variables con un espacio en medio.
greeting = "Hola"
name = "Luke Skywalker"
# Concatenamos ambas variables con un espacio en medio y las imprimimos
print(greeting + " " + name)  # Imprime: 'Hola Luke Skywalker'

# Ejercicio 7:
#Define una variable message_con el valor 'Buenos días'. 
# Luego modifica su valor a 'Buenas noches' e imprime ambos valores.
# Creamos una variable 'message' con un saludo inicial
message = "Buenos días"
print(message)  # Imprime: 'Buenos días'
# Ahora cambiamos su valor a otro mensaje y lo imprimimos
message = "Buenas noches"
print(message)  # Imprime: 'Buenas noches'


# Ejercicio 8:
# Crea un script que defina las variables word y name con los valores 'Hola, Doctor' y 'Who' respectivamente. 
# Luego, crea una variable sentence que almacene la concatenación de word y name con un espacio en medio. 
# Imprime sentence, cambia el valor de word a 'Adiós, Doctor', e imprime sentence nuevamente para observar que no cambia.

word = "Hola, Doctor"
name = "Who"
# Concatenamos las dos variables en 'sentence' con un espacio en medio
sentence = word + " " + name
print(sentence)  # Imprime: 'Hola, Doctor Who'
# Ahora cambiamos 'word' y vemos que 'sentence' no cambia
word = "Adiós, Doctor"
print(sentence)  # Imprime: 'Hola, Doctor Who' (sin cambio)
# Ejercicio 9:
#Crea un script que imprima cada letra de tu superhéroe favorito en una nueva línea usando un for loop.
# Definimos el nombre de nuestro superhéroe favorito
superheroe = "Spiderman"
# Usamos un bucle for para imprimir cada letra en una nueva línea
for letra in superheroe:
    print(letra)  # Imprime cada letra de 'Spiderman' en una línea separada

# Ejercicio 10:
# Modifica el script anterior para que imprima cada letra con un prefijo '---'
# Usamos el mismo nombre de superhéroe pero con un prefijo '---'
superheroe = "Spiderman"
for letra in superheroe:
    print(f"---{letra}")  # Imprime cada letra con '---' como prefijo

# Ejercicio 11:
# Crea un script que construya una "rampa" de caracteres uno a uno y la imprima en cada iteración.
name = 'Pikachu'
line = ''
# Usamos un bucle for para recorrer cada letra del nombre 'name'
for letra in name:
    line += letra  # Agregamos la letra actual a la variable 'line'
    print(line)  # Imprimimos la 'rampa' en cada iteración, mostrando los caracteres agregados hasta el momento

# Ejercicio 12:
# Escribe un script que imprima los números del 1 al 5 usando un for loop.
for i in range(1, 6):  # El rango es de 1 a 5
    print(i)  # Imprime cada número en una línea separada

# Ejercicio 13:
# Crea un script que verifique si una condición es verdadera e imprima un mensaje en consecuencia. 
# En este caso, tendremos que validar superhero_active y si es verdadero imprimir un mensaje y si no nada.
# Definimos una variable 'superhero_active' como True
superhero_active = True
# Verificamos si la condición es verdadera e imprimimos el mensaje correspondiente
if superhero_active:
    print("¡El superhéroe está activo!")  # Si es verdadero, imprime este mensaje
# Si cambiamos el valor de la variable a False, no se mostrará nada por terminal.

# Ejercicio 14:
# Crea un script que convierta una frase a mayúsculas si excited es verdadera y a minúsculas si excited es falsa.
# Usa una frase que te guste.
# Definimos una variable 'excited' para controlar la conversión
excited = True
frase = "me encanta aprender Python"

if excited:
    print(frase.upper())  # Si excited es True, convierte la frase a mayúsculas
else:
    print(frase.lower())  # Si excited es False, convierte la frase a minúsculas

# Ejercicio 15:
# Crea un script que verifique si un agente tiene acceso a una base secreta. 
# El agente tiene acceso si conoce la contraseña "openSesame" y su nivel de acceso es mayor a 5. 
# Si cualquiera de estas dos cosas no se cumplen, no tendrá acceso.
password = "openSesame"
access_level = 7

# Verificamos si el agente tiene acceso
if password == "openSesame" and access_level > 5:
    print("Acceso concedido")  # Si ambas condiciones se cumplen
else:
    print("Acceso denegado")  # Si alguna de las condiciones no se cumple


# Ejercicio 16:
# Crea un script que imprima cada personaje de una lista usando un for loop.
# Definimos una lista con nombres de personajes
characters = ['Luke Skywalker', 'Darth Vader', 'Leia Organa', 'Han Solo']

# Usamos un bucle for para imprimir cada personaje
for personaje in characters:
    print(personaje)  # Imprime cada personaje en una línea separada

# Ejercicio 17:
# Modifica el siguiente script para que sume las duraciones de una lista de películas 
# y luego imprima el total en minutos.
durations = [121, 154, 178, 132]
total_duration = 0

# Usamos la función sum para calcular el total de las duraciones
total_duration = sum(durations)
print(f"El total de minutos es: {total_duration}")  # Imprime el total de minutos

# Ejercicio 18:
# De forma similar al script anterior, haz que se concatenen los títulos de películas en una lista en un solo string.
movies = ['The Godfather', 'Pulp Fiction', 'Inception', 'The Dark Knight']
titulos = " ".join(movies)
print(titulos)
# Ejercicio 19:
# Extiende el script anterior para que inserte un separador entre cada título de película.
titulos = " | ".join(movies)  # Usamos ' | ' como separador entre los títulos
print(titulos) 



desayun = "cafe"
merienda = "cafe "
desayun== merienda