import physicsSim
import physicsObject
import forces
from tkinter import *
import time
import math
import pdb

ti = 0.0
tf = 10.0
dt = 0.02
objects = []
simforces = []
sim = physicsSim.PhysicsSim(ti,tf,dt)

object_image_mapping = {}

def init_objects():
    ball1 = physicsObject.PhysicsObject()
    ball2 = physicsObject.PhysicsObject()
    ball2.set_velocity(1,5)
    ball2.set_accel(0,-9.8)
    ball2.set_mass(10)

    ball1.set_velocity(2,10)

    ball1.set_position(0,0)
    ball1.set_accel(0,-9.8)
    ball1.set_mass(10)
    objects.append(ball1)
    objects.append(ball2)

def init_forces():
    for b in objects:
        g = forces.Force()

        g.add_object(b)
        g.set_ycomp(-9.8*b.get_mass())

        b.add_force(g)
        simforces.append(g)

def init_images(objects,images):
    if len(objects) != len(images):
        raise ValueError("Unequal images for objects")
    for i in range(len(objects)):
        object_image_mapping[objects[i]] = images[i]    


gui = Tk()
gui.geometry("800x600")
gui.title("Projectile Simulation Animation")
canvas = Canvas(gui, width=800,height=600,bg='white')
canvas.pack()

ball1_image = canvas.create_oval(180,530,220,570, fill='red')
ball2_image = canvas.create_oval(180,530,220,570, fill='blue')
images = [ball1_image, ball2_image]




def init_sim():
    for b in objects:
        sim.add_object(b)


init_objects()
init_forces()
init_images(objects,images)
init_sim()


prevCoords = {}
for b in objects:
    positionX = b.get_position()[0]
    positionY = b.get_position()[1]
    coords = [0,0]
    coords[0] = positionX
    coords[1] = positionY
    prevCoords[b] = coords

print("Beginning Simulation")

while sim.simulate():

    for b in objects:
        newPosx = sim.get_object_data(b)[0][0]
        newPosy = sim.get_object_data(b)[0][1]
        
        delta_pos_x = newPosx - prevCoords[b][0]
        delta_pos_y = prevCoords[b][1] - newPosy
        # print("{}, {}".format(delta_pos_x,delta_pos_y))
        image = object_image_mapping[b]
        if newPosy > 0:
            canvas.move(image,delta_pos_x*100, delta_pos_y*100)
        prevCoords[b][0] = newPosx
        prevCoords[b][1] = newPosy
        gui.update()

    
    time.sleep(0.05)

print("Sim Complete")





