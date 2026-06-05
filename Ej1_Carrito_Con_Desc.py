#Ejercicio 1

#1
nombre=input("Ingresar el nombre del cliente: ")
while(nombre.isalpha()==False):
    print("el nombre debe ser un string") 
    nombre=input("Ingresar nuevamente el nombre del cliente: ")
#2
cantidad=input("Ingresar la cantidad de productos: ")
while(cantidad.isdigit()==False or int(cantidad)==0):
    cantidad=input("La cantidad tiene que ser numerica mayor cero. Ingresar nuevamente: ")
cantidad=int(cantidad)
#3
precio_total=0
desc_total=0
for x in range(cantidad):
    precio=input("Ingresar el precio: ")
    while(precio.isdigit()==False):
        precio=input("Ingresar nuevamente el precio: ")
    precio=int(precio)
    precio_total+=precio
    tiene_desc=input("Tiene descuento? Ingresar s o n: ")
    while (tiene_desc!='s' and tiene_desc!='S' and tiene_desc!='n' and tiene_desc!='N'):
        tiene_desc=input("ERROR. Ingresar s o n: ")
    if(tiene_desc=='s' or tiene_desc=='S'):
        descuento=precio*0.1
        desc_total+=descuento
#4
print(f"Precio sin descuento: {precio_total}")
print(f"Precio con descuento: {precio_total - desc_total}")
print(f"Ahorro: {desc_total}")
prom=precio_total/cantidad
print(f"Promedio: {prom:.2f}")
print("Fin del programa #1")



