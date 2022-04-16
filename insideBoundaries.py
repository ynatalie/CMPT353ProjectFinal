import pandas as pd
import json
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def get_coords(bound):
    coor = bound["coordinates"][0]
    return coor


def assignNeighbourhood(a, n):
    for neighbourhood, boundary in n.items():
        if a.within(boundary):
            return neighbourhood
    return None

def main():
    bound = pd.read_csv('alldatafile/local-area-boundary.csv', sep=';')
    poly = bound["Geom"].apply(json.loads)
    poly = poly.apply(get_coords)
    poly = poly.apply(Polygon)

    boundaries = pd.DataFrame(bound['Name'])
    boundaries['Poly'] = poly
    boundaries.set_index('Name', inplace=True)
    boundaries = boundaries.squeeze()

    #food
    food = pd.read_csv("alldatafile/food_amenities.csv")
    food_coords = pd.Series(zip(food.iloc[:,4],food.iloc[:,3]))
    food_coords = food_coords.apply(Point)
    food["neighbourhood"] = food_coords.apply(assignNeighbourhood, n =boundaries)
    food = food[food["neighbourhood"].notnull()]
    food = food[["name","amenity","lat","lon","neighbourhood"]]
    food.to_csv("alldatafile/foodClean.csv")

    #entertaintment
    ent = pd.read_csv("alldatafile/ent_amenities.csv")
    ent_coords = pd.Series(zip(ent.iloc[:, 4], ent.iloc[:, 3]))
    ent_coords = ent_coords.apply(Point)

    ent["neighbourhood"] = ent_coords.apply(assignNeighbourhood, n=boundaries)
    ent = ent[ent["neighbourhood"].notnull()]
    ent = ent[["name", "amenity", "lat", "lon", "neighbourhood"]]
    ent.to_csv("alldatafile/entClean.csv")

    #art
    arts = pd.read_csv("alldatafile/arts_amenities.csv")
    arts_coords = pd.Series(zip(arts.iloc[:, 4], arts.iloc[:, 3]))
    arts_coords = arts_coords.apply(Point)

    arts["neighbourhood"] = arts_coords.apply(assignNeighbourhood, n=boundaries)
    arts = arts[arts["neighbourhood"].notnull()]
    arts = arts[["name", "amenity", "lat", "lon", "neighbourhood"]]
    arts.to_csv("alldatafile/artsClean.csv")

    #religion
    reli = pd.read_csv("alldatafile/reli_amenities.csv")
    reli_coords = pd.Series(zip(reli.iloc[:, 4], reli.iloc[:, 3]))
    reli_coords = reli_coords.apply(Point)

    reli["neighbourhood"] = reli_coords.apply(assignNeighbourhood, n=boundaries)
    reli = reli[reli["neighbourhood"].notnull()]
    reli = reli[["name", "amenity", "lat", "lon", "neighbourhood"]]
    reli.to_csv("alldatafile/reliClean.csv")

    #nightlife
    night = pd.read_csv("alldatafile/night_amenities.csv")
    night_coords = pd.Series(zip(night.iloc[:, 4], night.iloc[:, 3]))
    night_coords = night_coords.apply(Point)

    night["neighbourhood"] = night_coords.apply(assignNeighbourhood, n=boundaries)
    night = night[night["neighbourhood"].notnull()]
    night = night[["name", "amenity", "lat", "lon", "neighbourhood"]]
    night.to_csv("alldatafile/nightClean.csv")

    #transportation
    trans = pd.read_csv("alldatafile/transportRent_amenities.csv")
    trans_coords = pd.Series(zip(trans.iloc[:, 4], trans.iloc[:, 3]))
    trans_coords = trans_coords.apply(Point)

    trans["neighbourhood"] = trans_coords.apply(assignNeighbourhood, n=boundaries)
    trans = trans[trans["neighbourhood"].notnull()]
    trans = trans[["name", "amenity", "lat", "lon", "neighbourhood"]]
    trans.to_csv("alldatafile/transClean.csv")


if __name__ == '__main__':
    main()


