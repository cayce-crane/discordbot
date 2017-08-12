
from os import pardir
from os import path
import random

class prefix():

	# Pick a polite prefix.
    def choosePrefix():
        prefix_list = open(path.abspath(path.join(path.curdir, 'files', 'polite_prefixes.txt'))) \
                           .readlines()
        return (prefix_list[random.randint(0, len(prefix_list) - 1)] + '\n')