import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

directory = os.path.join(__location__, 'data/raw')

for name in os.listdir(directory):
	print name

# with open()