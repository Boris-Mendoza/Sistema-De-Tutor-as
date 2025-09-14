# ===================================================
# SISTEMA DE TUTORÍAS UVG - CON HORARIOS Y LÍMITES
# Versión para principiantes (sin funciones avanzadas)
# ===================================================

# -----------------------------
# Listas para guardar la info
# -----------------------------
lista_de_tutores = []
lista_de_estudiantes = []
lista_de_tutorias = []

# -----------------------------
# Mostrar menú principal
# -----------------------------
def mostrar_menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1) Registrar nuevo tutor")
        print("2) Registrar nuevo estudiante")
        print("3) Buscar tutores por materia")
        print("4) Agendar tutoría")
        print("5) Ver todas las tutorías agendadas")
        print("6) Configurar horarios y límites del tutor")
        print("7) Salir del sistema")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            registrar_tutor()
        elif opcion == "2":
            registrar_estudiante()
        elif opcion == "3":
            buscar_tutores()
        elif opcion == "4":
            agendar_tutoria()
        elif opcion == "5":
            mostrar_tutorias()
        elif opcion == "6":
            configurar_horarios_y_limites()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

# -----------------------------
# Registrar tutor
# -----------------------------
def registrar_tutor():
    print("\n--- Registro de Tutor ---")
    nombre = input("Nombre: ")
    materia = input("Materia que enseña: ")
    precio_texto = input("Precio por hora: ")

    try:
        precio = float(precio_texto)
    except:
        print("Precio inválido.")
        return

    horarios = ingresar_horarios()

    try:
        max_horas = int(input("Máximo horas por estudiante por reserva: "))
        max_tutorias = int(input("Máximo total de tutorías que puede dar: "))
    except:
        print("Límites inválidos.")
        return

    nuevo_tutor = {
        "nombre": nombre,
        "materia": materia,
        "precio": precio,
        "horarios": horarios,
        "horas_ocupadas": [],
        "max_horas_estudiante": max_horas,
        "max_tutorias_total": max_tutorias,
        "tutorias_realizadas": 0
    }

    lista_de_tutores.append(nuevo_tutor)
    print("Tutor registrado exitosamente.")

# -----------------------------
# Ingresar bloques horarios
# -----------------------------
def ingresar_horarios():
    bloques = []
    while True:
        bloque = input("Ingrese horario (formato HH:MM-HH:MM): ")
        if len(bloque) != 11 or ":" not in bloque or "-" not in bloque:
            print("Formato inválido.")
        else:
            bloques.append(bloque)
        otra = input("¿Agregar otro bloque? (s/n): ")
        if otra.lower() != "s":
            break
    return bloques

# -----------------------------
# Registrar estudiante
# -----------------------------
def registrar_estudiante():
    print("\n--- Registro de Estudiante ---")
    nombre = input("Nombre del estudiante: ")
    materia = input("Materia que necesita: ")

    nuevo_estudiante = {
        "nombre": nombre,
        "materia": materia
    }

    lista_de_estudiantes.append(nuevo_estudiante)
    print("Estudiante registrado.")

# -----------------------------
# Buscar tutores por materia
# -----------------------------
def buscar_tutores():
    materia = input("Ingrese la materia a buscar: ")
    encontrados = []

    for tutor in lista_de_tutores:
        if tutor["materia"].lower() == materia.lower():
            encontrados.append(tutor)

    if len(encontrados) == 0:
        print("No hay tutores disponibles.")
    else:
        print("\nTutores disponibles:")
        i = 1
        for tutor in encontrados:
            print(str(i) + ") " + tutor["nombre"] + " - Q" + str(tutor["precio"]) + "/hora")
            i += 1

# -----------------------------
# Convertir bloques a horas individuales
# Ejemplo: "14:00-16:00" → ["14:00", "15:00"]
# -----------------------------
def convertir_bloque_a_horas(bloque):
    try:
        partes = bloque.split("-")
        hora_inicio = int(partes[0].split(":")[0])
        hora_fin = int(partes[1].split(":")[0])

        horas = []
        h = hora_inicio
        while h < hora_fin:
            texto = str(h).zfill(2) + ":00"
            horas.append(texto)
            h += 1
        return horas
    except:
        return []

