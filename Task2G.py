from floodsystem.geo import stations_by_town
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    towns_stations = stations_by_town(stations)
    
    # To find mean RWL for the stations around each town:
    towns_mean_rwl = {}
    
    # # To find how quickly water level is increasing:
    # towns_slope = {}
    # dt = 2   # Poly fit line is based on 2 days' history
    # p = 1 # Degree 1 polynomial fit
    
    for town, stations_list in towns_stations.items():
        total_rwl = 0
        # total_slope = 0
        count = 0
        for station in stations_list:
            # Don't count erroneous stations
            if station.relative_water_level():
                total_rwl += station.relative_water_level()
                
                # # To find slope
                # dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=dt))
                # poly, d0, final_slope = polyfit(dates, levels, p)
                # total_slope += final_slope

                count += 1
        # Avoid division by zero error
        if count == 0:
            mean_rwl = 0
            # mean_slope = 0
        else:
            mean_rwl = total_rwl/count
            # mean_slope = total_slope/count
        towns_mean_rwl[town] = mean_rwl
        # towns_slope[town] = mean_slope


    # Create sorted list of (town, mean_rwl) tuples by mean_rwl in ascending order
    towns_mean_rwl = sorted(towns_mean_rwl.items(), key=lambda x:x[1])
    # towns_slope = sorted(towns_slope.items(), key=lambda x:x[1])

    # Consider ranks from both mean_rwl and slope of poly fit line.
    # towns_rank = {}
    # for i in towns_mean_rwl:
    #     towns_rank[i[0]] = towns_mean_rwl.index(i)
    # for i in towns_slope:
    #     towns_rank[i[0]] += towns_slope.index(i)

    severe_towns = [i[0] for i in towns_mean_rwl[-5:]]
    high_towns = [i[0] for i in towns_mean_rwl[-10:-5]]
    moderate_towns = [i[0] for i in towns_mean_rwl[-20:-10]]
    low_towns = [i[0] for i in towns_mean_rwl[-30:-20]]

    print(f'Towns at severe risk: {severe_towns}')
    print('\n')
    print(f'Towns at high risk: {high_towns}')
    print('\n')
    print(f'Towns at moderate risk: {moderate_towns}')
    print('\n')
    print(f'Towns at low risk: {low_towns}')


if __name__ == "__main__":
    run()