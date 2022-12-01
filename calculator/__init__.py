import math
import sys
import os

from .welcome import welcome_message
from .input import decide_calculator_function
from .constants import generate_constants

sys.path.insert(0, ".\\calculator\\calculator_logic")
from basic import Basic_Calculator
