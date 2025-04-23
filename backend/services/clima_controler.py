import requests
from backend.utils.helpers import get_key_api
from backend.app.cache import cache
key=get_key_api()

@cache.memoize(timeout=3600)
def make_request(location:str,date1=None,date2=None)-> dict:
    print("⛅ Llamando a la API externa (NO caché)")
    base_url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}"
    if date1:
        if date2:
            url = f"{base_url}/{date1}/{date2}?key={key}"
        
        else:
            url = f"{base_url}/{date1}?key={key}"
    
    else:
        url = f"{base_url}?key={key}"
   
        
    response=requests.get(url)

    if response.status_code == 200:
        data=response.json()


        return data
    else:
        print(f"Error: {response.status_code}")