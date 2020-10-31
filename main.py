import tkinter as tk
import forces
import physicsObject
import physicsSim

labels = []
entry_fields = []

objects = []
simforces = []
sim = physicsSim.PhysicsSim(0,1,0.1)
object_image_mapping = {}
master = tk.Tk()

def add_object_entry_field():
	labels.append(tk.Label(master,text="Object Name"))
	r = len(labels)
	labels[-1].grid(row=r)
	entry_fields.append(tk.Entry(master))
	entry_fields[-1].grid(row=r,column=1)

def remove_entry_field():
	global rows
	if len(labels) > 0:
		labels[-1].grid_forget()
		entry_fields[-1].grid_forget()
		labels.pop(-1)
		entry_fields.pop(-1)
		

def show_entry_fields():
	for i in range(rows):
		print("{} : {}".format(labels[i].text, entry_fields[i].get()))


def init_objects():
	pass

def init_forces():
	pass

def init_images(objects,images):
	pass

def init_sim():
	pass

def animate():
    gui = Tk()
    gui.geometry("800x600")
    gui.title("Projectile Simulation Animation")
    canvas = Canvas(gui, width=800,height=600,bg='white')
    canvas.pack()

    ball1_image = canvas.create_oval(180,530,220,570, fill='red')
    ball2_image = canvas.create_oval(180,530,220,570, fill='blue')
    images = [ball1_image, ball2_image]


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
            
            image = object_image_mapping[b]
            if newPosy >= 0:
                canvas.move(image,delta_pos_x*100, delta_pos_y*100)
            prevCoords[b][0] = newPosx
            prevCoords[b][1] = newPosy
        gui.update()
        time.sleep(0.05)
    print("Sim Complete")

def main():

	

	
	
	tk.Button(master, text='Add Object', command= add_object_entry_field).grid(row=0, sticky=tk.W, pady=4)
	tk.Button(master, text='Remove', command=remove_entry_field).grid(row=0,column=1)
	tk.mainloop()

if __name__=="__main__":
	main()