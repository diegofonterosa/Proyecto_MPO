import json
import os
from datetime import datetime
#Preguntas
def cargar_preguntas():
    preguntas = {
        "informática": {
            "nombre": "Informática Básica",
            "preguntas":[
                {
                    "pregunta": "¿Qué significa RAM?",
                    "opciones":["A. Ramdom Access Memory", "B. Read Access Memory",
                                "C. Real Access Memory", "D. Rapid Access Memory"],
                    "respuesta_correcta": "A"
                },
                 {
                    "pregunta": "¿Cúal es la función principal del sistema operativo?",
                    "opciones":["A. Ejecutar programas", "B. Gestionar recursos del sistema",
                                "C. Crear documentos", "D. Navegar por internet"],
                    "respuesta_correcta": "B"
                },
                 {
                    "pregunta": "¿Qué puerto usa por defecto el protocolo HTTP?",
                    "opciones": ["A. 21", "B. 22", "C. 80", "D. 443"],
                    "respuesta_correcta": "C"
                },
                {
                    "pregunta": "¿Cuál es la dirección IP de loopback?",
                    "opciones": ["A. 192.168.1.1", "B. 127.0.0.1", "C. 10.0.0.1", "D. 172.16.0.1"],
                    "respuesta_correcta": "B"
                }
            ]
        },
        "redes": {
            "nombre": "Redes y Comunicaciones",
            "preguntas": [
                {
                    "pregunta": "¿Qué significa DNS?",
                    "opciones": ["A. Domain Name System", "B. Data Network Service", 
                               "C. Digital Network System", "D. Dynamic Name Service"],
                    "respuesta_correcta": "A"
                },
                {
                    "pregunta": "¿En qué capa del modelo OSI trabaja un router?",
                    "opciones": ["A. Capa 1 (Física)", "B. Capa 2 (Enlace)", 
                               "C. Capa 3 (Red)", "D. Capa 4 (Transporte)"],
                    "respuesta_correcta": "C"
                },
                {
                    "pregunta": "¿Qué protocolo se usa para transferir archivos de forma segura?",
                    "opciones": ["A. FTP", "B. SFTP", "C. HTTP", "D. SMTP"],
                    "respuesta_correcta": "B"
                }
            ]
        },
        "seguridad": {
            "nombre": "Seguridad Informática",
            "preguntas": [
                {
                    "pregunta": "¿Qué es un firewall?",
                    "opciones": ["A. Un antivirus", "B. Un sistema de filtrado de tráfico", 
                               "C. Un programa de backup", "D. Un navegador web"],
                    "respuesta_correcta": "B"
                },
                {
                    "pregunta": "¿Qué significa HTTPS?",
                    "opciones": ["A. HyperText Transfer Protocol Secure", "B. High Transfer Protocol System", 
                               "C. HyperText Transfer Protocol System", "D. High Text Protocol Secure"],
                    "respuesta_correcta": "A"
                }
            ]
        }
    }
    return preguntas
# Seleccionar tema
def seleccionar_tema(preguntas):
    print("Seleccione un tema:")
    temas = list(preguntas.keys())
    
    for i, tema in enumerate(temas, 1):
        print(f"{i}. {preguntas[tema]["nombre"]}")
    print(f"{len(temas)+1}. Todas las preguntas  (modo mixto)")
   # Selección 
    while True:
        try:
            opcion = int(input(f"\nElige una opción (1-{len(temas)+1}):"))
            
            if 1 <= opcion <= len(temas):
                tema_elegido = temas[opcion - 1]
                return preguntas[tema_elegido]["preguntas"], preguntas[tema_elegido]["nombre"]
            elif opcion == len(temas) + 1:
                #Todas las preguntas
                todas_preguntas = []
                for tema in preguntas.values():
                    todas_preguntas.extend(tema["preguntas"])
                return todas_preguntas, "Todas las materias"
            else:
                print("Opción no válida. Inténtalo de nuevo")
        except ValueError:
            print("Por favor, introduce un número válido")
            
# Muestra pregunta
def mostrar_pregunta(pregunta, numero, total):
    print("\n" + "="*50)                                       
    print(f"PREGUNTA {numero} de {total}")
    print("="*50)
    print(f"{pregunta["pregunta"]}")
    print()
    for opcion in pregunta["opciones"]:
        print(f"{opcion}")
    print()
#Obtener respuesta
def obtener_respuesta():
    respuestas_validas = ["A", "B", "C", "D"]
    while True:
        respuesta = input("Selecciona una opción (A, B, C, D): ").strip().upper()
        if respuesta in respuestas_validas:
            return respuesta
        print("Opción no válida. Inténtalo de nuevo.")
 #Corregir la respuesta     
def corregir_respuesta(respuesta, correcta):
    return respuesta == correcta
# Valoración
def obtener_valoracion(porcentaje):
    if porcentaje >= 90:
        return "EXCELENTE - Eres un experto"
    elif porcentaje >= 75:
        return "MUY BIEN - Gran conocimiento"
    elif porcentaje >= 60:
        return "BIEN - Buen trabajo"
    elif porcentaje >= 50:
        return "REGULAR - Puedes mejorar"
    else:
        return "INSUFICIENTE - Necesitas estudiar más" 
