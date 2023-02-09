from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    # Put code here that demonstrates functionality
    
    erroneous_stations = inconsistent_typical_range_stations(build_station_list())
    print(sorted([i.name for i in erroneous_stations]))



if __name__ == "__main__":
    run()