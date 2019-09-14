#Stephen Duncanson
#jwcp2

import math
import openpyxl
import os

#Set Constants
ITERATION_LIMIT = 10000000000   #Limit of how many times it will iterate before giving up
ERROR_MARGIN    = 0.000100000   #Error must be < ERROR_MARGIN to be considered solved
GUESS_PERCENT   = 0.000010000   #When reguessing k, GUESS_PERCENT is the amount to multiply error by
G               = 32.17190000   #Constant for gravity                 


def get_k(t_0,d):
    k   = ((2*math.pi)**2)/(G*(t_0**2))                 #Assume tanh(kd) ~ 0, initial guess
    try:
        t_1 = (2*math.pi)/(math.sqrt(G*k*math.tanh(k*d)))   #Calculate t value from guess
    except ZeroDivisionError:
        return "N/A"
    e   = (math.fabs(t_1 - t_0))/t_0                    #Calculate error between t_0, t_1
    counter = 0

    while e > ERROR_MARGIN:
        counter +=1 
        #Calculate new k guess
        if t_1 < t_0:
            k = k-e*GUESS_PERCENT
        elif t_1 > t_0:
            k = k+e*GUESS_PERCENT
            #Calculate new t value
        t_1 = ((2*math.pi)/math.sqrt(G*k*math.tanh(k*d)))
        #Calculate new error
        e = (math.fabs(t_1 - t_0))/t_0
        #print new values
        #print("k: "+str(k))   
        #print("t: "+str(t_1))    
        #print("error: "+str(e))

    return k

#Get Spreadsheet Variables
SPREADSHEET_FILENAME = str(input('Enter path or local filename (include .xlsx): ')) 
SHEET_NAME = str(input("Enter the sheet name: "))
D_COLUMN = str(input("What column are the d values in? "))
START_ROW = int(input("What is the start row? "))
END_ROW = int(input("What is the end row? "))
T_COLUMN = str(input("What column are the t values in? "))
K_COLUMN = str(input("What column are the k values going into? "))
#Assuming that the start/end rows are the same for all three columns

#open spreadsheet and read all 
spreadsheet = openpyxl.load_workbook(SPREADSHEET_FILENAME,data_only=True)
data_sheet  = spreadsheet[SHEET_NAME]

#Go through rows and add all d and t values to list
for x in range(START_ROW,END_ROW+1):
    d = float(data_sheet[D_COLUMN+str(x)].value)
    t = float(data_sheet[T_COLUMN+str(x)].value)
    data_sheet[K_COLUMN+str(x)].value = get_k(t,d)

    
spreadsheet.save(SPREADSHEET_FILENAME)    
    



