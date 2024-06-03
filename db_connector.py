import psycopg2


class PGDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def post(self, query, args=()):
        try:
            self.cursor.execute(query, args)
        except Exception as err:
            print(repr(err))
