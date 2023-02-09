from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    # Put code here that demonstrates functionality
    
    print(rivers_by_station_number(build_station_list(), 9)) # We require N = 9
    


if __name__ == "__main__":
    run()