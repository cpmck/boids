class Flight(object):
	def __init__(self,boids,interaction_params):

		self.interaction_params = interaction_params
		self.boids = boids

	def fly_towards_middle(self):

		middle_strength = self.interaction_params[0]
		num_boids = len(self.boids[:,0])

		for i in range(num_boids):
			self.boids[:,2] = self.boids[:,2] + (self.boids[i,0] - self.boids[:,0] )*middle_strength/len(self.boids[:,0])
			self.boids[:,3] = self.boids[:,3] + (self.boids[i,1] - self.boids[:,1] )*middle_strength/len(self.boids[:,1])

		return self


	def fly_apart(self):

		fly_apart_range = self.interaction_params[1]
		num_boids = len(self.boids[:,0])

		for i in range(num_boids):
			target_indices = ( self.boids[i,0]-self.boids[:,0] )**2 + ( self.boids[i,1]-self.boids[:,1] )**2 < fly_apart_range
			self.boids[:,2] = self.boids[:,2] + ( self.boids[:,0] - self.boids[i,0] )*target_indices.astype(float)
			self.boids[:,3] = self.boids[:,3] + ( self.boids[:,1] - self.boids[i,1] )*target_indices.astype(float)

		return self



	def fly_together(self):

		fly_together_range = self.interaction_params[2]
		together_strength = self.interaction_params[3]
		num_boids = len(self.boids[:,0])

		for i in range(num_boids):
			target_indices = ( self.boids[i,0]-self.boids[:,0] )**2 + ( self.boids[i,1]-self.boids[:,1] )**2 < fly_together_range
			self.boids[:,2] = self.boids[:,2] + ( self.boids[:,2] - self.boids[i,2] )*together_strength/num_boids*target_indices.astype(float)
			self.boids[:,3] = self.boids[:,3] + ( self.boids[:,3] - self.boids[i,3] )*together_strength/num_boids*target_indices.astype(float)

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
