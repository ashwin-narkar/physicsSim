class Force():
	def __init__(self, physicsObject):
		self.fx = 0
		self.fy = 0
		
		self.objects = []
		self.objects.append(physicsObject)
		
	def get_objects(self):
		return self.objects

	def set_xcomp(self,x):
		self.fx = x

	def set_ycomp(self,y):
		self.fy = y

	def get_force(self):
		return (self.fx,self.fy)

	def update_force(self):
		pass