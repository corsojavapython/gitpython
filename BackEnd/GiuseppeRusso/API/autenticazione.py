from flask import request, jsonify
from Classi.cDataBaseGR import database
from Classi.cUtentiGR import utente

def DoLogin(db):
    
    dati = request.json

    try:
        UserName = dati['utente']
        pwd = dati['password']
        codice = 200

    except:
        codice = 500

    u = utente()
    
    if (not db.Con.in_transaction):
        db.BeginTransaction()
    
    ret = u.CercaUtente(UserName, pwd, db.Con)
    
    if (db.Con.in_transaction):
        db.RollbackTransaction()
    
    if u.Status == 'OK':
        print('ciao ' + u.Nome + ' ' + u.Cognome)
        codice = 200

    else:
        print('login fallito per ' + u.UserName+','+u.Password)
        codice = 404

    ret = jsonify(u.dizUtente())
    return ret, codice