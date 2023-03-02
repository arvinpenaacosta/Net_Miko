
import sqlite3

conn = sqlite3.connect('epmap.db', check_same_thread=False)
#conn = sqlite3.connect('mngr.dat', check_same_thread=False)
#conn = sqlite3.connect('floormap.dat', check_same_thread=False)
cur = conn.cursor()

def initialize_db(): 
    cur.execute('''
    CREATE TABLE IF NOT EXISTS mapping(id integer primary key autoincrement,station,port,interface,floor,info1,info2)    
    
    ''')

    #CREATE TABLE IF NOT EXISTS transactions(id integer primary key autoincrement,station,port,interface,floor,user,timedone,transtype)
    

def close_db():
    conn.close()

def create_pass(service, handle, password):
    try: 
        cur.execute('''
            INSERT INTO mapping(service, handle, password)
            VALUES(?, ?, ?)
            ''', (service, handle, password))
        conn.commit()
        return 0
    except:
        return 1


def log_transaction(station, port, interface, floor, user, timedone, transtype):
    try: 
        cur.execute('''
            INSERT INTO transactions(station, port, interface, floor, user, timedone, transtype)
            VALUES(?, ?, ?, ?, ?, ?, ?)
            ''', (station, port, interface, floor, user, timedone, transtype))
        conn.commit()
        return 0
    except:
        return 1




#def update_data(my_id, station, port, interface,floor, info1, info2):
def update_data(my_id, station, port, interface, floor, info1, info2):
    print(f"\n<UPDATE>:  {my_id}, {station}, {port}, {interface}, {floor}, {info1}, {info2}\n")
    try:
        cur.execute("""
        UPDATE mapping SET station = ? , port = ?, interface = ?, floor = ?, info1 = ?, info2 = ?
        WHERE id = ?;
        """, (station , port, interface ,floor , info1, info2, my_id))
        conn.commit()

        

        return 0
    except Exception as e:
        print(e)

     
def delete_pass(id):
    try:
        cur.execute('''
        DELETE FROM mapping
        WHERE id = ?;
        '''), (id)
        conn.commit()
        return 0
    except:
        return 1





def get_all():
    cur.execute('''SELECT * FROM mapping''')
    return cur.fetchall()




def get_by_service(service):

    service = "%" + service + "%"
    cur.execute(
        '''
        SELECT * FROM mapping
        WHERE service LIKE ?
        ''',
    (service,)
    )
    return cur.fetchall()




# searching here
def get_by_handle(handle):
    
    #handle = "%" + handle + "%"
    print(f"<db.py>  {handle}")
    cur.execute(
        '''
        SELECT * FROM mapping
        WHERE station LIKE ?
        ''', (handle,)
    )
    return cur.fetchall()



def get_by_id(id):
    cur.execute(
        '''
        SELECT * FROM mapping
        WHERE id = ?
        ''', (str(id),)
        )
    return cur.fetchone()
