class Flight(object):
	def __init__(self,boids,interaction_params):

		self.interaction_params = interaction_params
		self.boids = boids

	def fly_towards_middle(self):

		middle_strength = self.interaction_params[0]
		for i in range(self.num_boids()):
			self.boids[:,2] = self.boids[:,2] + (self.boids[i,0] - self.boids[:,0] )*middle_strength/self.num_boids()
			self.boids[:,3] = self.boids[:,3] + (self.boids[i,1] - self.boids[:,1] )*middle_strength/self.num_boids()

		return self


	def fly_apart(self):

		retreat_distance = self.interaction_params[1]

		for i in range(self.num_boids()):
			target_indices = ( self.boids[i,0]-self.boids[:,0] )**2 + ( self.boids[i,1]-self.boids[:,1] )**2 < retreat_distance
			self.boids[:,2] = self.boids[:,2] + ( self.boids[:,0] - self.boids[i,0] )*target_indices.astype(float)
			self.boids[:,3] = self.boids[:,3] + ( self.boids[:,1] - self.boids[i,1] )*target_indices.astype(float)

		return self


	def fly_together(self):

		attraction_distance = self.interaction_params[2]
		drag_strength = self.interaction_params[3]

		for i in range(self.num_boids()):
			target_indices = ( self.boids[i,0]-self.boids[:,0] )**2 + ( self.boids[i,1]-self.boids[:,1] )**2 < attraction_distance
			self.boids[:,2] = self.boids[:,2] + ( self.boids[:,2] - self.boids[i,2] )*drag_strength/self.num_boids()*target_indices.astype(float)
			self.boids[:,3] = self.boids[:,3] + ( self.boids[:,3] - self.boids[i,3] )*drag_strength/self.num_boids()*target_indices.astype(float)

		return self


	def update_boids(self):

		self = self.fly_towards_middle().fly_apart().fly_together()

		self.boids[:,0] = self.boids[:,0] + self.boids[:,2]
		self.boids[:,1] = self.boids[:,1] + self.boids[:,3]

		return self

	def num_boids(self):
		return len(self.boids[:,0])

	def get_x(self):
		return self.boids[:,0]

	def get_y(self):
		return self.boids[:,1]

