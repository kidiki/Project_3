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
k=500
c=0.5
f=5

w0=np.sqrt(k/m) #the natural angular frequency of the spring ω0
#w=2*w0 # driven force angular frequency ω
#wi=0.1
#wf=3.0
#points=20
#wLF=np.linspace(wi,wf,points+1)
wLF=np.arange(0.0,3.0,0.05)
w_array=w0*wLF  
 
t0 = 0.0  #  Sets the initial time
tmax=10.0  #  Sets the final final time
steps=1200  # Sets the number of time step
tLF = np.linspace(t0, tmax, steps+1)  # Creates a 1-D array of time values

in_cond = [0.0, 0.0]  # Creates an array with the initial condition for x-position and velocity.
A_array=[]
for w in w_array:
    def deriv(yLF,tF): #Creates the function which computes the derivatives 
        x = yLF[0]
        v = yLF[1]
        return [v, (f*np.cos(w*tF)-k*x-c*v)/m]   # The function outputs [dx/dt, dV/dt]
    position = odeint(deriv, in_cond, tLF)  #  The array containing the solution for the differential equation
    A=max(position[(steps-150):steps,0])
    A_array.append(A)
    if (w==w0/2):
        plt.subplot(311)
        plt.plot(tLF,position[:,0])
        #plt.xlabel('Time [sec]')
        #plt.ylabel('Displacement [meters]')
        plt.title('A model of an oscillator with parameters: \n mass={}, stiffness k={}, \n damping force c={} and driving force f={}\n w=w0/2'.format(m,k,c,f))
    if (w==w0):
        plt.subplot(312)
        plt.plot(tLF,position[:,0])
        #plt.xlabel('Time [sec]')
        plt.ylabel('Displacement [meters]')
        #plt.title('A model of an oscillator with parameters: \n mass={}, stiffness k={}, \n damping force c={} and driving force f={},'.format(m,k,c,f))
        plt.title('w=w0')
    if (w==2*w0):
        plt.subplot(313)
        plt.plot(tLF,position[:,0])
        plt.xlabel('Time [sec]')
        plt.title('w=2w0')
        
plt.savefig('oscillations.pdf')
plt.clf()
plt.plot(w_array/w0,A_array)
plt.title('A model of an oscillator with parameters: \n mass={}, stiffness k={}, \n damping force c={} and driving force f={},'.format(m,k,c,f))
plt.show()

