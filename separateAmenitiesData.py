
import numpy as np
import pandas as pd
import json

def main():
    df = pd.read_json('alldatafile/amenities-vancouver.json', lines=True)
    df = df[["name","amenity","lat","lon"]]

    # food related places: cafe, fast_food, bbq, pub, bar, food_court, ice_cream, vending_machine
    # bistro, disused:restaurant, biergarten,juice_bar,internet_cafe
    food = ["cafe","fast_food","bbq","pub","bar","food_court","ice_cream","vending_machine",
        "bistro","disused:restaurant","biergarten","juice_bar","internet_cafe"]
    df1 = df[df["amenity"].isin(food)]
    df1.to_csv("alldatafile/food_amenities.csv")


    # transportation rental :
    # boat_rental, car_rental, car_sharing, bicycle_rental, seaplane termal, taxi,
    # motorcycle_rental
    transportation = ["boat_rental","car_rental","car_sharing","bicycle_rental",
                  "seaplane terminal","taxi","motorcycle_rental","charging_station", "fuel"]
    df2 = df[df["amenity"].isin(transportation)]
    df2.to_csv("alldatafile/transportRent_amenities.csv")

    # entertaintment :
    # public_bookcase, university, fountain, photo_booth,
    # spa, marketplace, clock, internet_cafe, park, leisure, cinema, theather, arts_centre, library
    # pub, bar, nightclub, stripclub, gambling, casino
    places = ["university","fountain","photo_booth",
          "spa","marketplace","clock","internet_cafe","park","leisure"]
    df3 = df[df["amenity"].isin(places)]
    df3.to_csv("alldatafile/ent_amenities.csv")

    #nightlife:
    night = ["pub", "bar","nightclub","stripclub","gambling","casino","nightclub","stripclub","gambling","casino"]
    df4 = df[df["amenity"].isin(night)]
    df4.to_csv("alldatafile/night_amenities.csv")

    # arts:
    arts = ["cinema","theather","arts_centre","library","public_bookcase"]
    df5 = df[df["amenity"].isin(arts)]
    df5.to_csv("alldatafile/arts_amenities.csv")

    #religious:
    reli = ["meditation_centre", "monastery", "place_of_worship",]
    df6 = df[df["amenity"].isin(reli)]
    df6.to_csv("alldatafile/reli_amenities.csv")

if __name__ == '__main__':
    main()
