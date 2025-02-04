# Copyright 2025 PoliTo
# Solderpad Hardware License, Version 2.1, see LICENSE.md for details.
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
#
# Author: Tommaso Terzano <tommaso.terzano@polito.it> 
#                         <tommaso.terzano@gmail.com>
#  
# Info: Makefile library of VerifIt. Here you MUST define the commands needed to build the RTL model, 
#			  compile SW applications, run a simulation and flash the FPGA board.
#       This file is included in the main makefile of the project, which will use the commands
#       defined here to test and verify the RTL project under test.

#__________________________________________________________________________________________________#
#																			            																								 #
#																							DEPENDENCIES																				 #
#__________________________________________________________________________________________________#
# If existing, include here a makefile library with the commands needed to build the
# RTL, compile the SW, run a simulation or flash the FPGA board.

# include(your/project/dependencies)

#__________________________________________________________________________________________________#
#																			            																								 #
#																			          TARGETS   																				 #
#__________________________________________________________________________________________________#
# These targets must be defined, otherwise VerifIt will be unable to work.

# One argument: app (i.e. software application)
# IMPORTANT: the DUT-specific commands to build the SW must be able to take care of every aspect,
#            including linking the correct drivers or libraries and datasets. The only parameter
#            passed to the command is the application name.
sw:
	echo "Building SW $(app)..."
	@echo "ADD HERE YOUR COMMANDS"
	echo "Nothing happens! Define the DUT-specific commands to build the SW in verifit.mk"

# One argument: tool (e.g. verilator, questa, vcs)
sim-synth:
	echo "Building RTL model for $(tool)..."
	@echo "ADD HERE YOUR COMMANDS"
	echo "Nothing happens! Define the DUT-specific commands to build the RTL model in verifit.mk"

# One argument: tool (e.g. verilator, questa, vcs)
sim-run:
	echo "Running simulation on $(tool)..."
	@echo "ADD HERE YOUR COMMANDS"
	echo "Nothing happens! Define the DUT-specific commands to run the simulation in verifit.mk"

# One argument: board (e.g. pynqz2, zcu102)
fpga-synth:
	echo "Buiding the RTL model for $(board)..."
	@echo "ADD HERE YOUR COMMANDS"
	echo "Nothing happens! Define the DUT-specific commands to synthetize the RTL in verifit.mk"

# One argument: board (e.g. pynqz2, zcu102)
fpga-run:
	echo "Running test on $(board)..."
	@echo "ADD HERE YOUR COMMANDS"
	echo "Nothing happens! Define the DUT-specific commands to flash the FPGA board in verifit.mk"