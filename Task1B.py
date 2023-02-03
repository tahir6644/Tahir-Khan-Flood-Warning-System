from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    CambridgeCityCenter = (52.2053, 0.1218)   
    stations = stations_by_distance(build_station_list(), CambridgeCityCenter)
    
    closest_stations = []
    for station in stations[:10]:
        closest_stations.append((station[0].name, station[0].town, station[1]))


    furthest_stations = []
    for station in stations[-10:]:
        furthest_stations.append((station[0].name, station[0].town, station[1]))
    
    print(f'The closest 10 entries are {closest_stations}\n')
    print(f'The furthest 10 entries are {furthest_stations}\n')
    



if __name__ == "__main__":
    run()