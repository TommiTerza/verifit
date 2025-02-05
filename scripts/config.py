# Copyright 2025 PoliTo
# Solderpad Hardware License, Version 2.1, see LICENSE.md for details.
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
#
# Author: Tommaso Terzano <tommaso.terzano@polito.it> 
#                         <tommaso.terzano@gmail.com>
#  
# Info: This python script is used to parse the config.hjson to config.mk

#!/usr/bin/env python3

import hjson
import os

CONFIG_FILE = "config.hjson"  # Hardcoded input filename
OUTPUT_FILE = "config.mk"     # Output Makefile-compatible variable file

def flatten_dict(d, parent_key='', sep='_'):
    """
    Recursively flattens a nested dictionary into a flat dictionary with 
    keys formatted as 'PARENT_CHILD'.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k.upper()}" if parent_key else k.upper()
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        elif isinstance(v, list):
            # Convert lists into indexed variables
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}_{i}", sep).items())
                else:
                    items.append((f"{new_key}_{i}", item))
        else:
            items.append((new_key, v))
    return dict(items)

# Read HJSON file
try:
    with open(CONFIG_FILE, "r") as f:
        data = hjson.load(f)
except FileNotFoundError:
    print(f"Error: Could not find {CONFIG_FILE}")
    exit(1)

# Count number of tests if "test" key exists
test_count = len(data.get("test", []))

# Flatten the dictionary
flat_data = flatten_dict(data)

# Write to config.mk
with open(OUTPUT_FILE, "w") as f:
    f.write("# Auto-generated Makefile variables from config.hjson\n")
    
    # Write test count
    f.write(f"TEST_COUNT = {test_count}\n")
    
    for key, value in flat_data.items():
        if isinstance(value, str):
            f.write(f'{key} = "{value}"\n')  # Ensure strings are quoted
        elif isinstance(value, bool):  # Convert booleans to Makefile-friendly values
            f.write(f"{key} = {'1' if value else '0'}\n")
        else:
            f.write(f"{key} = {value}\n")