# ASIR Interactive Quiz System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-blue?style=flat-square)]()
[![Interface](https://img.shields.io/badge/Interface-CLI-4CAF50?style=flat-square)]()

Default language: Spanish (ES). English version is available below.
Idioma por defecto: español (ES). La versión en inglés está más abajo.

**ES:** Plataforma CLI de cuestionarios técnicos para contenidos ASIR. Incluye banco de preguntas por categorías, modos de examen, temporizador opcional, ranking persistente y métricas de distribución de respuestas.  
**EN:** Command-line technical quiz platform for ASIR learning domains. Includes categorized question banks, exam modes, optional timer, persistent ranking, and answer distribution metrics.

## Índice / Table of Contents

- [Versión en Español](#versión-en-español)
- [English Version](#english-version)

---

## Versión en Español

### Resumen

- Banco de preguntas por categorías técnicas.
- Modos de examen: completo, corto (10/20), personalizado y oficial.
- Temporizador configurable por pregunta.
- Aleatorización de preguntas y opciones de respuesta.
- Ranking Top 10 persistente en JSON.
- Informe final con distribución A/B/C/D.

### Estructura del proyecto

```text
ASIR-Interactive-Quiz-System/
├── Cuestionario.py
├── ranking.json
└── README.md
```

### Banco de preguntas

| Categoría | Preguntas |
|---|---:|
| Informática Básica | 20 |
| Redes y Comunicaciones | 20 |
| Seguridad Informática | 20 |

Total: **60 preguntas**.

### Modos de examen

| Modo | Descripción |
|---|---|
| Personalizado | Cantidad de preguntas y temporizador definidos por el usuario |
| Oficial | 20 preguntas con 20 segundos por pregunta |
| Por tema | Selección de una categoría concreta |
| Mixto | Combinación de preguntas de todas las categorías |

### Requisitos

- Python 3.10+
- Sin dependencias externas

### Ejecución

```bash
git clone https://github.com/diegofonterosa/ASIR-Interactive-Quiz-System.git
cd ASIR-Interactive-Quiz-System
python Cuestionario.py
```

### Escala de valoración

| Porcentaje | Resultado |
|---|---|
| 90% - 100% | EXCELENTE |
| 75% - 89% | MUY BIEN |
| 60% - 74% | BIEN |
| 50% - 59% | REGULAR |
| 0% - 49% | INSUFICIENTE |

---

## English Version

### Overview

- Question bank organized by technical domains.
- Multiple exam modes: full, short (10/20), custom, and official.
- Optional per-question timer.
- Randomized question order and answer options.
- Persistent Top 10 ranking stored in JSON.
- Final report with A/B/C/D correct-answer distribution.

### Project Structure

```text
ASIR-Interactive-Quiz-System/
├── Cuestionario.py
├── ranking.json
└── README.md
```

### Question Bank

| Category | Questions |
|---|---:|
| Basic IT | 20 |
| Networking & Communications | 20 |
| Cybersecurity | 20 |

Total: **60 questions**.

### Exam Modes

| Mode | Description |
|---|---|
| Custom | User-defined number of questions and timer |
| Official | 20 questions with 20 seconds per question |
| By topic | Single category selection |
| Mixed | Combined questions from all categories |

### Requirements

- Python 3.10+
- No external dependencies

### Run

```bash
git clone https://github.com/diegofonterosa/ASIR-Interactive-Quiz-System.git
cd ASIR-Interactive-Quiz-System
python Cuestionario.py
```

### Scoring Scale

| Percentage | Rating |
|---|---|
| 90% - 100% | EXCELLENT |
| 75% - 89% | VERY GOOD |
| 60% - 74% | GOOD |
| 50% - 59% | FAIR |
| 0% - 49% | INSUFFICIENT |

### Author

**Diego Pérez Fonterosa**

[![GitHub](https://img.shields.io/badge/GitHub-diegofonterosa-181717?style=flat-square&logo=github)](https://github.com/diegofonterosa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diego%20Pérez-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/diegoperezfonterosa)

### License

© Diego Pérez Fonterosa. All rights reserved.
