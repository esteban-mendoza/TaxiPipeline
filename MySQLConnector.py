# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:39:11 2020

@author: Jorge Esteban Mendoza Ortiz
"""

from mysql.connector.connection import MySQLConnection
from mysql.connector import errorcode
import mysql.connector
import traceback
import logging


config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'taxi'
}


class MySQLConnector:
    """
    Convenience wrapper that creates a connection with the 
    database taxi at localhost and is capable of performing
    operations to the MySQL database.
    """

    def __init__(self):
        try:
            self.connection = MySQLConnection(**config)
            print("Connection created")

            self.cursor = self.connection.cursor(dictionary=True)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def query(self, query, args=None):
        """
        Executes queries given a string with the query
        
        Input
            query:     str with MySQL query
            args=None: arguments to pass to cursor
            
        Output
            None
        """
        if args is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, args)

#    def fetchone(self):
#        return self.cursor.fetchone()
#
#    def fetchall(self):
#        return self.cursor.fetchall()

    def insert(self, data):
        """
        Inserts a dictionary into the trips table
        
        Input
            data: dict with proper registry
        
        Output
            None
        """
        
        fields, values = self.str_helper(data)

        query = ("INSERT INTO trips "
                 "(" + fields + ") "
                 "VALUES (" + values + ")")
        try:
            self.query(query)
            self.connection.commit()
        except Exception as e:
            logging.error(traceback.format_exc())
        self.query(query)
        

#    def update(self, query, args):
#        self.query(query, args)
#        self.connection.commit()
#
#    def delete(self, query):
#        self.query(query)
#        self.connection.commit()
#
    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed")
    
    @staticmethod
    def str_helper(data):
        fields = str()
        values = str()

        for field in data.keys():
            fields += f"{field}, "

        for value in data.values():
            if type(value) is int or type(value) is float:
                values += f"{value}, "
            else:
                values += f"\'{value}\', "

        fields = fields.rstrip(", ")
        values = values.rstrip(", ")

        return fields, values

if __name__ == '__main__':
    # Example
    cnx = MySQLConnector()

    cnx.query("""
              select * from trips
              limit 3
              """)
    for row in cnx.cursor:
        print(row)

    cnx.close()
