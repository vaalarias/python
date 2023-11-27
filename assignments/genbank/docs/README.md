# Tarea 7. BioPython: GenBank
## Valentina Janet Arias Ojeda
###  Introducción


Este programa en Python utiliza la librería Biopython para analizar un archivo GenBank y obtener información sobre genes específicos, incluyendo la secuencia, el transcrito y la proteína asociada, si están disponibles.

## Descripción

El programa permite extraer información detallada sobre uno o más genes presentes en un archivo GenBank proporcionado. Puede imprimir la información del gen, su secuencia, el transcrito y la proteína correspondiente, si está disponible en el archivo.

## Requisitos

- Python 3.x instalado
- Librería Biopython (`pip install biopython`)

### Ejecución

```
python getGeneInfo.py [-h] [-f FILE] [-g GENES [GENES ...]]
```