import requests
from bs4 import BeautifulSoup

class scrap_profiles():
    
    def __init__(self, interprize : str, roles : list):
        self.url  = self.create_url(interprize= interprize , roles=roles)
        self.html = self.get_html(self.url)
    
    @staticmethod
    def create_url(interprize : str, roles : list) -> str:
        BASE_URL = "https://www.google.com.br/search?q="
        roles_str = " OR ".join(roles)
        url = BASE_URL + (f"{interprize} {roles_str} site:linkedin.com").replace(" ", "+")
        return url
    
    @staticmethod
    def get_html(url: str) -> BeautifulSoup:
        resp = requests.get(url)
        doc = BeautifulSoup(resp.text ,"html.parser")
        return doc

    def get_urls(self) -> list:
        results_links = self.html.select('div div div a')
        urls = []
        for result in results_links:
            aux = str(result).find('href="/url?q=https://br.linkedin.com/in')
            
            if aux != -1:
                newItem = str(result).replace('<a href="/url?q=','')
                aux = newItem.find('&amp;')
                data = []
                for i in range(aux):
                    data.append(newItem[i])
                url = ''.join(data)
                urls.append(url)
            
        return urls

    def get_profiles_results(self) -> list:
        results_labels = self.html.select('div div div h3')
        profiles = []
        for item in results_labels:
            doc = BeautifulSoup(str(item), 'html.parser')
            
            aux = doc.select('div')
            newItem = str(aux[0])
            aux2 = newItem.find(">")
            
            data = []
            for i in range(int(aux2),len(newItem) -6): 
                value = str(newItem[i]).replace(">",'')
                data.append(value)
                
            profile = ''.join(data)
            profiles.append(profile)
            
        return profiles