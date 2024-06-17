import csv
lista=[] 

def menu():
    print("")
    print(".-.-.- MENU .-.-.-.")
    print("1. Agregar plan")
    print("2. Listar planes")
    print("3. Eliminar plan por ID")
    print("4. Generar bbdd")
    print("5. Cargar bbdd")
    print("6. Estadisticas")
    print("0. Salir")
    print("")
        
def agregar_plan():
    id=int(input("Ingrese id del plan: "))
    nombre=input("Ingrese nombre: ")
    porcentaje=int(input("Ingrese porcentaje: "))
    while porcentaje>100 and porcentaje<0:
        print("El porcentaje solo puede ser un valor entren 0 y 100")
        porcentaje=int(input("Ingrese porcentaje: ")) 
    if porcentaje>-1 and porcentaje<26:
        categoria="chiste"
    elif porcentaje>25 and porcentaje<50:
        categoria="anecdota"
    elif porcentaje>49 and porcentaje<76:
        categoria="Peligro"
    elif porcentaje>75 and porcentaje<100: 
        categoria="Atencion" 
    elif porcentaje==100:
        categoria="Esclavitud" 
    lista_datos=[id, nombre, porcentaje, categoria] 
    lista.append(lista_datos)

def listar_planes():
    for x in lista:
        print(f"ID: {x[0]} Nombre: {x[1]} Porcentaje: {x[2]} Categoria: {x[3]}")

def eliminar_plan_por_ID():
    print("")
    encontrado=False
    id_elimin=int(input("Ingrese id para eliminar plan: "))
    for x in lista:
        if id_elimin==x[0]:
            encontrado=True
            decision=input("¿Esta seguro de eliminar el plan? si/no: ").lower()
            if decision=="si":
                lista.remove(x) 
                print("El plan ha sido eliminado")
            else:
                print("Plan no eliminado")
            break 
        elif id_elimin!=x[0]: 
            print("No hay planes con el ID ingresado") 
        
def generar_csv():
    with open ('plan_datos.csv','w',newline='') as plan_datos:
        escritor_csv=csv.writer(plan_datos)
        escritor_csv.writerow(['id' , 'Nombre' , 'Porcentaje' , 'Categoria'])
        escritor_csv.writerows(lista)
        print("")               
        print("Archivo generado correctamente")               

def cargar_csv():
    print(".-.-. CARGAR DATOS DESDE CSV .-.-.")
    lista.clear()
    cont=0
    with open ('plan_datos.csv','r',newline='') as plan_datos:
        lector_csv=csv.reader(plan_datos)
        for fila in lector_csv:
            if cont==0:
                cont=cont+1
                continue
            id=int(fila[0])
            nom=fila[1]
            por=int(fila[2])
            cat=fila[3] 
            lista_nueva=[id,nom,por,cat] 
            lista.append(lista_nueva) 
              
def estadisticas():
    acumulador=0
    mayor_porcentaje=0
    for x in lista:
        acumulador=x[2]+acumulador
    for i in lista:
        if mayor_porcentaje<i[2]:
            mayor_porcentaje=i[2]
    cantidad=len(lista)
    promedio=acumulador/cantidad
    print(f"Promedio: {promedio}") 
    print(f"Porcentaje de efectividad mas alto: {mayor_porcentaje} ") 

while True:
    try:
        menu()
        op=int(input("Ingrese opcion: "))
        if op==1:
            agregar_plan()
        elif op==2:
            listar_planes()
        elif op==3:
            eliminar_plan_por_ID()
        elif op==4:
            generar_csv()
        elif op==5:
            cargar_csv() 
        elif op==6:
            estadisticas() 
        elif op==0:
            print("hasta pronto")
            break
        else:
            print("Error, ingrese una opcion valida")
    except:
        print("Ha ocurrido un error, redirigiendo ") 