from cDataBase import database

class utente:
    def __init__(self):
        pass

    def insert(self, 
               codice, nome, cognome, username, 
               password, eta, sesso, cfiscale, 
               nazionalita, indirizzo):

        self.Status = 'logout'
        self.Codice = codice
        self.Nome = nome
        self.Cognome = cognome
        self.UserName = username
        self.Password = password
        self.Eta = eta
        self.Sesso = sesso
        self.CFiscale = cfiscale
        self.Nazionalita = nazionalita
        self.Indirizzo = indirizzo