import physicsSim
import physicsObject
import forces
from tkinter import *
import time
import math

ti = 0.0
tf = 10.0
dt = 0.02

sim = physicsSim.PhysicsSim(ti,tf,dt)

ball1 = physicsObject.PhysicsObject()

ball1.set_velocity(2,10)

ball1.set_position(0,0)
ball1.set_accel(0,-9.8)
ball1.set_mass(10)

gravity = forces.Force(ball1)
g = -9.81
gravity.set_ycomp(g*ball1.get_mass())

ball1.add_force(gravity)
sim.add_object(ball1)

gui = Tk()
gui.geometry("800x600")
gui.title("Projectile Simulation Animation")
canvas = Canvas(gui, width=800,height=600,bg='white')
canvas.pack()

ball1_image = canvas.create_oval(180,530,220,570, fill='red')

print("Beginning Simulation")

prev_x = ball1.get_position()[0]
prev_y = -ball1.get_position()[1]
canvas.move(ball1_image,(prev_x)*10, (prev_y)*10)
sim_data = sim.simulate()


while sim_data is not None:
    new_x = sim_data[0][0] 
    new_y = sim_data[0][1] 

    sim_data = sim.simulate()
    
    
    canvas.move(ball1_image,(new_x - prev_x)*100, (prev_y-new_y)*100)
    prev_y = new_y
    prev_x = new_x
    if new_y < 0:
    	break
    gui.update()
    time.sleep(0.05)

print("Sim Complete")





