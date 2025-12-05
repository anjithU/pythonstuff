import httpx
import geocoder
from math import radians, sin, cos, sqrt, atan2
import prettytable

# user location


def location():
    geo_location_details = geocoder.ipinfo('me')
    ip = geo_location_details.ip
    lat =geo_location_details.latlng[0]
    long = geo_location_details.latlng[1]
    print(f"Your ip address is  { ip} , lattitude {lat} & longitude {long}")
    
    return [lat,long]



# function comparing distance


def distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c



# function url


def fetch_with_auth():
    url = "https://opensky-network.org/api/states/all"
    response = httpx.get(url)
    data = response.json()
    states = data["states"]
    return states


# comparison



def comparison(list_of_states ,latitude,longitude):
    near_by_flights = []
    
    
    for i in list_of_states:
        lat = i[6]
        lon = i[5]
        if lat and lon:
            d = distance(lat,lon,latitude,longitude)
        if d<50:
            near_by_flights.append((i[2], d))
    
    
    print(near_by_flights)



if __name__ == "__main__":
    my_location_variables = location()
    print(my_location_variables[0])
    state_list = fetch_with_auth()
    comparison(state_list,latitude=my_location_variables[0],longitude=my_location_variables[1])

    


