print(2 + 1)
print(2.0 + 1.)
print(2 + 1.0)

print(7 - 3)
print(7.0 - 3.)
print(7 + 3.0)

print(8 * 6)
print(8. * 6.)
print(8. * 6)

print(6 / 5)
print(6. / 5.0)
print(6 / 5.0)

''' 

División entera o Euclídea
Dados dos números naturales  a  y  b , con  b !== 0 , la división Euclídea de  a  entre  b  asocia un cociente  q  y un resto  r , ambos números naturales, que satisfacen

a = b * q + r 
r < b

Si queremos la división entera de  a=7  entre  b=5 , tendremos que el cociente es  q=1  y el resto es  r=2 , ya que

7= 5 ⋅ 1 + 2 

y el resto  r  es menor al divisor  b . Es decir,  2 < 5 .

'''


# Para obtener el cociente de la división entera, utilizamos la función //

print(10 // 3)


# Para obtener el resto de la división entera, utilizamos la función %

print(10 % 3)


''' 

Potencia
Para calcular la potencia  n -ésima de un número, usamos la función **

'''

print(5 ** 3)

print(5.0 ** 3.0)

print(5.0 ** 3)

print( pow(5,3)   ) # 5 * 5 * 5 = 125







''' 

Orden de las operaciones aritméticas

El orden en que se llevan a cabo las operaciones aritméticas en Python es el siguiente:

Primero se calcula lo que se halla entre paréntesis.

A continuación, las potencias.
Después, productos y divisiones. En caso de haber varias, el orden que se sigue es de izquierda a derecha.
Finalmente, sumas y restas. En caso de haber varias, el orden que se sigue es de izquierda a derecha.


'''

print(6 + 2 * 8 / 4 - 2 ** 3)

print((6 + 2) * (8 / (4 - 2)) ** 3)

print((6 + 2) * 8 / (4 - 2) ** 3)



z = 2 + 5j
print(z)
print(type(z))

z1 = 2-6j
z2 = 5+4j

print(z.real)
print(z.imag)
print(z1 + z2)
print(z1 - z2)
print(z1 * z2)
print(z1 / z2)


print( 45 // 6 )
print( 45 % 6 )

print( 10 + 20 / 7 - 2)

print((9 - (25 + 5 - 2)  / (7 * 4)) / 2 ** 3)

print((2 + 1.0) * (int(18.7) / (7 - 5.)) ** 3)

print( 9 ** 3)