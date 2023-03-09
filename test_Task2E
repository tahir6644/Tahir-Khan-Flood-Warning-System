from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation
import datetime
from dateutil.tz import tzutc

def test_plot_water_levels():
    # Simple graph with 5 points, steadily increasing with a small
    # horizontal segment. Test that the function can be 
    # called succesfully.

    i = 0
    s_id = 's_id'+ str(i)
    m_id = 'm_id' + str(i)
    name = 'name_'+ str(i)
    coord = (i, i)
    t_range = (5, 20)
    river = 'river_'+ str(i)
    town = 'town_' + str(i)
    station_0 = MonitoringStation(s_id, m_id, name, coord, t_range, river, town)

    dates = [datetime.datetime(2023, 3, 3, 1, 0, tzinfo=tzutc()),
             datetime.datetime(2023, 3, 3, 1, 15, tzinfo=tzutc()),
             datetime.datetime(2023, 3, 3, 1, 30, tzinfo=tzutc()),
             datetime.datetime(2023, 3, 3, 1, 45, tzinfo=tzutc()),
             datetime.datetime(2023, 3, 3, 2, 0, tzinfo=tzutc())
             ]
    
    levels = [7,
              12,
              12,
              16,
              19
              ]
    
    plot_water_levels(station_0, dates, levels)

    


