# This file will compile and plot data from the PurpleAir monitor

import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import timedelta, datetime
import Compile      # Import Compile.py module
import plotting     # Import plotting.py module

master = pd.read_csv('Master_Data.csv',
                     parse_dates=['DateTime'],
                     index_col='DateTime')  # Master Data CSV file

newdata = 'C:/Users/Tyler.daynes/Desktop/PurpleAir/DataToLoad'  # Path to "DataToLoad" folder on desktop

olddata = 'C:/Users/Tyler.daynes/Desktop/PurpleAir/LoadedData'  # Path to LoadedData folder on desktop

print('Looking for new data')
master = Compile.compiledata(newdatapath=newdata,
                             masterfile=master,
                             olddatapath=olddata)  # Compile new data with master file


master.to_csv('Master_Data.csv')  # Save compiled data to CSV
print('Finished updating Master_Data.csv')  # DO NOT EXIT PROGRAM UNTIL THIS TEXT SHOWS IN THE TERMINAL

end = master.last_valid_index()  # Find the last valid index for the dataframe
end_day = end.day
end_month = end.month
end_year = end.year

start = end - timedelta(days=7)  # Default value for date range
start_day = start.day
start_month = start.month
start_year = start.year

one_day = timedelta(hours=23, minutes=59)  # Time difference for one day


def date_entry():  # function for button
    date_entry.StartDate = datetime.strptime(d1.get(), '%m/%d/%y')  # get the start date
    date_entry.EndDate = datetime.strptime(d2.get(), '%m/%d/%y')  # get the end date
    root.destroy()  # close the popup window


root = tk.Tk()  # create the popup window
root.title('Date Range')  # title for the popup window

label0 = ttk.Label(root, text=f'Choose the date range for analysis\nDefault is one week from last recorded value')
# top center text
label0.grid(row=0, columnspan=2)  # placement of top center text

label1 = ttk.Label(root, text='Start Date:')  # middle left text
label1.grid(row=1, column=0, pady=5)  # placement of middle left text

label2 = ttk.Label(root, text='End Date:')  # bottom left text
label2.grid(row=2, column=0)  # placement of bottom left text

d1 = DateEntry(root, day=start_day, month=start_month, year=start_year)  # start date field
d1.grid(row=1, column=1, pady=5)  # placement of start date field

d2 = DateEntry(root, day=end_day, month=end_month, year=end_year)  # end date field
d2.grid(row=2, column=1)  # placement of end date field

btn1 = ttk.Button(root, text='Finish', command=date_entry)  # Finish button
btn1.grid(row=3, columnspan=2, pady=5)  # placement of button

root.mainloop()  # start the popup window

startdate = date_entry.StartDate  # retrieve the start date from the popup
start_day = startdate.day
start_month = startdate.month
start_year = startdate.year
check_start = start_day + start_month + start_year  # Start date without time as integer

enddate = date_entry.EndDate  # retrieve the date date from the popup
end_day = enddate.day
end_month = enddate.month
end_year = enddate.year
check_end = end_day + end_month + end_year  # End date without time as integer

if check_end == check_start:  # check if dates are the same
    enddate = startdate + timedelta(days=1)  # to next day at 00:00
    print('Start date and end date are the same, adding 24 hours to start date')
else:
    enddate = enddate + one_day  # include full day (add 23:59 to end date)

print(f'Start: {startdate}\nEnd: {enddate}')

master_hourly = master.resample('H').mean()  # Resample dataframe for hourly average

index = master_hourly.index  # Pull index from dataframe
index = index.tz_localize(None)  # Remove timezone from index
master_hourly.index = index  # Replace index in dataframe

pm2_5a = master_hourly[startdate: enddate].pm2_5_atm  # Load channel A pm2.5 data
pm2_5b = master_hourly[startdate: enddate].pm2_5_atm_b  # Load channel B pm2.5 data
pm10a = master_hourly[startdate: enddate].pm10_0_atm  # Load channel A pm10 data
pm10b = master_hourly[startdate: enddate].pm10_0_atm_b  # Load channel B pm10 data

plotting.create_plots(pm2_5a=pm2_5a,
                      pm2_5b=pm2_5b,
                      pm10a=pm10a,
                      pm10b=pm10b,
                      startdate=startdate,
                      enddate=enddate)  # Create & save plots for data
