'''
Title: sample_CSV_NOAA.py
Written by: Brad Portouw
Created: 6/7/25
output: .py file
'''

# Setup

import math
import collections
import numpy
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import datetime
import os


# This file is intended to import some weather data from NOAA's website from a CSV and seeing what it contains

# import 'airlift_mass_repeatability.csv' form the weather_data directory:
# calling the DF 'weather'
weather = pd.read_csv('../weather_data/NORMAL_HLY_sample_csv.csv')
print(weather)

# Performing a quick describe to check the data:
print(weather.columns)

#blanks = blanks[['Date','Filter ID', 'Mass (g)']]



