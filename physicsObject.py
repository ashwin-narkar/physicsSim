class PhysicsObject:
	def __init__(self):
		self.mass = 0
		self.position = [0,0]
		self.velocity = [0,0]
		self.accel = [0,0]
		self.forces = list()
		self.name = ""

	def set_mass(self,m):
		self.mass = m

	def set_position(self,x,y):
		self.position = [x,y]

	def set_velocity(self,vx,vy):
		self.velocity = [vx,vy]

	def set_accel(self,ax,ay):
		self.accel = [ax,ay]

	def add_force(self,f):
		self.forces.append(f)

	def update_accel(self):
		# take sum of forces, calculate acceleration
		if self.mass <= 0:
			raise ValueError("0 or negative mass object")
		for f in self.forces:
			if f.get_mass() != self.mass:
				raise ValueError("Unequal mass for force and object")
			(delta_ax, delta_ay) = f.get_accel()
			self.accel[0] = delta_ax
			self.accel[1] = delta_ay


	def update_velocity(self, delta_time):
		self.velocity[0] += self.accel[0] * delta_time
		self.velocity[1] += self.accel[1] * delta_time


	def update_position(self, delta_time):
		self.position[0] += self.velocity[0] * delta_time
		self.position[1] += self.velocity[1] * delta_time

	def get_position(self):
		return self.position

	def get_velocity(self):
		return self.velocity

	def get_accel(self):
		return self.accel

	def get_forces(self):
		return self.forces

	def get_mass(self):
		return self.mass

	def simulate(self, delta_time):
		self.update_accel()
		self.update_velocity(delta_time)
		self.update_position(delta_time)

class Force():
	def __init__(self, physicsObject):
		self.fx = 0
		self.fy = 0
		
		self.object = physicsObject
		self.mass = self.object.get_mass()

	def get_mass(self):
		return self.mass

	def set_mass(self,m):
		self.mass = m

	def set_xcomp(self,x):
		self.fx = x

	def set_ycomp(self,y):
		self.fy = y

	def get_force(self):
		return (self.fx,self.fy)

	def get_accel(self):
		if self.mass <= 0:
			raise ValueError("Negative or 0 mass object cannot have force")
		return (self.fx / self.mass , self.fy / self.mass)