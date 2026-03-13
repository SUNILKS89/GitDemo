import configparser
import os

import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "properties.ini")
    config.read(config_path)
    #config.read("../Utils/properties.ini")
    return config

dbconnect_config={
    'user':get_config()['SQL']['user'],
    'password':get_config()['SQL']['password'],
    'host':get_config()['SQL']['host'],
    'database':get_config()['SQL']['database']
}
def get_dbconnection():
    try:
        conn = mysql.connector.connect(**dbconnect_config)
        if conn.is_connected():
            print("connection successful")
            return conn
    except Error as e:
        print(e)

def get_query(query):
    conn = get_dbconnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row