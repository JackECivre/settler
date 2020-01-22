import sqlite3
from collections import defaultdict
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
        CREATE TABLE IF NOT EXISTS `users` (
          `user_id` INTEGER PRIMARY KEY AUTOINCREMENT,
          `username` varchar(255),
          `first_name` varchar(255),
          `last_name` varchar(255),
          `date_of_birth` datetime,
          `address` varchar(255),
          `current_city` varchar(255),
          `origin_country` varchar(255)
        );
        
        CREATE TABLE IF NOT EXISTS `shared_activities` (
          `creator_id` int,
          `activity_id` int PRIMARY KEY,
          `name` varchar(255),
          `address` varchar(255),
          `event_date` datetime,
          `max_people` int,
          `description` varchar(255)
        );
        
        CREATE TABLE IF NOT EXISTS `social_meals` (
          `meal_id` int PRIMARY KEY,
          `creator_id` int,
          `event_date` datetime,
          `max_people` int,
          `meal_preference` varchar(255)
        );
        
        CREATE TABLE IF NOT EXISTS `social_information` (
          `category` varchar(255),
          `website_id` int PRIMARY KEY,
          `website` varchar(255),
          `source` varchar(255),
          `source_id` int
        );
        
        CREATE TABLE IF NOT EXISTS `services` (
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

    def signup_to_db(self, data):
        """ add user name to users table in database """

        sql = """INSERT INTO users 
        (username, first_name, last_name,  date_of_birth, address, current_city, origin_country) 
        VALUES (?, ?, ?, ?, ?, ?, ?) """
        # data = ["avi326", "avi", "barazani", None, "add", "asd", "asd"]
        self.conn.execute(sql, data)
        self.conn.commit()

    def read_listing(self):
        """ read_listing from the database """
        cur = self.conn.cursor()
        sql = """SELECT * from users """
        cur.execute(sql)
        rows = cur.fetchall()
        return rows

# if __name__ == "__main__":
    # DB_FILE = "./settler.db"
    # db = DB(DB_FILE)
    # rows = db.read_listing()
    # host = defaultdict(list)
    # for r in rows:
    #     host["first_name"].append(r[1])