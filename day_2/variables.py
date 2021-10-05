#Day 2: 30 Days of python programming

#----------Level 1 ----------------------
first_name = 'Jordana'
last_name = 'Escalona'
full_name = first_name + ' ' + last_name
country = 'Argentina'
city = 'Rio Grande'
age = 33
year = 2021
is_married = False
is_true = True
is_light_on = True

first_name, last_name, country, age = 'Jordana','Escalona','Argentina',33

#------------Level 2 ------------------------------
#1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#2
print(len(first_name))
#3
print(len(first_name) < len(last_name))

#4
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

#5
import math 

radius = 30
area_of_circle = math.pi * (radius ** 2)
print(area_of_circle)

circum_of_circle = 2 *  math.pi * radius
print(circum_of_circle )

radius =input("Ingrese radio:")
print("El area es:",area_of_circle)

#6
first_name = input("Ingrese su nombre:")
last_name = input("Ingrese su apellido:")
country = input("Ingrese su pais:")
age = input("Ingrese su edad:")

#7
#--- Abrimos shell de python escribiendo en la terminal: python
#--- Ejecutamos el siguiente codigo: help('keywords)