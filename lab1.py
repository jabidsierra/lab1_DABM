lista_paciente = []
def entrada_datos():
    print("-"*50)
    print("Registro  de Pacientes".center(50," "))
    print("-"*50)
    nombre=input("Nombre: ")
    edad=input("Edad: ")
    sangre=input("Tipo de sangre (minúsculas: ej(o+, a-...)): ")
    peso=input("Peso [kg]: ")
    estatura=input("Estatura [cm]: ")
    glucosa=input("Glucosa en sangre: ")
    presion=input("Presión arterial (Sistólica/Diastólica ej: 120/80): ")
    colesterol=input("Colesterol: ")
    paciente ={
        "nombre":nombre,
        "edad":edad,
        "sangre":sangre,
        "peso": peso,
        "estatura": estatura,
        "glucosa": glucosa,
        "presion": presion,
        "colesterol": colesterol
    }
    lista_paciente.append(paciente)
    print("Paciente registrado con éxito".center(50,"*"))
    

def analisis_datos():
    print("-"*50)
    print("Análisis de datos generales".center(50," "))
    print("-"*50)
    promedio_glucosa(lista_paciente)
    promedio_colesterol(lista_paciente)
    tipo_sangre_mas_comun(lista_paciente)
    promedio = promedio_imc(lista_paciente)
    estado = estado_imc(promedio)
    print("El promedio del IMC de los pacientes es de: ", promedio, " y el estado general es: ", estado)
    

def reporte():
    print("-"*50)
    print("Reporte por paciente".center(50," "))
    print("-"*50)
    nombre = input("Ingrese el nombre del paciente que desea buscar: ")
    buscar_por_nombre(lista_paciente,nombre)


def promedio_glucosa(lista_pacientes):
    glucosas = []
    for paciente in lista_pacientes:
            glucosas.append(int(paciente['glucosa'])) 
    promedio = sum(glucosas) / len(glucosas)  
    
    return print("El promedio de glucosa en sangre de los pacientes es de: ", promedio)


def promedio_colesterol(lista_pacientes):
    colesteroles = []
    for paciente in lista_pacientes:
            colesteroles.append(int(paciente['colesterol']))
    promedio = sum(colesteroles) / len(colesteroles)
    
    return print("El promedio de colesterol de los pacientes es de: ", promedio)


def tipo_sangre_mas_comun(lista_pacientes):
    tipos_sangre = {}
    for paciente in lista_pacientes:
        tipo_sangre = paciente['sangre']
        tipos_sangre[tipo_sangre] = tipos_sangre.get(tipo_sangre, 0) + 1
    sangre_mas_comun = max(tipos_sangre, key=tipos_sangre.get)
    return print("El tipo de sangre más común es: ",sangre_mas_comun)


def promedio_imc(lista_pacientes):
    imcs = []
    for paciente in lista_pacientes:
        imc =round(int(paciente['peso']) / ((int(paciente['estatura']) / 100) ** 2),2) 
        imcs.append(imc)
    promedio = round(sum(imcs) / len(imcs),2)
    imcs = []
    return promedio


def estado_imc(imc):
    if imc < 18.5:
        return "Bajo peso (delgadez)"
    elif 18.5 <= imc < 25:
        return "Peso normal (saludable)"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Tipo I"
    elif 35 <= imc < 40:
        return "Obesidad Tipo II (severa)"
    else:
        return "Obesidad Tipo III (mórbida)"


def evaluar_glucosa(glucosa):
    if glucosa < 70:
        return "Hipoglucemia (bajo nivel de glucosa)"
    elif 70 <= glucosa < 100:
        return "Normal"
    elif 100 <= glucosa < 126:
        return "Prediabetes"
    else:
        return "Diabetes (alto nivel de glucosa)"


def evaluar_colesterol(colesterol):
    if colesterol < 130:
        return "Normal"
    elif 130 <= colesterol < 159:
        return "Borde alto"
    elif 160 <= colesterol < 189:
        return "Alto"
    else:
        return "Muy alto"


def evaluar_presion(presion):
    if len(presion) != 6:
        return "Formato de presión arterial inválido"
    sa, db = map(int, presion.split('/'))
    if sa < 90 or db < 60:
        return "Hipotensión (baja presión arterial)"
    elif sa <= 120 and db <= 80:
        return "Normal"
    elif 120 < sa < 140 and 80 < db < 90:
        return "Prehipertensión"
    elif 140 <= sa < 160 and 90 <= db < 100:
        return "Hipertensión grado 1"
    elif 160 <= sa < 180 and 100 <= db < 110:
        return "Hipertensión grado 2"
    else:
        return "Hipertensión grado 3 (crisis hipertensiva)"
    
def buscar_por_nombre(lista_paciente, nombre):
    pacientes_encontrados = []
    for paciente in lista_paciente:
        if paciente["nombre"].lower() == nombre.lower():
            pacientes_encontrados.append(paciente)
    if pacientes_encontrados:
        for paciente in pacientes_encontrados:
            print("Información del paciente encontrado".center(50, "-"))
            print("  || ", "Nombre:     ", paciente['nombre'],"\n"," || "," Edad:       ", paciente['edad'], "\n", " || ", " Tipo de sangre:  ", paciente['sangre'], "\n", " || ", " Peso(kg):       ", paciente['peso'],"\n", " || ", " Estatura(cm)      ", paciente['estatura'],"\n")
            print("Diagnóstico".center(50, "-"))
            glucosa_estado = evaluar_glucosa(int(paciente['glucosa']))
            print("  || ", "Glucosa:     ", paciente['glucosa'], " -> ", glucosa_estado, "\n")
            presion_estado = evaluar_presion(paciente['presion'])
            print("  || ", "Presión:     ", paciente['presion'], " -> ", presion_estado, "\n")
            colesterol_estado = evaluar_colesterol(int(paciente['colesterol']))
            print("  || ", "Colesterol:  ", paciente['colesterol'], " -> ", colesterol_estado, "\n")
            imc = round(int(paciente['peso']) / ((int(paciente['estatura']) / 100) ** 2), 2)
            print("  || ", "IMC:         ", imc)
            print("  || ", "Estado IMC:  ", estado_imc(imc), "\n")
            print("-" * 50)
    else:
        print("No se encontró información para la persona con el nombre especificado.")


def menu():
    print("\n"*5)
    print("-"*50)
    print("Sistema de Registro y Gestión de Pacientes".center(50," "))
    print("-"*50)
    print("[I]ngreso de pacientes")
    print("[A]nálisis de datos generales")
    print("[R]eporte por paciente")
    print("[S]alir")
    opcion=input(":>")
    opcion=opcion.upper()
    if opcion == "I":
        entrada_datos()
    elif opcion == "A":
        analisis_datos()
    elif opcion == "R":
        reporte()
    elif opcion == "S":
        exit()
    else:
        print("Opción invalida")
        menu()
    menu()



menu()
