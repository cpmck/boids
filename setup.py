from setuptools import setup, find_packages

setup(
		name = 'boids',
		version = '0.1.0',
		author = 'Conor Mc Keever',
		url = 'https://github.com/cpmck/boids.git',
		author_email = 'conor.mckeever.16@ucl.ac.uk',
		keywords = 'boids simulation',
		description = 'Package to simulate boids in flight by specifying parameters governing their initial positions and dynamics',
		licence = 'MIT',
		packages = find_packages(exclude=['test']),
		scripts = ['scripts/flyBoids'],
		classifiers = [
			"Development Status :: 3 - Alpha",
			"Topic :: Simulation",
			"Licence :: MIT"],
		install_requires = ['numpy','matplotlib','pyyaml','nose'],
		include_package_data = True


)