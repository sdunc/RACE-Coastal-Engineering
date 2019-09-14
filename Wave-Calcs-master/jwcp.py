#Stephen Duncanson
#Wave calc program for Jill

import math
import openpyxl
import os

#Constants
ITERATION_LIMIT = 10000     #Limit of how many times it will iterate before giving up
ERROR_MARGIN = 0.001        #Error must be < ERROR_MARGIN to be considered solved
GUESS_PERCENT = .1         #When reguessing k, GUESS_PERCENT is the amount to multiply error by
G = 32.1719                 #Constant for gravity


filename = str(input("Enter the name of the file to open: "))

spreadsheet = filename+"

t_0 = float(input("Enter t (sec): "))           #Get t_0, Float type
d   = float(input("Enter water depth (ft): "))  #Get d, Float type

k   = ((2*math.pi)**2)/(G*(t_0**2))             #Assume tanh(kd) ~ 0, initial guess

t_1 = (2*math.pi)/(math.sqrt(G*k*math.tanh(k*d)))   #Calculate t value from guess

e = (math.fabs(t_1 - t_0))/t_0      #Calculate error between t_0, t_1


print("Initial k guess: "+str(k)) #Print the initial k guess
print("t: "+str(t_1))               #Print t_1
print("Initial error: "+str(e))     #Print the initial error

counter = 0
for i in range(ITERATION_LIMIT):
    if e > ERROR_MARGIN:
        counter +=1 
        #Calculate new k guess
        if t_1 < t_0:
            k = k-e*GUESS_PERCENT
        elif t_1 > t_0:
            k = k+e*GUESS_PERCENT
        #Calculate new t value
        t_1 = ((2*math.pi)/math.sqrt(G*k*math.tanh(k*d)))
        #Calculate new error
        e = (math.fabs(t_1 - t_0))/t_0
        #print new values
        print("k: "+str(k))   
        print("t: "+str(t_1))    
        print("error: "+str(e))    
    else:
        print("Converged!")
        print(counter)
        break
    
print("Final error: "+str(e))
print("k: "+str(k))


        
            




