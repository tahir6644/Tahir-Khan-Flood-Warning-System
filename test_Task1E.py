

from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number():

    list_of_stations = []
    no_of_stations = 10
    no_of_rivers = 3
    N = 2
   
    # river_0 has 1 station
    # river_1 has 2 stations
    # river_2 has 3 stations

    for j in range(no_of_rivers):
        for i in range (j+1):  
            # j = 0, i = 0
            # j = 1, i = 0-1
            # j = 2, i = 0-2   
            s_id = 's_id'+ str(i)
            m_id = 'm_id' + str(i)
            name = 'name_'+ str(i)
            coord = (i, i)
            t_range = (i, i)
            river = 'river_'+ str(j)
            town = 'town_' + str(i)
            station = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
            list_of_stations.append(station)

    ans_list = rivers_by_station_number(list_of_stations, N)

    assert(ans_list == [('river_2', 3), ('river_1',2)])



        