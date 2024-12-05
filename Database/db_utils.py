import pandas as pd
import sqlite3

class Database:
    def __init__(self, db_name):
        """
        Initialize the database connection.

        Parameters
        ----------
        db_name : str
            The name of the SQLite database to connect to.
        """
        self.db_name = db_name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()

    def create_table(self, table_name, columns):
        """
        Create a table in the database if it doesn't already exist.

        Parameters
        ----------
        table_name : str
            The name of the table to create.
        columns : str
            The column names and their corresponding data types in SQL syntax.
        """
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.connect.commit()

    def insert_data(self, table, data):
        """
        Insert multiple rows of data into the specified table.

        Parameters
        ----------
        table : str
            The name of the table where the data will be inserted.
        data : list of tuple
            A list of tuples, where each tuple contains a row of data to insert into the table.
        """
        placeholders = ', '.join(['?'] * len(data[0]))
        sql = f"INSERT OR IGNORE INTO {table} VALUES ({placeholders})"
        self.cursor.executemany(sql, data)
        self.connect.commit()

    def select_data(self, table, columns):
        """
        Select and retrieve data from a specified table.

        Parameters
        ----------
        table : str
            The name of the table from which to retrieve the data.
        columns : str
            A string representing the column names to select, e.g., '*', or specific column names.

        Returns
        -------
        list of tuple
            A list of tuples where each tuple represents a row from the result of the query.
        """
        sql = f"SELECT {columns} FROM {table}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        """
        Close the database connection.
        """
        self.connect.close()
