import psycopg2


class Database:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except psycopg2.Error as e:
            print("Erro ao conectar ao banco de dados:", e)
            self.connection = None

    def close_db(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados fechada.")

    def is_connected(self):
        return self.connection is not None
