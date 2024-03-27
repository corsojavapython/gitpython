from flask import Flask,request, jsonify

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

    #Leggo il file di configurazione BackEnd.Config
        with open("C:\\Users\\39338\\OneDrive\\Desktop\\Python\\gitpython\\BackEnd\\AlessandroStorai\\BackEnd.Config",'r') as cfg:
            config = cfg.read()

        dati = json.loads(config)

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
            ###
            utenteDaCreare.create('FAIL', chiave,
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
    
    if (not db.Con.in_transaction):
        db.BeginTransaction()
    
    ret = u.CercaUtente(UserName, pwd, db.Con)
    
    if (db.Con.in_transaction):
        db.RollbackTransaction()
    
    if u.Status == 'OK':
        #utente  trovato
        print('ciao '+ u.Nome+' '+ u.Cognome)
        codice = 200
        pass
    else:
        #utente assente
        print('login fallito per ' + u.UserName+','+u.Password)
        codice = 404
        pass

    ret = jsonify(u.dizUtente())
    return ret, codice

@ecommerce.route('/registrazione', methods = ['POST'])
def registrazione():
    dati =request.json
    nome = dati['nome']
    cognome = dati['cognome']
    username = dati['username']
    password = dati['password']
    eta = dati['eta']
    sesso = dati['sesso']
    codicefiscale = dati['codiceFiscale']
    nazionalita = dati['nazionalita']
    indirizzo = dati['indirizzo']

    #********************************************************
    #MANCA - Bisogna aggiungere i controlli sui dati ricevuti
    #********************************************************

    u = utente()

    import uuid
    chiave = str(uuid.uuid4())
    
    connessione = db.Con
    ritorno = 'Registrazione avvenuta con successo'
    codice = 200

    try:
        u.create('FAIL', chiave, nome, cognome, username, password, 
        eta, sesso, codicefiscale, nazionalita, indirizzo)
    
        u.insert(connessione)
    except Exception as e:
        ritorno = 'Registrazione fallita!'
        codice = 500
    

    return ritorno, codice

if (__name__) == '__main__':
    ecommerce.run(host='0.0.0.0',port = 80)

#auto launch init function
#init()