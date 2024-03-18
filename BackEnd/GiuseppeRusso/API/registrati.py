from flask import request
from Classi.cUtentiGR import utente

def registrati(db):
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

    if nome != None or len(nome.strip()) < 30:
        if cognome != None or len(cognome.strip()) < 30:
            if username != None or len(username.strip()) < 30:
                if password != None or len(password) < 30:
                    if eta != None or eta > 0:
                        if sesso != None or len(sesso.strip()):
                            if codicefiscale!= None or len(codicefiscale) != 16:
                                if nazionalita != None or len(nazionalita.strip()) < 30:
                                    if indirizzo != None or len(indirizzo.strip()) < 40:
                                        u = utente()

                                        import uuid
                                        chiave = str(uuid.uuid4())
                                        
                                        connessione = db.Con

                                        u.create('FAIL', chiave, nome, cognome, username, password, 
                                            eta, sesso, codicefiscale, nazionalita, indirizzo)
                                        
                                        u.insert(connessione)

                                        ritorno = 'Registrazione avvenuta con successo'
                                        codice = 200
                                    else:
                                        ritorno = 'L\'indirizzo non può essere nullo e deve contenere meno di 40 caratteri'
                                        codice = 500 
                                else:
                                    ritorno = 'La nazionalità non può essere nullo e deve contenere meno di 30 caratteri'
                                    codice = 500         
                            else:
                                ritorno = 'Il codice fiscale non può essere nullo e deve contenere esattamente 16 caratteri'
                                codice = 500 
                        else:
                            ritorno = 'Il sesso non può essere nullo e deve contenere meno di 30 caratteri'
                            codice = 500 
                    else:
                        ritorno = 'L\'età non può essere nullo o minore di 0'
                        codice = 500 
                else:
                    ritorno = 'La password non può essere nulla e deve contenere meno di 30 caratteri'
                    codice = 500         
            else:
                ritorno = 'L\'username non può essere nullo e deve contenere meno di 30 caratteri'
                codice = 500 
        else:
            ritorno = 'Il cognome non può essere nullo e deve contenere meno di 30 caratteri'
            codice = 500 
    else:
        ritorno = 'Il nome non può essere nullo e deve avere meno di 30 caratteri'
        codice = 500

    return ritorno, codice
    





