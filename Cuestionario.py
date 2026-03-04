from __future__ import annotations

import json
import os
import random
import select
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

RANKING_FILE = Path("ranking.json")
VALID_OPTIONS = {"A", "B", "C", "D"}
OPTION_LETTERS = ["A", "B", "C", "D"]


def cargar_preguntas() -> dict[str, dict[str, Any]]:
    return {
        "informatica": {
            "nombre": "Informática Básica",
            "preguntas": [
                {"pregunta": "¿Qué significa RAM?", "opciones": ["A. Random Access Memory", "B. Read Access Memory", "C. Real Access Memory", "D. Rapid Access Memory"], "respuesta_correcta": "A"},
                {"pregunta": "¿Cuál es la función principal del sistema operativo?", "opciones": ["A. Ejecutar programas", "B. Gestionar recursos del sistema", "C. Crear documentos", "D. Navegar por internet"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué puerto usa por defecto HTTP?", "opciones": ["A. 21", "B. 22", "C. 80", "D. 443"], "respuesta_correcta": "C"},
                {"pregunta": "¿Cuál es la IP de loopback?", "opciones": ["A. 192.168.1.1", "B. 127.0.0.1", "C. 10.0.0.1", "D. 172.16.0.1"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué componente ejecuta operaciones matemáticas y lógicas?", "opciones": ["A. GPU", "B. RAM", "C. CPU", "D. SSD"], "respuesta_correcta": "C"},
                {"pregunta": "¿Qué significa SSD?", "opciones": ["A. Solid State Drive", "B. Secure Storage Disk", "C. Serial System Drive", "D. Shared State Device"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué sistema de archivos es típico de Linux?", "opciones": ["A. NTFS", "B. ext4", "C. FAT32", "D. APFS"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué comando muestra el directorio actual en Linux?", "opciones": ["A. ls", "B. pwd", "C. cd", "D. whoami"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué extensión suele tener un script de Bash?", "opciones": ["A. .py", "B. .sh", "C. .ps1", "D. .bat"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué significa BIOS?", "opciones": ["A. Basic Input Output System", "B. Binary Internal Operating Service", "C. Boot Integrated Operating Setup", "D. Basic Internet Output Service"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué memoria se borra al apagar el equipo?", "opciones": ["A. ROM", "B. RAM", "C. SSD", "D. Flash"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué atajo de teclado suele copiar en la mayoría de sistemas?", "opciones": ["A. Ctrl+X", "B. Ctrl+V", "C. Ctrl+C", "D. Ctrl+Z"], "respuesta_correcta": "C"},
                {"pregunta": "¿Qué protocolo se usa para recibir correo en local desde servidor?", "opciones": ["A. SMTP", "B. POP3", "C. SNMP", "D. SSH"], "respuesta_correcta": "B"},
                {"pregunta": "¿Cuál de estos es un navegador web?", "opciones": ["A. Docker", "B. Firefox", "C. Apache", "D. MySQL"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué comando instala paquetes en Ubuntu?", "opciones": ["A. yum", "B. apt", "C. pacman", "D. zypper"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué representa ASCII?", "opciones": ["A. American Standard Code for Information Interchange", "B. Advanced System Coding for Internet Integration", "C. Automated Standard Command Interface", "D. Application Secure Code Integration"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué es la virtualización?", "opciones": ["A. Cifrar discos", "B. Crear máquinas virtuales sobre hardware físico", "C. Comprimir archivos", "D. Cambiar DNS"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué comando lista archivos en Linux?", "opciones": ["A. dir", "B. ls", "C. tree", "D. cat"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué tipo de software es GNU/Linux?", "opciones": ["A. Propietario", "B. Freeware cerrado", "C. Software libre", "D. Shareware"], "respuesta_correcta": "C"},
                {"pregunta": "¿Cuál es la unidad mínima de información en informática?", "opciones": ["A. Byte", "B. Bit", "C. Nibble", "D. Word"], "respuesta_correcta": "B"},
            ],
        },
        "redes": {
            "nombre": "Redes y Comunicaciones",
            "preguntas": [
                {"pregunta": "¿Qué significa DNS?", "opciones": ["A. Domain Name System", "B. Data Network Service", "C. Digital Network System", "D. Dynamic Name Service"], "respuesta_correcta": "A"},
                {"pregunta": "¿En qué capa OSI trabaja un router?", "opciones": ["A. Capa 1", "B. Capa 2", "C. Capa 3", "D. Capa 4"], "respuesta_correcta": "C"},
                {"pregunta": "¿Qué protocolo transfiere archivos de forma segura?", "opciones": ["A. FTP", "B. SFTP", "C. HTTP", "D. SMTP"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué puerto usa HTTPS por defecto?", "opciones": ["A. 80", "B. 443", "C. 21", "D. 53"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué máscara corresponde a /24?", "opciones": ["A. 255.255.255.0", "B. 255.255.0.0", "C. 255.0.0.0", "D. 255.255.255.128"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué dispositivo conecta redes y toma decisiones de ruta?", "opciones": ["A. Hub", "B. Switch", "C. Router", "D. Repetidor"], "respuesta_correcta": "C"},
                {"pregunta": "¿Qué comando prueba conectividad ICMP?", "opciones": ["A. traceroute", "B. ping", "C. netstat", "D. nslookup"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué protocolo asigna IP automáticamente?", "opciones": ["A. DNS", "B. DHCP", "C. ARP", "D. FTP"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué capa OSI se ocupa del direccionamiento MAC?", "opciones": ["A. Física", "B. Enlace", "C. Red", "D. Aplicación"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué protocolo traduce IP a MAC en IPv4?", "opciones": ["A. ICMP", "B. ARP", "C. BGP", "D. RIP"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué comando muestra interfaces de red en Linux moderno?", "opciones": ["A. ip a", "B. iftop", "C. route", "D. host"], "respuesta_correcta": "A"},
                {"pregunta": "¿Cuál es un rango típico de IP privada clase C?", "opciones": ["A. 8.8.8.0/24", "B. 192.168.0.0/16", "C. 172.0.0.0/8", "D. 11.0.0.0/8"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué protocolo enruta entre sistemas autónomos en Internet?", "opciones": ["A. OSPF", "B. EIGRP", "C. BGP", "D. STP"], "respuesta_correcta": "C"},
                {"pregunta": "¿Qué significa VLAN?", "opciones": ["A. Virtual Local Area Network", "B. Variable Line Access Node", "C. Verified LAN", "D. Visual Link Address Network"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué comando consulta registros DNS?", "opciones": ["A. nslookup", "B. passwd", "C. digitar", "D. grep"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué tecnología evita bucles en switches L2?", "opciones": ["A. NAT", "B. STP", "C. ACL", "D. MPLS"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué valor de TTL reduce cada router en tránsito?", "opciones": ["A. 10", "B. 2", "C. 1", "D. 0"], "respuesta_correcta": "C"},
                {"pregunta": "¿Qué protocolo de aplicación usa puerto 25?", "opciones": ["A. SMTP", "B. IMAP", "C. POP3", "D. SNMP"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué comando muestra rutas en Linux?", "opciones": ["A. ip route", "B. ip scan", "C. route add", "D. net show"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué protocolo cifra el acceso remoto por terminal?", "opciones": ["A. Telnet", "B. FTP", "C. SSH", "D. TFTP"], "respuesta_correcta": "C"},
            ],
        },
        "seguridad": {
            "nombre": "Seguridad Informática",
            "preguntas": [
                {"pregunta": "¿Qué es un firewall?", "opciones": ["A. Un antivirus", "B. Un sistema de filtrado de tráfico", "C. Un programa de backup", "D. Un navegador web"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué significa HTTPS?", "opciones": ["A. HyperText Transfer Protocol Secure", "B. High Transfer Protocol System", "C. HyperText Transfer Protocol System", "D. High Text Protocol Secure"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué tipo de ataque intenta engañar al usuario para robar datos?", "opciones": ["A. DDoS", "B. Phishing", "C. Bruteforce", "D. Spoofing ARP"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué práctica mejora la seguridad de cuentas?", "opciones": ["A. Reutilizar contraseñas", "B. Usar 2FA", "C. Compartir credenciales", "D. Desactivar updates"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué algoritmo es de hash criptográfico?", "opciones": ["A. SHA-256", "B. AES", "C. RSA", "D. ECC"], "respuesta_correcta": "A"},
                {"pregunta": "¿Cuál es una buena política de contraseñas?", "opciones": ["A. Cortas y simples", "B. Largas y únicas", "C. Igual para todos los servicios", "D. Sin caracteres especiales"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué tipo de malware exige rescate para recuperar datos?", "opciones": ["A. Spyware", "B. Ransomware", "C. Adware", "D. Worm"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué objetivo tiene una copia de seguridad?", "opciones": ["A. Mejorar el ping", "B. Recuperar datos ante incidentes", "C. Aumentar RAM", "D. Evitar cifrado TLS"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué comando en Linux cambia permisos de archivo?", "opciones": ["A. chown", "B. chmod", "C. passwd", "D. umask"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué significa CVE en ciberseguridad?", "opciones": ["A. Common Vulnerabilities and Exposures", "B. Central Virus Evaluation", "C. Certified Virtual Encryption", "D. Critical Verification Engine"], "respuesta_correcta": "A"},
                {"pregunta": "¿Cuál es un principio de seguridad básico?", "opciones": ["A. Mínimo privilegio", "B. Máximo acceso", "C. Credenciales compartidas", "D. Sin registros"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué técnica compara un hash para verificar integridad?", "opciones": ["A. Backup incremental", "B. Checksum", "C. Segmentación VLAN", "D. NAT dinámico"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué herramienta ayuda a detectar puertos abiertos?", "opciones": ["A. nmap", "B. nano", "C. top", "D. unzip"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué significa 2FA?", "opciones": ["A. Two-Factor Authentication", "B. Two File Access", "C. Trusted Firewall Access", "D. Transfer Function Authorization"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué es una VPN?", "opciones": ["A. Virtual Private Network", "B. Verified Public Node", "C. Virtual Protocol Number", "D. Variable Protected Network"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué tipo de cifrado usa la misma clave para cifrar y descifrar?", "opciones": ["A. Asimétrico", "B. Simétrico", "C. Híbrido", "D. Cuántico"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué herramienta se usa para analizar logs del sistema en Linux?", "opciones": ["A. journalctl", "B. lsblk", "C. free", "D. uname"], "respuesta_correcta": "A"},
                {"pregunta": "¿Qué medida reduce superficie de ataque en servidores?", "opciones": ["A. Instalar servicios innecesarios", "B. Hardening", "C. Abrir todos los puertos", "D. Desactivar parches"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué tipo de ataque prueba muchas contraseñas automáticamente?", "opciones": ["A. SQL Injection", "B. Fuerza bruta", "C. XSS", "D. CSRF"], "respuesta_correcta": "B"},
                {"pregunta": "¿Qué cabecera ayuda a prevenir ataques de clickjacking?", "opciones": ["A. X-Frame-Options", "B. Content-Length", "C. User-Agent", "D. Referer"], "respuesta_correcta": "A"},
            ],
        },
    }


def cargar_ranking() -> list[dict[str, Any]]:
    if not RANKING_FILE.exists():
        return []
    try:
        with RANKING_FILE.open("r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def guardar_ranking(ranking: list[dict[str, Any]]) -> bool:
    try:
        with RANKING_FILE.open("w", encoding="utf-8") as archivo:
            json.dump(ranking, archivo, indent=2, ensure_ascii=False)
        return True
    except OSError:
        return False


def pedir_entero(mensaje: str, minimo: int, maximo: int) -> int:
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo <= valor <= maximo:
                return valor
            print(f"Introduce un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")


def pedir_respuesta() -> str:
    while True:
        respuesta = input("Selecciona una opción (A, B, C, D): ").strip().upper()
        if respuesta in VALID_OPTIONS:
            return respuesta
        print("Opción no válida. Debe ser A, B, C o D.")


def pedir_respuesta_con_tiempo(segundos: int) -> str | None:
    if segundos <= 0:
        return pedir_respuesta()

    if os.name == "nt":
        return pedir_respuesta_con_tiempo_windows(segundos)
    return pedir_respuesta_con_tiempo_unix(segundos)


def pedir_respuesta_con_tiempo_windows(segundos: int) -> str | None:
    import msvcrt

    tiempo_limite = time.monotonic() + segundos
    buffer: list[str] = []

    while True:
        restantes = int(tiempo_limite - time.monotonic() + 0.999)
        if restantes <= 0:
            print("\n⏰ Tiempo agotado.")
            return None

        prompt = f"\rSelecciona una opción (A, B, C, D) [{restantes}s]: {''.join(buffer)}"
        print(prompt, end="", flush=True)

        if msvcrt.kbhit():
            tecla = msvcrt.getwch()

            if tecla in ("\r", "\n"):
                print()
                respuesta = "".join(buffer).strip().upper()
                if respuesta in VALID_OPTIONS:
                    return respuesta
                print("Opción no válida. Debe ser A, B, C o D.")
                buffer = []
                continue

            if tecla == "\x08":
                if buffer:
                    buffer.pop()
                continue

            if tecla.isprintable():
                if len(buffer) < 4:
                    buffer.append(tecla)
                continue

        time.sleep(0.05)


def pedir_respuesta_con_tiempo_unix(segundos: int) -> str | None:
    tiempo_limite = time.monotonic() + segundos
    while True:
        restantes = int(tiempo_limite - time.monotonic() + 0.999)
        if restantes <= 0:
            print("\n⏰ Tiempo agotado.")
            return None

        print(f"Selecciona una opción (A, B, C, D) [{restantes}s]: ", end="", flush=True)
        listo, _, _ = select.select([sys.stdin], [], [], restantes)
        if not listo:
            print("\n⏰ Tiempo agotado.")
            return None

        respuesta = sys.stdin.readline().strip().upper()
        if respuesta in VALID_OPTIONS:
            return respuesta
        print("Opción no válida. Debe ser A, B, C o D.")


def seleccionar_temporizador() -> int | None:
    print("\nTemporizador por pregunta:")
    print("1. Sin temporizador")
    print("2. Activar temporizador")
    opcion = pedir_entero("Elige una opción (1-2): ", 1, 2)
    if opcion == 1:
        return None
    return pedir_entero("Segundos por pregunta (5-300): ", 5, 300)


def seleccionar_modo_inicio() -> str:
    print("\nModo de juego:")
    print("1. Modo personalizado")
    print("2. Modo examen oficial (20 preguntas + 20s por pregunta)")
    opcion = pedir_entero("Elige una opción (1-2): ", 1, 2)
    return "oficial" if opcion == 2 else "personalizado"


def obtener_valoracion(porcentaje: float) -> str:
    if porcentaje >= 90:
        return "EXCELENTE - Eres un experto"
    if porcentaje >= 75:
        return "MUY BIEN - Gran conocimiento"
    if porcentaje >= 60:
        return "BIEN - Buen trabajo"
    if porcentaje >= 50:
        return "REGULAR - Puedes mejorar"
    return "INSUFICIENTE - Necesitas estudiar más"


def seleccionar_preguntas(preguntas_por_tema: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], str]:
    temas = list(preguntas_por_tema.keys())
    print("\nSelecciona un tema:")
    for i, clave in enumerate(temas, start=1):
        nombre = preguntas_por_tema[clave]["nombre"]
        total = len(preguntas_por_tema[clave]["preguntas"])
        print(f"{i}. {nombre} ({total} preguntas)")
    print(f"{len(temas) + 1}. Modo mixto (todas las preguntas)")

    opcion = pedir_entero(f"\nElige una opción (1-{len(temas) + 1}): ", 1, len(temas) + 1)

    if opcion == len(temas) + 1:
        combinadas: list[dict[str, Any]] = []
        for tema in preguntas_por_tema.values():
            combinadas.extend(tema["preguntas"])
        random.shuffle(combinadas)
        return combinadas, "Modo mixto"

    clave_tema = temas[opcion - 1]
    seleccion = preguntas_por_tema[clave_tema]["preguntas"][:]
    random.shuffle(seleccion)
    return seleccion, preguntas_por_tema[clave_tema]["nombre"]


def aleatorizar_opciones_preguntas(preguntas: list[dict[str, Any]]) -> list[dict[str, Any]]:
    preguntas_aleatorias: list[dict[str, Any]] = []

    for pregunta in preguntas:
        letra_correcta_original = pregunta["respuesta_correcta"]
        opcion_correcta_original = next(
            (op for op in pregunta["opciones"] if op.startswith(f"{letra_correcta_original}.")),
            None,
        )

        if opcion_correcta_original is None:
            preguntas_aleatorias.append(pregunta)
            continue

        textos_opciones = [op.split(". ", 1)[1] if ". " in op else op for op in pregunta["opciones"]]
        texto_correcto = opcion_correcta_original.split(". ", 1)[1] if ". " in opcion_correcta_original else opcion_correcta_original

        random.shuffle(textos_opciones)
        opciones_reetiquetadas = [f"{letra}. {texto}" for letra, texto in zip(OPTION_LETTERS, textos_opciones)]
        nueva_letra_correcta = OPTION_LETTERS[textos_opciones.index(texto_correcto)]

        preguntas_aleatorias.append(
            {
                "pregunta": pregunta["pregunta"],
                "opciones": opciones_reetiquetadas,
                "respuesta_correcta": nueva_letra_correcta,
            }
        )

    return preguntas_aleatorias


def seleccionar_modo_examen(preguntas: list[dict[str, Any]], tema: str) -> tuple[list[dict[str, Any]], str]:
    total_disponibles = len(preguntas)
    opciones_cantidad = [10, 20]
    opciones_validas = [cantidad for cantidad in opciones_cantidad if cantidad <= total_disponibles]

    print("\nSelecciona modalidad:")
    print(f"1. Examen completo ({total_disponibles} preguntas)")
    for indice, cantidad in enumerate(opciones_validas, start=2):
        print(f"{indice}. Examen corto ({cantidad} preguntas)")
    opcion_personalizada = 2 + len(opciones_validas)
    print(f"{opcion_personalizada}. Examen personalizado (elige cantidad)")

    opcion_maxima = opcion_personalizada
    opcion = pedir_entero(f"\nElige una opción (1-{opcion_maxima}): ", 1, opcion_maxima)

    if opcion == 1:
        return preguntas, tema

    if opcion == opcion_personalizada:
        cantidad = pedir_entero(
            f"¿Cuántas preguntas quieres responder? (1-{total_disponibles}): ",
            1,
            total_disponibles,
        )
        if cantidad == total_disponibles:
            return preguntas, tema
        return preguntas[:cantidad], f"{tema} - Examen personalizado ({cantidad})"

    cantidad_elegida = opciones_validas[opcion - 2]
    return preguntas[:cantidad_elegida], f"{tema} - Examen corto ({cantidad_elegida})"


def mostrar_pregunta(pregunta: dict[str, Any], indice: int, total: int) -> None:
    print("\n" + "=" * 60)
    print(f"PREGUNTA {indice}/{total}")
    print("=" * 60)
    print(pregunta["pregunta"])
    print()
    for opcion in pregunta["opciones"]:
        print(opcion)


def texto_respuesta_correcta(pregunta: dict[str, Any]) -> str:
    letra = pregunta["respuesta_correcta"]
    for opcion in pregunta["opciones"]:
        if opcion.startswith(f"{letra}."):
            return opcion
    return letra


def calcular_distribucion_respuestas_correctas(preguntas: list[dict[str, Any]]) -> dict[str, int]:
    distribucion = {letra: 0 for letra in OPTION_LETTERS}
    for pregunta in preguntas:
        letra = pregunta.get("respuesta_correcta")
        if letra in distribucion:
            distribucion[letra] += 1
    return distribucion


def mostrar_resultados(aciertos: int, total: int, tema: str, distribucion_correctas: dict[str, int]) -> float:
    porcentaje = (aciertos / total) * 100 if total else 0.0
    fallos = total - aciertos
    valoracion = obtener_valoracion(porcentaje)

    print("\n" + "=" * 60)
    print("RESULTADOS DEL CUESTIONARIO")
    print("=" * 60)
    print(f"Tema: {tema}")
    print(f"Preguntas totales: {total}")
    print(f"Respuestas correctas: {aciertos}")
    print(f"Respuestas incorrectas: {fallos}")
    print(f"Porcentaje de aciertos: {porcentaje:.1f}%")
    print(f"Valoración: {valoracion}")
    print("Distribución de respuestas correctas:")
    for letra in OPTION_LETTERS:
        cantidad = distribucion_correctas.get(letra, 0)
        porcentaje_letra = (cantidad / total * 100) if total else 0.0
        print(f"  {letra}: {cantidad} ({porcentaje_letra:.1f}%)")
    print("=" * 60)
    return porcentaje


def agregar_al_ranking(
    ranking: list[dict[str, Any]],
    nombre: str,
    tema: str,
    aciertos: int,
    total: int,
    porcentaje: float,
) -> list[dict[str, Any]]:
    ranking.append(
        {
            "nombre": nombre,
            "tema": tema,
            "aciertos": aciertos,
            "total": total,
            "porcentaje": porcentaje,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
    )
    ranking.sort(key=lambda item: item["porcentaje"], reverse=True)
    return ranking


def mostrar_ranking(ranking: list[dict[str, Any]]) -> None:
    if not ranking:
        print("\nEl ranking está vacío. ¡Sé el primero en participar!")
        return

    print("\n" + "=" * 78)
    print("RANKING TOP 10")
    print("=" * 78)
    print(f"{'#':<4}{'Nombre':<20}{'Tema':<25}{'Aciertos':<12}{'%':<8}{'Fecha'}")
    print("-" * 78)
    for i, resultado in enumerate(ranking[:10], start=1):
        aciertos = f"{resultado['aciertos']}/{resultado['total']}"
        print(
            f"{i:<4}{resultado['nombre'][:19]:<20}{resultado['tema'][:24]:<25}"
            f"{aciertos:<12}{resultado['porcentaje']:.1f}%  {resultado['fecha']}"
        )
    print("=" * 78)


def ejecutar_cuestionario(ranking: list[dict[str, Any]]) -> list[dict[str, Any]]:
    preguntas_por_tema = cargar_preguntas()
    preguntas_base, tema_base = seleccionar_preguntas(preguntas_por_tema)
    preguntas_base = aleatorizar_opciones_preguntas(preguntas_base)

    if seleccionar_modo_inicio() == "oficial":
        cantidad = min(20, len(preguntas_base))
        preguntas = preguntas_base[:cantidad]
        tema = f"{tema_base} - Examen oficial ({cantidad})"
        temporizador = 20
    else:
        preguntas, tema = seleccionar_modo_examen(preguntas_base, tema_base)
        temporizador = seleccionar_temporizador()

    nombre = input("\nIntroduce tu nombre: ").strip() or "Anónimo"
    print(f"\nHola {nombre}. Responderás {len(preguntas)} preguntas de: {tema}.")
    if temporizador is not None:
        print(f"Tiempo por pregunta: {temporizador} segundos.")
    input("Pulsa Enter para comenzar...")

    aciertos = 0
    total = len(preguntas)
    distribucion_correctas = calcular_distribucion_respuestas_correctas(preguntas)

    for indice, pregunta in enumerate(preguntas, start=1):
        mostrar_pregunta(pregunta, indice, total)
        if temporizador is None:
            respuesta = pedir_respuesta()
        else:
            respuesta = pedir_respuesta_con_tiempo(temporizador)

        if respuesta == pregunta["respuesta_correcta"]:
            print("✅ Correcto")
            aciertos += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta: {texto_respuesta_correcta(pregunta)}")

        if indice < total:
            input("Pulsa Enter para continuar...")

    porcentaje = mostrar_resultados(aciertos, total, tema, distribucion_correctas)
    ranking = agregar_al_ranking(ranking, nombre, tema, aciertos, total, porcentaje)
    if guardar_ranking(ranking):
        print("\nPuntuación guardada en el ranking.")
    else:
        print("\nNo se pudo guardar el ranking.")
    return ranking


def mostrar_menu() -> None:
    print("\n" + "=" * 50)
    print("CUESTIONARIO INTERACTIVO ASIR")
    print("=" * 50)
    print("1 - Empezar cuestionario")
    print("2 - Mostrar ranking")
    print("3 - Salir")
    print("=" * 50)


def main() -> None:
    ranking = cargar_ranking()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ").strip()
        if opcion == "1":
            ranking = ejecutar_cuestionario(ranking)
        elif opcion == "2":
            mostrar_ranking(ranking)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elige 1, 2 o 3.")


if __name__ == "__main__":
    main()

