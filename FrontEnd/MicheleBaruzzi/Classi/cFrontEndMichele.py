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
    
    
    
    def DashBoard(self):
        layout = [
            [sg.Text('Benvenuto', size=(20,1)), sg.Text(self.LoginData['Nome'], size=(20,1)),sg.Text(self.LoginData['Cognome'], size=(20,1))],
            [sg.Text('CREDITO: +CREDITO UTENTE'), sg.Button('Ricarica'), sg.Button('Area Personale'), sg.Button('Logout')],

            # Definizione del layout

            [sg.Column([
                [sg.Text('Categoria',size=(8,2)), sg.Input(key="categoria")],
                [sg.Text('Nome Prodotto',size=(8,2)), sg.Input(key="nome_prodotto")],
                [sg.Text('Descrizione',size=(8,2)), sg.Input(key="descrizione")],
                [sg.Text('Prezzo',size=(8,2)), sg.Input(key="Prezzo")],
                [sg.Text('Foto',size=(8,2)), sg.Input(key="foto")],
                [sg.Button('Metti in Vendita')],
                [sg.Input(key="cerca"), sg.Button('Cerca')]
            ], size=(400, 600)),  # Prima colonna

            sg.Column([
                [sg.Frame('Ultimi Oggetti Messi in Vendita', [
                    [sg.Listbox(values=[], size=(80, 30), key='oggetti_venduti')]
                ])]
            ], size=(400, 600)),  # Seconda colonna

            sg.Column([
                [sg.Frame('Ultimi Oggetti comprati', [
                    [sg.Listbox(values=[], size=(80, 30), key='oggetti_comprati')]
                ])]
                # Qui puoi aggiungere altri elementi per la terza colonna
            ], size=(400, 600))]  # Terza colonna
        ]

        window = sg.Window('E-commerce Dashboard', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Area Personale':
                self.needDati = True
                ritorno = False
                break
                

            elif event == 'Logout':
                self.needLogOut = True
                ritorno = False
                break
                # Inserisci qui il codice per effettuare il logout effettivo dall'applicazione
            elif event == 'Metti in Vendita':
                sg.popup('Hai cliccato su Metti in Vendita.')
            elif event == 'Cerca':
                sg.popup('Hai cliccato su Cerca.')
            elif event == 'Ultimi Oggetti':
                # Simuliamo una lista di oggetti
                items = ['Oggetto 1', 'Oggetto 2', 'Oggetto 3', 'Oggetto 4', 'Oggetto 5']
                # Aggiorniamo la lista nella GUI
                window['oggetti_venduti'].update(values=items)

    def Logout(self):
        layout = [
            [sg.Text('ci vediamo presto', size=(20,1)), sg.Text(self.LoginData['Nome'], size=(20,1))],
            [sg.Button('LogOut'),sg.Button('annulla'),]


        ]

        w = sg.Window('Login E-Commerce', layout)

        while True:

            ev, va = w.Read()
        
            if ev == 'Annulla' or ev == sg.WIN_CLOSED:
                break

            elif ev == 'Logout':
                u = self.LoginData['utente']
                p = self.LoginData['password']
                
                dati = {}
                dati['utente'] = u 
                dati['password'] = p

            risposta = requests.post(f'http://{backend}/logout', json = dati)
                


