# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from .station import MonitoringStation

def stations_by_distance(stations : MonitoringStation , p : tuple) -> list :
    """
    For a given list of stations and coordinate p, returns
    a sorted list of station, distance tuple 
    (based on the distance of the station from coordinate p) 
    
    """

    station_distance = []
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station, distance))

    station_distance = sorted_by_key(station_distance, 1)

    return station_distance

