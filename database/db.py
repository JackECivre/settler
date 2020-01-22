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


    def create_tables(self, sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.executescript(sql)
        except Error as e:
            print(e)
    #  settler.db

    def create_all_tables(self):
        """ script that create all the tables by ERD diagram """

        conn = self.conn

        sql_create_tables = """
        CREATE TABLE `users` (
          `user_id` int PRIMARY KEY,
          `username` varchar(255),
          `first_name` varchar(255),
          `last_name` varchar(255),
          `date_of_birth` datetime,
          `address` varchar(255),
          `current_city` varchar(255),
          `origin_country` varchar(255)
        );
        
        CREATE TABLE `shared_activities` (
          `creator_id` int,
          `activity_id` int PRIMARY KEY,
          `name` varchar(255),
          `address` varchar(255),
          `event_date` datetime,
          `max_people` int,
          `description` varchar(255)
        );
        
        CREATE TABLE `social_meals` (
          `meal_id` int PRIMARY KEY,
          `creator_id` int,
          `event_date` datetime,
          `max_people` int,
          `meal_preference` varchar(255)
        );
        
        CREATE TABLE `social_information` (
          `category` varchar(255),
          `website_id` int PRIMARY KEY,
          `website` varchar(255),
          `source` varchar(255),
          `source_id` int
        );
        
        CREATE TABLE `services` (
          `service_id` int PRIMARY KEY,
          `service_name` varchar(255),
          `service` varchar(255) UNIQUE,
          `address` varchar(255),
          `opening_hour` datetime,
          `closing_hour` datetime,
          `source` varchar(255),
          `source_id` int
        );
        

             
        """
        # create tables
        if conn is not None:
            self.create_tables(sql_create_tables)
        else:
            print("Error! cannot create the database connection.")

# <<<<<<< HEAD
    # def host_to_db(self):
    #     sql =  "INSERT INTO table_name (columnName,columnName,columnName,columnName) VALUES (%s, %s, %s, %s)")
    #     # c.execute(sql, (guest_vnaam, guest_anaam, guest_cnaam, guest_datum))
    #     return
# =======
    def form_to_db(self, table, columns, data):
        sql = f"INSERT INTO {table} (username, first_name, last_name,  date_of_birth, address, current_city, origin_country) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = ["avi326", "avi", "barazani", None, "add", "asd", "asd"]
        self.conn.execute(sql, data)
        self.conn.commit()
# >>>>>>> c025357c52e80128caa5a86226143b302075a455
