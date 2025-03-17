import array
import copy

import random

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3
import numpy as np
from deap import algorithms, base, benchmarks, creator, tools
from deap.tools.indicator import hv

from nsgaiii.selection import (
    associate,
    construct_hyperplane,
    find_extreme_points,
    find_ideal_point,
    generate_reference_points,
    normalize_objectives,
    sel_nsga_iii,
)

# 生成并显示一个示例图像
creator.create("FitnessMin3", base.Fitness, weights=(-1.0,) * 3)
creator.create("Individual3", array.array, typecode="d", fitness=creator.FitnessMin3)