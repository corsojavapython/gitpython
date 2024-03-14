#progamma di FRONTEND Per applicazione PYTHON
# PySimpleGUI_License = 'eUyEJGMMajWKNrlRbKnJNblBVqH1lewDZFSRI86CIAkDRDlXdPmBVOsfbM32BolQc2iVIzsaIDkJxMpSY22kVdubcd2oVJJbReCfID6xMXTocxx9M9DvAx4rNjjycjzpMfS6wmidTBGplTjNZLWD5yz8ZnUERQlacdGbxLvIevWI1VlzbRnjR5WpZyXGJLzVaIWI9fu0Icjjotx3L7CpJaORYmWE15llRrmTlSyUcL3KQfi1O1iUJKFYb2n6J3psYM2F8jiaLwCSJcO8YiWV1Ml2TRGIFNzid3CVIL6qIilwRmltcRntpEvKbJGm8niSLBCFJdDobq2Q1nwJYUWT5P5nIGjno5iuI4i0wEi4Qq3vVezWdhGk9Lt7Z9X7JxJfRdCuIi6QIsjdgyxwMqDbYEi8L1CiJnEVYFX1RTlPS6X5NnzBdTWYVKknI4jmoti8MMD6MUvjMHTKA3vXMmjZANy9NVCWIxsyIAkDRFh7d7GJVmFXeyHEBRpQcBmxVIzDIvjSo9iCMYD4M1v1MLT3ACv7MQjDA1ydNySaIzsEIwkOV8tJYGW3l0sUQPWlR5koc2miVTz4cDyVIR6EIwmSVYuCcQmSlsjbbhyl5W0JZkXWJC6ube2QxmvMQHGsdhtFYTWllysfLSmEN8vtb8SxIasSIEkvlVQIQXWSRokYcUmcVHz0c0ywIf68I2jVc54jLEjhIkxLMiC44ZxHMADMY3ucMTTLcn21IVnQ01=s08d20db3813e7b51f92b711631e979db1493013e30d716b392f50d47b590abb76345948680503cb238f6ac6842b1206b947f8fc0baf6b15b115f31ffa6330f18ddf17412b438eea1c2ae924280186bce801cd2aa1596efac21fbf8162be4fdaae024ed5b89277d23a5afed81514e0f93a8eafda19938852352f09efd02cd58230b1f68e651000e4ae9ee4be317b6e063208bd5292163f1c14125547bccb314147f31d99c3f70d351d4376439141bf930f76865d598e00fb3667d6812f816ea5bcaac3fb7514cf595ea2ef4f2a903702e8a7bb04342f09110520f1ffbf3a73b560dce5d6e3aa38d79320d283ffa1a232a941ea5ce204307c32392ec9961fdcf6c94ae60c5a351d57a52c932fd93a2ed4f3c50f51f681127c4f3cf37ca18b83c787bd20ba3afc1007e1a3512dbcf00de8c8e385ef6d69200deeec2eb8cd6073cf3d52b2668e2a82de2f96bfcf93474d2868d3147fc1cc60dfa34cccebd535175c6211793cddaa237e01d8a075368464a0a8b1feeae5ed52c68567f7e3425a475c4708dfb41ccdbb6ff2dd9b2d18bb62006e78d2356c41a982ef2e580bd771213b94948b9ef4fbf96830af3546888aa3fdb8e2f2a022ebff7d60b7081ff64d8f05c1da3ea58ce842cf16dc9814fa74104d1e2731f08c7c96a8e9db4f18901f10401dfe5fc85bdaafd1328b6d9f7196b20849e9654cb92fa22be2199e8c979a47fd5'
import PySimpleGUI as sg
from flask import jsonify
import json
from datetime import datetime
import requests

def custom_input(size):
    return sg.Input(key="dob", size=size, pad=(0, 0), tooltip="Formato: gg/mm/aaaa")


layout = [

    [sg.Text('Username'), sg.Input(key = 'user')],
    [sg.Text('Password'), sg.Input(key = 'pwd', password_char= '*')],
    [sg.Button('Annulla'), sg.Button('OK')]

]

w = sg.Window('Applicazione', layout)

while True:

    ev, va = w.Read()

    if ev == 'Annulla' or ev == sg.WIN_CLOSED:
        break

    elif ev == 'OK':
        u = va['user']
        p = va['pwd']

        print (f'Sto facendo il login per {u} , {p}')

        #ora devo chiamare la API auenticazione del BackEnd
        #ho bisogno di un dizionario che contenga:
        # utente, password
        #poi dev jonificarlo e mandarlo al backend

        dati = {}
        dati['utente'] = u 
        dati['password'] = p

        risposta = requests.post('http://192.168.10.235/autenticazione', json = dati)
        
        print(risposta.status_code)
        print(risposta.text)

        msg = risposta.text

        datiRisposta = json.loads(msg)

        if (risposta.status_code) == 200:
            #faccio vedere i dati
            pass

            #voglio una finestra PopUp
        
            layoutRisposta = [

                [sg.Text('Benvenuto '),sg.Text(datiRisposta['Nome']),sg.Text(datiRisposta['Cognome'])],    
                [sg.Text('il tuo codice fiscale è: '),sg.Text(datiRisposta['CodiceFiscale'])],
                [sg.Text('tu abiti: '),sg.Text(datiRisposta['Indirizzo'])],
                [sg.Text('e hai: '),sg.Text(datiRisposta['Eta']),sg.Text('anni')],
                [sg.Text('e sei: '),sg.Text(datiRisposta['Nazionalita'])],
                [sg.Button('OK')]
            ]

            w2 = sg.Window('Login Eseguito', layoutRisposta)
            
            while True:

                ev2, va2 = w2.Read()

                if ev2 == sg.WIN_CLOSED:
                    break

                elif event == 'OK':
                    break


        elif (risposta.status_code) == 404:
            
            # e nessun dato.
            pass

            layoutRispostaErrata = [

                [sg.Text(f'non è stato trovato nessun utente di nome: {u}')],    
                
                [sg.Button('Registrati'),sg.Button('ESCI')]
            ]

            w3 = sg.Window('errore nel login', layoutRispostaErrata)
            
            while True:

                ev3, va3 = w3.Read()

                if ev3 == sg.WIN_CLOSED :
                    break
                elif ev3 == 'ESCI':
                    window.close()
                    

                

                

                elif ev3 == 'Registrati':

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
                    layoutRegistrazione = [
                        [sg.Frame('Accesso', frame1)],
                        [sg.Frame('Dati personali', frame2)],
                        [sg.Frame('Ulteriori informazioni', frame3)],
                        [sg.Button('Annulla',size=(8,1)), sg.Button('Registrati')]
                    ]       
                    
                        
                    window = sg.Window('registrazione', layoutRegistrazione)



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
                        


        


