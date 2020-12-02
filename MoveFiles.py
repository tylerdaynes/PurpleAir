# This file will move the created plots and copy the master data file to the Y drive

import os
import shutil

y_drive = 'Y:/Environmental/ENV.Secure/Ambient Air Monitoring/Data/PurpleAir'  # Path to PurpleAir folder in Y drive
plots = 'Y:/Environmental/ENV.Secure/Ambient Air Monitoring/Data/PurpleAir/Plots'  # Path to plots in Y drive

for entry in os.scandir('./Plots'):  # Scan folder for new plots
    if entry.path.endswith('.png'):  # Check if file is a png
        shutil.move(entry.path, f'{plots}/{entry.name}')  # Move plot to Y drive
        print(f'Moved {entry.name} to Y drive')

print('Copying Master_Data.csv to Y drive')
shutil.copy2('Master_Data.csv', y_drive)  # Copy Master_Data.csv to Y drive
print('Copied Master_Data.csv to Y drive')
