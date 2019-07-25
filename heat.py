#Stephen Duncanson
#A study in Heatmaps
#7/24/2019

import geopy
import math
import geopy.distance
import random
from geopy.distance import geodesic



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

    #Start in SW corner (-,-)
    STEP_AMOUNT = 1#length of each square 
    steps_right = 0
    
    current_lat = float(min_lat)
    current_long = float(min_long)
    
    dist_xy = geopy.distance.geodesic(miles = STEP_AMOUNT)
    dist_z = geopy.distance.geodesic(miles = (math.sqrt(2)*STEP_AMOUNT))
    dist_c = geopy.distance.geodesic(miles = (math.sqrt(2)*STEP_AMOUNT)/2)#sqrt(2n)/2
    
    grids = []
    
    # Find all the grid points
    while current_long < max_long and current_long >= min_long: #Since we always go to min_long I need = here
        if current_lat < max_lat:
            t_grid = [0,0,0,0]
            start = geopy.Point(current_lat, current_long) #Starting point at current_lat and lon
            dest_up = dist_xy.destination(start,0) # move upwards 
            dest_right = dist_xy.destination(start,90) #move right
            dest_corner = dist_z.destination(start,45)  #move diagonally
            t_grid[0] = (current_lat, current_long)
            t_grid[1] = (dest_up.latitude,dest_up.longitude)
            t_grid[2] = (dest_corner.latitude,dest_corner.longitude)
            t_grid[3] = (dest_right.latitude,dest_right.longitude)
            
            current_lat = dest_up.latitude

            grids.append(t_grid)
            
        elif current_lat > max_lat:
            steps_right +=1
            current_lat = min_lat
            origin = geopy.Point(min_lat, min_long)
            dist_x = geopy.distance.geodesic(miles = STEP_AMOUNT*steps_right)
            dest_right = dist_x.destination(origin,90)
            current_long = dest_right.longitude



    center_points = []
    #find all centers
    
    for grid in grids:
        corner = geopy.Point(grid[0][0], grid[0][1])
        center = dist_c.destination(corner,45)
        center_points.append((center.latitude,center.longitude))
    #print(center_points)
        

    #calculate a_values for each center
    
    R_FACTOR = 6
    a_vals = []
    for center in center_points:
        a_val = 0
        for point in list_of_lat_longs:
            distance = geodesic(center,point).miles
            a_point_val = math.exp(-1*(distance**2/(R_FACTOR*STEP_AMOUNT)))
            a_val += a_point_val
        a_vals.append(a_val)
        print(a_val)
        
    #a_vals_ordered = a_vals
    #a_vals_ordered.sort()
    #max_a_val = a_vals_ordered[-1]

    #for x in range(len(a_vals)):
    #    a_vals[x] = a_vals[x]/max_a_val #get a value between 0 and 1


        


    export_file = open('test.kml','w')
    export_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    export_file.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
    export_file.write(' <Document>\n')
    export_file.write('  <Style id="red">\n')
    export_file.write('   <PolyStyle>\n')
    export_file.write('    <color>6f0000ff</color>\n')
    export_file.write('     <outline>0</outline>\n')
    export_file.write('   </PolyStyle>\n')
    export_file.write('  </Style>\n')
    
    export_file.write('  <Style id="yellow">\n')
    export_file.write('   <PolyStyle>\n')
    export_file.write('    <color>6f00ffff</color>\n')
    export_file.write('     <outline>0</outline>\n')
    export_file.write('   </PolyStyle>\n')
    export_file.write('  </Style>\n')

    export_file.write('  <Style id="green">\n')
    export_file.write('   <PolyStyle>\n')
    export_file.write('    <color>6f00ff00</color>\n')
    export_file.write('     <outline>0</outline>\n')
    export_file.write('   </PolyStyle>\n')
    export_file.write('  </Style>\n')

    export_file.write('  <Style id="blue">\n')
    export_file.write('   <PolyStyle>\n')
    export_file.write('    <color>6fff0000</color>\n')
    export_file.write('     <outline>0</outline>\n')
    export_file.write('   </PolyStyle>\n')
    export_file.write('  </Style>\n')

    export_file.write('  <Style id="black">\n')
    export_file.write('   <PolyStyle>\n')
    export_file.write('    <color>00000000</color>\n')
    export_file.write('     <outline>0</outline>\n')
    export_file.write('   </PolyStyle>\n')
    export_file.write('  </Style>\n')
    
    counter = 0
    for g in grids:
        #print(g)
        corners = g
        bot_left_s = ''
        top_left_s = ''
        top_right_s = ''
        bot_right_s = ''
        for i in reversed(corners[0]):
            bot_left_s = bot_left_s+str(i)+','
        for i in reversed(corners[1]):
            top_left_s = top_left_s+str(i)+','
        for i in reversed(corners[2]):
            top_right_s = top_right_s+str(i)+','
        for i in reversed(corners[3]):
            bot_right_s = bot_right_s+str(i)+','
            
        bot_left = '     '+bot_left_s+'0\n'
        top_left = '     '+top_left_s+'0\n'
        top_right = '     '+top_right_s+'0\n'
        bot_right = '     '+bot_right_s+'0\n'

        i = random.randint(1,5)
        
        export_file.write('  <Placemark>\n')
        if a_vals[counter] <= .1:
            export_file.write('   <styleUrl>#black</styleUrl>\n')
        elif a_vals[counter] <= .8:
            export_file.write('   <styleUrl>#blue</styleUrl>\n')
        elif a_vals[counter] <= 1.2:
            export_file.write('   <styleUrl>#green</styleUrl>\n')

        elif a_vals[counter] <= 1.4:
            export_file.write('   <styleUrl>#yellow</styleUrl>\n')
        else:
            export_file.write('   <styleUrl>#red</styleUrl>\n')


        export_file.write('   <Polygon> <outerBoundaryIs>  <LinearRing> \n')
        export_file.write('    <coordinates>\n')
        export_file.write(bot_left)
        export_file.write(bot_right)
        export_file.write(top_right)
        export_file.write(top_left)
        export_file.write(bot_left)
        
       

        export_file.write('   </coordinates>\n')
        export_file.write('  </LinearRing> </outerBoundaryIs> </Polygon>\n')
        export_file.write(' </Placemark>\n')
        counter+=1

        
    export_file.write(' </Document>\n')
    export_file.write('</kml>')
   
    export_file.close()

create_heatmap(list_of_lat_longs)



