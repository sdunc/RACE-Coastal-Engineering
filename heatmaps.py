#Stephen Duncanson
#A study in Heatmaps
#7/24/2019

import turtle

t = turtle.Turtle()
turtle.setworldcoordinates(0,0,10,10)
t.hideturtle()
t.penup()

points = [('1','3'),
          ('3','5'),
          ('2','7'),
          ('4','9'),
          ('6','2'),
          ('7','0'),
          ('3','6'),
          ('5','1'),
          ]

lats = []
longs = []


for p in points:
    t.setposition(int(p[1]),int(p[0]))
    lats.append(p[0])
    longs.append(p[1])
    t.dot()


lats.sort()
longs.sort()

max_lat = lats[0]
min_lat = lats[-1]

max_long = longs[0]
min_long = longs[-1]

t.setposition(int(min_long),int(max_lat))
t.pendown()
t.setposition(int(max_long),int(max_lat))
t.setposition(int(max_long),int(min_lat))
t.setposition(int(min_long),int(min_lat))
t.setposition(int(min_long),int(max_lat))

    
turtle.done()
