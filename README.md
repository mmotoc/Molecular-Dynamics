# Molecular-Dynamics
To track the movement of different types of molecules. 


#! python3
#
# Biophysics 117 : April 25 2018 : Michael Motoc : particle.py
#
'''
To make a path for particles that diffuse
'''

import numpy as np
import matplotlib.pyplot as plt

class Particle:
    
    def __init__(self,name, position, mass, v):
        self.position = position
        self.name = name
        self.mass = mass
        self.v = v
        self.oldx=[]
        self.oldy=[]
        
    def current_position(self):
        print(position)
        print(name + "is located at " + position)

    def getX(self):
        return self.position[0]

    def getY(self):
        return self.position[1]

    def getMass(self):
        return self.mass

    def changeX(self, x):
        self.position[0] = x

    def changeY(self, y):
        self.position[1] = y
        
    def update_position(self,newx, newy):
        self.oldx.append(self.position[0])
        self.oldy.append(self.position[1])
        self.position[0] = newx+self.oldx[-1]
        self.position[1] = newy+self.oldy[-1]

    def take_random_step(self,D):
         self.newx = D*self.v*np.random.randn()
         self.newy = D*self.v*np.random.randn() 
         self.update_position(self.newx, self.newy)

    def take_random_steps(self,D, nsteps):
        for int in range(0, nsteps):
            self.take_random_step(D)

    def plot_trajectory(self):
        plt.plot(self.oldx, self.oldy, '-', label = "first particle")
        plt.ylabel("y displacement")
        plt.xlabel("x displacement")
        legend = plt.legend(loc = 'best', shadow = True)
        plt.axis("equal")


class ImmobileParticle(Particle):
    def __init__(self, name, position, mass, v):
        super(Particle, self).__init__()
        self.position = position
        self.name = name
        self.mass = mass
        self.v = v
        self.oldx = []
        self.oldy = []
        self.orgx = position[0]
        self.orgy = position[1]
        
    def update_position(self,newx, newy):
        self.oldx.append(self.position[0])
        self.oldy.append(self.position[1])
        self.position[0] = newx
        self.position[1] = newy
        
    def take_random_step(self,D):
        self.newx = D*self.v*np.random.randn() + self.position[0]
        self.newy = D*self.v*np.random.randn() + self.position[1]
        self.update_position(self.newx, self.newy)
        self.update_position(self.orgx, self.orgy)
        
    def take_random_steps(self,D, nsteps):
        for int in range(0, nsteps):
            self.take_random_step(D)
            
    def plot_trajectory(self):
        plt.plot(self.oldx, self.oldy, '-', label = "Immobile particle")
        plt.ylabel("y displacement")
        plt.xlabel("x displacement")
        legend = plt.legend(loc = 'best', shadow = True)
        plt.axis("equal")
        

class PartiallyBoundParticle(Particle): #Moves only within a certain radius 
    def __init__(self, name, position, mass, v):
        super(Particle, self).__init__()
        self.position = position
        self.name = name
        self.mass = mass
        self.v = v
        self.oldx = []
        self.oldy = []
        self.orgx = position[0]
        self.orgy = position[1]
        
    def update_position(self,newx, newy):
        self.oldx.append(self.position[0])
        self.oldy.append(self.position[1])
        self.position[0] = newx
        self.position[1] = newy
        
    def take_random_step(self,D):
        distx = D*self.v*np.random.randn()
        disty = D*self.v*np.random.randn()
        
        if (distx <= self.position[0] + D and distx >= self.position[0] - D
            and disty <= self.position[1] + D and disty >= self.position[1] - D):
            self.newx = distx
            self.newy = disty
            self.update_position(self.newx, self.newy)
            
        
    def take_random_steps(self, D, nsteps):
        for int in range(0, nsteps):
            self.take_random_step(D)
            
    def plot_trajectory(self):
        plt.plot(self.oldx, self.oldy, '-', label = "Partially Bound Particle")
        plt.ylabel("y displacement")
        plt.xlabel("x displacement")
        legend = plt.legend(loc = 'best', shadow = True)
        plt.axis("equal")



class BlackHole(Particle): #Impacts position, v, mass of other particles
    def __init__(self, name, position, mass, size):
        super(Particle, self).__init__()
        self.position = position
        self.name = name
        self.mass = mass
        self.size = size
        self.r = (2 * (6.674) * 100 * self.mass) / 9
        self.oldx = []
        self.oldy = []
        self.orgx = position[0]
        self.orgy = position[1]

    def update_radius(self):
        r = (2 * (6.674) * 100 * self.mass) / 9

    def is_near(self, Particle):
        if (Particle.getX(self) <= self.orgx + self.r and
            Particle.getX(self) >= self.orgx - self.r and
            Particle.getY(self) <= self.orgy + self.r and
            Particle.getY(self) >= self.orgy - self.r ):
            return True
        
    def getParticles(self, Particle):
        if (self.is_near(Particle)):
            self.mass = self.mass + Particle.getMass(self)
            Particle.v = 0
            Particle.changeX(self, self.oldx[-1])
            Particle.changeY(self, self.oldy[-1])
            self.update_radius()
            self.update_size()
            del Particle

    def update_position(self,newx, newy):
        self.oldx.append(self.position[0])
        self.oldy.append(self.position[1])
        self.position[0] = newx
        self.position[1] = newy

    def update_size(self):
        self.size += 1
        
    def take_random_step(self,D):
         self.newx = self.orgx + self.size*np.random.rand()
         self.newy = self.orgy + self.size*np.random.rand()
         self.update_position(self.newx, self.newy)

    def take_random_steps(self,D, nsteps):
        for int in range(0, nsteps):
            self.take_random_step(D)
            
    def plot_trajectory(self):
        plt.plot(self.oldx, self.oldy, '-', label = "Black Hole")
        plt.ylabel("y displacement")
        plt.xlabel("x displacement")
        legend = plt.legend(loc = 'best', shadow = True)
        plt.axis("equal")
