from flask import Flask,request

import mysql.connector

ecommerce = Flask(__name__)

@ecommerce.route('/test', methods = ['POST', 'GET', 'PUT', 'DELETE'])
def test():
    dati = request.data
    return dati

@ecommerce.route('/autenticazione', methods = ['POST'])
def DoLogin():

    #devo gestire i dati in ingresso

    try:

        dati = request.json

        UserName = dati['utente']
        pwd = dati['password']

        ritorno = 'i dati sono ok'
        codice = 200

        #u = CercaUtente(UserName, pwd)
        u = None #in realtà dovrebbe fare la ricerca

        host = 'python.hostingstudenti.fortechance.com'
        db = 'c3db'
        user = 'c3python'
        passwd = 'ThePythonCourse098'

        conn = mysql.connector.connect(
            host = host,
            user = user,
            password = passwd,
            database = db)

        richiesta = f'SELECT * FROM UTENTI Where USERNAME = "{UserName}" AND PASSWORD = "{pwd}"'

        cur = conn.cursor(richiesta)
        u = cur.fetchone()
        
        if u == None:
            #Utente non trovato
            pass
        else:
            #Utente trovato
            pass

        resp = '' # poi la implementiamo       

    except:

        ritorno = 'hai fatto puttanate con i dati, e moo sono cazzi'
        codice = 500

    
    return ritorno, codice

if (__name__) == '__main__':
    ecommerce.run(host='0.0.0.0',port = 80)

