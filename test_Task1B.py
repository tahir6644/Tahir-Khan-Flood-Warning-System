from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation 
from haversine import haversine
import math

def test_stations_by_distance():
    
    # creating sample data to test
    list_of_stations = []

    no_of_stations = 10
    for i in range(no_of_stations):
        s_id = 's_id'+ str(i)
        m_id = 'm_id' + str(i)
        name = 'name_'+ str(i)
        coord = (i, i)
        t_range = (i, i)
        river = 'river_'+ str(i)
        town = 'town_' + str(i)
        station = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
        list_of_stations.append(station)

    test_coord = (no_of_stations + 20, no_of_stations + 20)
    station_ans = stations_by_distance(list_of_stations, test_coord)
    
    for i in range(no_of_stations - 1, -1, -1):
        assert(station_ans[no_of_stations - 1 -i][0].name == 'name_' + str(i))
        assert(math.isclose(station_ans[i][1] , haversine(station_ans[i][0].coord, test_coord)))

