import psycopg2
import dblib


class Crud :


    def __init__(self,conn , tableName ):
        self.conn = conn
        all_template = dblib.readIni( "ini/table.ini" , tableName )
        self.select_by_id_template = all_template['select_by_id_template']
        self.select_by_condition_template = all_template['select_by_condition_template']
        self.insert_template = all_template['insert_template']
        self.update_template  = all_template['update_template'] 
        self.delete_template = all_template['delete_template'] 
        self.clear_template = all_template['clear_template'] 

    def get( self,id  ) :
        cur = self.conn.cursor()
        cur.execute(self.select_by_id_template , (id,))
        record = cur.fetchone()
        return record 

    def gets( self , condition , record ):
        cur = self.conn.cursor()
        sql = self.select_by_condition_template + " where " + condition 
        cur.execute( sql  ,record ) 
        records = cur.fetchall()
        return records 


    def insert( self, record ) :
        cur = self.conn.cursor()
        cur.execute(self.insert_template , record )
        self.conn.commit()
        try :
            id = cur.fetchone()[0]
            return id 
        except :
            return 0


    def update(self , record):
        cur = self.conn.cursor()
        cur.execute(self.update_template, record)
        self.conn.commit()
        return cur.rowcount == 1

    def delete(self ,  id):
        cur = self.conn.cursor()
        cur.execute(self.delete_template,(id,))
        self.conn.commit
        return cur.rowcount == 1

    def clear(self):
        cur = self.conn.cursor()
        cur.execute(self.clear_template)
        self.conn.commit
        print('table cleared')
        return True 


if __name__ == '__main__':
    conn = dblib.connectDb( "database.ini" , "postgresql")
    person = Crud( conn , 'person')
    record = person.get( 1 )
    print( record )

    records = person.gets( "name = %s" , ( 'supakit' , ))
    print( records )

    id = person.insert( ( "john"  , 27 ))
    print( person.get( id ))

    if person.update( ( "john 1"  , 40  , id ) ) : 
        print( person.get( id ))
    else :
        print( "Error update record")

    print( "Success " if person.delete( id ) else "Error"  , "DELETE")
"""
    if person.delete( id ) :
        print( "Success")
    else :
        print( "Error")
    print( "DELETE")
"""