'''
This program investigates the harmonic oscillations for any combinations of parameters the user would like to model. 
It generates a pdf file of three subplots showing the position of the mass attached to the spring 
when the driving frequency is half, same and double the natural frequency of the system. 
It also generates the graph of the amplitude as a function of w/w0.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#User Inputs:
mu=input("Enter the mass attached to the spring m=: ")
m=float(mu)
ku=input("Enter the spring constant k=: ")
k=float(ku)
cu=input("Enter the damping term c=: ")
c=float(cu)
fu=input("Enter the driving force Fo=: ")
f=float(fu)
    
w0=np.sqrt(k/m-c*c/(4*m*m)) #the natural angular frequency of the spring ω0
wLF=np.arange(0.0,2.5,0.01) #Creates the array containing many values for w as a fraction of w0
w_array=w0*wLF  
 
t0 = 0.0  #  Sets the initial time
tmax=500.0  #  Sets the final final time
steps=100000  # Sets the number of time step
tLF = np.linspace(t0, tmax, steps+1)  # Creates a 1-D array of time values

def deriv(yLF,tF,w): #Creates the function which computes the derivatives 
        x = yLF[0]
        v = yLF[1]
        return [v, (f*np.cos(w*tF)-k*x-c*v)/m]   # The function outputs [dx/dt, dV/dt]
    
in_cond = [0.0, 0.0]  # Creates an array with the initial condition for x-position and velocity.
A_array=[] #Creates the array which will contains the values of the amplitude for different w.

for w in w_array:
    position = odeint(deriv, in_cond, tLF, args = (w,))  #  The array containing the solution for the differential equation
    A=max(np.abs(position[(steps-10000):steps,0])) #Take the amplitude to be the max value of x amongst the last 10 000 points 
    A_array.append(A)
    if (w==w0/2):
        plt.subplot(311)
        plt.plot(tLF,position[:,0])
        plt.title('A model of an oscillator with parameters: \n mass={}, stiffness k={}, \n damping force c={} and driving force f={}\n w=w0/2'.format(m,k,c,f))
    if (w==w0):
        plt.subplot(312)
        plt.plot(tLF,position[:,0])
        plt.ylabel('Displacement [meters]')
        plt.title('w=w0')
    if (w==2*w0):
        plt.subplot(313)
        plt.plot(tLF,position[:,0])
        plt.xlabel('Time [sec]')
        plt.title('w=2w0')
        
plt.savefig('oscillations.pdf')
plt.clf()
plt.plot(w_array/w0,A_array)
plt.xlabel('w/w0')
plt.ylabel('Amplitude A [m]')
plt.title('A model of an oscillator with parameters: \n mass={}, stiffness k={}, \n damping force c={} and driving force f={},'.format(m,k,c,f))
plt.savefig('resonance.pdf')

