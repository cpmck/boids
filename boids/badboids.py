from matplotlib import pyplot as plt 
from matplotlib import animation
import random


#initial poor code
x_init_pos_min = -1000.0
x_init_pos_max = -500.0

y_init_pos_min = 300.0
y_init_pos_max = 600.0


x_init_vel_min = 0
x_init_vel_max = 30

y_init_vel_min = -30
y_init_vel_max = 20

num_boids = 50

boids_x = [random.uniform(x_init_pos_min,x_init_pos_max) for x in range(num_boids)]
boids_y = [random.uniform(y_init_pos_min,y_init_pos_max) for x in range (num_boids)]
boid_x_velocities = [random.uniform(x_init_vel_min,y_init_vel_max) for x in range(num_boids)]
boid_y_velocities = [random.uniform(y_init_vel_min,y_init_vel_max) for x in range(num_boids)]
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

#boids is a set of initial positions and velocities

middle_strength = 0.001
match_strength = 0.125

retreat_dist = 10


def update_boids(boids, middle_strength, match_strength, num_boids):
	xs,ys,xvs,yvs = boids
	#fly towards middle
	for i in range(num_boids):
		for j in range(num_boids):
			xvs[i] = xvs[i] + ( xs[j] - xs[i])*middle_strength/len(xs)
	for i in range(num_boids):
		for j in range(num_boids):
			yvs[i] = yvs[i] + ( ys[j] - ys[i])*middle_strength/len(xs)

	#fly away from nearby boids
	for i in range(num_boids):
		for j in range(num_boids):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10:
				xvs[i] = xvs[i]+(xs[i]-xs[j])
				yvs[i] = yvs[i]+(ys[i]-ys[j])

	#try to match speed with nearby boids
	for i in range(num_boids):
		for j in range(num_boids):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 1000:
				xvs[i] = xvs[i] + ( xvs[j] - xvs[i] )*match_strength/len(xs)
				yvs[i] = yvs[i] + ( yvs[j] - yvs[i] )*match_strength/len(xs)

	#move according to velocities
	for i in range(num_boids):
		xs[i] = xs[i] + xvs[i]
		ys[i] = ys[i] + yvs[i]



x_margin = 1000
y_margin = 1000

figure = plt.figure()
axes = plt.axes(xlim=(x_init_pos_min - x_margin, x_init_pos_max + x_margin), ylim = (y_init_pos_min - y_margin,y_init_pos_max + y_margin))
scatter = axes.scatter(boids[0],boids[1])

def animate(frame):
	update_boids(boids,middle_strength, match_strength, num_boids)
	scatter.set_offsets(zip(boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate, frames = 500, interval = 50)

if __name__ == "__main__":
	plt.show()



