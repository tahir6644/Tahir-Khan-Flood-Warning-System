from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    dt = 2

    risky_stations = stations_highest_rel_level(stations, 5)
    for i in risky_stations:
        dates, levels = fetch_measure_levels(i.measure_id, dt = datetime.timedelta(days=dt))
        plot_water_level_with_fit(i, dates, levels, p=4)



if __name__ == "__main__":
    run()
