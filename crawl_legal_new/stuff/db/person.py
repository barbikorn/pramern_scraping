from crud import Crud

conn = dblib.connectDb( "ini/database.ini" , "postgresql")

person = Crud( conn , 'person')
customer = Crud( conn , 'customer')
