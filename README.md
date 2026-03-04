# 🎯 Sistema de Cuestionarios Interactivo ASIR

Aplicación CLI en Python para practicar contenidos de ASIR con ranking persistente y feedback inmediato.

## ✨ Mejoras aplicadas

- Código refactorizado con funciones tipadas y estructura más mantenible.
- Manejo robusto de errores en carga/guardado de ranking.
- Validación de entrada más estricta y mensajes más claros.
- Preguntas mezcladas automáticamente en cada ejecución.
- Modalidad de examen configurable: completo, corto de 10, corto de 20 o personalizado (cantidad elegida, siempre aleatoria).
- Temporizador opcional por pregunta con tiempo configurable.
- Modo examen oficial de un clic: 20 preguntas con 20 segundos por pregunta.
- Salida de ranking más legible (Top 10).

## 📚 Banco de preguntas

El proyecto incluye ahora **60 preguntas** (se añadieron más de 50 nuevas):

- **Informática Básica**: 20
- **Redes y Comunicaciones**: 20
- **Seguridad Informática**: 20

También puedes usar **modo mixto** para combinar todas las preguntas.

## 🛠️ Requisitos

- Python 3.10+
- Sin dependencias externas

## 🚀 Ejecución

```bash
python Cuestionario.py
```

## 📁 Archivos

- `Cuestionario.py`: lógica completa del cuestionario
- `ranking.json`: ranking persistente (se crea automáticamente)

## 📊 Valoración de resultados

| Porcentaje | Valoración |
|------------|-----------|
| 90% - 100% | EXCELENTE - Eres un experto |
| 75% - 89%  | MUY BIEN - Gran conocimiento |
| 60% - 74%  | BIEN - Buen trabajo |
| 50% - 59%  | REGULAR - Puedes mejorar |
| 0% - 49%   | INSUFICIENTE - Necesitas estudiar más |

## 🧪 Nota

Si quieres ampliar todavía más el banco, solo hay que añadir entradas al diccionario de `cargar_preguntas()` respetando el formato actual.
