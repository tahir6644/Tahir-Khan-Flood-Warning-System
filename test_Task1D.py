from floodsystem.geo import rivers_with_station 
from floodsystem.geo import stations_by_river
from floodsystem.station import MonitoringStation 

def test_rivers_with_station():
    list_of_stations = []
    no_of_stations = 10
    
    for i in range(no_of_stations):
        s_id = 's_id'+ str(i)
        m_id = 'm_id' + str(i)
        name = 'name_'+ str(i)
        coord = (i, i)
        t_range = (i, i)
        river = 'river_'+ str(i//2)  # so that more than one stations are on the same river
        # i goes from 0-9 so i//2 goes from 0-4.
        town = 'town_' + str(i)
        station = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
        list_of_stations.append(station)

    rivers = rivers_with_station(list_of_stations)

    assert(rivers == {'river_0', 'river_1', 'river_2', 'river_3', 'river_4'})

def test_stations_by_river():
    
    list_of_stations = []
    no_of_stations = 10
    
    for i in range(no_of_stations):
        s_id = 's_id'+ str(i)
        m_id = 'm_id' + str(i)
        name = 'name_'+ str(i)
        coord = (i, i)
        t_range = (i, i)
        river = 'river_'+ str(i//2)  # so that more than one stations are on the same river
        town = 'town_' + str(i)
        station = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)
        list_of_stations.append(station)

    dictionary = stations_by_river(list_of_stations)
    
    for i in range(5):
        # E.g. the only stations on river_2 should be name_4 and name_5.
        assert{ dictionary['river_'+str(i)] == [
            MonitoringStation('s_id' + str(2*i), 'm_id' + str(2*i), 'name' + str(2*i), (2*i, 2*i), (2*i, 2*i) , 'river_'+ str(i), 'town_'+ str(2*i)),
            MonitoringStation('s_id' + str(2*i + 1), 'm_id' + str(2*i + 1), 'name' + str(2*i + 1), (2*i + 1, 2*i + 1), (2*i + 1, 2*i + 1) , 'river_'+ str(i), 'town_'+ str(2*i + 1))
            ]}



