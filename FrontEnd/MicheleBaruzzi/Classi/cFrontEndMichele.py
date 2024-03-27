import PySimpleGUI as sg
from flask import json, jsonify
import requests
from datetime import datetime
import uuid

class cLogin():

    def __init__(self, backend):
        
        self.BackEnd = backend
        self.LoginData = {}

    def Init(self):

        backend = self.BackEnd

        risposta = requests.put(f'http://{backend}/init')

        if risposta.status_code == 200:
            #tutto ok
            datiRet = risposta.text

            dizRisposta = json.loads(datiRet)

            codice = dizRisposta['init']

            if codice == 'OK':
                #init OK.

                return 'OK'
        
        return 'FAIL'

    def EseguiLogin (self):

        ritorno = False

        backend = self.BackEnd

        layout = [

        [sg.Text('Username'), sg.Input(key = 'user')],
        [sg.Text('Password'), sg.Input(key = 'pwd', password_char= '*')],
        [sg.Button('Annulla'), sg.Button('OK'), sg.Button('Registrati')]

        ]

        w = sg.Window('Login E-Commerce', layout)

        while True:

            ev, va = w.Read()
        
            if ev == 'Annulla' or ev == sg.WIN_CLOSED:
                break
            
            elif ev == 'Registrati':
                registrazione_instance = cRegistrazione()
                registrazione_instance.EseguiRegistrazione()

            elif ev == 'OK':
                u = va['user']
                p = va['pwd']
                
                dati = {}
                dati['utente'] = u 
                dati['password'] = p

                risposta = requests.post(f'http://{backend}/autenticazione', json = dati)
        
                if risposta.status_code == 200:
                    #dati sono in risposta.text
                    #il login è andato a buon fine
                    ritorno = True
                    break
                
                elif risposta.status_code == 500:
                    #errore nel server, probabilmente
                    #devo fare la init

                    self.Init()

                else:
                    
                    #non è 200, non è 500, il login ha fallito
                    sg.popup_error('Login Fallito')
                
        # se sono qui, il login è ok
        if ritorno:
            datiLogin = json.loads(risposta.text)
            self.LoginData = datiLogin
            
        return ritorno

    def ShowLoginData(self):

        #layout di presentazione

        layout = [

                [sg.Text('Benvenuto ')],    
                [sg.Text('Nome: '),sg.Text(self.LoginData['Nome'])],
                [sg.Text('Cognome: '),sg.Text(self.LoginData['Cognome'])],
                [sg.Text('Il tuo codice fiscale'),sg.Text(self.LoginData['CodiceFiscale'])],
                [sg.Text('Tu abiti in'),sg.Text(self.LoginData['Indirizzo'])],
                [sg.Text('Ed hai'),sg.Text(self.LoginData['Eta'])],
                [sg.Text('E sei di nazionalità'),sg.Text(self.LoginData['Nazionalita'])],
                [sg.Button('OK')]

            ]

        w = sg.Window('Dati Login', layout)

        while True:

            ev, va = w.Read()

            if (ev == 'OK') or (ev == sg.WIN_CLOSED):
                #chiudo la finestra
                break

class cRegistrazione ():

    def custom_input(self, size):
        
        return sg.Input(key="dob", size=size, pad=(0, 0), tooltip="Formato: gg/mm/aaaa")


    def EseguiRegistrazione(self):

        frame1 = [
            [sg.Text('Username',size=(8,2)), sg.Input(key="utente")],
            [sg.Text('Password',size=(8,2)), sg.Input(key="password", password_char='*')],
        ] 
        frame2 = [
            [sg.Text('Nome',size=(8,2)), sg.Input(key="nome")],
            [sg.Text('Cognome',size=(8,2)), sg.Input(key="cognome")],
        ]    
        frame3 = [    
            [sg.Text('Data di nascita',size=(8,3)), self.custom_input(size=(10,1))],
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
        
            
        window = sg.Window('Registrazione', layout)



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
                dob_input = values['dob']#sarebbe da fare in un modo più furbo non mi piace come si inserisce la data
                sesso = 'M' if values['sesso'] else 'F'  # Seleziona il valore corrispondente al radio button
                codice_fiscale = values['cfisc'].upper()[:16]  # Converte in maiuscolo e tronca a 16 caratteri
                nazionalita = values['naz'].upper()[:3]
                indirizzo = values['ind']
                #qui genero la chiave non sarà visibile all'utenete nel momento della registrazione
                codice = str(uuid.uuid4())

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
                print(f'sto Registrando utente:{codice} {nome}, {cognome}, {username}, {password}, {eta}, {sesso}, {codice_fiscale}, {nazionalita}, {indirizzo}')
                
                dati = {}

                dati['codice'] = codice
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



