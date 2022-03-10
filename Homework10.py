import sqlite3


class DBConnection:
    """
    Class that creates DB Connection
    """
    def __init__(self, dbname):
        self.dbname = dbname
        self.create_table()

    def create_table(self):
        """
        Creates tables
        :return:
        """
        try:
            with sqlite3.connect(self.dbname) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                                             CREATE TABLE IF NOT EXISTS news (
                                             new_name TEXT,
                                             new_text TEXT,
                                             new_city TEXT,
                                             UNIQUE(new_name)
                                             )
                                             """)
                cursor.execute("""
                                             CREATE TABLE IF NOT EXISTS ads (
                                             ad_name TEXT,
                                             ad_text TEXT,
                                             actual_until DATE,
                                             UNIQUE(ad_name)
                                             )
                                             """)
                cursor.execute("""
                                             CREATE TABLE IF NOT EXISTS streams (
                                             stream_name TEXT,
                                             stream_text TEXT,
                                             stream_link TEXT,
                                             stream_start DATETIME,
                                             duration INT,
                                             UNIQUE(stream_name)
                                             )
                                             """)
                connection.commit()
                cursor.close()
        except sqlite3.Error:
            print("Create tables error")

    def insert_data(self, sql_stmt):
        """
        Single row insert
        :param sql_stmt:
        :return:
        """
        try:
            with sqlite3.connect(self.dbname) as connection:
                cursor = connection.cursor()
                cursor.execute(f'insert or ignore into {sql_stmt}')
                connection.commit()
                cursor.close()
        except sqlite3.Error:
            print("Incorrect data to insert")

    def batch_insert(self, sql_stmt, values):
        """
        Batch insert execution
        :param sql_stmt:
        :param values:
        :return:
        """
        try:
            with sqlite3.connect(self.dbname) as connection:
                cursor = connection.cursor()
                cursor.executemany(f'insert or ignore into {sql_stmt}', values)
                connection.commit()
                cursor.close()
        except sqlite3.Error:
            print("Incorrect data to insert")

    def select_data(self, table_name):
        """
        Execute select statement and return rows from table
        :param table_name:
        :return rows of data:
        """
        try:
            with sqlite3.connect(self.dbname) as connection:
                cursor = connection.cursor()
                cursor.execute(f'select * from {table_name}')
                connection.commit()
                rows = cursor.fetchall()
                cursor.close()
        except sqlite3.Error:
            print("Incorrect data to select")
        return rows


if __name__ == '__main__':
    conn = DBConnection('server.db')
    # print data from tables
    print(conn.select_data('news'))
    print(conn.select_data('ads'))
    print(conn.select_data('streams'))
