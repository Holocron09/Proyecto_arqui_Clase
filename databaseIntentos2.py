import psycopg2
from psycopg2 import Error
def Database():
    try:
        connection=psycopg2.connect(user="pi", password="raspberry",host="127.0.0.1",port="5432",database="pi")
        cursor=connection.cursor()
        try:
            createTableQuery='''Create TABLE IF NOT EXISTS alumnos
                (ID SERIAL  PRIMARY KEY,
                NOMBRE          TEXT    NOT NULL,
                CARRERA         TEXT   NOT NULL);'''
            cursor.execute(createTableQuery)
            connection.commit()
            print('Table created successfully in PostgresSQL')
        except:
            print('Table already created')
        
        try:
            nombre=["Juan1","Pedro1","Alan1","Arti"]
            carrera=["Elec","Meca","Elec","Ind"]
            for i in range(0,4):
                addTableQuerry="INSERT INTO alumnos (nombre,carrera) VALUES (\'%s\',\'%s\');" %(nombre[i],carrera[i])
                print(addTableQuerry)
                cursor.execute(addTableQuerry)
                connection.commit()
            print("Data added successfully")
        except:
            print("Data could not be added")
    except(Exception,psycopg2.DatabaseError)as error:
        print('Error while creating PostgresSQL table', error)
    finally:
        #closing database connection
        if (connection):
            cursor.close()
            connection.close()
            print("PostgresSQL connection is closed")

Database()