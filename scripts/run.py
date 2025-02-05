# Copyright 2025 PoliTo
# Solderpad Hardware License, Version 2.1, see LICENSE.md for details.
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
#
# Author: Tommaso Terzano <tommaso.terzano@polito.it> 
#                         <tommaso.terzano@gmail.com>
#  
# Info: Run script of VerifIt, effectivly runs the verification campaign using lib.py

import hjson
import verifit

# Set this to True to enable debugging prints
DEBUG_MODE = True

# Redefine print() to be enabled only during debugging
def PRINT(*args, **kwargs):
    if DEBUG_MODE:
        print(*args, **kwargs)

#__________________________________________________________________________________________________#
#																			            																								 #
#																							  SET-UP    																				 #
#__________________________________________________________________________________________________#

# Load the configuration hjson file
with open("../config.hjson", "r") as file:
    data = hjson.load(file)

# Debug the configuration hjson
PRINT(data['target']['name'])

env = verifit.VerifIt(data)