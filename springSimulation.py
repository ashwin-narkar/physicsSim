import physicsSim
import physicsObject
import forces
from tkinter import *
import time
import math

ti = 0.0
tf = 10.0
dt = 0.02
k=20
objects = []
simforces = []
images = []
sim = physicsSim.PhysicsSim(ti,tf,dt)

object_image_mapping = {}

def init_objects():
    ball1 = physicsObject.PhysicsObject()
   
    ball1.set_velocity(0,0)

    ball1.set_position(10,0)
    ball1.set_accel(0,0)
    ball1.set_mass(10)
    objects.append(ball1)
   

def init_forces():
    for b in objects:
        spr = forces.SpringForce(k,(0,0))

        spr.add_object(b)
       

        b.add_force(spr)
        simforces.append(spr)
        spr.update_force()

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

ball1_image = canvas.create_oval(380,530,420,570, fill='red')

images.append(ball1_image)




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


for b in objects:
        delta_pos_x = prevCoords[b][0]
        delta_pos_y = -prevCoords[b][1] 
        # print("{}, {}".format(newPosx,newPosy))
        # print("{}, {}".format(delta_pos_x,delta_pos_y))
        image = object_image_mapping[b]
        canvas.move(image,delta_pos_x*10, delta_pos_y*10)


while sim.simulate():

    for b in objects:
        newPosx = sim.get_object_data(b)[0][0]
        newPosy = sim.get_object_data(b)[0][1]
        
        delta_pos_x = newPosx - prevCoords[b][0]
        delta_pos_y = prevCoords[b][1] - newPosy
        # print("{}, {}".format(newPosx,newPosy))
        # print("{}, {}".format(delta_pos_x,delta_pos_y))
        image = object_image_mapping[b]
        if newPosy >= 0:
            canvas.move(image,delta_pos_x*10, delta_pos_y*10)
        prevCoords[b][0] = newPosx
        prevCoords[b][1] = newPosy
        for f in b.get_forces():
        	f.update_force()
        gui.update()

    
    time.sleep(0.05)

print("Sim Complete")


