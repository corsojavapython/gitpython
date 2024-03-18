import PySimpleGUI as sg
from Finestre.Registrazione import registrazione

def loginFallito():
    layout = [

    [sg.Text('Username o password errate!')],
    [sg.Button('Annulla'), sg.Button('Registrati')]

    ]

    w3 = sg.Window('Login fallito', layout)

    while True:
        ev, va = w3.Read()
        
        if ev == 'Annulla' or ev == sg.WIN_CLOSED:
            break
        elif ev == 'Registrati':
            w3.close()
            registrazione()
            break