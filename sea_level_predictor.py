import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))

    # Create scatter plot on the axis
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    ax.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2050)])
    y_pred = slope * x_pred + intercept
    ax.plot(x_pred, y_pred, 'r', label='Best Fit Line 1880-2050')

    # Create second line of best fit (for data from 2000 onwards)
    df_forecast = df[df['Year'] >= 2000]
    x_forecast = df_forecast['Year']
    y_forecast = df_forecast['CSIRO Adjusted Sea Level']
    
    slope, intercept, r_value, p_value, stderr = linregress(x_forecast, y_forecast)
    x_pred2 = pd.Series([i for i in range(2000, 2050)])
    y_pred2 = slope * x_pred2 + intercept
    ax.plot(x_pred2, y_pred2, 'green', label='Best Fit Line 2000-2050')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Add a legend
    ax.legend()

    # Save plot and return the current axis (for testing purposes)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
