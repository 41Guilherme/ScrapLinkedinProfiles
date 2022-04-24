from scrap_profiles import scrap_profiles
import numpy as np
import pandas as pd
import time as t

if __name__ == "__main__":
    
    CARGOS   = ['CEO', 'CFO', 'DIRETOR']
    EMPRESAS = list(np.loadtxt('interprizes.txt', dtype=str, delimiter='\n'))
    
    for EMPRESA in EMPRESAS:
    
        scrap = scrap_profiles(EMPRESA,CARGOS)
        print("Sleeping...")
        t.sleep(10)
        print("Scraping...")
        
        urls = scrap.get_urls()

        dictionary = {
            "ID"       : [i for i in range(1,len(urls)+1)],
            "Profiles" : scrap.get_profiles_results(),
            "Url"      : urls,
        }
        
        try:
            df = pd.DataFrame(dictionary)
            print("----------------------------------------------------")
            print(df)
            print("----------------------------------------------------")
            t.sleep(3)
            df.to_csv(f"{EMPRESA}.csv", encoding="utf-8",index=False)
        except:
            continue
        
    

     
    # Teste = scrap_profiles(EMPRESA, CARGOS)
    # print(Teste.get_urls())
    # DB.insertItem(1,'Teste','teste.com','Teste S.A.')
    
    