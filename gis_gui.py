#Stephen Duncanon
#RACE GIS gui
#Final version

import tkinter as tk
from tkinter import ttk
import datetime
now = datetime.datetime.now()

VERSION = .7

def startup_check():
    '''
    The initial check for project and database spreadsheets
    '''

def database_gen():
    '''
    if database is missing
    '''

def database_update():
    '''
    if the database is incomplete
    '''

def map_gen():
    '''
    When map button is pressed
    '''
    print("Normally I'd generate a map here")

def excel_gen():
    '''
    When map button is pressed
    '''
    print("Normally I'd generate a spreadsheet here")

def all_client():
    print("all clients!")
    
def client():
    if client:
        all_proj_var.set(0)


def all_proj():
    print("all projects!")
    

def proj():
    if proj:
        all_proj_var.set(0)

def location_spec():
    if loc_spec_var.get():
        location_drop_down.config(state=tk.NORMAL)
        loc_entry.config(state=tk.NORMAL)
        loc_radius.config(state=tk.NORMAL)    

    else:
        location_drop_down.config(state=tk.DISABLED)    
        loc_entry.config(state=tk.DISABLED)
        loc_radius.config(state=tk.DISABLED)    

      
def checkyear(year):
    loc_entry_var.set(str(year_var_2.get())+"001")
    #Check to see if year_var_1 > year_var 2, change year_var 1 to be a year less, unless the year is 1996
    

def check_loc_dd_type(string):
    if location_var_1.get() == 'By ID':
        loc_entry_var.set(str(year_var_2.get())+"001")
    elif location_var_1.get() == 'By Address':
        loc_entry_var.set("611 Access Road Startford CT")




    
root = tk.Tk()                 
root.title("RACE GIS "+str(VERSION))


##YEARS##
year_choices = []
year_var_1 = tk.StringVar()
year_var_1.set(str(now.year))
year_var_2 = tk.StringVar()
year_var_2.set(str(now.year))
for x in range(1995,now.year+1):
    year_choices.append(x)
    
years = ttk.Labelframe(root,text="Years")
to_label = tk.Label(years, text="to")
from_label = tk.Label(years, text="From")


years.grid(row=0, column=1,columnspan=2,sticky=tk.W+tk.E,ipadx=2,ipady=2,padx=2,pady=2)
from_label.grid(row=0,column=1)
year_menu_1 = tk.OptionMenu(years,year_var_1, *year_choices)
year_menu_1.grid(row=0,column=2)
to_label.grid(row=0,column=3)

year_menu_2 = tk.OptionMenu(years,year_var_2, *year_choices,command=checkyear)
year_menu_2.grid(row=0,column=4)


###PROJECTS###
projects = ttk.Labelframe(root,text="Project Types")
projects.grid(row=1, column=1,sticky=tk.N,ipadx=2,ipady=2,padx=2,pady=2)

all_proj_var = tk.IntVar(value=1)
all_proj_checkbox = tk.Checkbutton(projects, text="All",variable=all_proj_var,command=all_proj)
all_proj_checkbox.grid(row=0, column=1,sticky=tk.W)

dredge_var = tk.IntVar(value=1)
dredge_checkbox = tk.Checkbutton(projects, text="Dredging",variable=dredge_var,command=proj)
dredge_checkbox.grid(row=1, column=1,sticky=tk.W)

floodwave_var = tk.IntVar(value=1)
floodwave_checkbox = tk.Checkbutton(projects, text="Flood / Wave Study",variable=floodwave_var,command=proj)
floodwave_checkbox.grid(row=2, column=1,sticky=tk.W)

hydro_var = tk.IntVar(value=1)
hydro_checkbox = tk.Checkbutton(projects, text="Hydrographic Survey",variable=hydro_var,command=proj)
hydro_checkbox.grid(row=3, column=1,sticky=tk.W)

pierdock_var = tk.IntVar(value=1)
pierdock_checkbox = tk.Checkbutton(projects, text="Pier / Dock",variable=pierdock_var,command=proj)
pierdock_checkbox.grid(row=4, column=1,sticky=tk.W)

floodcontrol_var = tk.IntVar(value=1)
floodcontrol_checkbox = tk.Checkbutton(projects, text="Flood / Erosion Control",variable=floodcontrol_var,command=proj)
floodcontrol_checkbox.grid(row=5, column=1,sticky=tk.W)

upland_var = tk.IntVar(value=1)
upland_checkbox = tk.Checkbutton(projects, text="Upland Structure",variable=upland_var,command=proj)
upland_checkbox.grid(row=6, column=1,sticky=tk.W)

facilities_var = tk.IntVar(value=1)
facilities_checkbox = tk.Checkbutton(projects, text="Facilities Assessment",variable=facilities_var,command=proj)
facilities_checkbox.grid(row=7, column=1,sticky=tk.W)

beach_var = tk.IntVar(value=1)
beach_checkbox = tk.Checkbutton(projects, text="Beach Nourishment",variable=beach_var,command=proj)
beach_checkbox.grid(row=8, column=1,sticky=tk.W)

construction_var = tk.IntVar(value=1)
construction_checkbox = tk.Checkbutton(projects, text="Construction Admin",variable=construction_var,command=proj)
construction_checkbox.grid(row=9, column=1,sticky=tk.W)

other_var = tk.IntVar(value=1)
other_checkbox = tk.Checkbutton(projects, text="Other",variable=other_var,command=proj)
other_checkbox.grid(row=10, column=1,sticky=tk.W)
#############

###CLIENTS###
clients = ttk.Labelframe(root,text="Client Types")
clients.grid(row=1,column=2,sticky=tk.N+tk.S,ipadx=2,ipady=2,padx=2,pady=2)

