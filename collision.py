#! python3
#
#Biophysics 117 : April 25 2018 : Michael Motoc : Collision checker 
#
'''
To simulate and track the collisions between particles
'''


'''
How to check collisions:
    -track movement of each particle
    -if [x1,y1] of particle1 == [x2, y2] of particle 2
        -use collision equation to determine new location
            -based on masses of particles
            -update positions of particles
'''


def check_collisions(*args):
    for Particle in args:
        if Particle.position[0] == Particle.other.position[0]:
            if Particle.self.position[1] == Particle.other.position[1]:
                return True

def change_speeds(






                
            Particle.self.v = (((Particle.self.mass - Particle.other.mass) / (Particle.self.mass + Particle.other.mass))*Particle.self.v)+ (((2 * Particle.other.mass)/ (Particle.self.mass + Particle.other.mass))*Particle.other.v)
                Particle.other.v = (((2 * Particle.self.mass) / (Particle.self.mass + Particle.other.mass))*Particle.self.v) + (((Particle.other.mass - Particle.self.mass)/(Particle.self.mass + Particle.other.mass))*Particle.other.v)

    


