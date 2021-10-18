#Asher Shores
#Dr. Ricardo Citro
#This is my own work

#Differential Equations:
# y"+2y'+2=2x;t>=0;y(0)=y'(0)=0
# y"+y=4;t>=0;y(0)=y'(0)=0

#Implementation
#Use numerical and odeint based methods to create and solve differential equations.
#Solve dy/dx compare results.

import numpy as np                  #import lib numpy as np for math
import matplotlib.pyplot as plt     #import lib matplotlib to graph
from scipy.integrate import odeint  #importing scipy to use ODEINT

#ODEs models
#Using U as a vector to contain terms of the ODE
def dU0_dx(U, x):                           #inputs U and x
    return [U[1], -2 * U[1] + 2 * x - 2]    #returns the array of y' and -2y' + 2x -2

def dU1_dx(U, x):                           #inputs U and x
    return [U[1], 4 - U[0]]                 #returns the array of y' and 4 - y


#Green's formulas
def green1(x):
    return (0.5 * pow(x, 2)) - (1.5 * x) - (0.75 * np.exp(-2 * x)) + 0.75
    #based on manual solution shown in supporting document

def green2(x):
    return 4 - (4 * np.cos(x))
    #based on manual solution shown in supporting document


# ODEint solution


U0 = [0, 0]                     #vector for values of y and y'
xs0 = np.linspace(0, 10, 200)   #x space from 0-10 with n=200 steps
ys0 = odeint(dU0_dx, U0, xs0)   #y space using odeint to solve
ys0 = ys0[:,0]                  #y space

U1 = [0, 0]                     #vector for values of y and y'
xs1 = np.linspace(0, 10, 200)   #x space from 0-10 with n=200 steps
ys1 = odeint(dU1_dx, U1, xs1)   #y space using odeint to solve
ys1 = ys1[:,0]                  #y space


# Green's Forumla Solution

#Initial conditions
x = 0   #set x to 0
y0 = 0  #y0 to 0
y1 = 0  #y1 to 0

xs2 = []    #array to hold data
ys2 = []    #array to hold data
xs3 = []    #array to hold data
ys3 = []    #array to hold data

for i in range(0, 200): #for loop to run 200 times
    xs2.append(x)       #add the x-vals to the x-space
    ys2.append(y0)      #add the y-vals to the y-space
    xs3.append(x)       #add the x-vals to the x-space
    ys3.append(y1)      #add the y-vals to the y-space
    y0 = green1(x)      #update values
    y1 = green2(x)      #update values
    x += 0.05           #increment by (0.05)


# Plots

#ODE 1
plt.title("ODE Analysis #1")                                             #set the title
plt.xlabel("x")                                                         #label the x-axis
plt.ylabel("y")                                                         #label the y-axis
plt.plot(xs0, ys0, 'b-', label = "ODEint 1", linewidth = 2)             #label blue line
plt.plot(xs2, ys2, 'r-', label = "Green's Function 1", linewidth = 2)   #label red line
plt.legend()                                                            #add legend
plt.show()                                                              #plot and show graph

#ODES 2
plt.title("ODE Analysis #2")                                             #set the title
plt.xlabel("x")                                                         #label the x-axis
plt.ylabel("y")                                                         #label the y-axis
plt.plot(xs1, ys1, 'b-', label = "ODEint 2", linewidth = 2)             #label blue line
plt.plot(xs3, ys3, 'r-', label = "Green's Function 2", linewidth = 2)   ##label red line
plt.legend()                                                            #add legend
plt.show()                                                              #plot and show graph
