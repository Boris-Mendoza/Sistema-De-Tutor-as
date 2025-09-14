

# -----------------------------
# Listas para guardar la info
# -----------------------------
lista_de_tutores = []
lista_de_estudiantes = []
lista_de_tutorias = []

# -----------------------------
# Menú principal mejorado
# -----------------------------
def mostrar_menu():
    while True:
        print("\n🎓 ========== SISTEMA DE TUTORÍAS UVG ========== ")
        print("1) 👨‍🏫 Registrar nuevo tutor")
        print("2) 👨‍🎓 Registrar nuevo estudiante (con horarios)")
        print("3) 🔍 Buscar tutores compatibles con mi horario")
        print("4) 📅 Agendar tutoría")
        print("5) 📋 Ver todas las tutorías agendadas")
        print("6) ⚙️  Configurar horarios de tutor")
        print("7) 👁️  Consultar todos los tutores disponibles")
        print("8) ❌ Salir del sistema")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
            registrar_tutor()
        elif opcion == "2":
            registrar_estudiante_con_horarios()
        elif opcion == "3":
            buscar_tutores_compatibles()
        elif opcion == "4":
            agendar_tutoria()
        elif opcion == "5":
            mostrar_tutorias()
        elif opcion == "6":
            configurar_horarios_y_limites()
        elif opcion == "7":
            consultar_tutores_disponibles()
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

# -----------------------------
# Validar y registrar horarios estudiante
# -----------------------------
def ingresar_horarios_estudiante():
    print("\n⏰ Ingrese los horarios disponibles del estudiante.")
    print("Ejemplo válido: 14:00-16:00")

    horarios = []
    while True:
        bloque = input("Ingrese horario (formato HH:MM-HH:MM): ")
        if len(bloque) != 11 or ":" not in bloque or "-" not in bloque:
            print("Formato inválido. Intente de nuevo.")
        else:
            horarios.append(bloque)
        otra = input("¿Agregar otro bloque? (s/n): ")
        if otra.lower() != "s":
            break
    return horarios

# -----------------------------
# Registrar estudiante con horarios
# -----------------------------
def registrar_estudiante_con_horarios():
    print("\n--- Registro de Estudiante ---")
    nombre = input("Nombre del estudiante: ")
    materia = input("Materia que necesita: ")
    horarios_disponibles = ingresar_horarios_estudiante()

    nuevo_estudiante = {
        "nombre": nombre,
        "materia": materia,
        "horarios_disponibles": horarios_disponibles
    }

    lista_de_estudiantes.append(nuevo_estudiante)
    print("✅ Estudiante registrado con horarios.")

# -----------------------------
# Convertir "14:00-16:00" a ["14:00", "15:00"]
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
# Buscar tutores compatibles con horario
# -----------------------------
def buscar_tutores_compatibles():
    print("\n--- Buscar Tutores Compatibles ---")
    nombre_estudiante = input("Ingrese su nombre registrado: ")
    estudiante = None

    # Buscar estudiante en la lista
    for est in lista_de_estudiantes:
        if est["nombre"].lower() == nombre_estudiante.lower():
            estudiante = est
            break

    if estudiante is None:
        print("Estudiante no encontrado.")
        return

    materia = estudiante["materia"]
    horarios_estudiante = []
    for bloque in estudiante["horarios_disponibles"]:
        horarios_estudiante.extend(convertir_bloque_a_horas(bloque))

    encontrados = []
    for tutor in lista_de_tutores:
        if tutor["materia"].lower() == materia.lower():
            horarios_tutor = []
            for bloque in tutor["horarios"]:
                horarios_tutor.extend(convertir_bloque_a_horas(bloque))
            compatibles = []
            for hora in horarios_estudiante:
                if hora in horarios_tutor and hora not in tutor["horas_ocupadas"]:
                    compatibles.append(hora)
            if len(compatibles) > 0:
                encontrados.append(tutor)

    if len(encontrados) == 0:
        print("No se encontraron tutores compatibles.")
    else:
        print("\n📚 Tutores compatibles con tu horario:")
        for i in range(len(encontrados)):
            print(str(i+1) + ") " + encontrados[i]["nombre"] + " - Q" + str(encontrados[i]["precio"]))

# -----------------------------
# Mostrar horarios visualmente
# -----------------------------
def mostrar_horarios_visual(tutor):
    print("\n🕓 Horarios del tutor:", tutor["nombre"])
    print("----------------------------------------")
    print("✅ DISPONIBLES:")
    disponibles = []
    ocupados = []

    for bloque in tutor["horarios"]:
        horas = convertir_bloque_a_horas(bloque)
        for hora in horas:
            if hora in tutor["horas_ocupadas"]:
                ocupados.append(hora)
            else:
                disponibles.append(hora)

    for hora in disponibles:
        print("  ", hora)

    print("\n❌ OCUPADOS:")
    for hora in ocupados:
        print("  ", hora)
    print("----------------------------------------")

# -----------------------------
# Verificar disponibilidad tutor (simple)
# -----------------------------
def verificar_disponibilidad_tutor(tutor):
    disponibles = []
    for bloque in tutor["horarios"]:
        horas = convertir_bloque_a_horas(bloque)
        for hora in horas:
            if hora not in tutor["horas_ocupadas"]:
                disponibles.append(hora)
    return disponibles

# -----------------------------
# Consultar todos los tutores disponibles
# -----------------------------
def consultar_tutores_disponibles():
    print("\n👁️ Lista de todos los tutores registrados:")
    print("=============================================")

    if len(lista_de_tutores) == 0:
        print("No hay tutores registrados.")
        return

    for tutor in lista_de_tutores:
        print("👨‍🏫 Tutor:", tutor["nombre"])
        print("📘 Materia:", tutor["materia"])
        print("💵 Precio por hora: Q", tutor["precio"])
        print("⏳ Tutorías restantes:", tutor["max_tutorias_total"] - tutor["tutorias_realizadas"])
        mostrar_horarios_visual(tutor)
        print("=============================================")

# -----------------------------
# Registro de tutor (igual)
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
    print("✅ Tutor registrado exitosamente.")

# -----------------------------
# Ingresar bloques horarios para tutor
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
# Agendar tutoría (sin cambios)
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

    disponibles = verificar_disponibilidad_tutor(tutor)

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
        print("✅ Tutoría agendada con éxito.")

    except:
        print("Error al procesar la selección.")

# -----------------------------
# Configurar horarios y límites del tutor
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
    print("✅ Horarios y límites actualizados.")

# -----------------------------
# Mostrar tutorías agendadas
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
