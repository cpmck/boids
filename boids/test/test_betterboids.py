from matplotlib import pyplot as plt 
from matplotlib import animation
import random
import numpy as np
from boids.flock import Flock
from boids.flight import Flight
from argparse import ArgumentParser
import yaml
from nose.tools import assert_equal
from nose.tools import assert_raises