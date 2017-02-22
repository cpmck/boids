import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation

class Flock(object):
	def __init__(self,num_boids, initial_params):
		self.num_boids = num_boids
		self.initial_params = initial_params

	def init_cond_matrix(self):

		x_init_pos_min = self.initial_params[0,0]
		x_init_pos_max = self.initial_params[0,1]
		x_init_vel_min = self.initial_params[0,2]
		x_init_vel_max = self.initial_params[0,3]
		y_init_pos_min = self.initial_params[1,0]
		y_init_pos_max = self.initial_params[1,1]
		y_init_vel_min = self.initial_params[1,2]
		y_init_vel_max = self.initial_params[1,3]

		boids_x = np.array(np.random.uniform(x_init_pos_min, x_init_pos_max, self.num_boids))
		boids_y = np.array(np.random.uniform(y_init_pos_min, y_init_pos_max, self.num_boids))

		boid_x_velocities = np.array(np.random.uniform(x_init_vel_min,x_init_vel_max,self.num_boids))
		boid_y_velocities = np.array(np.random.uniform(y_init_vel_min,y_init_vel_max,self.num_boids))

		return np.column_stack((boids_x, boids_y, boid_x_velocities, boid_y_velocities))