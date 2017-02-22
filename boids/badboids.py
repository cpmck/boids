from matplotlib import pyplot as plt 
from matplotlib import animation
import random
import numpy as np

from flock import Flock
from flight import Flight



#initial poor code
x_init_pos_min = -500.0
x_init_pos_max = 0.0

y_init_pos_min = -20.0
y_init_pos_max = 20.0


x_init_vel_min = 0
x_init_vel_max = 10

y_init_vel_min = -5
y_init_vel_max = 5

num_boids = 50

initial_params = np.array([[x_init_pos_min,x_init_pos_max,x_init_vel_min,x_init_vel_max], [y_init_pos_min,y_init_pos_max,y_init_vel_min, y_init_vel_max]])

attract_dist = 100
middle_strength = 0.001
match_strength = 0.125
retreat_dist = 10

interaction_params = np.array([0.001, 10, 100, 0.125])
interaction_params = np.array([middle_strength, retreat_dist, attract_dist, match_strength])



#boids_x_np = np.array(np.random.uniform(x_init_pos_min, x_init_pos_max, num_boids))
#boids_y_np = np.array(np.random.uniform(y_init_pos_min, y_init_pos_max, num_boids))

#boid_x_velocities_np = np.array(np.random.uniform(x_init_vel_min,x_init_vel_max,num_boids))
#boid_y_velocities_np = np.array(np.random.uniform(y_init_vel_min,y_init_vel_max,num_boids))

#boids_np = np.column_stack((boids_x_np, boids_y_np, boid_x_velocities_np, boid_y_velocities_np))


#print(boids_np)

#boids_x = [random.uniform(x_init_pos_min,x_init_pos_max) for x in range(num_boids)]
#boids_y = [random.uniform(y_init_pos_min,y_init_pos_max) for x in range (num_boids)]
#boid_x_velocities = [random.uniform(x_init_vel_min,y_init_vel_max) for x in range(num_boids)]
#boid_y_velocities = [random.uniform(y_init_vel_min,y_init_vel_max) for x in range(num_boids)]
#boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)


#print(boids_x_np)
#print(boids_x)
#boids is a set of initial positions and velocities



#test = np.broadcast(boids_np[:,1], boids_np[1,1])

#def update_boids(middle_strength, match_strength, num_boids, boids_np):
	#xs,ys,xvs,yvs = boids
	
	#fly towards middle refactored to numpy
#	for i in range(num_boids):
#		boids_np[:,2] = boids_np[:,2] + (boids_np[i,0] - boids_np[:,0] )*middle_strength/len(boids_np[:,0])
#		boids_np[:,3] = boids_np[:,3] + (boids_np[i,1] - boids_np[:,1] )*middle_strength/len(boids_np[:,1])
#
#	#
#	for i in range(num_boids):
#		target_indices = ( boids_np[i,0]-boids_np[:,0] )**2 + ( boids_np[i,1]-boids_np[:,1] )**2 < 100
#		boids_np[:,2] = boids_np[:,2] + ( boids_np[:,0] - boids_np[i,0] )*target_indices.astype(float)
#		boids_np[:,3] = boids_np[:,3] + ( boids_np[:,1] - boids_np[i,1] )*target_indices.astype(float)
#
#
#	for i in range(num_boids):
#		target_indices = ( boids_np[i,0]-boids_np[:,0] )**2 + ( boids_np[i,1]-boids_np[:,1] )**2 < 100
#		boids_np[:,2] = boids_np[:,2] + ( boids_np[:,2] - boids_np[i,2] )*match_strength/num_boids*target_indices.astype(float)
#		boids_np[:,3] = boids_np[:,3] + ( boids_np[:,3] - boids_np[i,3] )*match_strength/num_boids*target_indices.astype(float)
#
#	boids_np[:,0] = boids_np[:,0] + boids_np[:,2]
#	boids_np[:,1] = boids_np[:,1] + boids_np[:,3]
#



	#for i in range(num_boids):
	#	for j in range(num_boids):
	#		xvs[i] = xvs[i] + ( xs[j] - xs[i])*middle_strength/len(xs)
	#for i in range(num_boids):
	#	for j in range(num_boids):
	#		yvs[i] = yvs[i] + ( ys[j] - ys[i])*middle_strength/len(xs)

	

	#fly away from nearby boids
	#for i in range(num_boids):
	#	for j in range(num_boids):
	#		if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10:
	#			xvs[i] = xvs[i]+(xs[i]-xs[j])
	#			yvs[i] = yvs[i]+(ys[i]-ys[j])

	#try to match speed with nearby boids
	#for i in range(num_boids):
	#	for j in range(num_boids):
	#		if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 1000:
	#			xvs[i] = xvs[i] + ( xvs[j] - xvs[i] )*match_strength/len(xs)
	#			yvs[i] = yvs[i] + ( yvs[j] - yvs[i] )*match_strength/len(xs)

	#move according to velocities
	#for i in range(num_boids):
	#	xs[i] = xs[i] + xvs[i]
	#	ys[i] = ys[i] + yvs[i]


x_margin = 1000
y_margin = 1000


boids_flock = Flock(50, initial_params)
flock_matrix = boids_flock.init_cond_matrix()
flight_matrix = Flight(flock_matrix,interaction_params)




figure = plt.figure()
axes = plt.axes(xlim=(x_init_pos_min - x_margin, x_init_pos_max + x_margin), ylim = (y_init_pos_min - y_margin,y_init_pos_max + y_margin))
scatter = axes.scatter(flock_matrix[:,0],flock_matrix[:,1])



def animate(frame):

	#fly = flight_matrix.update_boids()
	#update_boids(middle_strength, match_strength, num_boids, boids_np)
	#boids_flock.fly_apart(flock_matrix)
	#scatter.set_offsets(zip(fly[:,0], fly[:,1]))

	scatter.set_offsets(zip(flight_matrix.update_boids().get_x(), flight_matrix.update_boids().get_y()))

anim = animation.FuncAnimation(figure, animate, frames = 50, interval = 50)

if __name__ == "__main__":
	plt.show()



