#Stephen Duncanson
#A study in Heatmaps
#7/24/2019

import geopy
import geopy.distance


#When I actually add this to the RACE-GIS program, this list of lats and longs will be generated as the list is filtered
#if passes filter -> add lat and long as a tuple to this list
#before the KML file is finished being written
#call this function with the list of lat longs and create the heatmap
#if heatmap.get():
#create_heatmap(list_of_lat_longs)
#in this example im using old jobs
list_of_lat_longs = [(41.2088457,-73.3945954),
                     (41.2098825,-73.1328486),
                     (41.2102034,-73.1294992),
                     (41.1681799,-73.1386122),
                     (41.3820431,-72.9177813),
                     (41.3323299,-72.9519936),
                     (41.7632012,-72.6811454)]

def create_heatmap(list_of_lat_longs):
    '''
    This function takes a list of tuples as a paremeter, I think thats what its called
    we don't particularly care here about the points themselves, that is handled by the placemarks
    as long as we keep them in pairs, we don't need to preserve any other information about them
    '''
    #1. Create the square
    lats = []
    longs = [] 
    for p in list_of_lat_longs:
        lats.append(p[0])
        longs.append(p[1])

    lats.sort()
    longs.sort()


    max_lat = lats[-1]
    min_lat = lats[0]
    max_long = longs[-1]
    min_long = longs[0]

##    bot_left = str(min_long)+','+str(min_lat)+',0\n'
##    top_left = str(min_long)+','+str(max_lat)+',0\n'
##    top_right = str(max_long)+','+str(max_lat)+',0\n'
##    bot_right = str(max_long)+','+str(min_lat)+',0\n'
##   
##    #maybe use style url's to specify themes
##
##    export_file = open('test.kml','w')
##    export_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
##    export_file.write('<kml xmlns="http://earth.google.com/kml/2.0"> <Document>\n')
##    export_file.write('<Placemark>\n')
##    export_file.write('\t<Polygon> <outerBoundaryIs>  <LinearRing> \n')
##    export_file.write('\t\t<coordinates>')
##    export_file.write(bot_left)
##    export_file.write(top_left)
##    export_file.write(top_right)
##    export_file.write(bot_right)
##    export_file.write(bot_left)
##    export_file.write('\t\t</coordinates>\n')
##    export_file.write('\t </LinearRing> </outerBoundaryIs> </Polygon>\n')
##    export_file.write(' <Style> ')
##    export_file.write('  <PolyStyle>  ')
##    export_file.write('   <color>#a00000ff</color>')
##    export_file.write('  <outline>0</outline>')
##    export_file.write('  </PolyStyle> ')
##    export_file.write('  </Style> ')
##    export_file.write('</Placemark>\n')
##    export_file.write('</Document> </kml>')


    #Start in SW corner (-,-)
    current_lat = float(min_lat)
    current_long = float(min_long)

    row_count = 0
    column_count = 0
    grid_points = []
    center_points = []
    current_point = (current_lat,current_long)
    grid_points.append(current_point)
    dist_xy = geopy.distance.geodesic(miles = 5)
    dist_c = geopy.distance.geodesic(miles = 0.70710678118)#sqrt(2)/2
    # Find all the grid points
    while current_long < max_long and current_long >= min_long: #Since we always go to min_long I need = here
        if current_lat < max_lat: 
            #print("1 ",end='')
            #step 1 up 
            start = geopy.Point(current_lat, current_long) #Starting point at current_lat and long

            dest = dist_xy.destination(start,0) # move upwards by 1 mile
            grid_points.append((dest.latitude,dest.longitude))
            row_count+=1
            current_lat = dest.latitude
            current_long = dest.longitude
            #print((dest.latitude,dest.longitude))
        elif current_lat > max_lat:
            #print("2 ",end='')
            start = geopy.Point(min_lat, current_long) #Starting point at current_lat and long
            dest = dist_xy.destination(start,90) # move right by 1 mile
            grid_points.append((dest.latitude,dest.longitude))
            #print((dest.latitude,dest.longitude))
            #go back to min_lat
            #set row_count to 0
            column_count +=1
            current_lat = dest.latitude
            current_long = dest.longitude

    print(grid_points)
    print(row_count/column_count)
    print(column_count)


create_heatmap(list_of_lat_longs)


