# test_framework

This framework can generate a driving scenario file for LGSVL simulator from a MATLAB file.
Driving Scenario Designer provided by MATLAB/Simulink enables developers to create driving scenarios graphically.
The scenarios are converted to the suite formats for LGSVL simulator by this framework.

## System Model
<img src="./image/system_model_detail-1.png" alt="System_Model" title="System Model">

## Requirements
- LGSVL simulator
- Python API for LGSVL simulator
- MATLAB/Simulink
	- Automated Driving Toolbox

## Release Compatibility
- LGSVL simulator 2020.06
- Python 3.5
- MATLAB R2020b

## Getting Started

1. Installation

	1. [LGSVL simulator](https://github.com/lgsvl/simulator)

	2. [Python API for LGSVL simulator](https://github.com/lgsvl/PythonAPI)

	3. MATLAB/Simulink

2. Setup

	To clone,

		git clone https://github.com/keita1523/test_framework.git
		pip3 install numpy

	To run python API, execute the following command in the PythonAPI directory:

		pip3 install --user -e .


	In LGSVL simulator directory, you run a folloing command.
	If you download binary version, the directory is lgsvlsimulator-linux64-xxxx-xx.
	To launches LGSVL simulator
	```
		./simulator
	```

	Push "Open Browser..." and start simulation.
	[Add maps, vehicles, and simulations](https://www.lgsvlsimulator.com/docs/maps-tab/#how-to-add-a-map)


3. Demonstration
	Launches two terminals A and B.
	On the terminal A, change directory to LGSVL simulator directory.
	```
		./simulator
	```

	On terminal B, execute the following command, and then a python file is generated in the output directory:

		python3 scenario_converter.py BorregasAve.m
		cd output
		python3 BorregasAve.py



