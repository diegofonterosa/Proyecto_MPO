# ASIR Interactive Quiz System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-blue?style=flat-square)]()
[![Interface](https://img.shields.io/badge/Interface-CLI-4CAF50?style=flat-square)]()

A command-line technical quiz platform focused on ASIR learning domains. The project includes categorized question banks, multiple exam modes, optional timers, persistent ranking, and answer distribution metrics.

## Overview

- Question bank organized by technical domains.
- Multiple exam modes: full, short (10/20), custom, and official.
- Optional per-question timer.
- Randomized question order and answer options.
- Persistent Top 10 ranking stored in JSON.
- Final report with A/B/C/D correct-answer distribution.

## Project Structure

```text
ASIR-Interactive-Quiz-System/
├── Cuestionario.py
├── ranking.json
└── README.md
```

## Question Bank

| Category | Questions |
|---|---:|
| Basic IT | 20 |
| Networking & Communications | 20 |
| Cybersecurity | 20 |

Total: **60 questions**.

## Exam Modes

| Mode | Description |
|---|---|
| Custom | User-defined number of questions and timer |
| Official | 20 questions with 20 seconds per question |
| By topic | Single category selection |
| Mixed | Combined questions from all categories |

## Requirements

- Python 3.10+
- No external dependencies

## Run

```bash
git clone https://github.com/diegofonterosa/ASIR-Interactive-Quiz-System.git
cd ASIR-Interactive-Quiz-System
python Cuestionario.py
```

## Scoring Scale

| Percentage | Rating |
|---|---|
| 90% - 100% | EXCELLENT |
| 75% - 89% | VERY GOOD |
| 60% - 74% | GOOD |
| 50% - 59% | FAIR |
| 0% - 49% | INSUFFICIENT |

## Author

**Diego Pérez Fonterosa**

[![GitHub](https://img.shields.io/badge/GitHub-diegofonterosa-181717?style=flat-square&logo=github)](https://github.com/diegofonterosa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diego%20Pérez-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/diegoperezfonterosa)

## License

© Diego Pérez Fonterosa. All rights reserved.
