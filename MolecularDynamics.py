#! python3
#
#Biophysics 117 : April 25 2018 : Michael Motoc : Molecular Dynamics
#
'''
To simulate and track the movement of particles
'''

import numpy as np
import matplotlib.pyplot as plt
import random
from particle import Particle
from particle import ImmobileParticle
from particle import PartiallyBoundParticle
from particle import BlackHole

#Set Random spawn points
RandSpawnX = []
RandSpawnY = []
for int in range(0, 100):
    RandSpawnX.append(35 * np.random.randn())
    RandSpawnY.append(35 * np.random.randn())


#Set random masses for particles (kg)
RandMass = []
for int in range(0, 100):
    RandMass.append(10 * np.random.rand())

#Set random initial speeds for particles (m/s)
RandV = []
for int in range(0, 100):
    RandV.append(20 * np.random.rand())


class Particles:
    def __init__(self,name, position, mass, v):
        self.position = position
        self.name = name
        self.mass = mass
        self.v = v
        self.oldx = []
        self.oldy = []
        self.particle_list = []

    def addParticle(self,Particle):
        self.particle_list.append(Particle)

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
        
    def plot_traj(self):
        for int in range(0, len(self.particle_list)):
            particleN = self.particle_list[int]
            particle_name = particleN.name
            particle_positionx = particleN.oldx
            particle_positiony = particleN.oldy
            
            plt.plot(particle_positionx, particle_positiony, '-', label = particle_name)
            plt.ylabel("y displacement")
            plt.xlabel("x displacement")
            legend = plt.legend(loc = 'best', shadow = True)
            plt.axis("equal")

for int in range(0, 3):
    if __name__=='__main__':
        
        particles = Particles("Particles",
                              [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                              random.choice(RandMass),
                              random.choice(RandV))
        
        myimparticle1 = ImmobileParticle("Immobile Particle 1",
                                         [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                                         random.choice(RandMass),
                                         random.choice(RandV))
        myimparticle1.take_random_steps(1,100)
        particles.addParticle(myimparticle1)
        
        myimparticle2 = ImmobileParticle("Immobile Particle 2",
                                         [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                                         random.choice(RandMass),
                                         random.choice(RandV))
        myimparticle2.take_random_steps(1,100)
        particles.addParticle(myimparticle2)

        myimparticle3 = ImmobileParticle("Immobile Particle 3",
                                         [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                                         random.choice(RandMass),
                                         random.choice(RandV))
        myimparticle3.take_random_steps(1,100)
        particles.addParticle(myimparticle3)


        myparticle1 = Particle("Particle 1",
                               [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                               random.choice(RandMass),
                               random.choice(RandV))
        myparticle1.take_random_steps(1,100)
        particles.addParticle(myparticle1)

        myparticle2 = ImmobileParticle("Particle 2",
                                       [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                                       random.choice(RandMass),
                                       random.choice(RandV))
        myparticle2.take_random_steps(1,100)
        particles.addParticle(myparticle2)

        myparticle3 = Particle("Particle 3",
                               [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                               random.choice(RandMass),
                               random.choice(RandV))
        myparticle3.take_random_steps(1,100)
        particles.addParticle(myparticle3)


        myPBP1 = PartiallyBoundParticle("Partially Bound Particle 1",
                                        [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                                        random.choice(RandMass),
                                        random.choice(RandV))
        myPBP1.take_random_steps(1, 100) 
        particles.addParticle(myPBP1)

        myBH = BlackHole("Black Hole 1",
                         [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                         random.choice(RandMass),
                         0.75)
        myBH.take_random_steps(1,100)
        myBH.getParticles(Particle)
        myBH.update_radius()
        particles.addParticle(myBH)

        myBH2 = BlackHole("Black Hole 2",
                         [random.choice(RandSpawnX),random.choice(RandSpawnY)],
                         random.choice(RandMass),
                          1)
        myBH2.take_random_steps(1,100)
        myBH2.getParticles(Particle)
        myBH2.update_radius()
        particles.addParticle(myBH2)
    
    plt.tight_layout()
    particles.plot_traj()
    plt.title("Molecular Dynamics")
    plt.show()
