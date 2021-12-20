import mysql.connector
from mysql.connector import errorcode
import os

# from mysql.connector.connection import Connection


class OutgoingConnection:
    """Contains connection initializer and queries to communicate with the database."""

    db_user = os.environ.get('WIKIDE_DB_USER')
    db_passwd = os.environ.get('WIKIDE_DB_PASSWORD')
    mydb = mysql.connector.connect(host="localhost", user=db_user,
                                   database="test_db",
                                   passwd=db_passwd, charset='utf8mb4',
                                   collation='utf8mb4_unicode_ci', use_pure=True)

    def __init__(self):
        """Establishes connection with the database once an object of the class is initialized."""

        if self.mydb.is_connected():
            print('Connection is successful')
        else:
            print('Connection failed')

    def create_db(self, DB_NAME):

        mycursor = self.mydb.cursor()

        try:
            mycursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8_unicode_ci'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

            # mycursor.execute(f"CREATE DATABASE {db_name}")
            # print(f'DB with the name {db_name} has been created!')

    def create_table(self, tablename):

        mycursor = self.mydb.cursor()

        TABLES = {}

        TABLES[tablename] = (
            """CREATE TABLE overview (
              wiki_id int NOT NULL,
              uuid TEXT NOT NULL,
              title TEXT,
              wiki_title TEXT,
              intro TEXT,
              article TEXT,
              coordinates int,
              PRIMARY KEY (wiki_id)
            ) ENGINE=InnoDB""")

        for table_name in TABLES:
            table_description = TABLES[table_name]

        try:
            print("Creating table {}: ".format(table_name), end='')
            mycursor.execute(table_description)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

        mycursor.close()
    

    def insert(self, input_dict):
        another_cursor = self.mydb.cursor()

        add_data = ("INSERT INTO overview "
                    "(wiki_id, uuid, title, wiki_title, intro, article, coordinates) "
                    "VALUES (%(wiki_id)s, %(UUID)s, %(title)s, %(wiki_title)s, %(intro)s, %(article)s, %(coordinates)s)")

        # Insert salary information
        
        another_cursor.execute(add_data, input_dict)
        self.mydb.commit()

        another_cursor.close()


    def terminate_connection(self):
        """Terminates database connection"""

        self.mydb.close()
        print('DB disconnected')


# con = OutgoingConnection()
# dictionary_test = {
#     'wiki_id': '87784',
#     'UUID': 'tttt',
#     'title': 'something',
#     'wiki_title': 'another',
#     'intro': 'this here',
#     'article': 'yeah again',
#     'coordinates': '892739'
# }
# con.insert(dictionary_test)