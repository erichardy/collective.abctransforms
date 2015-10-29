import re
import glob
from sys import modules
from os.path import join, abspath, dirname, basename


PREFIX = abspath(dirname(__file__))


def input_file_path(f):
    return join(PREFIX, 'inputs', f)


def output_file_path(f):
    return join(PREFIX, 'outputs', f)


def matching_inputs(pattern):
    return [basename(path) for path in
            glob.glob(join(PREFIX, "input", pattern))]