# -----------------------------
# Ver disponibilidad del tutor
# -----------------------------
def mostrar_disponibilidad(tutor):
    disponibles = []
    ocupados = []

    for bloque in tutor["horarios"]:
        horas = convertir_bloque_a_horas(bloque)
        for hora in horas:
            if hora in tutor["horas_ocupadas"]:
                ocupados.append(hora)
            else:
                disponibles.append(hora)

    print("\n========================================")
    print("HORARIOS DE", tutor["nombre"].upper())
    print("Máximo horas por reserva:", tutor["max_horas_estudiante"])
    print("Tutorías restantes:", tutor["max_tutorias_total"] - tutor["tutorias_realizadas"])
    print("\n✅ DISPONIBLES:")
    for hora in disponibles:
        print("  ", hora)
    print("\n❌ OCUPADOS:")
    for hora in ocupados:
        print("  ", hora)
    print("========================================")

    return disponibles

# -----------------------------
# Agendar tutoría
# -----------------------------
def agendar_tutoria():
    estudiante = input("Nombre del estudiante: ")
    materia = input("Materia a buscar: ")

    tutores_disponibles = []
    for tutor in lista_de_tutores:
        if tutor["materia"].lower() == materia.lower():
            tutores_disponibles.append(tutor)

    if len(tutores_disponibles) == 0:
        print("No hay tutores disponibles.")
        return

    print("\nTutores disponibles:")
    i = 1
    for tutor in tutores_disponibles:
        print(str(i) + ") " + tutor["nombre"])
        i += 1

    seleccion_texto = input("Seleccione el número del tutor: ")
    try:
        seleccion = int(seleccion_texto)
        tutor = tutores_disponibles[seleccion - 1]
    except:
        print("Selección inválida.")
        return

    if tutor["tutorias_realizadas"] >= tutor["max_tutorias_total"]:
        print("Este tutor ya alcanzó su límite de tutorías.")
        return

    disponibles = mostrar_disponibilidad(tutor)

    if len(disponibles) == 0:
        print("No hay horas disponibles.")
        return

    print("\nPuede elegir hasta", tutor["max_horas_estudiante"], "hora(s).")
    for i in range(len(disponibles)):
        print(str(i+1) + ") " + disponibles[i])

    seleccion_horas = input("Seleccione los números de hora (ej. 1,2): ")
    try:
        partes = seleccion_horas.split(",")
        if len(partes) > tutor["max_horas_estudiante"]:
            print("Excede el límite de horas permitidas.")
            return

        horas_reservadas = []
        for texto in partes:
            numero = int(texto)
            hora = disponibles[numero - 1]
            horas_reservadas.append(hora)

        for hora in horas_reservadas:
            tutor["horas_ocupadas"].append(hora)

        tutor["tutorias_realizadas"] += 1

        nueva_tutoria = {
            "estudiante": estudiante,
            "tutor": tutor["nombre"],
            "materia": materia,
            "horas": horas_reservadas
        }

        lista_de_tutorias.append(nueva_tutoria)
        print("Tutoría agendada con éxito.")

    except:
        print("Error al procesar la selección.")

# -----------------------------
# Configurar horarios y límites
# -----------------------------
def configurar_horarios_y_limites():
    nombre = input("Ingrese el nombre del tutor: ")
    tutor_encontrado = None

    for tutor in lista_de_tutores:
        if tutor["nombre"].lower() == nombre.lower():
            tutor_encontrado = tutor
            break

    if tutor_encontrado is None:
        print("Tutor no encontrado.")
        return

    tutor_encontrado["horarios"] = ingresar_horarios()
    tutor_encontrado["max_horas_estudiante"] = int(input("Nuevo máximo de horas por estudiante: "))
    tutor_encontrado["max_tutorias_total"] = int(input("Nuevo máximo total de tutorías: "))
    print("Horarios y límites actualizados.")

# -----------------------------
# Ver todas las tutorías agendadas
# -----------------------------
def mostrar_tutorias():
    if len(lista_de_tutorias) == 0:
        print("No hay tutorías agendadas.")
        return

    print("\n--- Tutorías Agendadas ---")
    contador = 1
    for tutoria in lista_de_tutorias:
        print(str(contador) + ") Estudiante:", tutoria["estudiante"])
        print("   Tutor:", tutoria["tutor"])
        print("   Materia:", tutoria["materia"])
        print("   Horas:", ", ".join(tutoria["horas"]))
        contador += 1

# -----------------------------
# Iniciar el sistema
# -----------------------------
mostrar_menu()
