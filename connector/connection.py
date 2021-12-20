import mysql.connector
import os


class Connection:
    """ Contains connection initializer and queries to communicate with the database."""

    db_user = os.environ.get('WIKIDE_DB_USER')
    db_passwd = os.environ.get('WIKIDE_DB_PASSWORD')
    mydb = mysql.connector.connect(host="localhost", user=db_user,
                                   passwd=db_passwd, database="wikide", charset='utf8mb4',
                                   collation='utf8mb4_unicode_ci', use_pure=True)


    def __init__(self):
        """Establishes connection with the database once an object of the class is initialized."""

        if self.mydb.is_connected():
            print('Connection is successful')
        else:
            print('Connection failed')


    def select_column(self, tablename, select_column, specific_query=''):
        """ Selects column(s) from a database table.

        Default selection should be either a column containing wikipedia articles,
        or one that has an identical markdown language

        :param tablename: name of the table in the database
        :param select_column: name of the column within the specified table
        :param specific_query: default value is an empty string. Could be used to expand the SQL query.
        """

        cursor = self.mydb.cursor()
        query = ("SELECT {1} from {0} {2};").format(
            tablename, select_column, specific_query)
        cursor.execute(query)
        tuples_list = cursor.fetchall()
        return tuples_list


    def terminate_connection(self):
        """Terminates database connection"""

        self.mydb.close()
        print('DB disconnected')
