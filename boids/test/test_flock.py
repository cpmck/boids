import numpy as np 
import os
from boids.flock import Flock
from matplotlib import pyplot as plt 
from matplotlib import animation
from nose.tools import assert_equal
from nose.tools import assert_raises
import mock
import yaml

def test_num_boids_positive_int():
	with open(os.path.join(os.path.dirname(__file__),
		'fixtures','flock_samples.yaml')) as fixtures_file:
			fixtures = yaml.load(fixtures_file)
			for fixture in fixtures:
				instance = Flock(**fixture)
				with assert_raises(TypeError) as exception:
					instance.init_cond_matrix()


def test_bounds_min_lessthan_max():
	with open(os.path.join(os.path.dirname(__file__),
		'fixtures','flock_samples_minmax.yaml')) as fixtures_file:
			fixtures = yaml.load(fixtures_file)
			for fixture in fixtures:
				instance = Flock(**fixture)
				with assert_raises(ValueError) as exception:
					instance.init_cond_matrix()


