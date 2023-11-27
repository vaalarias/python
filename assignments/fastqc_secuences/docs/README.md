# Tarea 6. BioPython: Manejo de secuencias
## Valentina Janet Arias Ojeda
###  Introducción

Este programa en Python permite analizar un archivo FASTQ y contar el número de secuencias cuyo promedio de calidad está por encima o por debajo de un umbral especificado.

## Requisitos

- Python 3.x instalado
- Librería Biopython (`pip install biopython`)

### Ejecución

```
python filtro_calidad.py <archivo.fastq> <umbral> [debajo]
```

## Detalles del Programa
- Lee un archivo FASTQ proporcionado como argumento.
- Calcula el promedio de calidad de cada lectura.
- Cuenta el número de secuencias por encima o por debajo del umbral especificado.
- Utiliza la librería Biopython para parsear el archivo FASTQ y realizar los cálculos necesarios.