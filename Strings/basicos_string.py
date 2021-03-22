s1 = "Esto es un string entre comillas dobles"

print( type(s1))

print(s1)

s1 = "Juan dijo \"me gusta el chocolate \""
print(s1)

s2 = ' Juan dijo: "me gusta el chocolate" '
print(s1)

s3 = "Ricardo dijo: 'me gusta la playa'"
print(s3)

s4 = 'Ricardo dijo: \'me gusta la playa\''
print(s4)

s5 = "Con diez cañones por banda, \nviento en popa a toda vela"

print(s5)

"""
    Repetición de strings
"""

sn = "¿Falta mucho? "

print(sn * 5)
print(5 * sn)

"""
    Función str()
"""

nombre = "Alexis"
edad = 22
print("Mi hermano se llama " + nombre + " y su edad es " + str(edad))

print("Mi abuelo se llama {} y tiene {} años".format(nombre, edad))


s4 = "La string literal \\t producía \t una tabulación horizontal"

print(s4)


s9 = "Soy fan de los videojuegos"

print(s9[0], s9[5], s9[18])

print(s9[-1])

print(s9[4:7])
print(s9[:7])  # Del primero al séptimo
print(s9[8:])  # Del noveno al final
print(s9[-10:])
print(s9[:-10])

s = "Me ENCANTAN el chocolate y las galletas"

print(s.lower())
print(s.upper())

print(s.count("o"))
print(s.count("la"))
print(s.capitalize())
print(s.title())
print(s.swapcase())

print(s.replace("ENCANTAN", "odio"))

s = "El elefante tiene las orejas muy grandes"

print(s.split("e"))
print(s.split(" "))
print(s.split("tiene"))

s = "       El elefante tiene las orejas muy grandes        "


# rstrip() final del string
# lstrip() inicio del string

print(s.strip())

s = "Este es un curso de Python para hacer en casa o en cualquier lado"

print(s.find("e"))
print(s.find("casa"))

string = "El camino está cerrado pero seguro que podemos encontrar una alternativa"
print("Este es el string original:", end=" ")
print(string)

print("Introduce la palabra que quieras eliminar del string original:")
word = input("Palabra: ")

idx = string.find(word)
print(idx)
print(len(word))
substring = string[(idx + len(word) + 1):]
print(substring)
substring = string[:idx] + string[(idx + len(word) + 1):]
print(substring)

s1 = "Había una vez, "
s2 = "un barquito chiquitito "
s3 = "que no podía, "
s4 = "que no podía navegar."

print( (s1 + s2) * 2 + s3 * 2 + s4)

print("Érase un hombre a una nariz pegado, \nÉrase una nariz superlativa, \nÉrase una alquitara medio viva, \nÉrase un peje espada mal barbado; ")


s = "me encantan las matemáticas"
print(s.upper())

s = "Mi pasión por el chocolate es superior a mis fuerzas"
print(len(s))

print(s.find("chocolate"))
inicio = s.find("chocolate")
final = inicio + len("chocolate")
s_sub = s[inicio:(final + 1)]
print(s_sub)


nombre = input("Introduce tu nombre")
apellido = input("Introduce tu apellido")
# edad = int(input("Introduce el año actual: "))
ciudad = input("Introduce tu ciudad")
print("Su nombre es {} {}, tiene {} años y actualmente vive en {}".format(nombre, apellido, edad, ciudad))