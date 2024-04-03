class Prodotto:
    def __init__(self):
        pass

    def dizOggetto(self):

        diz = {}

        diz['Disponibile'] = self.Status
        diz['CodiceOggetto'] = self.CodiceOggetto
        diz['Categoria'] = self.Categoria
        diz['Nome'] = self.Nome
        diz['Prezzo'] = self.Prezzo
        diz['Descrizione'] = self.Descrizione
        diz['Foto'] = self.Foto
        

        return diz

    def ObjectCreate (self, status,
               codiceOggetto, categoria, nome, prezzo, descrizione, 
               foto):

        self.Status = status
        self.CodiceOggetto = codiceOggetto
        self.Categoria = categoria
        self.Nome = nome
        self.Prezzo = prezzo
        self.Descrizione = descrizione
        self.Foto = foto

    def CercaPRODOTTO(self, n, con):

        if con:
            #cerco l'utente
        
            cur = con.cursor()
            SQL = """
                SELECT * FROM PRODOTTI where 
                    NOME = %s 
            """
            cur.execute(SQL,(n))
            risultato = cur.fetchall()
            if risultato:
                
                status, codiceOggetto, categoria, nome, prezzo, descrizione, foto  = risultato

                # trasformare la tupla 'risultato' in un insieme di variabili
                #esempiio : t = (3,5,7)
                #spacchettato -> var1, var2, var 3 = t

                #chiamare il metodo create della classe passando i giusti parametri

                self.create(
                    'DISPONIBILE',
                    codiceOggetto,
                    categoria,
                    nome,
                    prezzo,
                    descrizione,
                    foto)
                
            else:
                self.create(
                    'NON DISPONIBILE',
                    '',
                    '',
                    n,
                    '',
                    '',
                    '')
                
                #chiamate create con username e password cercati e status = logout

            #print(risultato)
            return risultato

        else:
            return "database non connesso"
        

    def insertProdotto(self, conn):

        # Prepariamo l'istruzione SQL di insert

        SQL = """
            INSERT INTO PRODOTTI (
                DISPONIBILE,
                CODICEOGGETTO,
                CATEGORIA,
                NOME,
                PREZZO,
                DESCRIZIONE,
                FOTO

            ) VALUES (
            
                %s,
                %s,%s,%s,
                %s,%s,%s
                
            )
        """

        parametri = (self.Status,
                     self.CodiceOggetto, self.Categoria ,self.Nome,
                     self.Prezzo, self.Descrizione ,self.Foto)
        
        conn.start_transaction()

        try:

            cur = conn.cursor()
            cur.execute(SQL, parametri)

            conn.commit()

        except Exception as e:

            conn.rollback()
            print (e)
        
