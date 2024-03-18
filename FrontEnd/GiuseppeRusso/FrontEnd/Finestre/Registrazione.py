import PySimpleGUI as sg
import requests


def registrazione():
    layout = [

        [sg.Text('Nome: '),sg.Input(key = 'Nome')],    
        [sg.Text('Cognome: '), sg.Input(key = 'Cognome')],
        [sg.Text('Username: '), sg.Input(key = 'Username')],
        [sg.Text('Password: '), sg.Input(key = 'Password')],
        [sg.Text('Età: '), sg.Input(key = 'Eta')],
        [sg.Text('Sesso: '), sg.Input(key = 'Sesso')],
        [sg.Text('Codice Fiscale: '), sg.Input(key = 'CodiceFiscale')],
        [sg.Text('Nazionalità: '), sg.Input(key = 'Nazionalita')],
        [sg.Text('Indirizzo: '), sg.Input(key = 'Indirizzo')],
        [sg.Button('Torna al login'),sg.Button('Annulla'), sg.Button('OK')]

    ]

    w4 = sg.Window('Registrazione', layout)

    while True:
        from Finestre.Login import login
        ev, va = w4.Read()

        if ev == 'Annulla' or ev == sg.WIN_CLOSED:
            break

        elif ev == 'Torna al login':
            
            w4.close()
            login()
            break

        elif ev == 'OK':
            nome = va['Nome']
            cognome = va['Cognome']
            username = va['Username']
            password = va['Password']
            eta = va['Eta']
            sesso = va['Sesso']
            codiceFiscale = va['CodiceFiscale']
            nazionalita = va['Nazionalita']
            indirizzo = va['Indirizzo']

            dati = {}
            dati['nome'] = nome
            dati['cognome'] = cognome
            dati['username'] = username
            dati['password'] = password
            dati['eta'] = eta
            dati['sesso'] = sesso
            dati['codiceFiscale'] = codiceFiscale
            dati['nazionalita'] = nazionalita
            dati['indirizzo'] = indirizzo

            risposta = requests.post('http://127.0.0.1/registrazione', json = dati)

            print(risposta.status_code)
            print(risposta.text)

            if risposta.status_code == 200:
                w4.close()
                print('Registrazione avvenuta con successo')
                login()
