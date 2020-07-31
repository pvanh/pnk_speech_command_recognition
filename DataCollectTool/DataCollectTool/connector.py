import mysql.connector
import pyaudio

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="krifferson",
    database="record_sentences"
)

