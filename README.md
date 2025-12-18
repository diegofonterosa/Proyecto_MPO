# 🎯 Sistema de Cuestionarios Interactivo ASIR

Sistema de evaluación por línea de comandos (CLI) especializado en preguntas de Administración de Sistemas Informáticos en Red (ASIR). Incluye sistema de puntuación, ranking persistente y múltiples categorías temáticas.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 📋 Descripción

Aplicación interactiva de consola que permite a estudiantes de ASIR evaluar sus conocimientos en distintas áreas técnicas mediante cuestionarios de opción múltiple. El sistema registra y clasifica las puntuaciones en un ranking persistente almacenado en formato JSON.

## ✨ Características

- 📚 **Múltiples categorías temáticas**: Informática Básica, Redes y Comunicaciones, Seguridad Informática
- 🎲 **Modo mixto**: Posibilidad de responder todas las preguntas aleatoriamente
- 💾 **Persistencia de datos**: Ranking guardado en archivo JSON
- 📊 **Sistema de puntuación**: Cálculo de porcentajes y valoración cualitativa
- 🏆 **Ranking top 10**: Clasificación de mejores puntuaciones con fecha y hora
- ✅ **Validación de respuestas**: Feedback inmediato con respuesta correcta en caso de error
- 👤 **Registro de usuarios**: Identificación personalizada de participantes
- 🎨 **Interfaz CLI clara**: Menús estructurados y navegación intuitiva

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **JSON** - Almacenamiento de datos
- **datetime** - Registro temporal de resultados
- **os** - Gestión de archivos del sistema

## 📦 Requisitos

- Python 3.6 o superior
- No requiere librerías externas

## 🚀 Instalación y uso

### Clonar el repositorio
```bash
git clone https://github.com/diegofonterosa/Proyecto_MPO.git
cd Proyecto_MPO
```

### Ejecutar el programa
```bash
python Cuestionario.py
```

## 💻 Funcionalidades del menú

### 1. Empezar cuestionario
- Selección de tema específico o modo mixto
- Introducción del nombre del participante
- Responder preguntas de opción múltiple (A, B, C, D)
- Feedback inmediato tras cada respuesta
- Resultados finales con porcentaje y valoración

### 2. Mostrar ranking
- Visualización del top 10 de mejores puntuaciones
- Información detallada: nombre, tema, aciertos, porcentaje, fecha

### 3. Salir
- Cierre del programa

## 📊 Sistema de valoración

| Porcentaje | Valoración |
|------------|-----------|
| 90% - 100% | EXCELENTE - Eres un experto |
| 75% - 89%  | MUY BIEN - Gran conocimiento |
| 60% - 74%  | BIEN - Buen trabajo |
| 50% - 59%  | REGULAR - Puedes mejorar |
| 0% - 49%   | INSUFICIENTE - Necesitas estudiar más |

## 📸 Ejemplo de uso
```
¡BIENVENIDO AL CUESTIONARIO DE ASIR!

Seleccione un tema:
1. Informática Básica
2. Redes y Comunicaciones
3. Seguridad Informática
4. Todas las preguntas (modo mixto)

Elige una opción (1-4): 1

Introduce tu nombre: Diego

Hola Diego! Vas a responder 4 preguntas sobre: Informática Básica
Presiona Enter cuando estés listo...

==================================================
PREGUNTA 1 de 4
==================================================
¿Qué significa RAM?

A. Random Access Memory
B. Read Access Memory
C. Real Access Memory
D. Rapid Access Memory

Selecciona una opción (A, B, C, D): A
✓ ¡CORRECTO!
```

## 📁 Estructura de archivos
```
Proyecto_MPO/
│
├── Cuestionario.py      # Código principal del programa
├── ranking.json         # Ranking de puntuaciones (se crea automáticamente)
└── README.md           # Este archivo
```

## 🎯 Temas y preguntas incluidas

### Informática Básica (4 preguntas)
- Conceptos de hardware (RAM)
- Sistemas operativos
- Protocolos de red (HTTP)
- Direccionamiento IP (loopback)

### Redes y Comunicaciones (3 preguntas)
- DNS (Domain Name System)
- Modelo OSI y routers
- Protocolos de transferencia segura (SFTP)

### Seguridad Informática (2 preguntas)
- Firewalls
- HTTPS y seguridad en la web

## 🔧 Posibles mejoras futuras

- [ ] Añadir más preguntas y categorías
- [ ] Implementar dificultad progresiva
- [ ] Exportar resultados a PDF
- [ ] Interfaz gráfica (GUI) con Tkinter
- [ ] Base de datos SQLite en lugar de JSON
- [ ] Temporizador para cada pregunta
- [ ] Estadísticas detalladas por usuario

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 👤 Autor

**Diego Pérez Fonterosa**
- GitHub: [@diegofonterosa](https://github.com/diegofonterosa)
- LinkedIn: [Diego Pérez Fonterosa](https://linkedin.com/in/diegoperezfonterosa)

## 📞 Contacto

Para preguntas o sugerencias, puedes contactarme en:
- Email: diegofonterosa@gmail.com
- LinkedIn: https://linkedin.com/in/diegoperezfonterosa

---

⭐ Si te ha gustado este proyecto, ¡dale una estrella en GitHub!
```

python
cli
quiz-app
asir
interactive-quiz
education
ranking-system
json-database
terminal-app
learning-tool
