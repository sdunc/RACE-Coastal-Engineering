#Written By Stephen Duncanson
#RACE Coastal Engineering
#Development: 7/12/19 -

#Imports
import time
import os
import os.path
import tkinter as tk
from tkinter import ttk
import datetime
import time
import openpyxl
from geopy.geocoders import Nominatim
from geopy.distance import geodesic         #In presentation, mention the model which this uses to calculate distance

#For now, I am operating under the assumption that the files will be called 'projects.txt', 'clients.txt','database.txt'
#The idea is that 'projects.txt' + 'clients.txt' -> 'database.txt'
#The database will be checked each time the program is opened, and cleaned, meaning any malformed entries will be purged
#This may result in an incomplete dataset, but it will be an accurate one. 
#A log file will be created to provide a list of all the IDs that did not make it into the final database. 

#Constants
PROJECTS_FILE = 'projects.txt'
CLIENTS_FILE  = 'clients.txt'
DATABASE_FILE = 'database.txt'

VERSION = .9


DATABASE_HEADER = 'id,name,location,project type,client,client type,lat,long'#,permit,boring'


#Create a list of all the years between 1996 (end of records?) and the current year. 
#If I can I want to use this both for the buttons to add/remove to, and for the drop down menus
#My only concern would be if removing from this list would change the available drop down menus?
YEARS = [x for x in range(1996,now.year())]

CLIENT_TYPES = ['Residential',          #0
                'Government',           #1
                'Marina / Yacht Club',  #2
                'Industrial / Utility', #3
                'Consultant',           #4
                'Contractor'            #5
                ]

PROJECT_TYPES = ['Dredging',                            #0
                 'Flood and erosion control structure', #1
                 'Beach / Dune / Living Shoreline',     #2
                 'Pier / Dock',                         #3
                 'Hydrographic Survey',                 #4
                 'Facility Assessment',                 #5
                 'Construction Administration',         #6
                 'Flood / Wave Study',                  #7
                 'Upland Structure',                    #8
                 'Other'                                #9
                ]


def startup_database_check():
    if is_database_present():
        if is_database_updated():
            clean_database()
        else:
            update_database()
    else:
        if are_sources_present():
            create_database()
        else:
            popup("Error! Sources are missing")

def is_database_present():
    if os.path.exists(DATABASE_FILE):
        return True
    else:
        return False


def is_database_updated():
    database = open(DATABASE_FILE,'r')
    project_file = open(PROJECTS_FILE,'r')
    #to test if the database is updated, iterate over the number of lines and count them, then compare
    counter = 0
    for line in database:
        counter+=1
    for line in project_file:
        counter-=1
    if counter == 0:
        return True
    elif counter < 0:
        return False
    else:
        popup('ERROR! Database is ahead of project files')
        

def are_sources_present():
    if os.path.exists(CLIENTS_FILE) and os.path.exists(PROJECTS_FILE):
        return True
    else:
        return False

def create_database():
    '''
    The create database function is called when no database is found but source files are present
    it creates a new text file and writes the header constant to it before calling the update database function
    '''
    database = open(DATABASE_FILE,'w')
    database.write(DATABASE_HEADER)
    database.close()
    update_database()
    

def update_database():
    add_new_projects()
    add_client_types()
    geocode_database()
    clean_database()

def add_new_projects():
    '''
    The add_new_projects function is called when the database is being updated
    it opens the database and projects files, and adds all their contents into nested lists
    once the lists are complete, it iterates through the database list and creates a list of current ids
    then it iterates through the project files list and removes all the projects which are in that list
    the remaining projects must therefore be new, and are added to the database file
    '''
    database = open(DATABASE_FILE,'w')
    projects_file = open(PROJECTS_FILE,'r')
    
    current_database_lines = []
    currnet_project_lines = []
    current_database_ids = []
    
    line_counter = 1
    
    for line in database:
        if line_counter != 1:
            split_line = line.split(',')
            current_database_lines.append(split_line[0])
            #using the split method here splits the long string into a list of words, which will get nested
            #I will need to see the behavior of the output text file to ensure that this works as desired 
            #it could be the case that AJERA will merely skip something if it has no value, which would cause this to become 
            #out of alignment. I need it to print out a None or 0 or some other null character for this to work as desired
            #otherwise I will have to find a better solution to this. 
            #line counter+=1 #I could put there here to keep counting lines, but there is no good reason to
            #the line counter is here to ensure that the header of the text file is not included when the list of projects is generated
            #think of a better way to do this. 
        line_counter+=1
        
    line_counter = 1
    #set the line counter back to one for the next for loop
    for line in projects_file:
        if line_counter != 1:
            current_project_lines.append(line.split(','))
            #line counter+=1 #I could put there here to keep counting lines, but there is no good reason to
        line_counter +=1 
    #since the line counter is no longer needed, I'm deleting it and freeing up the memory
    del line_counter
    

    

def add_client_types():

def geocode_database():

def clean_database():

def popup(message):
    popup = tk.Tk()
    popup.wm_title("Error")
    popup_label = ttk.Label(popup,text=message)
    popup_label.pack(side="top",fill="x"pady=10)
    popup.mainloop()


def excel_button():

def google_earth_button():

def passes_filter():

def add_to_excel():

def add_to_kml():







