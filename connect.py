import psycopg2


class Connect:
    def __init__(self):
        self.connect = psycopg2.connect(dbname='health_control', user='postgres', password='postgres', host='localhost'
                                        , port='5432')
        self.cursor = self.connect.cursor()

    def Close(self):
        self.cursor.close()
        self.connect.close()

    def ExecuteQuery(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
