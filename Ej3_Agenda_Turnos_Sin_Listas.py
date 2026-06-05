#3
operador = input("Nombre del operador: ")
op=0
lunes1=""
lunes2=""
lunes3=""
lunes4=""
martes1=""
martes2=""
martes3=""
while(op!=5):
    print("\n++++++Menu++++++")
    print("1- Reservar turno")
    print("2-Cancelar turno(por nombre)")
    print("3-Ver agenda del dia")
    print("4-Ver resumen general")
    print("5-Cerrar sistema")
    op=int(input("Opcion: "))

    if(op==1):
        reserva=int(input("Ingresar el numero 1(Lunes) o 2(Martes)"))
        paciente=input("Ingresar nombre del paciente: ")
        while(paciente.isalpha()==False):
            paciente=input("Ingresar nuevamente nombre del paciente: ")
        if(reserva==1):
            if(lunes1==""):
                lunes1=paciente
            elif(lunes2==""):
                lunes2=paciente
            elif(lunes3==""):
                lunes3=paciente
            elif(lunes4==""):
                lunes4=paciente
            else:
                print("\nNo hay turnos para el dia ingresado")
        elif (reserva==2):
            if(martes1==""):
                martes1=paciente
            elif(martes2==""):
                martes2=paciente
            elif(martes3==""):
                martes3=paciente
            else:
                print("\nNo hay turnos para el dia ingresado")

        else: 
            print("\nNo hay turnos para el dia ingresado")
    elif(op==2):
        cancelar=input("Elegir el dia: ")    
        while(cancelar.isdigit()==False or cancelar!="1" or cancelar!="2"):
            cancelar=input("error. Elegir nuevamente el dia: ")
        paciente=input("Ingresar el nombre del paciente")
        while(paciente.isalpha()==False):
            paciente=input("\nIngresar nuevamente el paciente(solo letras)")
        if(cancelar=="1"):
            if(paciente==lunes1):
                lunes1=""
            elif(paciente==lunes2):
                lunes2=""
            elif(paciente==lunes3):
                lunes3=""
            elif(paciente==lunes4):
                lunes4=""
            else: 
                print("/nEl paciente no se ha encontrado")
        elif(cancelar=="2"):
            if(paciente==martes1):
                martes1=""
            elif(paciente==martes2):
                martes2=""
            elif(paciente==martes3):
                martes3=""
            else: 
                print("/nEl paciente no se ha encontrado")
    elif(op==3):
        print("Agenda")
        dia=int(input("\nIngresar el dia: "))
        if(dia==1):
            print("Lunes")
            print(f"Turno1: {lunes1}")
            print(f"Turno2: {lunes2}")
            print(f"Turno3: {lunes3}")
            print(f"Turno4: {lunes4}")
        elif(dia==2):
            print("Martes")
            print(f"Turno1: {martes1}")
            print(f"Turno2: {martes2}")
            print(f"Turno3: {martes3}")
        else:
            ("\nSin turnos")
    elif(op==4):
        print("\nResumen general")
        print("\n Turnos disponibles")
        #lunes
        diasLibres=0;
        if(lunes1==""):
            diasLibres+=1
        if(lunes2==""):
            diasLibres+=1
        if(lunes3==""):
            diasLibres+=1
        if(lunes4==""):
            diasLibres+=1
        print(f"Lunes: {diasLibres}")
        #martes
        diasLibres=0;
        if(martes1==""):
            diasLibres+=1
        if(martes2==""):
            diasLibres+=1
        if(martes3==""):
            diasLibres+=1
        print(f"Martes: {diasLibres}")
    elif(op==5):
        print("\nFin del programa")
    else:
        print("\nopcion incorrecta")
