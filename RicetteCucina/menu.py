import PySimpleGUI as sg
import os
import json

listaRicette = {}
#leggo il file .csv
dati = ''
nomefile = os.path.abspath('RicetteCucina\\ricette.csv')
with open(nomefile, 'r',encoding = 'utf-8') as fr:
    dati = fr.read()

ricette = dati.split('\n')
#[ogni ricetta ha:] nome, ingredienti, gradimento, proteine, carboidrati, lipidi

for ricetta in ricette:

    ingredienti = ricetta.split(';')
    nome = ingredienti[0]
    componenti = ingredienti[1]
    gradimento = ingredienti[2]
    proteine = ingredienti[3]
    carboidrati = ingredienti[4]
    lipidi = ingredienti[5]

    ric = {}
    ric['Nome'] = nome
    ric['ingedienti'] = componenti
    ric['gradimento'] = gradimento
    ric['proteine'] = proteine
    ric['carboidrati'] = carboidrati
    ric['lipidi'] = lipidi

    listaRicette[nome] = ric.copy()

    #listaRicette.append(ric.copy())

print(listaRicette)
#salvo il dizionario
datiJ = json.dumps(listaRicette)
with open(nomefile+'.json','w') as fw:
    fw.write(datiJ)

#Preparare l'applicazione:

#recupero la lista
lista= []

for k,v in listaRicette.items():
    lista.append(k)

layout = [

    [sg.Listbox(lista,size=(50, 10))],
    [sg.Button('OK')]

]

finestra = sg.Window('Elenco piatti',layout)

while True:

    ev, va = finestra.read()

    if ev == 'OK':
        break

