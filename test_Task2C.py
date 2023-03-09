from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
import math

def test_stations_highest_rel_level():
    # Stations 0, 1, 2, 3 have RWLs 0.667, 0, 1, 0.75 respectively.
    # So expected output for N=3 is [station_2, station_3, station_0]


    i = 0
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
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
    t_range = (3, 12)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_2 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    station_2.latest_level = 12

    i = 3
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    t_range = (1, 5)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_3 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    station_3.latest_level = 4

    stations = [station_0, station_1, station_2, station_3]
    result = stations_highest_rel_level(stations, 3)
    expected_list = [station_2, station_3, station_0]

    assert(result == expected_list)
