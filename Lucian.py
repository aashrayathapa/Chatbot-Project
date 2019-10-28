import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if message.content == "!Hi":
        await message.channel.send("Hello")

client.run("bot token has been removed")
  
    
    
#create database for barry's accounts
import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn
 
 
def create_table(conn, create_table_sql):
    """ create a table from the censored statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 
 
def main():
    database = r"C:\sqlite\db\barry.db"
 
    sql_create_censoredacc_table = """ CREATE TABLE IF NOT EXISTS censored (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL,
                                        email text
                                    ); """
 
    sql_create_uncensoredacc_table = """ CREATE TABLE IF NOT EXISTS uncensored (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL,
                                        email text
                                    ); """

    conn = create_connection(database)
 
    if conn is not None:
        create_table(conn, sql_create_censoredacc_table)
        create_table(conn, sql_create_uncensoredacc_table)
    else:
        print("Error! cannot create the database connection.")
 
if __name__ == '__main__':
    main()
#introduce values into the database


