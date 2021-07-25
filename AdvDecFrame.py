#import numpy as np
#import pandas as pd
#import csv
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print(type(file_path))
print(file_path)

class Stock(object):
    def __init__(self, ticker_symbol):
        self.ticker = ticker_symbol.upper()
        self.data = self._get_data()
        self.open = open
        self.high = high
        self.low = low
        self.close = close





