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
                
                self.NeedRegister = True
                ritorno = False
                break

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





