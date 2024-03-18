from flask import Flask
from API.init import init
from API.autenticazione import DoLogin
from Classi.cDataBaseGR import database
from API.registrati import registrati

ecommerce = Flask(__name__)

db = database()

@ecommerce.route('/init', methods = ['PUT'])
def inizializzazione():
    return init(db)

@ecommerce.route('/autenticazione', methods = ['POST'])
def autenticazione():
    return DoLogin(db)

@ecommerce.route('/registrazione', methods = ['POST'])
def registrazione():
    return registrati(db)
    
if (__name__) == '__main__':
    ecommerce.run(host='0.0.0.0', port = 80)

