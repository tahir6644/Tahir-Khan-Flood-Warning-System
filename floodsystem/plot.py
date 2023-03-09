from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

def plot_water_levels(station: MonitoringStation, dates: list, levels: list):
    """
    Displays a plot of the water level data against time
    for a station.
    """

    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Plot lines showing typical low and high levels
    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station: MonitoringStation, dates: list, levels: list, p: int):
    """
    Plots the water level data as well as a best-fit polynomial
    of degree p.
    """
    poly, d0 = polyfit(dates, levels, p)

    x = matplotlib.dates.date2num(dates)
    y = levels

    # Plot original data
    plt.plot(x, y)

    # Plot polynomial at 30 points along the interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Plot lines showing typical low and high levels
    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')

    plt.tight_layout()
    plt.show()

