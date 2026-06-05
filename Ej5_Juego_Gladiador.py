#Ejercicio 5
nombre=input("\nIngresar nombre del Gladiador: ")
while not nombre.isalpha():
    print("\nError: Solo se permiten letras")
    nombre=input("\nIngresar nombre del Gladiador: ")
Vida_Gladiador=100
Vida_Enemigo=100  
Pociones_Vida=3
Daño_base_Ataque_Pesado=15
Daño_base_enemigo=12  
Turno_Gladiador=True   
while Vida_Gladiador>0 and Vida_Enemigo>0:
    #Mi turno
    print(f"\nVida del Gladiador: {Vida_Gladiador}")
    print(f"Vida del Enemigo: {Vida_Enemigo}")
    print(f"Pociones de Vida: {Pociones_Vida}")
    #Menu
    print("\n++++++Menu+++++")
    print("1-Ataque Pesado")
    print("2-Ráfaga Veloz ")
    print("3-Curar")
    eleccion=input("Ingresar opcion: ")

    while(not eleccion.isdigit()) or int(eleccion)<1 or int(eleccion)>3:
        if(not eleccion.isdigit()):
            print("Error.La opcion ingresada debe ser un numero")
        else:
            print("Error.La opcion ingresada debe ser 1, 2 o 3 ")
        eleccion=input("Ingresar opcion nuevamente: ")
    eleccion=int(eleccion)
    if(eleccion==1):
        if Vida_Enemigo<20:
            #realiza un golpe critico multiplicando el daÑo base por 1.5
            Vida_Enemigo-=(Daño_base_Ataque_Pesado*1.5)
            print(f"\n¡Atacaste al enemigo por {Daño_base_Ataque_Pesado*1.5} puntos de daño!")
        else: 
            Vida_Enemigo-=Daño_base_Ataque_Pesado
            print(f"\n¡Atacaste al enemigo por {Daño_base_Ataque_Pesado} puntos de daño!")
        
    elif(eleccion==2):
        for x in range(3):
            Vida_Enemigo-=5
            print("\nGolpe conectado por 5 de daño")
    else:
        if(Pociones_Vida>0):
            Vida_Gladiador+=30
            Pociones_Vida-=1
        else:
            print("\n¡No quedan pociones!")
    #turno del enemigo
    Vida_Gladiador-=12
    print("¡El enemigo contraataca por 12 puntos de daño!")

if Vida_Gladiador>0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")
