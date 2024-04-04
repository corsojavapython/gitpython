from flask import Flask,request, jsonify
from ClassiBackendMichele.cProdotto import Prodotto

from ClassiBackendMichele.cDataBase import database
from ClassiBackendMichele.cUtenti import utente

import json
import uuid
import os
import time

ecommerce = Flask(__name__)

db = database()
utentiLogin = []

def VerifyLogin(user,password):

    login = False

    for u in utentiLogin:
        if (u.UserName == user) and \
           (u.Password == password):

            if u.Status == 'OK':
                login = True
                break
    if login:
        retMsg = 'LOGIN'
    else:
        retMsg = 'LOGOUT'

    return retMsg

@ecommerce.route('/registrazione' , methods = ['PUT'])
def register():

    #recupero i dati dalla request
    retCode = 200

    try:
        dati = request.json

        Nome = dati['nome']
        Cognome = dati['cognome']
        Utente = dati['utente']
        Password = dati['password']
        Eta = dati['eta']
        Sesso = dati['sesso']
        CFiscale = dati['cfiscale']
        Nazionalita = dati['nazionalita']
        Indirizzo = dati['indirizzo']
    
        print(f'sto registrando {Cognome} {Nome}')

        #Mi serve una chiave primaria.
        chiave = str(uuid.uuid4())

        print(f'la chiave assegnata è {chiave}')

        #devo creare un utente di classe Utente e poi scrivere
        # i dati nel database
    
        u = utente()
        u.create('FAIL',
                 chiave,
                 Nome,
                 Cognome,
                 Utente,
                 Password,
                 Eta,
                 Sesso,
                 CFiscale,
                 Nazionalita,
                 Indirizzo)

        u.insert(db.Con)

    except Exception as e:

        print(e.__repr__())

        retCode = 500
        chiave = 'null'
        u.UserName = 'null'
        u.Password = 'null'
        u.Status = 'FAIL'

    finally:

        # DEVO Comporre la risosta in formato JSON come da
        #Documentazione

        '''
        Risposta:   Chiave univoca del nuovo utente in formato JSON con user e password
                    Ed il codice di errore per operazione non riuscita ed un messaggio
        Esempio:    {"codice":"3ed2134a-3432-34244242-EFFF", "utente":"ppp", "password":"rrr", 
                    "messaggio": "OK" se tutto è a posto, | "FAIL" se errore in regisrazione}
        
        
        
        '''
        datiRet = {}
        datiRet['chiave'] = chiave
        datiRet['utente'] = u.UserName
        datiRet['password'] = u.Password
        datiRet['loginstatus'] = u.Status

        datiJson = json.dumps(datiRet)

        return datiJson, retCode






@ecommerce.route('/init', methods = ['PUT'])
def init():

    #leggere i parametri JSON,
    #da cui beccare il nome del file e i dati di connessione
    #try:

    #Leggo il file di configurazione BackEnd.Config
        try:

            fname = os.path.abspath('.\\BackEnd\\BackEnd.Config')

            print(f'leggo {fname}')

            print(fname)

            with open(fname,'r') as cfg:
                config = cfg.read()

            dati = json.loads(config)

            filename = dati['filename']
            host = dati['host']
            dbase = dati['database']
            username = dati['username']
            password = dati['password']

        except Exception as e:
            print(e.__repr__())

        ritorno = 'i dati sono ok'
        codice = 200

        # devo leggere il file di dati

        try:

            fname = os.path.abspath(filename)

            print(f'leggo {fname}')

            with (open(fname,'r',encoding='utf-8')) as fr:
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
    # Devo gestire i dati in ingresso
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

    if not db.Con.in_transaction:
        db.BeginTransaction()

    ret = u.CercaUtente(UserName, pwd, db.Con)

    if db.Con.in_transaction:
        db.RollbackTransaction()

    if u.Status == 'OK':
        # Utente trovato
        print('ciao ' + u.Nome + ' ' + u.Cognome)
        codice = 200
        
        # Verifica se l'utente è già loggato
        if not VerifyLogin(u.UserName, u.Password) == 'LOGIN':
            # Utente non è già online, aggiungilo alla lista
            utentiLogin.append(u)
            print('status utente Login')
        else:
            # Utente già online, non aggiungere nuovamente
            print('Utente già loggato')
    else:
        # Utente non trovato
        print('Login fallito per ' + u.UserName + ',' + u.Password)
        codice = 404

    ret = jsonify(u.dizUtente())


    print(f'utenti on line {len(utentiLogin)}')

    return ret, codice



