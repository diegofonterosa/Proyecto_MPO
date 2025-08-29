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
                    todas_preguntas.extend(temas["preguntas"])
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

