from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    # Put code here that demonstrates functionality
    
    CamCityCentre = (52.2053, 0.1218)

    # List of all (station, distance) tuples where distance is 
    # measured from CamCityCentre.
    stations_distances = stations_by_distance(build_station_list(), CamCityCentre)

    # We require a list of (name, town, distance) tuples instead of (station, distance).
    names_towns_distances = [] 
    for i in stations_distances:
        names_towns_distances.append((i[0].name, i[0].town, i[1]))

    closest_stations = names_towns_distances[:10]
    furthest_stations = names_towns_distances[-10:]
    
    print(f'The closest 10 stations are {closest_stations} \n')
    print(f'The furthest 10 stations are {furthest_stations} \n')

    
if __name__ == "__main__":
    run()

