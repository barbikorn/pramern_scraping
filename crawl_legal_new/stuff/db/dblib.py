#!/usr/bin/python
from configparser import RawConfigParser
import psycopg2

######
#   read section of ini file to dictionary
#   error return NULL
######
def readIni(filename, section):
    # create a parser
    parser = RawConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    dict_ = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            dict_[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        dict_ = None

    return dict_

def connectDb( iniFileName , section ):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = readIni( iniFileName , section )
        if params is None :
            raise Exception( "File " + iniFileName + " not found section " + section )

        # connect to the PostgreSQL server
        #print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn 


if __name__ == '__main__':
    params = readIni( "database.ini" , "postgresql") 
    if params is not None :
        print( params )
        conn = connectDb( "database.ini" , "postgresql")
        if conn is not None :
            print( "Connection success")
            conn.close()
            
