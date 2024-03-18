import PySimpleGUI as sg
import json
import requests
from Finestre.DatiUtente import datiUtente
from Finestre.LoginFallito import loginFallito

def login():
  layout = [

    [sg.Text('Username'), sg.Input(key = 'user')],
    [sg.Text('Password'), sg.Input(key = 'pwd', password_char= '*')],
    [sg.Button('Registrati'),sg.Button('Annulla'), sg.Button('OK')]

    ]

  w = sg.Window('Applicazione', layout)

  while True:

    ev, va = w.Read()

    if ev == 'Annulla' or ev == sg.WIN_CLOSED:
      break

    elif ev == 'Registrati':
      from Finestre.Registrazione import registrazione
      registrazione()
      w.close()

    elif ev == 'OK':
      u = va['user']
      p = va['pwd']
        
      print (f'Sto facendo il login per {u} , {p}')
      dati = {}
      dati['utente'] = u 
      dati['password'] = p

      risposta = requests.post('http://127.0.0.1/autenticazione', json = dati)
            
      print(risposta.status_code)
      print(risposta.text)

      msg = risposta.text

      datiRisposta = json.loads(msg)

      if (risposta.status_code) == 200:
        w.close()
        datiUtente(datiRisposta)

      elif (risposta.status_code) == 404:
        w.close()
        loginFallito()

      




