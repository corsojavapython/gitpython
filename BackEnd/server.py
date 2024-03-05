from flask import Flask,request

from Classi.cDataBase import database
from Classi.cUtenti import utente

import json

import os


ecommerce = Flask(__name__)

db = database()

@ecommerce.route('/init', methods = ['PUT'])
def init():

    #leggere i parametri JSON,
    #da cui beccare il nome del file e i dati di connessione
    #try:

        dati = request.json

        filename = dati['filename']
        host = dati['host']
        dbase = dati['database']
        username = dati['username']
        password = dati['password']

        ritorno = 'i dati sono ok'
        codice = 200

        # devo leggere il file di dati

        try:

            with (open(filename,'r',encoding='utf-8')) as fr:
                datiJson = fr.read()
                dizDati = json.loads(datiJson)

        except Exception as e:

            ritorno = 'Il nome del file dati è errato'
            codice = 500

        if codice != 200:
            return ritorno, codice                            

        #devo connettermi al DB

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

            #per Ogni chiave, ci serve fare una insert
            #nel database, sempre che i dati non ci siano già
            #nel qual caso faccio una update 

            #prima di tutto voglio creare una istanza della classe Utente
            #per ogni utente presente nel dizionario

            utenteDaCreare = utente()

            utenteDaCreare.create(chiave,
                          datiDiz['nome'],
                          datiDiz['cognome'],
                          datiDiz['username'],
                          datiDiz['password'],
                          datiDiz['eta'],
                          datiDiz['sesso'],
                          datiDiz['cfisc'],
                          datiDiz['nazionalita'],
                          datiDiz['indirizzo'])


            #if not utenteDaCreare.exists(connessione):
            utenteDaCreare.insert(connessione)

            ritorno = {"init":"OK"}
            codice = 200


        return ritorno, codice

@ecommerce.route('/test', methods = ['POST', 'GET', 'PUT', 'DELETE'])
def test():
    dati = request.data
    return dati


@ecommerce.route('/autenticazione', methods = ['POST'])
def DoLogin():

    #devo gestire i dati in ingresso
    dati = request.json

    try:

        UserName = dati['utente']
        pwd = dati['password']

        ritorno = 'i dati sono ok'
        codice = 200

    except:

        ritorno = 'i dati fanno schifo'
        codice = 500

    u = utente()
    ret = u.CercaUtente(UserName, pwd, db.Con)
    #u = None #in realtà dovrebbe fare la ricerca
    
    if u:
        #utente trovato
        pass
    else:
        #utente assente
        pass

    listRet = list(ret)

    return listRet ,codice

if (__name__) == '__main__':
    ecommerce.run(host='0.0.0.0',port = 80)

