import mysql.connector

class database:

    def __init__(self):
        pass

    def connetti(self, hostname, dbname, username, password):

        self.Host = hostname
        self.Db = dbname
        self.User = username
        self.Pwd = password

        try:

            conn = mysql.connector.connect(
           
                host = self.Host,
                user = self.User,
                password = self.Pwd,
                database = self.Db

            )

            self.Con = conn

        except:

            self.Con = None

    def cursore(self,istruzione):

        if self.Con:
            self.Cur = self.Con.cursor(istruzione)
        else:
            self.Cur = None

    def BeginTransaction(self):

        self.Con.start_transaction()

    def CommitTransacion(self):

        self.Con.commit()

    def RollbackTransaction(self):

        self.Con.rollback()
