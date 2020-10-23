import physicsSim
import physicsObject
import forces
from tkinter import *
import time
import math

ti = 0.0
tf = 20.0
dt = 0.02


gui = Tk()
gui.geometry("800x600")
gui.title("Spring Simulation Animation")
canvas = Canvas(gui, width=800,height=600,bg='white')
canvas.pack()

sim = physicsSim.PhysicsSim(ti,tf,dt)

ball1 = physicsObject.PhysicsObject()

ball1.set_velocity(0,0)
ball1.set_position(5,0)
ball1.set_mass(10)

springforce = forces.Force(ball1)
k = 8
equilPosition = (0,0)
springforce.set_xcomp(-1*k* (ball1.get_position()[0] - equilPosition[0]) )

springforce.set_ycomp(0)
ball1.add_force(springforce)
sim.add_object(ball1)



ball1_image = canvas.create_oval(380,530,420,570, fill='red')

print("Beginning Simulation")

prev_x = ball1.get_position()[0]
prev_y = ball1.get_position()[1]

canvas.move(ball1_image,(prev_x)*20, (prev_y)*20)
sim_data = sim.simulate()


while sim_data is not None:
    new_x = sim_data[0][0] 
    new_y = -sim_data[0][1] 
    sim_data = sim.simulate()
    
    springforce.set_xcomp(-1*k*(ball1.get_position()[0]-equilPosition[0]))
    


    canvas.move(ball1_image,(new_x - prev_x)*20, (new_y - prev_y)*20)
    prev_y = new_y
    prev_x = new_x



    gui.update()
    time.sleep(0.01)

print("Sim Complete")





