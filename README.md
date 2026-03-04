# ASIR Interactive Quiz System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Estado](https://img.shields.io/badge/Estado-Activo-blue?style=flat-square)]()
[![Interfaz](https://img.shields.io/badge/Interfaz-CLI-4CAF50?style=flat-square)]()

Aplicación de evaluación técnica en consola para contenidos de ASIR. El proyecto incluye banco de preguntas por categorías, modos de examen, temporizador opcional, ranking persistente y métricas de distribución de respuestas.

## Resumen

- Banco de preguntas organizado por categorías técnicas.
- Modos de examen: completo, corto (10/20), personalizado y oficial.
- Temporizador configurable por pregunta.
- Aleatorización de preguntas y opciones de respuesta.
- Ranking Top 10 persistente en JSON.
- Informe final de resultados con distribución A/B/C/D.

## Estructura del proyecto

```text
ASIR-Interactive-Quiz-System/
├── Cuestionario.py
├── ranking.json
└── README.md
```

## Banco de preguntas

| Categoría | Nº preguntas |
|---|---:|
| Informática Básica | 20 |
| Redes y Comunicaciones | 20 |
| Seguridad Informática | 20 |

Total: **60 preguntas**.

## Modos de ejecución

| Modo | Descripción |
|---|---|
| Personalizado | Cantidad de preguntas y temporizador definidos por el usuario |
| Oficial | 20 preguntas con 20 segundos por pregunta |
| Por tema | Selección de una categoría concreta |
| Mixto | Combinación de preguntas de todas las categorías |

## Requisitos

- Python 3.10 o superior
- Sin dependencias externas

## Ejecución

```bash
git clone https://github.com/diegofonterosa/ASIR-Interactive-Quiz-System.git
cd ASIR-Interactive-Quiz-System
python Cuestionario.py
```

## Escala de valoración

| Porcentaje | Resultado |
|---|---|
| 90% - 100% | EXCELENTE |
| 75% - 89% | MUY BIEN |
| 60% - 74% | BIEN |
| 50% - 59% | REGULAR |
| 0% - 49% | INSUFICIENTE |

## Autor

**Diego Pérez Fonterosa**

[![GitHub](https://img.shields.io/badge/GitHub-diegofonterosa-181717?style=flat-square&logo=github)](https://github.com/diegofonterosa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diego%20Pérez-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/diegoperezfonterosa)

## Licencia

© Diego Pérez Fonterosa. Todos los derechos reservados.
