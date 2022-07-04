
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from tkinter import *
from tkinter import filedialog

# ############################################
# ############ Declare Global Variables ######
# ############################################

# global np_lap_data
# global brake
# global time
# global left_bases
# global left_base

###################################################
############ Imports Pertinent Data from CSV ######
###################################################

#A generic function for any. 
def get_data_and_time(df, column_of_interest, debug = False):
    data_and_time = df.loc[:,[column_of_interest,'elapsedTime']] 
    if (debug):
        print(data_and_time)
    return data_and_time


###################################################
#######Calculates the derivative at each point ####
###################################################

#insert later

###################################################
#######Find Zones and Calculate the slope #########
###################################################

#"process_data_of_interest_parameter" as a parameter.
def finds_peaks_and_properties(data_and_time):
    peaks, peak_properties = find_peaks(data_and_time, height=0, width = 5)
    return peaks, peak_properties

def find_left_base(peaks, peak_properties):
    left_bases = peaks['left_bases']
    left_base = peak_properties['left_bases'][0]
    return left_bases, left_base

def calculate_slope_of_interest(data_and_time, peaks, left_bases):
    #calculates y2 and x2
    y2 = []
    x2 = []
    ds_data_column = data_and_time.iloc[:,0]
    ds_time = data_and_time.iloc[:,1]
    for i in peaks:
        pi = ds_data_column[i]
        ti = ds_time[i]
        y2 = np.append(y2, pi, axis=None)
        x2 = np.append(x2, ti, axis=None)
    print(y2)
    print(x2)

    #calculates y1 and x1
    #fix below to amke sure variables are set correctly
    y1 = []
    x1 = []

    for i in left_bases:
        li = ds_data_column[i]
        ti = ds_time[i]
        y1 = np.append(y1,li, axis=None)
        x1 = np.append(x1, ti, axis=None)
    print(y1)
    print(x1)

    all_slopes = (y2-y1)/(x2-x1)

    print("The slopes for all the braking zones are: " + all_slopes)
    return all_slopes

###########################################
############ Graphs Data ##################
###########################################

def graphs_data(data_and_time, peaks):
    ds_data_column = data_and_time.iloc[:,0]
    ds_time = data_and_time.iloc[:,1]
    plt.plot(ds_time, ds_data_column)
    plt.plot(peaks, ds_data_column[peaks], "x")
    

##################################################
############ Calling Functions####################
##################################################
#then pass these above to find left bases function. 

df_lap_data = pd.read_csv("f1_lap_1246.csv", delimiter=",")
print("Wicked")
brake_and_time = get_data_and_time(df_lap_data, 'brake')
brake_peaks, brake_properties = finds_peaks_and_properties(brake_and_time)
brake_left_bases = find_left_base(brake_peaks, brake_properties)
brake_slopes = calculate_slope_of_interest(brake_and_time, brake_peaks, brake_left_bases)

graphs_data(brake_and_time, brake_peaks)

###################################################
############ Questions Comments, Learning##########
###################################################

"""
def multi (a, b):
    
    if(a != string)
    
    return a * b

x = 4
y = 4
z = 2
k = 1


oranges = "oranges"

result1 = multi(y, z)
result2 = multi(k, x)
result3 = multi("apples", oranges)

result4 = muilti(result1, result2)


"""

###################################################
############ Opens File and GUI ###################
###################################################
"""
Leaving this out for now. 
def open_csv_File_and_get_data():
    filepath = filedialog.askopenfilename(title="Open a Hotlaps csv file")
    file = open(filepath,"r")
    print(filepath)
    file.close()
    np_lap_data = pd.read_csv(filepath, delimiter=",")
    

#Tkinter GUI
window = Tk()
button = Button(text = "Open Driver Data", command=open_csv_File_and_get_data)
button.pack()
window.mainloop()
"""