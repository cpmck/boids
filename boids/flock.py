import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation

class Flock(object):
	def __init__(self,num_boids, initial_params, interaction_params):
		self.num_boids = num_boids
		self.initial_params = initial_params
		self.interaction_params = interaction_params


	def init_cond_matrix(self, initial_params, num_boids):

		x_init_pos_min = initial_params[0,0]
		x_init_pos_max = initial_params[0,1]
		x_init_vel_min = initial_params[0,2]
		x_init_vel_min = initial_params[0,3]

		y_init_pos_min = initial_params[1,0]
		y_init_pos_max = initial_params[1,1]
		y_init_vel_min = initial_params[1,2]
		y_init_vel_min = initial_params[1,3]

		boids_x = np.array(np.random.uniform(x_init_pos_min, x_init_pos_max, num_boids))
		boids_y = np.array(np.random.uniform(y_init_pos_min, y_init_pos_max, num_boids))

		boid_x_velocities = np.array(np.random.uniform(x_init_vel_min,x_init_vel_max,num_boids))
		boid_y_velocities = np.array(np.random.uniform(y_init_vel_min,y_init_vel_max,num_boids))

		return np.column_stack((boids_x, boids_y, boid_x_velocities, boid_y_velocities))

	def fly_towards_middle(self, num_boids, interaction_params):

		middle_strength = interaction_params[0,0]

		for i in range(num_boids):
		boids[:,2] = boids[:,2] + (boids[i,0] - boids[:,0] )*middle_strength/len(boids_np[:,0])
		boids[:,3] = boids[:,3] + (boids[i,1] - boids[:,1] )*middle_strength/len(boids_np[:,1])

		return boids


	def fly_apart(self, num_boids, interaction_params):

		fly_apart_range = interaction_params[0,1]

		for i in range(num_boids):
			target_indices = ( boids[i,0]-boids[:,0] )**2 + ( boids[i,1]-boids[:,1] )**2 < fly_apart_range
			boids[:,2] = boids[:,2] + ( boids[:,0] - boids[i,0] )*target_indices.astype(float)
			boids[:,3] = boids[:,3] + ( boids[:,1] - boids[i,1] )*target_indices.astype(float)

		return boids



	def fly_together(self, num_boids, interaction_params):

		fly_together_range = interaction_params[0,2]
		together_strength = interaction_params[0,3]

		for i in range(num_boids):
			target_indices = ( boids[i,0]-boids[:,0] )**2 + ( boids[i,1]-boids[:,1] )**2 < fly_together_range
			boids[:,2] = boids[:,2] + ( boids[:,2] - boids[i,2] )*together_strength/num_boids*target_indices.astype(float)
			boids[:,3] = boids[:,3] + ( boids[:,3] - boids[i,3] )*together_strength/num_boids*target_indices.astype(float)

		return boids

	def update_boids(self, num_boids, interaction_params)

		return self.fly_towards_middle.fly_apart.fly_together

