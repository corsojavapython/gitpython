from flask import request
from Classi.cUtentiGR import utente
import json


def init(db):
    
    dati = request.json

    filename = dati['filename']
    host = dati['host']
    dbase = dati['database']
    username = dati['username']
    password = dati['password']

    ritorno = 'i dati sono ok'
    codice = 200

    try:

        with (open(filename,'r',encoding='utf-8')) as fr:
            datiJson = fr.read()
            dizDati = json.loads(datiJson)

    except Exception as e:

        ritorno = 'Il nome del file dati è errato'
        codice = 500

    if codice != 200:
        return ritorno, codice                            

    db.connetti(

        host,
        dbase,
        username,
        password

    )

    connessione = db.Con

    for k in dizDati.keys():
                
        chiave = k
        datiDiz = dizDati[chiave]

        utenteDaCreare = utente()
            
        utenteDaCreare.create(
                
            'FAIL', chiave,
            datiDiz['nome'],
            datiDiz['cognome'],
            datiDiz['username'],
            datiDiz['password'],
            datiDiz['eta'],
            datiDiz['sesso'],
            datiDiz['cfisc'],
            datiDiz['nazionalita'],
            datiDiz['indirizzo']
                
            )

        utenteDaCreare.insert(connessione)

        ritorno = {"init":"OK"}
        codice = 200


    return ritorno, codice