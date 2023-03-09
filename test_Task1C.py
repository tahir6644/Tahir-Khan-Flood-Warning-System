from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation 
from haversine import haversine
import math



def test_stations_within_radius( ):

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
        #print(haversine(coord, (5.25, 5.25))) - distances from the coordinate 5.25, 5.25
        # 825.0028680357574 - station 0
        # 667.7536677805683 - station 1
        # 510.5284475742315 - station 2
        # 353.35102891052964 - station 3
        # 196.24522707578885 - station 4
        # 39.23487645276363  - station 5
        # 117.65614426777739 - station 6
        # 274.40388694107077 - station 7
        # 430.98430886202436 - station 8
        # 587.3732476734236  - station 9

    stations_ans = stations_within_radius( list_of_stations, (5.25, 5.25), 500)

    # From the results above, only stations 3-8 are
    # within the 500 km radius. i goes from 0-5 so 
    # i+3 goes from 3-8. Note stations_within_radius()
    # does not sort by distance so the order should just
    # be from stations 3-8.
    for i in range(6):
        assert(stations_ans[i].name == 'name_'+str(i + 3))
    





