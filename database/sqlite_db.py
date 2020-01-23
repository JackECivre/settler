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
          `event_time` datetime,
          `event_city` varchar(255),
          `event_address` varchar(255),
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
         
        CREATE TABLE IF NOT EXISTS `questions` (
          `question_id` int PRIMARY KEY,
          `category` varchar(255),
          `answer_type` varchar(255)
        );
        
        CREATE TABLE IF NOT EXISTS `answer` (
          `answer_id` int PRIMARY KEY,
          `user_id` int,
          `question_id` int,
          `answer` varchar(255)
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
        self.conn.execute(sql, data)
        self.conn.commit()

    def host_meal_to_db(self, data):
        """ add meal to social_meals table in database """

        sql = """INSERT INTO social_meals 
        (creator_id, event_date, max_people,  date_of_birth, meal_preference) 
        VALUES (?, ?, ?, ?) """
        self.conn.execute(sql, data)
        self.conn.commit()

    def read_table(self, table_name, columns="*"):
        """ read_listing from the database """
        cur = self.conn.cursor()
        sql = f"SELECT {columns} from {table_name}"
        cur.execute(sql)
        rows = cur.fetchall()
        return rows


if __name__ == "__main__":
    DB_FILE = "./settler.db"
    db = DB(DB_FILE)
    rows = db.read_table("shared_activities")
    host = defaultdict(list)
    for r in rows:
        host["first_name"].append(r[1])
    x=1