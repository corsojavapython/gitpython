#progamma di FRONTEND Per applicazione PYTHON

import PySimpleGUI as sg

layout = [

    [sg.Text('Username'), sg.Input()],
    [sg.Text('Password'), sg.Input()],
    [sg.Button('Annulla'), sg.Button('OK')]

]

w = sg.Window('Applicazione', layout)

while True:

    ev, va = w.Read()

    if ev == 'Annulla':
        break



