class PhysicsSim():
	def __init__(self, ti, tf, dt):
		self.objects = []
		self.time_initial = ti
		self.time = self.time_initial
		self.timeInterval = dt
		self.time_final = tf

	def add_object(self,o):
		self.objects.append(o)

	

	def simulate(self):
		if self.time <= self.time_final:
			for o in self.objects:
				(pos,vel,accel) = (o.get_position(),o.get_velocity(),o.get_accel())
				# print("Time: {}".format(self.time))
				# print("Position: {}".format(pos))
				# print("Velocity: {}".format(vel))
				# print("Acceleration: {}".format(accel))
				o.simulate(self.timeInterval)
				self.time += self.timeInterval
			return (pos,vel,accel)
		else:
			return None
