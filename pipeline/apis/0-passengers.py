#!/usr/bin/env python3
import requests

def availableShips(passenger_count):
    """
    Returns a list of starships that can hold at least `passenger_count` passengers.
    
    Args:
        passenger_count (int): The minimum number of passengers the starship must hold.
    
    Returns:
        list: A list of starship names that meet the passenger count criteria.
    """
    url = 'https://swapi-api.alx-tools.com/api/starships'
    ships_list = []
    
    while url:
        r = requests.get(url)
        data = r.json()
        ships = data['results']
        
        for ship in ships:
            try:
                passengers = int(ship['passengers'].replace(',', ''))
                if passengers >= passenger_count:
                    ships_list.append(ship['name'])
            except ValueError:
                continue
        
        url = data['next']
    
    return ships_list

# Test the function
if __name__ == "__main__":
    ships = availableShips(4)
    for ship in ships:
        print(ship)