#! python
import MySQLdb
from getpass import getpass
from mysql.connector import connect, Error

def Main():
	#conn = MySQLdb.connect('localhost', 'roman', 'jdgaa1111')
	#cursor = conn.cursor()

	#cursor.execute("CREATE DATABASE STS database_db")

	#row = cursor.fetchone()
	#print(row)

    try:
        with connect(
                host = 'localhost',
                user = input("Enter user name: "),
                password = getpass("Enter password: "),
        ) as connection:
            use_db_query = "use test_database_db"
            with connection.cursor() as cursor:
                cursor.execute(use_db_query)

            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                print("--show database--")
                for db in cursor:
                    print(db)

            show_table_query = "SHOW TABLES"
            with connection.cursor() as cursor:
                cursor.execute(show_table_query)
                print("--show tables--")
                for db in cursor:
                    print(type(cursor))
                    print(type(db))
                    print(db)


    except Error as e:
        print(e)


if __name__ == '__main__':
    Main()

