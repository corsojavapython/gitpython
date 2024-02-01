from flask import Flask,request
#from Librerie.utente import CercaUtente

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

