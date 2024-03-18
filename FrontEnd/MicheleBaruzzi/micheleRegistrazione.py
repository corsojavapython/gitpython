import PySimpleGUI as sg
from flask import jsonify
from datetime import datetime



def custom_input(size):
    return sg.Input(key="dob", size=size, pad=(0, 0), tooltip="Formato: gg/mm/aaaa")

frame1 = [
    [sg.Text('Username',size=(8,2)), sg.Input(key="utente")],
    [sg.Text('Password',size=(8,2)), sg.Input(key="password", password_char='*')],
] 
frame2 = [
    [sg.Text('Nome',size=(8,2)), sg.Input(key="nome")],
    [sg.Text('Cognome',size=(8,2)), sg.Input(key="cognome")],
]    
frame3 = [    
    [sg.Text('Data di nascita',size=(8,3)), custom_input(size=(10,1))],
    [sg.Text('Sesso',size=(8,2)), sg.Radio('Maschio', "RADIO1", key="sesso", default=True), sg.Radio('Femmina', "RADIO1")],
    [sg.Text('Codice fiscale',size=(8,2)), sg.Input(key="cfisc", size=(16, 1))],
    [sg.Text('Nazionalità',size=(8,2)), sg.Input(key="naz", size=(3, 1))],
    [sg.Text('Indirizzo',size=(8,2)), sg.Input(key="ind")]
    
]

#creo il layout
layout = [
    [sg.Frame('Accesso', frame1)],
    [sg.Frame('Dati personali', frame2)],
    [sg.Frame('Ulteriori informazioni', frame3)],
    [sg.Button('Annulla',size=(8,1)), sg.Button('Registrati')]
]       
  
       
window = sg.Window('registrazione', layout)



while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Annulla':
        break
    elif event == 'Registrati':
        # estrae i dati dal dizionario
        nome = values['nome']
        cognome = values['cognome']
        username = values['utente']
        password = values['password']
        dob_input = values['dob']
        sesso = 'M' if values['sesso'] else 'F'  # Seleziona il valore corrispondente al radio button
        codice_fiscale = values['cfisc'].upper()[:16]  # Converte in maiuscolo e tronca a 16 caratteri
        nazionalita = values['naz'].upper()[:3]
        indirizzo = values['ind']

        # Verifica se è stata inserita una data di nascita
        if dob_input:
            # converte la data di nascita in anni
            dob_date = datetime.strptime(dob_input, "%d/%m/%Y")

            # calcola gli anni in base alla data di nascita
            today = datetime.today()
            eta = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        else:
            eta = None  # Se non è stata inserita una data di nascita, eta viene impostato su None

        # stampa i dati utente
        print(f'sto Registrando utente: {nome}, {cognome}, {username}, {password}, {eta}, {sesso}, {codice_fiscale}, {nazionalita}, {indirizzo}')
        
        dati = {}

        #dati['codice'] 
        dati['nome'] = nome
        dati['cognome'] = cognome
        dati['utente'] = username
        dati['password'] = password
        dati['eta'] = eta
        dati['sesso'] = sesso
        dati['codicefiscale'] = codice_fiscale
        dati['nazionalita'] = nazionalita
        dati['indirizzo'] = indirizzo
        
        #risposta = requests.put('http://192.168.10.35/registrazione', json = dati)

        break

window.close()