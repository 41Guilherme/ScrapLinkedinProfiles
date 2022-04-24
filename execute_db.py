import pandas as pd
import numpy as np
from db import DB


if __name__ == "__main__":
    
    EMPRESAS = list(np.loadtxt('interprizes.txt', dtype=str, delimiter='\n'))
    
    for EMPRESA in EMPRESAS:
        try:
            file = pd.read_csv(f"{EMPRESA}.csv")
            df   = pd.DataFrame(file)
        except:
            continue
        
        cursor = DB.con.cursor()
        cursor.execute( f"""CREATE TABLE `scrap`.`{EMPRESA}` 
                            (`ID` INT NOT NULL,
                            `Profiles` VARCHAR(300) NOT NULL,
                            `Urls` VARCHAR(150) NOT NULL,
                            PRIMARY KEY (`ID`));
                        """)
        DB.con.commit()
        cursor.close()
        print(f"Tabela {EMPRESA} Criada")
        
        for row in range(len(df)):
            ID      = df.loc[row,['ID']][0]
            PROFILE = df.loc[row,['Profiles']][0]
            URL     = df.loc[row,['Url']][0]
            try:
                DB.insert_item(ID,PROFILE,URL,EMPRESA)
            except:
                continue
        
    
        
        