'''A module for db connect'''
import sqlite3

class DB:
    '''A class for database connecting'''
    def __init__(self):
        self.conn = sqlite3.connect('src/data/blog.db')

    def insert(self, table, data):
        '''Insert function. Data must be a list'''
        conn_cursor = self.conn.cursor()
        for item in data:
            columns_list = []
            values_list = []
            for key, value in item:
                columns_list.append(key)
                values_list.append(value)
            columns = ','.join(columns_list)
            values = ','.join(values_list)
            sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table, columns, values)
            conn_cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

    def select(self, table):
        '''Select function'''
        conn_cursor = self.conn.cursor()
        sql = 'SELECT * FROM  `%s` ORDER BY id' % (table)
        cursor = list(conn_cursor.execute(sql))
        self.conn.close()
        return cursor
