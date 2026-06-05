energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 
bloqueo=False
anti_spam=0
agente=input("\nIngresar nombre del agente: ")
while(agente.isalpha()==False):
    print("\nError. El nombre solo debe contener letras")
    agente=input("\nIngresar nuevamente el nombre del agente: ")
#MENU de accione
while(energia>0 and tiempo>0 and cerraduras_abiertas<3 and not bloqueo):
    print("\nMENU DE ACCIONES")
    print("1-Forzar la cerradura")
    print("2-Hackear panel")
    print("3-Descansar")
    opcion=input("\nOpcion: ")

    while((not opcion.isdigit()) or int(opcion)<1 or int(opcion)>3):
        if not opcion.isdigit():
            print("Error. Debe ingresar un numero: ")
        else:
            print("Error. Debe ingresar 1,2 o 3: ")
        opcion=input("\nOpcion: ")

    opcion=int(opcion)

    if(opcion==1):
        print("\nForzando cerradura...")
        energia-=20
        tiempo-=2
        anti_spam+=1
        print(f"\nForzando por {anti_spam} vez seguida")
        if(anti_spam<3):
            if(energia<40):
                print("Energia baja.Riesgo de alarma")
            numero=input("\nIngresar un numero de 1 al 3: ")
            while(not numero.isdigit() or int(numero)<1 or int(numero)>3):
                numero=input("\nError. Debe ingresar un numero de 1 al 3: ")
                numero=input("\nIngresar nuevamente un numero de 1 al 3: ")
            numero=int(numero)
            if(numero==3):
                print("\nActivando alarma...")
                alarma=True
            if(not alarma):
                print("\nabriendo una cerradura...")
                cerraduras_abiertas+=1
        else: 
            print("\nSpam.Se forzo por tercera vez consecutiva")
            print("\nActivando alarma...")
            alarma=True
    elif(opcion==2):
        energia-=10
        tiempo-=3
        anti_spam=0
        print(f"\nAntiespam= {anti_spam}")
        for i in range(4):
            letra=input("\ningresar una letra: ")

            while(len(letra)!=1 or not letra.isalpha()):
                if letra.isalpha():
                    print("Error.Ingreso mas de una letra")
                else:
                    print("\nError.No ingreso una letra")
                letra=input("\nIngresar nuevamente una letra: ")
                
            letra.upper()
            codigo_parcial+=letra
            print(f"\nCodigo Parcial: {codigo_parcial}")
        if(len(codigo_parcial)>=8):
            print("\nCompleto el codigo")
            print("\abriendo una cerradura...")
            cerraduras_abiertas+=1
    else:
        tiempo-=1
        energia+=15
        anti_spam=0
        if(energia>100):
            energia=100
        print("Recuperaste energia")   
        if(alarma):#Esta parte no entendi, el juego sigue con la alarma activada?
            energia-=10
        print("Recuperaste energia")
    
    print(f"energia= {energia}")
    print(f"tiempo= {tiempo}")
    print(f"cerraduras_abiertas= {cerraduras_abiertas}")
    if(alarma and tiempo<=3 and cerraduras_abiertas<3):
        print("Sistema bloqueado")
        bloqueo=True

if(cerraduras_abiertas==3):
    print("\nVICTORIA")
elif(energia<=0 or tiempo<=0 or bloqueo==True):
    if bloqueo:
        print("\nDERROTA(bloqueo)")
    else:
        print("\nDERROTA")

print(f"energia= {energia}")
print(f"tiempo= {tiempo}")
print(f"cerraduras_abiertas= {cerraduras_abiertas}")
print("\nFIN DEL JUEGO")