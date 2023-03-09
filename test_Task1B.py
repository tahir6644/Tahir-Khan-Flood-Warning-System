from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation 
from haversine import haversine
import math

def test_stations_by_distance():
    
    # Creates sample data to test.
    # Each fake station is given simple attributes with a number from
    # 0-9 at the end to differentiate between them.

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

    # The way test_coord is defined means the list_of_stations
    # should already be sorted by distance but in descending order.
    test_coord = (no_of_stations + 20, no_of_stations + 20)

    # stations_by_distance returns a list of (station, distance)
    # in ascending order.
    station_ans = stations_by_distance(list_of_stations, test_coord)
    
    for i in range(no_of_stations - 1, -1, -1):
        # i goes from 9 down to 0 inclusive.

        # 'name_9' should have the smallest distance so it should
        # be the first entry in station_ans and so on.
        assert(station_ans[no_of_stations - 1 -i][0].name == 'name_' + str(i))

        # Verify that stations_by_distance accurately calculated
        # the distances.
        assert(math.isclose(station_ans[i][1] , haversine(station_ans[i][0].coord, test_coord)))

