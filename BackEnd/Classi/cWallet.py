from Classi.cUtenti import utente
from Classi.cDataBase import database

import json

class wallet:

    def __init__(self, proprietario, d, db:database ):

        '''

        self.proprietario = proprietario
        self.saldo = 0.0
        self.descrizione = d
        self.Connection = db.Con
        '''
    def Generate(self):
        # scrive nel DataBase un nuovo wallet

        SQL = """
            Insert into WALLET (
                COD_PROPRIETARIO,
                SALDO,
                DESCRIZIONE)
            
                Values(%s, %s, %s)

           """    

        parametri = (self.proprietario,
                    self.saldo,
                    self.descrizione)

        self.Connection.start_transaction()

        retCode = 200

        try:

            cur = self.Connection.cursor
            cur.execute(SQL,parametri)

            self.Connection.commit()
            ret = {'esito':'OK'} 

        except Exception as e:
            print(e)
            self.Connection.rollback()
            retCode = 500
            ret = {'esito':'FAIL'}


        retJson = json.dumps(ret)
    
        return retJson,retCode
    