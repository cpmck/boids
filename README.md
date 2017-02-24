# boids

This module simulates boids in flight. 
	

Usage:
	
	Setup:
	
		setup using the command: "sudo python setup.py install"
			
		OR: "pip install git+https://github.com/cpmck/boids.git"


	Edit confguration file:

		The config file ./boids/config/config.yaml can be edited to the desired parameters:

		x_bounds:				[minimum x position, maximum x position, minimum x velocity, maximum x velocity]
		y_bounds: 				[minimum y position, maximum y position, minimum y velocity, maximum y velocity]
		number_of_boids: 		The number of boids in the simulation
		attraction_distance:	Distance under which boids will be attracted to eachother
		retreat_distance: 		Distance under which boids will experience repulsion from eachother
		drag_strength: 			Parameter characterising degree to which boids will follow eachother
		centre_attraction: 		Parameter characterising degree to which boids will fly towards their collective "centre of mass"
		x_margin: 				Size of margins around x_bounds
		y_margins: 				Size of margins around y_bouds
		frame_number: 			Number of frames in animation
		frame_interval: 		Number of intervals in animation


	Run the simulation:

		simulation is run ising the command: flyBoids
