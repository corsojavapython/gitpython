import PySimpleGUI as sg
from Finestre.MainPage import mainPage

def datiUtente(datiRisposta):
    layoutRisposta = [

        [sg.Text('Benvenuto '),sg.Text(datiRisposta['Nome']), sg.Text(datiRisposta['Cognome'])],    
        [sg.Text('il tuo codice fiscale è: '), sg.Text(datiRisposta['CodiceFiscale'])],
        [sg.Text('tu abiti a: '), sg.Text(datiRisposta['Indirizzo'])],
        [sg.Text('ed hai: '), sg.Text(datiRisposta['Eta']),sg.Text(' anni')],
        [sg.Text('e sei di nazionalità: '), sg.Text(datiRisposta['Nazionalita'])],
        [sg.Button('OK')]

    ]

    w2 = sg.Window('Login Eseguito', layoutRisposta)
            
    while True:

        ev2, va2 = w2.Read()

        if ev2 == sg.WIN_CLOSED:
            break
      
        elif ev2 == 'OK':
            mainPage()
            w2.close()