list = ['ab56','bh84','hv76', 'ay93', 'ap97', 'bd72']
myfile = open("../results/one.txt","w")
myfile2 = open("../results/two.txt","w")
# Si la cadena empieza con a escribir el contenido en un archivo
for cont in list:
    if cont.startswith('a'):
        myfile.write(cont + "\n")
# Todo lo demás se va a otro archivo
    else:
        myfile2.write(cont + "\n")
print("Done")