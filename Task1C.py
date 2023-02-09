from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    # Put code here that demonstrates functionality
    
    CambridgeCityCenter = (52.2053, 0.1218)
    stations = [i.name for i in stations_within_radius(build_station_list(), CambridgeCityCenter, 10.0)] # Within 10 km.

    print(sorted(stations)) # sorted() arranges the names in alphabetical order.



if __name__ == "__main__":
    run()

