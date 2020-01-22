import sqlite3
from sqlite3 import Error

class DB:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)
        self.create_all_tables()

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            if conn:
                return conn
                # conn.close()


    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
    #  settler.db

    def create_all_tables(self):
        """ script that create all the tables by ERD diagram """

        conn = self.create_connection(r"settler.db")

        create_table = """
            CREATE TABLE IF NOT EXISTS projects (
                id integer PRIMARY KEY,
                name text NOT NULL,
                begin_date text,
                end_date text
            );
             
        """
        # create tables
        if conn is not None:
            self.create_table(create_table)
        else:
            print("Error! cannot create the database connection.")

    def host_to_db(self):
        sql =  "INSERT INTO table_name (columnName,columnName,columnName,columnName) VALUES (%s, %s, %s, %s)")
        # c.execute(sql, (guest_vnaam, guest_anaam, guest_cnaam, guest_datum))
        return