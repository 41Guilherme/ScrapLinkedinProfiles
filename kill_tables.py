from db import DB
import numpy as np


EMPRESAS = list(np.loadtxt('interprizes.txt', dtype=str, delimiter='\n'))
cursor = DB.con.cursor()

for EMPRESA in EMPRESAS:
    try:
        cursor.execute(f"DROP TABLE {EMPRESA}")
        DB.con.commit()
    except:
        continue
cursor.close()
    
