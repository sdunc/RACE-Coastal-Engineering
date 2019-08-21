#Stephen Duncanson
#Town Counter
#Using Reverse geocoding
from geopy.geocoders import GoogleV3

GOOGLE_API_KEY = ''
geolocator = GoogleV3(api_key=GOOGLE_API_KEY)

export_file = open('town_count.txt','w')


lat_longs = open('lat_longs.csv','r')
list_of_lat_longs = []
for line in lat_longs:
    line_s = line.strip("\n''")
    line_sp =line_s.split(',')
    tup = tuple(float(s) for s in line_sp)
    list_of_lat_longs.append(tup)

towns = {}

for t_coords in list_of_lat_longs:
    try:
        adr = geolocator.reverse(t_coords, exactly_one=True)
        adr = adr.raw
        adr = adr['address_components']
        adr = adr[2]
        adr = str(adr['short_name']) #town name
    except:
        AttributeError

    if adr in towns:
        towns[adr] += 1
        print(adr)
    else: #town is not yet added
        towns[adr] = 1
        #print(adr)

for x, y in towns.items():
    export_file.write(str(x)+ ',')
    export_file.write(str(y)+'\n')

export_file.close()
    
    

