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
list_of_lat_longs = [('',''),
                     ('',''),
                     ('',''),
                     ('',''),
                     ('',''),
                     ('',''),
                     ('',''),]

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
    current_lat = min_lat
    current_long = min_long

    grid_points = []
    current_point = (current_lat,current_long)
    grid_points.append(current_point)
    # Find all the grid points
    while current_lat < max_lat and current_long < max_long:
        if current_lat < max_lat:
            #step 1 up 
            start = geopy.Point(current_lat, current_long) #Starting point at current_lat and long
            dist_xy = geopy.distance.geodesic(miles = 1)
            dist_c = geopy.distance.geodesic(miles = 0.70710678118)#sqrt(2)/2
            dest = dist_xy.destination(start,0) # move upwards by 1 mile
            
        else:
            #Step right 1
            #go back to min_lat
            #set row_count to 0
            #Column count +=1

            
start = geopy.Point(48.853, 2.349)
dist_xy = geopy.distance.geodesic(miles = 1)
dist_c = geopy.distance.geodesic(miles = 0.70710678118)#sqrt(2)/2
dest = dist_xy.destination(start,0)
center_point = dist_c.distance(start,45) #45 degree heading?

print(dest.latitude)
print(dest.longitude)






