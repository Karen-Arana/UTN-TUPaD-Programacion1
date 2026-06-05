intento=1
usuario=input("Ingresar usuario: ")
clave=input("Ingresar clave(6 caracteres minimo): ")
while(intento<3 and (usuario== "" or len(clave)<6)):
    print("ERROR: credenciales invalidas")
    intento+=1
    usuario=input("Ingresar nuevamente usuario: ")
    clave=input("Ingresar nuevamente clave(6 caracteres minimo): ")
if(usuario!= "" and len(clave)>=6):
    print("acceso concedido")
    op=0
    while(op!=4):
        print("\n ++++++++++++Menu++++++++++")
        print("1-Ver estado de inscripción")
        print("2-Cambiar clave")
        print("3-Mostrar mensaje motivacional")
        print("4-Salir")
        op=input("Ingresar opcion: ")
        if (op.isdigit()==True):
            op=int(op)
            if(op==1): 
                print("\nInscripto")
            elif(op==2):
                clave=input("\nIngresar clave(6 caracteres minimo): ")
                if(len(clave)<6):
                    print("Error: mínimo 6 caracteres.")
                else:
                    clave1=input("Confirmar clave: ")
                    if(clave!=clave1):
                        print("\nLas claves no coinciden")
                    else: 
                        print("\nClave confirmada")
            elif(op==3):
                print("\nLas cosas buenas toman tiempo")
            elif op==4:
                print("Fin del programa #2")
            else: print("\nOpcion fuera de rango")
        else: print("\nIngrese un numero valido")
else: print("\nUsuario bloqueado")