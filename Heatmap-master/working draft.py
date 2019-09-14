from PIL import Image
import sys
import math
import numpy
from random import uniform

#using a lot of code from jeff

points = []
MAX_X = 500
MAX_Y = 500

lats = []
longs = []
def newpoint():
        return uniform(41,43), uniform(-71,-73)

for x in range(500):
        points.append(newpoint())
        
for x in points:
    lats.append(x[0])
    longs.append(x[1])

lats.sort()
longs.sort()

MAX_LAT = lats[-1]
MIN_LAT = lats[0]
MAX_LON = longs[-1]
MIN_LON = longs[0]

#jeff code
IGNORE_DIST=0.01

def pixel_to_ll(x,y):
    delta_lat = MAX_LAT-MIN_LAT
    delta_lon = MAX_LON-MIN_LON

    #x is lon, y is lat
    #0,0 is MIN_LONG, MAX_LAT

    x_frac = float(x)/MAX_X
    y_frac = float(y)/MAX_Y

    lon = MIN_LON + x_frac*delta_lon
    lat = MAX_LAT - y_frac*delta_lat

    calc_x, calc_y = ll_to_pixel(lat,lon)

    return lat, lon

def ll_to_pixel(lat,lon):
    adj_lat = lat-MIN_LAT
    adj_lon = lon-MIN_LON

    delta_lat = MAX_LAT-MIN_LAT
    delta_lon = MAX_LON-MIN_LON

    lon_frac = adj_lon/delta_lon
    lat_frac = adj_lat/delta_lat

    x = int(lon_frac*MAX_X)
    y = int(lat_frac*MAX_Y)

    return x,y

def linear_regression(pairs):
    xs = [x for (x,y) in pairs]
    yx = [y for (x,y) in pairs]

    A = numpy.array([xs, numpy.ones(len(xs))])
    w = numpy.linalg.lstsq(A.T,ys)[0]

    return w[0], w[1]

def distance_squared(x1,y1,x2,y2):
    return(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

def distance(x1,y1,x2,y2):
    return math.sqrt(distance_squared(x1,y1,x2,y2))


def color(val):
    if val == None:
        return (255,255,255,0)

    #0-1 scale
    #by .18s
    colors = [(255, 0, 0),
              (255, 91, 0),
              (255, 127, 0),
              (255, 171, 0),
              (255, 208, 0),
              (255, 240, 0),
              (255, 255, 0),
              (218, 255, 0),
              (176, 255, 0),
              (128, 255, 0),
              (0, 255, 0),
              (0, 255, 255),
              (0, 240, 255),
              (0, 213, 255),
              (0, 171, 255),
              (0, 127, 255),
              (0, 86, 255),
              (0, 0, 255),
              ]

    if val <= .5:
        return colors[17]
    elif val <= .10:
        return colors[16]
    elif val <= .15:
        return colors[15]
    elif val <= .20:
        return colors[14]
    elif val <= .25:
        return colors[13]
    elif val <= .30:
        return colors[12]
    elif val <= .35:
        return colors[11]
    elif val <= .40:
        return colors[10]
    elif val <= .45:
        return colors[9]
    elif val <= .50:
        return colors[8]
    elif val <= .55:
        return colors[7]
    elif val <= .60:
        return colors[6]
    elif val <= .65:
        return colors[5]
    elif val <= .70:
        return colors[4]
    elif val <= .75:
        return colors[3]
    elif val <= .80:
        return colors[2]
    elif val <= .85:
        return colors[1]
    else:
        return colors[0]

    #if value in x percentile return x color
    #hardcoded.


gaussian_variance = IGNORE_DIST/2
gaussian_a = 1 / (gaussian_variance * math.sqrt(2 * math.pi))
gaussian_negative_inverse_twice_variance_squared = -1 / (2 * gaussian_variance * gaussian_variance)

def gaussian(points, lat, lon):
    num = 0
    c = 0

    for p in points:
        plat = p[0]
        plon = p[1]
        weight = gaussian_a * math.exp(distance_squared(lat,lon,plat,plon) *
                                       gaussian_negative_inverse_twice_variance_squared)

        num += weight
        
        if weight > 2:
            c += 1

    # don't display any averages that don't take into account at least five data points with significant weight
    if c < 1:
        return None

    return num


def start():
    val = {}
    #find the value for each pixel
    for x in range(MAX_X):
        for y in range(MAX_Y):
            lat, lon = pixel_to_ll(x,y)
            val[x,y] = gaussian(points, lat, lon)


    #normalize data values between 0-1
    biggest_val = 0
    for value in val.values():
        #print(value)
        try:
            if value > biggest_val:
                biggest_val = value
        except:
            TypeError
    for key in val:
        try:
            val[key] = val[key]/biggest_val
            #print(val[key])
        except:
            TypeError
    I = Image.new('RGBA', (MAX_X, MAX_Y))
    IM = I.load()
    for x in range(MAX_X):
        for y in range(MAX_Y):
            IM[x,y] = color(val[x,y])

    I.save('text' + ".png", "PNG")


if __name__ == "__main__":
    start()