@ecommerce.route('/logout', methods=['POST'])
def logout():
    dati = request.json
    messaggio = ''

    try:
        username = dati['utente']
    except KeyError:
        messaggio = 'Nome utente non fornito'
        codice = 400
        

    for utente in utentiLogin:
        if utente.UserName == username:
            utentiLogin.remove(utente)
            utente.Status = 'FAIL'  # Imposta lo status del login su 'FAIL'
            print('Logout effettuato per l\'utente:', username)
            print('Status utente:', utente.Status)
            messaggio = (f'Logout effettuato con successo per {username}')
            codice = 200
            break
    else:
        messaggio = (f'Utente {username} non trovato o già disconnesso')
        codice = 404

    return jsonify({'messaggio': messaggio}), codice
    





@ecommerce.route('/vendi', methods=['PUT'])
def vendi_prodotto():
    # Ottieni i dati inviati nella richiesta
    dati = request.json

    try:
        # Estrapola i dati relativi al prodotto dalla richiesta
        nome = dati['nome']
        categoria = dati['categoria']
        prezzo = dati['prezzo']
        descrizione = dati['descrizione']
        foto = dati['foto']

        # Crea un'istanza della classe Prodotto
        nuovo_prodotto = Prodotto()

        # Crea il nuovo oggetto con i dati ricevuti dalla richiesta
        nuovo_prodotto.ObjectCreate('DISPONIBILE', '', categoria, nome, prezzo, descrizione, foto)

        # Inserisci il nuovo prodotto nel database
        nuovo_prodotto.insertProdotto(db.Con)

        # Restituisci una risposta JSON di conferma
        return jsonify({'message': 'Prodotto inserito con successo nel database'}), 200
    
    except KeyError:
        # Se alcuni dati richiesti non sono presenti nella richiesta
        return jsonify({'message': 'Alcuni dati richiesti non sono stati forniti'}), 400
    
    except Exception as e:
        # Se si verifica un errore durante l'inserimento del prodotto nel database
        print(e)
        return jsonify({'message': 'Si è verificato un errore durante l\'inserimento del prodotto'}), 500
   
        

@ecommerce.route('/compra', methods=['POST'])
def acquista_prodotto():
    # Ottieni i dati inviati nella richiesta
    data = request.json

    # Estrapola il codice del prodotto dall'ID ricevuto nella richiesta
    codice_prodotto = data.get('id_prodotto')

    # Esegui la ricerca del prodotto nel database tramite il codice
    prodotto = Prodotto()
    risultato = prodotto.CercaPRODOTTO(codice_prodotto, db.Con)

    # Se il prodotto è stato trovato nel database
    if risultato:
        # Effettua l'acquisto (esempio di implementazione)
        # Qui puoi inserire la logica per gestire l'acquisto del prodotto, ad esempio aggiornare lo stato del prodotto nel database
        
        # Restituisci una risposta JSON di conferma
        return jsonify({'message': 'Acquisto effettuato con successo'}), 200
    else:
        # Se il prodotto non è stato trovato nel database
        return jsonify({'message': 'Prodotto non trovato'}), 404


if (__name__) == '__main__':

    print(init())

    ecommerce.run(host='0.0.0.0',port = 80)