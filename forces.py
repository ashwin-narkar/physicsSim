class Force():

	# Each force correponds to an object

	def __init__(self):
		self.fx = 0
		self.fy = 0
		
		self.object = None
		
	def add_object(self, o):
		self.object = o
		
	def get_object(self):
		return self.object

	def set_xcomp(self,x):
		self.fx = x

	def set_ycomp(self,y):
		self.fy = y

	def get_force(self):
		return (self.fx,self.fy)

	def update_force(self):
		pass

class SpringForce(Force):
	def __init__(self,k,eqPos):
		super().__init__()
		self.k = k
		self.equilPosition = eqPos



	def update_force(self):
		self.fx = -1 * self.k * (self.object.get_position()[0] - self.equilPosition[0])
		self.fy = -1 * self.k * (self.object.get_position()[1] - self.equilPosition[1])
		
