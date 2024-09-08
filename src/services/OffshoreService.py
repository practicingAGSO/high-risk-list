import requests
from bs4 import BeautifulSoup
from src.models.OffshoreElementModel import OffshoreElement
from src.models.ResponseModel import Response


def get_data_from_offshore_leaks(query):
    url = 'https://offshoreleaks.icij.org/search'
    params = {
        'q': query,
        'c': '',
        'j': '',
        'd': ''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Referer': 'https://offshoreleaks.icij.org/',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    
    elements = []
    total = 0

    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra la tabla de resultados
    table = soup.find('table')

    # Verifica si la tabla existe
    if table:
        rows = table.find_all('tr')[1:]  

        for row in rows:
            columns = row.find_all('td')
            data = [col.get_text(strip=True) for col in columns]
            element = OffshoreElement(
                entity=data[0],         
                jurisdiction=data[1],      
                linkedTo=data[2],        
                dataFrom=data[3],      
            )
            elements.append(element)
    else:
        print("No se encontró ninguna tabla.")
    
    rsp = Response(total=len(elements), data=elements)
    return rsp

