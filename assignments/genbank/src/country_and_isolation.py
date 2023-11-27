from Bio import SeqIO
for gb_virus in SeqIO.parse("virus.gb","genbank"):

    print('ID',gb_virus.id)
    if 'date' in gb_virus.annotations:
        print('Date:', gb_virus.annotations['date'])
    if 'organism' in gb_virus.annotations:
        print('Organism:', gb_virus.annotations['organism'])
    if 'country' in gb_virus.features[0].qualifiers:
        print('Country:',gb_virus.features[0].qualifiers['country'])
    if 'isolation_source' in gb_virus.features[0].qualifiers:
        print('Isolation source:',gb_virus.features[0].qualifiers['isolation_source'])from Bio import SeqIO
for gb_virus in SeqIO.parse("virus.gb","genbank"):

    print('ID',gb_virus.id)
    if 'date' in gb_virus.annotations:
        print('Date:', gb_virus.annotations['date'])
    if 'organism' in gb_virus.annotations:
        print('Organism:', gb_virus.annotations['organism'])
    if 'country' in gb_virus.features[0].qualifiers:
        print('Country:',gb_virus.features[0].qualifiers['country'])
    if 'isolation_source' in gb_virus.features[0].qualifiers:
        print('Isolation source:',gb_virus.features[0].qualifiers['isolation_source'])