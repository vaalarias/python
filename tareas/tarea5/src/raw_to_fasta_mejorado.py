'''
    NAME
        raw_to_fasta.py

    VERSION
        1.1

    AUTHOR
        Valentina Janet Arias Ojeda

    DESCRIPTION
        Convierte un archivo de .txt a un formato .faa

    CATEGORY
       Sequence    

    ARGUMENTS
        None    
'''
# Metemos todo en un bloque try

try:
    
    # Recibir del teclado el nombre a asignar del archivo .txt
    name_txt = input("Ingrese el nombre del archivo .txt: ")

    # Recibir de teclado el identificador para la secuencia (necesario en los archivos fasta)
    identifier = input("Ingrese el identificador de la secuencia contenida: ")

    # Recibir del teclado nombre del archivo fasta
    name_fasta = input("Ingrese el nombre para el archivo de salida (formato fastA): ")

    # Crear el archivo con extensión fasta
    fasta_file = open(f'../results/{name_fasta}.fasta', 'w')

    # Abrir archivo txt y almacenar secuencia
    txt_file = open(f"../data/{name_txt}")
    sequence = txt_file.read().rstrip('\n')

    # Transcribir secuencia en formato fasta creado
    fasta_file.write(f"> {identifier}\n{sequence}\n")

    fasta_file.close()
    txt_file.close()

    print(f'El archivo {fasta_file.name} se ha creado correctamente')

# Excepciones
    # Error de no encontrar el archivo en la ruta indicada
except FileNotFoundError:
    raise FileNotFoundError("No se encontró el archivo .txt en la ruta especificada.")

    #Error al no poder transcribir el contenido del archivo .txt
except IOError:
    raise IOError("Ocurrió un error al leer o escribir en los archivos.")
