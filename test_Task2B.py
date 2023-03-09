from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
import math


def test_relative_water_level():

    i = 0
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    # Artifical range
    t_range = (5, 20)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_0 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    station_0.latest_level = 15
    assert(math.isclose(station_0.relative_water_level, 2/3))

    i = 1
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    # Artifical range
    t_range = (2, 7)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_1 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    station_1.latest_level = 2
    assert(math.isclose(station_1.relative_water_level, 0))

    i = 2
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    # Artifical range
    t_range = (3, 12)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_2 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    station_2.latest_level = 12
    assert(math.isclose(station_2.relative_water_level, 1))


def test_stations_level_over_threshold():
    # Define stations 0 and 2 as having a level 
    # over tol so station 1 shouldn't be included.
    # The stations are the same as before with RWLs
    # of 0.667, 0 and 1 respectively.

    i = 0
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    # Artifical range
    t_range = (5, 20)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_0 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    station_0.latest_level = 15

    i = 1
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    # Artifical range
    t_range = (2, 7)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_1 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    station_1.latest_level = 2

    i = 2
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    # Artifical range
    t_range = (3, 12)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_2 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    station_2.latest_level = 12

    stations = [station_0, station_1, station_2]
    result = stations_level_over_threshold(stations, 0.5)
    expected_list = [(station_2, station_2.relative_water_level), 
                     (station_0, station_0.relative_water_level)
                     ]
    
    assert(result == expected_list)

