import os

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

#% matplotlib inline


path = os.getcwd() + '\ex1data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
data.head()
