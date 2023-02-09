from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    # Put code here that demonstrates functionality
    
    rivers_set = rivers_with_station(build_station_list)
    print(f'There are {len(rivers_set)} rivers with at least one station.\n')
    



if __name__ == "__main__":
    run()