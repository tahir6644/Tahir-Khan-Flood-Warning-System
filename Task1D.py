from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    # Put code here that demonstrates functionality
    
    # sorted() ensures the river strings are in alphabetical order in the set.
    rivers_set = sorted(rivers_with_station(build_station_list()))
    print(f'There are {len(rivers_set)} rivers with at least one station. \n')
    print(f'The first 10 are {rivers_set[:10]} \n')

    rivers_stations = stations_by_river(build_station_list())
    
    print(f'The stations on the River Aire are: {sorted(i.name for i in rivers_stations["River Aire"])} \n')
    print(f'The stations on the River Cam are: {sorted(i.name for i in rivers_stations["River Cam"])} \n')
    print(f'The stations on the River Thames are: {sorted(i.name for i in rivers_stations["River Thames"])} \n')



if __name__ == "__main__":
    run()