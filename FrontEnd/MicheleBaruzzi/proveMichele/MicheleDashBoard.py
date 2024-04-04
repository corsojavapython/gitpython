#progamma di FRONTEND Per applicazione PYTHON
# PySimpleGUI_License = 'eUyEJGMMajWKNrlRbKnJNblBVqH1lewDZFSRI86CIAkDRDlXdPmBVOsfbM32BolQc2iVIzsaIDkJxMpSY22kVdubcd2oVJJbReCfID6xMXTocxx9M9DvAx4rNjjycjzpMfS6wmidTBGplTjNZLWD5yz8ZnUERQlacdGbxLvIevWI1VlzbRnjR5WpZyXGJLzVaIWI9fu0Icjjotx3L7CpJaORYmWE15llRrmTlSyUcL3KQfi1O1iUJKFYb2n6J3psYM2F8jiaLwCSJcO8YiWV1Ml2TRGIFNzid3CVIL6qIilwRmltcRntpEvKbJGm8niSLBCFJdDobq2Q1nwJYUWT5P5nIGjno5iuI4i0wEi4Qq3vVezWdhGk9Lt7Z9X7JxJfRdCuIi6QIsjdgyxwMqDbYEi8L1CiJnEVYFX1RTlPS6X5NnzBdTWYVKknI4jmoti8MMD6MUvjMHTKA3vXMmjZANy9NVCWIxsyIAkDRFh7d7GJVmFXeyHEBRpQcBmxVIzDIvjSo9iCMYD4M1v1MLT3ACv7MQjDA1ydNySaIzsEIwkOV8tJYGW3l0sUQPWlR5koc2miVTz4cDyVIR6EIwmSVYuCcQmSlsjbbhyl5W0JZkXWJC6ube2QxmvMQHGsdhtFYTWllysfLSmEN8vtb8SxIasSIEkvlVQIQXWSRokYcUmcVHz0c0ywIf68I2jVc54jLEjhIkxLMiC44ZxHMADMY3ucMTTLcn21IVnQ01=s08d20db3813e7b51f92b711631e979db1493013e30d716b392f50d47b590abb76345948680503cb238f6ac6842b1206b947f8fc0baf6b15b115f31ffa6330f18ddf17412b438eea1c2ae924280186bce801cd2aa1596efac21fbf8162be4fdaae024ed5b89277d23a5afed81514e0f93a8eafda19938852352f09efd02cd58230b1f68e651000e4ae9ee4be317b6e063208bd5292163f1c14125547bccb314147f31d99c3f70d351d4376439141bf930f76865d598e00fb3667d6812f816ea5bcaac3fb7514cf595ea2ef4f2a903702e8a7bb04342f09110520f1ffbf3a73b560dce5d6e3aa38d79320d283ffa1a232a941ea5ce204307c32392ec9961fdcf6c94ae60c5a351d57a52c932fd93a2ed4f3c50f51f681127c4f3cf37ca18b83c787bd20ba3afc1007e1a3512dbcf00de8c8e385ef6d69200deeec2eb8cd6073cf3d52b2668e2a82de2f96bfcf93474d2868d3147fc1cc60dfa34cccebd535175c6211793cddaa237e01d8a075368464a0a8b1feeae5ed52c68567f7e3425a475c4708dfb41ccdbb6ff2dd9b2d18bb62006e78d2356c41a982ef2e580bd771213b94948b9ef4fbf96830af3546888aa3fdb8e2f2a022ebff7d60b7081ff64d8f05c1da3ea58ce842cf16dc9814fa74104d1e2731f08c7c96a8e9db4f18901f10401dfe5fc85bdaafd1328b6d9f7196b20849e9654cb92fa22be2199e8c979a47fd5'
import PySimpleGUI as sg
from flask import jsonify
import json

import requests

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