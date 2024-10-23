import requests

def availableShips(passenger_count):
    url = 'https://swapi-api.alx-tools.com/api/starships'
    ships_list = []
    
    while url:
        r = requests.get(url)
        data = r.json()
        ships = data['results']
        
        for ship in ships:
            try:
                if int(ship['passengers']) >= passenger_count:
                    ships_list.append(ship['name'])
            except ValueError:
                continue
        
        url = data['next']
    
    return ships_list