# Mostrar el resultado    
def mostrar_resultados(aciertos, total, tema):
    print("\n" + "="*60)
    print("RESULTADOS DEL CUESTIONARIO")
    print("="*60)
    
    porcentaje = (aciertos / total) * 100
    fallos = total - aciertos
    valoracion = obtener_valoracion(porcentaje)
    
    print(f"Tema: {tema}")
    print(f"Preguntas totales: {total}")
    print(f"Respuestas correctas: {aciertos}")
    print(f"Respuestas incorrectas: {fallos}")
    print(f"Porcentaje de aciertos: {porcentaje:.1f}%")
    print(f"Valoración: {valoracion}")
    print("="*60)
    
    return porcentaje
# Cargar el ranking
def cargar_ranking():
    archivo_ranking = "ranking.json"
    try:
        if os.path.exists(archivo_ranking):
            with open(archivo_ranking, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        else:
            return []
    except:
        print("Error al cargar el ranking. Se iniciará de nuevo")
        return []
#Guardar el ranking    
def guardar_ranking(ranking):
    archivo_ranking = "ranking.json"
    try:
        with open(archivo_ranking, "w", encoding="utf-8") as archivo:
            json.dump(ranking, archivo, indent=2, ensure_ascii=False)
        return True
    except:
        print("Error al guardar el ranking.")
        return False
# Añadir al ranking resultados  
def agregar_al_ranking(ranking, nombre, tema, aciertos, total, porcentaje):
    
    nuevo_resultado = {
        "nombre": nombre,
        "tema": tema,
        "aciertos": aciertos,
        "total": total,
        "porcentaje": porcentaje,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    ranking.append(nuevo_resultado) 
    ranking.sort(key=lambda x: x["porcentaje"], reverse=True)
    
    return ranking
# Mostar ranking
def mostrar_ranking(ranking):
    
    if not ranking:
        print("\nEl ranking está vacío. ¡Sé el primero en participar!")
        return

    print("\n" + "="*70)
    print("\nRANKING DE MEJORES PUNTUACIONES")
    print("="*70)
    print(f"{"#":<3} {"Nombre":<20} {"Tema":<20} {"Aciertos":<10} {"%":<10} {"Fecha":<19}")
    print("="*70)
    
    top_10 = ranking[:10]
    for i, resultado in enumerate(top_10, 1):
        nombre = resultado["nombre"][:20]
        tema = resultado["tema"][:20]
        aciertos = f"{resultado["aciertos"]}/{resultado["total"]}"
        porcentaje = f"{resultado["porcentaje"]:.1f}%"
        fecha = resultado["fecha"]

        print(f"{i:<3}. {nombre:<21} - {tema:<21} - {aciertos:<10} - {porcentaje:<10} - {fecha}")
        
    print("="*70)
# Ejecutar el cuestionario
def ejecutar_cuestionario():
    
    print("\n¡BIENVENIDO AL CUESTIONARIO DE ASIR!")
    
    # Cargar preguntas y ranking
    preguntas = cargar_preguntas()
    ranking = cargar_ranking()
    
    # Seleccionar tema
    preguntas_elegidas, tema = seleccionar_tema(preguntas)
    
    # Obtener nombre del usuario
    nombre = input("\nIntroduce tu nombre: ").strip()
    if not nombre:
        nombre = "Anónimo"
    
    print(f"\nHola {nombre}! Vas a responder {len(preguntas_elegidas)} preguntas sobre: {tema}")
    input("Presiona Enter cuando estés listo...")
    
    # Variables para el cuestionario
    aciertos = 0
    
    # Ejecutar cada pregunta
    for i, pregunta in enumerate(preguntas_elegidas, 1):
        mostrar_pregunta(pregunta, i, len(preguntas_elegidas))
        respuesta = obtener_respuesta()
        
        if corregir_respuesta(respuesta, pregunta['respuesta_correcta']):
            print(" ¡CORRECTO!")
            aciertos += 1
        else:
            print("X INCORRECTO")
            # Mostrar cuál era la respuesta correcta
            respuesta_correcta = pregunta['respuesta_correcta']
            for opcion in pregunta['opciones']:
                if opcion.startswith(respuesta_correcta):
                    print(f"La respuesta correcta era: {opcion}")
                    break
        
        # Pausa entre preguntas
        if i < len(preguntas_elegidas):
            input("\nPresiona Enter para continuar...")
    
    # Mostrar resultados
    porcentaje = mostrar_resultados(aciertos, len(preguntas_elegidas), tema)
    
    # Agregar al ranking
    ranking = agregar_al_ranking(ranking, nombre, tema, aciertos, len(preguntas_elegidas), porcentaje)
    
    # Guardar ranking
    if guardar_ranking(ranking):
        print("\n¡Tu puntuación ha sido guardada en el ranking!")
    
    return ranking

def mostrar_menu():
    print("\n" + "="*40)
    print("   CUESTIONARIO INTERACTIVO ASIR")
    print("="*50)
    print("### MENU PRINCIPAL ###")
    print("1 - Empezar cuestionario")
    print("2 - Mostrar ranking")
    print("3 - Salir")
    print("="*40)
    
def main():
    
    ranking = cargar_ranking()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            ranking = ejecutar_cuestionario()
        elif opcion == "2":
            mostrar_ranking(ranking)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")
            
if __name__ == "__main__":
    main()

