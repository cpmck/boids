from matplotlib import pyplot as plt 
from matplotlib import animation
import random
import numpy as np
from flock import Flock
from flight import Flight
import yaml


config = yaml.load(open("config.yaml"))

num_boids = config["number_of_boids"]
initial_params = np.array([config["x_bounds"], config["y_bounds"]])

attract_dist = 100
middle_strength = 0.001
match_strength = 0.125
retreat_dist = 10

interaction_params = np.array([config["centre_attraction"], config["retreat_distance"], config["attraction_distance"], config["drag_strength"]])

x_margin = 1000
y_margin = 1000

boids_flock = Flock(50, initial_params)
flock_matrix = boids_flock.init_cond_matrix()
flight_matrix = Flight(flock_matrix,interaction_params)


frame_x_min = config["x_bounds"][0]-config["x_margin"]
frame_x_max = config["x_bounds"][1]+config["x_margin"]

frame_y_min = config["y_bounds"][0]-config["y_margin"]
frame_y_max = config["y_bounds"][1]+config["y_margin"]


figure = plt.figure()
axes = plt.axes(xlim=(frame_x_min, frame_x_max), ylim = (frame_y_min, frame_y_max))
scatter = axes.scatter(flock_matrix[:,0],flock_matrix[:,1])



def animate(frame):
	scatter.set_offsets(zip(flight_matrix.update_boids().get_x(), flight_matrix.update_boids().get_y()))

anim = animation.FuncAnimation(figure, animate, frames = 50, interval = 50)

if __name__ == "__main__":
	plt.show()



