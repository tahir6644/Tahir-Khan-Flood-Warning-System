# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

 #typical range: (0.231, 0.971)

    def typical_range_consistent(self):
        """
            Checks the typical high/low range data for consistency
        """        

        return True if self.typical_range and self.typical_range[0] < self.typical_range[1] else False
    

    def relative_water_level(self):
        """
        Returns the latest water level as a fraction of the typical range
        from 0.0 to 1.0
        """
        if self.typical_range_consistent() and self.latest_level:
            diff = self.latest_level - self.typical_range[0]
            range_width = self.typical_range[1] - self.typical_range[0]
            return (diff/range_width)
        else:
            return None


def build_test_list(no_of_stations = 10):
    """
    Builds and returns a list of fake sample station objects for tests.
    Each fake station is given simple attributes with a number from
    0-(9) at the end to differentiate between them.
    """

    list_of_stations = []

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

    return list_of_stations



def inconsistent_typical_range_stations(stations : list ) -> list:

    """
        Given a list of station objects returns a list of stations that have inconsistent data.
    
    """
    stations_inconsistent = []
    for station in stations:
        if not station.typical_range_consistent():
            stations_inconsistent.append(station)
    
    return stations_inconsistent









