def stations_level_over_threshold(stations: list, tol: float) -> list:
    """
    Returns a list of tuples where each tuple holds a station at which
    the latest relative water level is over tol and the relative water
    level at the station. 
    i.e. a list of (station, relative_water_level) tuples.
    """

    stations_rwl = []
    for station in stations:
        if station.relative_water_level():
            if station.relative_water_level() > tol:
                stations_rwl.append((station, station.relative_water_level()))

    # Sort by relative water level in descending order.
    stations_rwl.sort(key = lambda i:i[1], reverse=True)

    return stations_rwl

def stations_highest_rel_level(stations: list, N: int) -> list:
    """
    Returns a list of the N stations with the highest relative water levels 
    in descending order.
    """
    risky_stations = []
    
    # Check for validity first
    for station in stations:
        if station.relative_water_level():
            risky_stations.append(station)

    # Sort by relative water level in descending order.
    risky_stations.sort(key = lambda i:i.relative_water_level(), reverse=True)
    # Return first N stations
    return risky_stations[:N]
            


    




