#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn 

def select( conn , sql ) :
    cur = conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    return records 

    

def insert( conn , sqlTemplate , record ) :
    cur = conn.cursor()
    cur.execute(sqlTemplate , record )
    conn.commit()


def update(conn , sqlTemplate , record):
    cur = conn.cursor()
    cur.execute(sql_update_query, record)
    conn.commit()

def delete(conn , sqlTemplate, id):
    cur = conn.cursor()
    cur.execute(sqlTemplate,(id,))
    conn.commit


if __name__ == '__main__':
    conn = connect()
    if conn != None :
        insertTemplate = """insert into person( name , age ) values( %s , %s)"""
        record = ( "john" , 23 )
   
        insert( conn , insertTemplate , record )
        

        sql_update_query = """Update person set name = %s ,age = %s where id = %s"""
        update_record = ('manoj',12,7)

        update( conn , sql_update_query,update_record)

        sql_delete_query = """Delete from person where id = %s"""
        delete(conn , sql_delete_query , 9)


        sqlString = "select * from person"
        records = select( conn , sqlString )
        print( records )
    else :
        print("connection error")




    # 		postgreSQL_select_Query = "select * from mobile"
    #     # create a cursor
    #     cur = conn.cursor()
        
	# # execute a statement
    #     print('PostgreSQL database version:')
    #     cur.execute('SELECT version()')

    #     # display the PostgreSQL database server version
    #     db_version = cur.fetchone()
    #     print(db_version)
       
	# # close the communication with the PostgreSQL
    #     cur.close()

        # finally:
        # if conn is not None:
        #     conn.close()
        #     print('Database connection closed.')
