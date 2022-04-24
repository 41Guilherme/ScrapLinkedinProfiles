import mysql.connector
from configparser import ConfigParser


config = ConfigParser()
config.read('auth.ini')

host  = config['auth']['host']
db    = config['auth']['db']
user  = config['auth']['user']
passw = config['auth']['passw']

class Query():
    
    def __init__(self, host, db, user, passw):
        self.con = mysql.connector.connect(host=host,
                                           database=db,
                                           user=user,
                                           password=passw)
        
    def insert_item(self, id : int, label : str, url : str, table: str):
        if self.con.is_connected:
            cursor = self.con.cursor()
            cursor.execute(f"INSERT INTO {table}(ID, Profiles,Urls ) VALUES ('{id}','{label}','{url}') ")
            self.con.commit()
            cursor.close()
            print(f"{table} - {id} INSERIDO")
            return True
        else:
            print("NOT NOICE YOUR PIECE OF SHIT")
            return False
    
    def get_all_data(self, table : str):
        if self.con.is_connected():
            cursor = self.con.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            data = []
            for item in cursor:
                data.append({
                    "ID"           : item[0],
                    "Profile_Label": item[1],
                    "Profile_Url"  : item[2],

                })
                
            cursor.close()
            return data
        else:
            return None
        
    def get_specific_item(self, table : str, ID : int):
        if self.con.is_connected():
            cursor = self.con.cursor()
            cursor.execute(f""" SELECT * FROM {table} WHERE ID = "{ID}" """)
            data = []
            for item in cursor:
                data.append({
                    "ID"           : item[0],
                    "Profile_Label": item[1],
                    "Profile_Url"  : item[2],
                    "Interprize"   : item[3]
                })
            cursor.close()
            return data
        return None
    
    def delete_especific_item(self, id : int):
        if self.con.is_connected:
            cursor = self.con.cursor()
            cursor.execute(f"DELETE FROM profiles WHERE ID = {id}")
            self.con.commit()
            cursor.close()
            return True
    
        return False
    

    
DB = Query(host,db,user,passw)


    
    
    