import PySimpleGUI as sg
from flask import jsonify
import json

import requests


class cDashBoard():
    
    def DashBoard(self):
        layout = [
    [sg.Text('Benvenuto NOME CONGOME', font=('Arial', 18))],
    [sg.Text('CREDITO: +CREDITO UTENTE'),sg.Button('Ricarica'),sg.Button('Area Personale'), sg.Button('Logout')],

    # Definizione del layout

    [sg.Column([
        [sg.Text('Categoria',size=(8,2)), sg.Input(key="categoria")],
        [sg.Text('Nome Prodotto',size=(8,2)), sg.Input(key="nome_prodotto")],
        [sg.Text('Descrizione',size=(8,2)), sg.Input(key="descrizione")],
        [sg.Text('Prezzo',size=(8,2)), sg.Input(key="Prezzo")],
        [sg.Text('Foto',size=(8,2)), sg.Input(key="foto")],
        [sg.Button('Metti in Vendita')],
        [],
        [sg.Input(key="cerca"),sg.Button('Cerca')]
            
            
            
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
            sg.popup('Questa è l\'area personale dell\'utente.')
        elif event == 'Logout':
            sg.popup('Logout effettuato con successo.')
            # Inserisci qui il codice per effettuare il logout effettivo dall'applicazione
        elif event == 'Metti in Vendita':
            sg.popup('Hai cliccato su Metti in Vendita.')
        elif event == 'Compra':
            sg.popup('Hai cliccato su Compra.')
        elif event == 'Cerca':
            sg.popup('Hai cliccato su Cerca.')
        elif event == 'Ultimi Oggetti':
            # Simuliamo una lista di oggetti
            items = ['Oggetto 1', 'Oggetto 2', 'Oggetto 3', 'Oggetto 4', 'Oggetto 5']
            # Aggiorniamo la lista nella GUI
            window['-LAST_ITEMS-'].update(values=items)

    window.close()