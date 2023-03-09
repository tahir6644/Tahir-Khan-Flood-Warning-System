from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

def test_typical_range_consistent():

    i = 0
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    # Inconsistent range
    t_range = (i + 1, i)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
    assert(station.typical_range_consistent() == False)

    i = 1
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    # Inconsistent range
    t_range = None
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)        
    assert(station.typical_range_consistent() == False)

    i = 2
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    t_range = (i , i + 1)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)        
    assert(station.typical_range_consistent() == True)


def test_inconsistent_typical_range_stations():
    
    list_of_stations = []
    ans_list = []
    no_of_stations = 10
    
    for i in range(no_of_stations):
        s_id = 's_id'+ str(i)
        m_id = 'm_id' + str(i)
        name = 'name_'+ str(i)
        coord = (i, i)
        if i % 3 == 0 :
            t_range = (i, i + 1)
        elif i % 3 == 1 :
            # Stations 1, 4, 7 have inconsistent ranges
            t_range = None
        else:
            # Stations 2, 5, 8 have inconsistent ranges
            t_range = (i + 1, i)
        river = 'river_'+ str(i)
        town = 'town_' + str(i)
        station = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
        list_of_stations.append(station)
        if i % 3 == 1 or i % 3 == 2:
            # ans_list contains all the stations with inconsistent ranges
            ans_list.append(station)

    
    ans = inconsistent_typical_range_stations( list_of_stations )
    assert(ans == ans_list)




    

    
