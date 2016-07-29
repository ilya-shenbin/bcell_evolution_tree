import numpy as np
from distance_calculator import calc_distance
from tree import Tree

# builds evolution tree for several (V or D or J) regions
# @origin_region - original version of (V or D or J) region of B-cell
# @regions - set of mutations of original region of B-cell
# @returns - tree
# example:
# origin_region (V11) -  "ATGCATGCATGCATGCATGC"
# mutated_regions -     ["ATGCATGCATGCATGC",
#                        "ATTCATGCATGCATG",
#                        "ATTCATTCATGCATGCA"]
# result
#def build_tree(origin_region, mutated_regions):
    #return tree


