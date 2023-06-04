

import mysql.connector


class DatabaseConnector:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host

        self.mydb = mysql.connector.connect(host = self.db_host, database = self.db_name, user = self.db_user, password = self.db_password)


    def connect_to_db(self, query, default=False):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(query)
            if default == True:
                self.mydb.commit()
            res = cursor.fetchall()
            print('res is', res)
            return res
        except Exception as err:
            print("SQL Error ", err)
            return None
