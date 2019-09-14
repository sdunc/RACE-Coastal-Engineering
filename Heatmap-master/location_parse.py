#Stephen Duncanson
#A messy script to clean up JSON location export
#Get all Lats longs
#save as txt
#in form (lat,long)
#important note!
#The addition of the decimal into the lat and long is
#hard coded for my area ~41.xx,-73.xx,
#it would require more code to account for the character of the - and
#make a general solution

open_file = open("loc.json","r")
write_file = open("out.txt","w")

saved_lines = []


for line in open_file:
    line_r = line.split()
    if line_r[0] == '"latitudeE7"':
        lat = line_r[2].strip("'")
        lat = lat[:2]+'.'+lat[2:]
        write_file.write(lat)
        
    elif line_r[0] == '"longitudeE7"':
        long = line_r[2].strip("',")
        long = long[:3]+'.'+long[3:]
        write_file.write(long+'\n')
    

open_file.close()
write_file.close()
