filedaleggere = 'classe.csv'

with open(filedaleggere,'r', encoding='utf-8') as fr:

    contenuto = fr.read()

cont =  contenuto

#print (cont)

righe = cont.split('\n')
#print(righe)

rownum = 0
colonne = []
dizdati = {}
listdati = []


for record in righe:

    if rownum == 0:
        colonne = record.split(';')

    else:
        #sono su una riga dati
        dati = record.split(';')

        for ncol in range(len(colonne)):

            #print(f'{colonne[ncol]} = {dati[ncol]}')

            dizdati[colonne[ncol]] = dati[ncol]

        listdati.append(dizdati.copy())

    rownum +=1

#cerchiamo qalcosa per le chiavi 
import uuid

dizdidiz = {}

for elemento in listdati:

    chiave = str(uuid.uuid4())
    dizdidiz[chiave] = elemento


#print(dizdidiz)

chiaviattive = dizdidiz.keys()

for k in chiaviattive:
    print(k,' -> ', dizdidiz[k])
    print('==============================================')


print('Ora stampo equivalente json del dizionario')

import json

miojson = json.dumps(dizdidiz)

fileJson = 'classe.json'

with open(fileJson, 'w', encoding = 'utf-8') as fw:
    fw.write(miojson)

with open (fileJson, 'r', encoding= 'utf-8') as fr:
    buffer = fr.read()

nuovodizionario = json.loads(buffer)

print('Nuovo dizionario latto da file')
print(nuovodizionario) 

