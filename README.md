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
	1. [LGSVL simulator][https://github.com/lgsvl/simulator]
	2. [Python API for LGSVL simulator][https://github.com/lgsvl/PythonAPI]
	3. MATLAB/Simulink
2. Clone this framework and Demonstrate
	1. git clone https://github.com/keita1523/test_framework.git
	2. To run python API, execute the following command in the PythonAPI directory:
		```pip3 install --user -e .```
	3. execute the following command, and then a python file is generated in the output directory:
		```python scenario_converter.py BorregasAve.m```

## How to use


