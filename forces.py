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