# This is a module for main.py that compiles new PurpleAir data with existing data

import os
import pandas as pd
from datetime import timedelta
import shutil

if __name__ == '__main__':
    print("This file is a module and is not meant to run on it's own")
else:
    def timeconvert(x):  # User defined function to convert time to logger time
        x = x - timedelta(hours=7)  # Subtract 7 hours to convert from UTC to logger time
        return x


    def compiledata(newdatapath, masterfile, olddatapath):
        for entry in os.scandir(newdatapath):  # Iterate through each file in folder
            if entry.path.endswith('.csv'):  # Check if the file is a CSV file
                df = pd.read_csv(entry.path, parse_dates=['UTCDateTime'])  # Read data from CSV file
                df.UTCDateTime = df.UTCDateTime.apply(timeconvert)  # Apply udf
                df.rename(columns={'UTCDateTime': 'DateTime'}, inplace=True)  # Rename the DateTime column
                df = df.set_index('DateTime')  # Set index to date time
                masterfile = pd.concat([masterfile, df])  # Combine the data from current CSV file to master dataframe
                masterfile.drop_duplicates(inplace=True)  # Remove duplicates
                shutil.move(entry.path, f'{olddatapath}/{entry.name}')  # Move file to "LoadedData" folder
                print(f'loaded {entry.name}')
            else:
                print(f'skipping {entry.name}')
        print('Compiled new data successfully')
        return masterfile
