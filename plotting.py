# This is a module for main.py that plots the pm data from the PurpleAir monitor

from matplotlib import pyplot as plt, dates as mpl_dates
from datetime import timedelta

if __name__ == '__main__':
    print("This file is a module and is not meant to run on it's own")
else:
    plt.style.use('seaborn-whitegrid')  # Sets plot style to pre-made style

    locator = mpl_dates.AutoDateLocator()  # Format tick marks for dates

    formatter = mpl_dates.ConciseDateFormatter(locator)  # Automatically adjust ticks for best fit
    formatter.formats = ['%y',      # If ticks are mostly years (yy)
                         '%b',      # If ticks are mostly months (mon)
                         '%d',      # If ticks are mostly days (dd)
                         '%H:%M',   # If ticks are mostly hours  (hh:mm)
                         '%H:%M',   # If ticks are mostly minutes  (hh:mm)
                         '%s.%f'    # If ticks are mostly seconds (ss.micro)
                         ]   # Formats for tick labels
    formatter.zero_formats = [''] + formatter.formats[:-1]  # Formatting for zero values
    formatter.zero_formats[3] = '%d-%b'  # If ticks are hours, then zero ticks are (dd-mon)
    formatter.offset_formats = ['',                 # Blank if limits are years
                                '%Y',               # If limits are months (yyyy)
                                '%b %Y',            # If limits are days (mon yyyy)
                                '%b %Y',            # If limits are hours (mon yyyy)
                                '%d %b %Y',         # If limits are minutes (dd mon yyyy)
                                '%d %b %Y %H:%M'    # If limits are seconds (dd mon yyyy hh:mm)
                                ]   # Formats for bottom right label


    def create_plots(pm2_5a,
                     pm2_5b,
                     pm10a,
                     pm10b,
                     startdate,
                     enddate):

        start_day = startdate.day  # day for starting date
        start_month = startdate.month  # month for starting date
        start_year = startdate.year  # year for starting date
        check_start = start_day + start_month + start_year  # starting date without time

        end_day = enddate.day  # day for end date
        end_month = enddate.month  # month for end date
        end_year = enddate.year  # year for end date
        check_end = end_day + end_month + end_year  # end date without time

        EPA2_5 = 35  # NAAQS limit for pm2.5
        EPA10 = 150  # NAAQS limit for pm10

        fig, (pm2_5, pm10) = plt.subplots(nrows=2, figsize=[9.6, 7.2])  # Create new window with two subplots
        pm2_5.plot(pm2_5a, label='Channel A')  # Plot channel a data in pm2.5 subplot
        pm2_5.plot(pm2_5b, label='Channel B')  # Plot channel b data in pm2.5 subplot
        pm2_5.axhline(EPA2_5, label='NAAQS PM 2.5 24hr', linestyle='--')  # Plot horizontal line for NAAQS limit
        pm2_5.set_title('PurpleAir PM 2.5')  # Title for subplot
        pm2_5.set_ylabel('PM 2.5 (\u03bcg/m$^3$)')  # \u03bc unicode characters for mu
        pm2_5.legend(loc='upper left', borderaxespad=1)  # show legend in upper left corner
        pm2_5.xaxis.set_major_locator(locator)  # Format x-axis ticks
        pm2_5.xaxis.set_major_formatter(formatter)  # Format x-axis tick labels

        pm10.plot(pm10a, label='Channel A')  # Plot channel a data in pm10 subplot
        pm10.plot(pm10b, label='Channel B')  # Plot channel b data in pm10 subplot
        pm10.axhline(EPA10, label='NAAQS PM 10 24hr', linestyle='--')  # Plot horizontal line for NAAQS limit
        pm10.set_title('PurpleAir PM 10')  # Title for subplot
        pm10.set_ylabel('PM 10 (\u03bcg/m$^3$)')  # \u03bc unicode characters for mu
        pm10.legend(loc='upper left', borderaxespad=1)  # show legend in upper left corner
        pm10.xaxis.set_major_locator(locator)  # Format x-axis ticks
        pm10.xaxis.set_major_formatter(formatter)  # Format x-axis tick labels

        plt.tight_layout()  # fit plot to window

        if check_end == check_start + 1:  # check if start date and end date are same
            plt.savefig(f'Plots/{startdate:%Y.%m.%d}.png')
        else:
            plt.savefig(f'Plots/{startdate:%Y.%m.%d}-{enddate:%Y.%m.%d}.png')

        plt.show()  # show plot window
