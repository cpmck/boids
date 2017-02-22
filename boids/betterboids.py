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

interaction_params = np.array([config["centre_attraction"], config["retreat_distance"], config["attraction_distance"], config["drag_strength"]])

frame_x_min = config["x_bounds"][0]-config["x_margin"]
frame_x_max = config["x_bounds"][1]+config["x_margin"]

frame_y_min = config["y_bounds"][0]-config["y_margin"]
frame_y_max = config["y_bounds"][1]+config["y_margin"]


flock_of_boids = Flock(num_boids, initial_params).init_cond_matrix()
flying_flock = Flight(flock_of_boids,interaction_params)

figure = plt.figure()
axes = plt.axes(xlim=(frame_x_min, frame_x_max), ylim = (frame_y_min, frame_y_max))
scatter = axes.scatter(flying_flock.get_x(),flying_flock.get_y())

def animate(frame):
	scatter.set_offsets(zip(flying_flock.update_boids().get_x(), flying_flock.update_boids().get_y()))

anim = animation.FuncAnimation(figure, animate, frames = config["frame_number"], interval = config["frame_interval"])

if __name__ == "__main__":
	plt.show()



