import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#User Input:
#mu=input("Enter the mass attached to the spring m=: ")
#m=int(ku)
#ku=input("Enter the spring constant k=: ")
#k=int(ku)
#cu=input("Enter the damping term c=: ")
#c=int(ku)
#fu=input("Enter the driving force Fo=: ")
#f=int(ku)
    
m=1
k=100
c=2.0
f=5

w0=np.sqrt(k/m) #the natural angular frequency of the spring ω0
print(w0)
w=2*w0 # driven force angular frequency ω
   
t0 = 0.0  #  Sets the initial time
tmax=10.0  #  Sets the final final time
steps=1200  # Sets the number of time step
tLF = np.linspace(t0, tmax, steps+1)  # Creates a 1-D array of time values

in_cond = [0.0, 0.0]  # Creates an array with the initial condition for x-position and velocity.

def deriv(yLF,tF): #Creates the function which computes the derivatives 
    x = yLF[0]
    v = yLF[1]
    return [v, (f*np.cos(w*tF)-k*x-c*v)/m]   # The function outputs [dx/dt, dV/dt]



position = odeint(deriv, in_cond, tLF)  #  The array containing the solution for the differential equation
print(position)
A1=max(position[(steps-100):steps,0])
#A2=max(position[(2/3)*tmax:steps,0])
print(A1)
plt.clf()
plt.plot(tLF,position[:,0])
plt.xlabel('Time [sec]')
plt.ylabel('Displacement [meters]')
plt.title('A model of an oscillator with parameters: \n mass={}, stiffness k={}, \n damping force c={} and driving force f={},'.format(m,k,c,f))
#plt.savefig('oscillations.pdf')
plt.show()