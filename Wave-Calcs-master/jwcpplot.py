#Stephen Duncanson
#Wave calc program for Jill

import math
import openpyxl
import os
import matplotlib.pyplot as plt

#Constants
ITERATION_LIMIT = 10000000000   #Limit of how many times it will iterate before giving up
ERROR_MARGIN    = 0.000100000   #Error must be < ERROR_MARGIN to be considered solved
GUESS_PERCENT   = 0.000010000   #When reguessing k, GUESS_PERCENT is the amount to multiply error by
G               = 32.17190000   #Constant for gravity

#filename = str(input("Enter the name of the file to open: "))

t_0 = float(input("Enter t (sec): "))               #Get t_0, Float type
d   = float(input("Enter water depth (ft): "))      #Get d, Float type
def get_k(t_0,d):
    t_vals = []
    k   = ((2*math.pi)**2)/(G*(t_0**2))                 #Assume tanh(kd) ~ 0, initial guess

    t_1 = (2*math.pi)/(math.sqrt(G*k*math.tanh(k*d)))   #Calculate t value from guess
    t_vals.append(t_1)
    e   = (math.fabs(t_1 - t_0))/t_0                    #Calculate error between t_0, t_1


    #print("Initial k guess: "+str(k))   #Print the initial k guess
    #print("t: "+str(t_1))               #Print t_1
    #print("Initial error: "+str(e))     #Print the initial error

    counter = 0

    while e > ERROR_MARGIN:
            counter +=1 
            #Calculate new k guess
            if t_1 < t_0:
                k = k-e*GUESS_PERCENT
            elif t_1 > t_0:
                k = k+e*GUESS_PERCENT
            #Calculate new t value
            t_1 = ((2*math.pi)/math.sqrt(G*k*math.tanh(k*d)))
            t_vals.append(t_1)
            #Calculate new error
            e = (math.fabs(t_1 - t_0))/t_0
            #print new values
            #print("k: "+str(k))   
            #print("t: "+str(t_1))    
            #print("error: "+str(e))

    return k, t_vals

k, t_vals = get_k(t_0,d)

plt.plot(t_vals)

t_true = [t_0 for x in range(len(t_vals))]

plt.plot(t_true)
plt.ylabel('some numbers')
plt.show()
