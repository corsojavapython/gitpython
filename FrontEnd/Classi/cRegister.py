#classi per la registrazione

import PySimpleGUI as sg
import requests
import json

class registrati:

    def registrazione(self,backend):

        layout = [

            [sg.Text('Nome: '), sg.Input(key='Nome'),sg.Text('Cognome: '),sg.Input(key='Cognome')],
            [sg.Text('Username: '), sg.Input(key='Username'),sg.Text('Password'), sg.Input(key='Password', password_char='*')],
            [sg.Text('Età: '),sg.Input(key = 'Eta'), sg.Text('Sesso: '),sg.Combo(values=['F','M'])],
            [sg.Button('Registrati'), sg.Button('Annulla')]
        ]

        w = sg.Window('Registrazione', layout)

        while True:

            ev, va = w.Read()

            if ev == sg.WIN_CLOSED or ev == 'Annulla':
                break

            elif ev == 'Registrati':

                #raccogliere i dati e chiamare l'API apposita

                dati = {}

                Nome = va['Nome']
                Cognome = va['Cognome']
                User = va['Username']
                Password = va['Password']
                Eta = int(va['Eta'])
                Sesso = va['Sesso']

                dati['nome'] = Nome
                dati['cognome'] = Cognome

                #Devo chiamare l'API giusta
                risposta = requests.put(f'http://{backend}/registrazione',json = dati)

                codice = risposta.status_code   
                payload = risposta.text

                datiRet = json.loads(payload)











