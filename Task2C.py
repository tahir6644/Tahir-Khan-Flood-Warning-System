from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Put code here that demonstrates functionality

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    for i in stations_highest_rel_level(stations, 10):
        print(f'{i.name} {i.relative_water_level()}')



if __name__ == "__main__":
    run()
