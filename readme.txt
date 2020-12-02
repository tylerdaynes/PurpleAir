main.py uses Compile.py and plotting.py as modules to compile and plot pm data from the PurpleAir monitor

Required Steps for initial setup:
1.  If you are using PyCharm, create a new project and copy all of the necessary files from the Y drive
    a.  main.py
    b.  Compile.py
    c.  plotting.py
    d.  MoveFiles.py
    e.  Master_data.csv
    f.  readme.txt
    If you are not using PyCharm, copy the above files to a folder of your choice
2.  Create a folder called "Plots" in the project folder (same directory as the python files)
    You can name it something else, just adjust lines 72 & 74 of plotting.py and line 9 of MoveFiles.py
3.  Create a folder called "PurpleAir" on the desktop
    You can name it something else or put it somewhere else if you'd prefer
4.  Within the "PurpleAir" folder create two new folders called "DataToLoad" & "LoadedData"
5.  Adjust lines 15 & 17 in main.py with the file paths to these folders
    They need to be string and the \ need to be replaced with /
    example: path = 'C:/path'
6.  Install the following libraries using "pip install x" in the terminal
    a.  pandas
    b.  matplotlib
    c.  tkcalendar
    example: pip install pandas

Instructions for using this program:
1.  Download the Purple air data from the sensor
    The data is on a micro SD card in the sensor
2.  Copy all of the csv files to the "DataToLoad" folder
3.  Run main.py
    If you are using PyCharm use Alt+Shift+F10 or hit the play button in the top right
    This will create plots for PM data in the "Plots" folder for the selected time period
    It will also move the csv files used in Compile.py to the "LoadedData" folder
4.  Run MoveFiles.py
    This will move the new plots to the Y drive with the path listed on line 7 of MoveFiles.py
    It will also copy the Master_Data.csv file to the Y drive within the path listed on line 6 of MoveFiles.py
