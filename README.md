# RACE-GIS
Summer 2019 Internship Project

I am a physics/engineering student, not a programmer. That's my excuse for why the code is like this.
Regardless, messy code gets the work done.

This program is designed specifically to work within the company enviorment, it won't work if you run the code as is.

This program takes data from two excel spreadsheets, 'projects.xlsx' and 'clients.xlsx' once verifying that both these spreadsheets exist in the required directory, it checks to see if a database spreadsheet has been made. 
If the database has not been created, or is missing, the program will first combine the two spreadsheets into a single one using openpyxl, it will also use geopy and nominatim to geocode an adress field and add that information to the database spreadsheet as well. This can be a lengthy operation, due to the throttled nature of Nominatim.
If the database has been created, the program will check to see if it is updated by comparing the length (in rows) of each spreadsheet. If they are unequal, the program will update the database for the number of rows which they are different by. 
If they are equal, the program will continue.

With the populated database, the program will display a helpful GUI for sorting the database.
The projects can be sorted by year, project type, client type, permit, boring, and whether they fall into DEEP Zones.
Visuals can be selected, such as a heatmap.
Also a location can be specified, choose a starting point (either by ID or address), and set a radius in miles in which to limit results. 

Three buttons are available along the bottom: Folder, spreadsheet, earth.
Clicking folder will open the project folders for all specified jobs.
Clicking spreadsheet will generate an excel spreadsheet containing the information of all specified jobs.
Clicking earth will generate a KML file with all selected jobs that will be opened in google earth. 


