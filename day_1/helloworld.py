import sys
import math
#-------Nivel 2--------------

#1
print("Python version:",sys.version)

#2
print( 3 + 4 ) #addition
print( 3 - 4 )  #subtraction
print( 3 * 4 ) #multiplication
print( 3 % 4 ) #modulus
print( 3 / 4 ) #division
print( 3 ** 4 ) #exponential

#3
print("Jordana")
print("Escalona")
print("Tierra del Fuego")
print("I am enjoying 30 days of python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh','Python','Finland']))
print(type('Jordana'))
print(type('Escalona'))
print(type('Tierra del Fuego'))

#-------------- Nivel 3 -----------------------

#1
print( 20 + 15 ) # Integer
print( 3.5 ** 3.3 ) # float
print( (5 + 3j) + (8 + 5j)) # complex
print("Hola desde Tierra del Fuego") #string

print( 3 > 0) #Boolean
print(['Blue','Red','White',1,9,3.5,True]) #List
print((9,8.93,10)) # Tuple
print({2.4,5.6,9}) #Set
print({"Name":"Juan","Edad":30}) #Dictionary

#2 Find an Euclidian distance between (2, 3) and (10, 8)

print('Eucladian distance:',math.sqrt(((10-2)**2)+((8-3)**2)))