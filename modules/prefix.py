
from os import path
import random

class prefix():

	# Pick a polite prefix.
    def choosePrefix():
        prefix_list = open(path.abspath(path.join(path.curdir, os.pardir, 'files', 'polite_prefixes.txt'))) \
                           .readlines()
        return (prefix_list[random.randint(0, len(prefix_list) - 1)] + '\n')