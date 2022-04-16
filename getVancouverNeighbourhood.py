#learning website

import googlemaps
import pandas as pd
import numpy as np


def gettingLocation(loc,gmaps):
    location = loc + "British Columbia"
    result = gmaps.geocode(location)
    lat = result[0]['geometry']['location']['lat']
    lon = result[0]['geometry']['location']['lng']

    return (lat, lon)

def main():
    # private API key
    gmaps = googlemaps.Client(key='')

    #names of neighbourhood
    places = ["Arbutus Ridge","Downtown","Dunbar-Southlands","Fairview","Grandview-Woodland",
              "Hastings-Sunrise","Kensington-Cedar Cottage","Kerrisdale","Killarney",
              "Kitsilano","Marpole","Mount Pleasant","Oakridge","Renfrew-Collingwood",
              "Riley Park","Shaughnessy","South Cambie","Strathcona","Sunset","Victoria-Fraserview",
              "West End","West Point Grey"]
    places_func = np.vectorize(gettingLocation)
    lat_lons = places_func(places, gmaps)

    van_places = pd.DataFrame(data={"Places name": places, 'lat': lat_lons[0], 'lon': lat_lons[1]})

    van_places.to_csv("alldatafile/van_placesData.csv")


if __name__ == '__main__':
    main()