import numpy as np 
import os
from boids.flock import Flock
from boids.flight import Flight
from matplotlib import pyplot as plt 
from matplotlib import animation
from nose.tools import assert_equal
from nose.tools import assert_raises
import mock
import yaml

def test_fly_towards_middle():
	with open(os.path.join(os.path.dirname(__file__),
		'fixtures','flight_samples_fly_towards_middle.yaml')) as fixtures_file:
			fixtures = yaml.load(fixtures_file)
			for fixture in fixtures:
				instance = Flight(**fixture)
				with assert_raises(TypeError) as exception:
					instance.fly_towards_middle()

def test_fly_apart():
	with open(os.path.join(os.path.dirname(__file__),
		'fixtures','flight_samples_fly_apart.yaml')) as fixtures_file:
			fixtures = yaml.load(fixtures_file)
			for fixture in fixtures:
				instance = Flight(**fixture)
				with assert_raises(TypeError) as exception:
					instance.fly_apart()

def test_fly_together():
	with open(os.path.join(os.path.dirname(__file__),
		'fixtures','flight_samples_fly_together.yaml')) as fixtures_file:
			fixtures = yaml.load(fixtures_file)
			for fixture in fixtures:
				instance = Flight(**fixture)
				with assert_raises(TypeError) as exception:
					instance.fly_together()

def test_num_boids():
	with open(os.path.join(os.path.dirname(__file__),
		'fixtures','flight_sample_num_boids.yaml')) as fixtures_file:
			fixtures = yaml.load(fixtures_file)
			for fixture in fixtures:
				instance = Flight(**fixture)
				with assert_raises(TypeError) as exception:
					instance.num_boids()