# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from .station import MonitoringStation

def stations_by_distance(stations : list , p : tuple) -> list :
    """
    For a given list of station objects and coordinate p, returns
    a sorted list of (station, distance) tuples 
    (based on the distance of the station from coordinate p) 
    
    """

    station_distance = []
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station, distance))

    station_distance = sorted_by_key(station_distance, 1)

    return station_distance

def stations_within_radius(stations : list, centre : tuple, r : float) -> list:

    """
    For a given list of stations , geographic center and 
    radius, returns a list of stations within the radial area
   
    """

    stations_radius = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r :
            stations_radius.append(station)
    
    return stations_radius

def rivers_with_station(stations : list) -> set:

    """
    For a given list of station objects, returns a set of rivers 
    associated with the stations.
 
    """

    stations_rivers = { station.river for station  in stations }
    return stations_rivers

def stations_by_river(stations : list ) -> dict:

    """
        For a given list of station objects, returns a dictionary with key:
        value pairs as river names and list of station object associated with the river.

    """

    dictionary = {}

    for station in stations:
        dictionary.setdefault(station.river, []).append(station)
            
    return dictionary

def stations_by_town(stations: list) -> dict:
    """
        For a given list of station objects, returns a dictionary with key:
        value pairs as town names and list of station object associated with the town.

    """

    dictionary = {}

    for station in stations:
        dictionary.setdefault(station.town, []).append(station)
            
    return dictionary


def rivers_by_station_number(stations : list, N : int) -> list:

    """
    Given a list of stations and integer N, it should return a list of N (river, no. of stations) tuples
    with the greatest number of stations. In case of more rivers with the same number of stations as the Nth entry,
    the rivers are included as well in the list.
       
    """
    # can try default dict
    stations_dict = {}

    for station in stations:
        stations_dict[station.river] = stations_dict.setdefault(station.river, 0) + 1 

    # List of (river, no. of stations) tuples.
    stations_list = list(stations_dict.items())

    # Sort by no. of stations in descending order.
    stations_list.sort(key = lambda i:i[1], reverse=True)

    # If there are more rivers with the same no. of stations as
    # the Nth entry (i = N-1 as we start from 0), increase the
    # no. of tuples included in the final list so that they are included.
    i = N - 1
    while stations_list[i][1] == stations_list[ i + 1 ][1]:
        i += 1
    
    return stations_list[ : i + 1 ] 

