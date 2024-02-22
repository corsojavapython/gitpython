
class utente:
    def __init__(self):
        pass

    def create (self, 
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

    def exists(self, conn):

        SQL = "SELECT * FROM UTENTI WHERE CODICE = %s"

        parametri = (self.Codice,)

        cur = conn.cursor()
        cur.execute(SQL, parametri)

        ret = cur.fetchone()

        conn.rollback()

        if ret:
            return True
        else:
            return False


    def insert(self, conn):

        # Prepariamo l'istruzione SQL di insert

        SQL = """
            INSERT INTO UTENTI (
                CODICE,
                NOME,
                COGNOME,
                USERNAME,
                PASSWORD,
                ETA,
                SESSO,
                CFISCALE,
                NAZIONALITA,
                INDIRIZZO

            ) VALUES (
            
                %s,
                %s,%s,%s,%s,
                %s,%s,%s,
                %s,%s
            )
        """

        parametri = (self.Codice, self.Nome,self.Cognome,
                     self.UserName, self.Password,
                     self.Eta,self.Sesso, self.CFiscale,
                     self.Nazionalita, self.Indirizzo)
        
        conn.start_transaction()

        try:

            cur = conn.cursor()
            cur.execute(SQL, parametri)

            conn.commit()

        except Exception as e:

            conn.rollback()
            print (e)
