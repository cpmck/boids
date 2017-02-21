from setuptools import setup, find_packages

setup(
		name = 'boids',
		version = '0.1.0',
		packages = find_packages(exclude=['test']),
		scripts = ['scripts/flyBoids'],
		install_requires = ['numpy'] #add all packages

)