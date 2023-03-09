def stations_level_over_threshold(stations: list, tol: float) -> list:
    """
    Returns a list of tuples where each tuple holds a station at which
    the latest relative water level is over tol and the relative water
    level at the station. 
    i.e. a list of (station, relative_water_level) tuples.
    """

    stations_rwl = []
    for station in stations:
        if station.typical_range_consistent and station.relative_water_level():
            if station.relative_water_level() > tol:
                stations_rwl.append((station, station.relative_water_level()))

    # Sort by relative water level in descending order.
    stations_rwl.sort(key = lambda i:i[1], reverse=True)

    return stations_rwl



    




