import psycopg2
from config import config
from table_config import table_config



class Crud :


    def __init__(self,conn ,all_template):
        self.conn = conn
        self.select_by_id_template = all_template['select_by_id_template']
        self.select_by_condition_template = all_template['select_by_condition_template']
        self.insert_template = all_template['insert_template']
        self.update_templte  = all_template['update_templte'] 
        self.delet_template = all_template['delete_template'] 


    def select_by_id( self,id  ) :
        cur = self.conn.cursor()
        cur.execute(self.select_by_id_template , (id,))
        record = cur.fetchone()
        return record 

    def select( self , record ):
        cur = self.conn.cursor()
        cur.execute(self.select_by_condition_template ,record ) 
        records = cur.fetchall()
        return records 


    def insert( self,sqlTemplate , record ) :
        cur = self.conn.cursor()
        cur.execute(self.insert_template , record )
        conn.commit()


    def update(self , sqlTemplate , record):
        cur = self.conn.cursor()
        cur.execute(self.update_template, record)
        conn.commit()

    def delete(self ,  id):
        cur = self.conn.cursor()
        cur.execute(self_delete_template,(id,))
        conn.commit

if __name__ == '__main__':

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

    def read_table_template():
        templates = table_config()
        return templates



    conn = connect() 
    all_template = read_table_template()
    # print(all_template)
    # select_by_id_template = """select * from person where id = %s"""
    # select_by_condition = """select * from person where name = %s"""
    # insert_template = """insert into person( name , age ) values( %s , %s)"""
    # update_templte = """Update person set name = %s ,age = %s where id = %s"""
    # delete_template = """Delete from person where id = %s"""

    crud = Crud( conn , all_template)

# select ,delete use only id
#insert record (id,value,value)
#update record(price,id)????
#other use record
    record  = crud.select_by_id( 1 ) 
    print( record ) 