all_client_var = tk.IntVar(value=1)
all_proj_checkbox = tk.Checkbutton(clients, text="All",variable=all_client_var,command=all_client)
all_proj_checkbox.grid(row=0, column=1,sticky=tk.W)

residential_var = tk.IntVar(value=1)
residential_checkbox = tk.Checkbutton(clients, text="Residential",variable=residential_var,command=client)
residential_checkbox.grid(row=1, column=1,sticky=tk.W)

government_var = tk.IntVar(value=1)
government_checkbox = tk.Checkbutton(clients, text="Goverment",variable=government_var,command=client)
government_checkbox.grid(row=2, column=1,sticky=tk.W)

myc_var = tk.IntVar(value=1)
myc_checkbox = tk.Checkbutton(clients, text="Marina / Yacht Club",variable=myc_var,command=client)
myc_checkbox.grid(row=3, column=1,sticky=tk.W)

util_var = tk.IntVar(value=1)
util_checkbox = tk.Checkbutton(clients, text="Utility / Industrial",variable=util_var,command=client)
util_checkbox.grid(row=4, column=1,sticky=tk.W)

consultant_var = tk.IntVar(value=1)
consultant_checkbox = tk.Checkbutton(clients, text="Consultant",variable=consultant_var,command=client)
consultant_checkbox.grid(row=5, column=1,sticky=tk.W)

contractor_var = tk.IntVar(value=1)
contractor_checkbox = tk.Checkbutton(clients, text="Contractor",variable=contractor_var,command=client)
contractor_checkbox.grid(row=6, column=1,sticky=tk.W)
#############

###EXTRAS###
extras = ttk.Labelframe(root,text="Extras")
extras.grid(row=2,column=2,sticky=tk.W+tk.E,ipadx=2,ipady=2,padx=2,pady=2)

permit_var = tk.IntVar(value=0)
permit_checkbox = tk.Checkbutton(extras, text="Permit",variable=permit_var)
permit_checkbox.grid(row=0, column=1,sticky=tk.W)

boring_var = tk.IntVar(value=0)
boring_checkbox = tk.Checkbutton(extras, text="Boring",variable=boring_var)
boring_checkbox.grid(row=1, column=1,sticky=tk.W)
#############

###DEEP ZONES###
deep = ttk.Labelframe(root,text="DEEP Zones")
deep.grid(row=2,sticky=tk.W+tk.E, column=1,ipadx=2,ipady=2,padx=2,pady=2)

aquifer_var = tk.IntVar(value=0)
aquifer_checkbox = tk.Checkbutton(deep, text="Aquifer Protection",variable=aquifer_var)
aquifer_checkbox.grid(row=0, column=1,sticky=tk.W)

diversity_var = tk.IntVar(value=0)
diversity_checkbox = tk.Checkbutton(deep, text="Diversity Database",variable=diversity_var)
diversity_checkbox.grid(row=1, column=1,sticky=tk.W)
#############


##VISUALS##
visuals = ttk.Labelframe(root, text="Visuals")
visuals.grid(row=3,column=1,sticky=tk.W+tk.E,columnspan=2,ipadx=2,ipady=2,padx=2,pady=2)
heatmap_checkbox_var = tk.IntVar(value=0)
heatmap_checkbox = tk.Checkbutton(visuals, text="Heatmap",variable=heatmap_checkbox_var)
heatmap_checkbox.grid(row=0, column=1,sticky=tk.W)

#LOCATION
location_by_options = ['By Address','By ID']
location = ttk.Labelframe(root,text="Location")
location.grid(row=4,column=1,sticky=tk.W+tk.E,columnspan=2,ipadx=2,ipady=2,padx=2,pady=2)

loc_spec_var = tk.IntVar(value=0)
location_spec = tk.Checkbutton(location,text="Specify Location", command=location_spec, var=loc_spec_var)
location_spec.grid(row=0,column=1)

location_var_1 = tk.StringVar()
location_var_1.set('By ID')
location_drop_down = tk.OptionMenu(location,location_var_1, *location_by_options,command=check_loc_dd_type)

location_drop_down.grid(column=2,row=0,sticky=tk.W+tk.E)
location_drop_down.config(state=tk.DISABLED)

starting_point_label = tk.Label(location,text="Starting Point")
starting_point_label.grid(column=1,row=2,sticky=tk.W+tk.E)

loc_entry_var = tk.StringVar()
loc_entry = tk.Entry(location,textvariable=loc_entry_var)
loc_entry.config(state=tk.DISABLED)
loc_entry.config(font=("Arial",10))

loc_entry_var.set(str(year_var_2.get())+"001")
loc_entry.grid(column=2,row=2,sticky=tk.W+tk.E)

loc_radius_label = tk.Label(location,text="Radius (mi)")
loc_radius_label.grid(column=1,row=3,sticky=tk.W+tk.E)

loc_radius_var = tk.StringVar()
loc_radius = tk.Entry(location,textvariable=loc_radius_var)
loc_radius.config(state=tk.DISABLED)    
loc_radius_var.set("10")
loc_radius.grid(column=2,row=3)

#MAP
map_button = tk.Button(root,text='Google Earth',command='map_gen')
map_button.grid(row=5,column=1,sticky=tk.W+tk.E,ipadx=2,ipady=2,padx=2,pady=2)


#SPREADSHEET
excel_button = tk.Button(root,text='Excel',command='excel_gen')
excel_button.grid(row=5,column=2,sticky=tk.W+tk.E,ipadx=2,ipady=2,padx=2,pady=2)

root.mainloop()
