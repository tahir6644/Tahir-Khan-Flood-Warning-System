from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Put code here that demonstrates functionality

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    for i in stations_level_over_threshold(stations, 0.8):
        print(f'{i[0].name} {i[1]}')
    print('\n\n')
    
    # "Explore your implementation for different tolerances."
    # To see the stations which have high relative water levels
    # i.e. tol = 1.0, 1.2 and 1.5 

    print('*** RWL > 1.0 ***')
    for i in stations_level_over_threshold(stations, 1.0):
        print(f'{i[0].name} {i[1]}')
    print('\n\n')

    print('*** RWL > 1.2 ***')
    for i in stations_level_over_threshold(stations, 1.2):
        print(f'{i[0].name} {i[1]}')
    print('\n\n')

    print('*** RWL > 1.5 ***')
    for i in stations_level_over_threshold(stations, 1.5):
        print(f'{i[0].name} {i[1]}')



if __name__ == "__main__":
    run()
