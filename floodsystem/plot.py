from floodsystem.station import MonitoringStation
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