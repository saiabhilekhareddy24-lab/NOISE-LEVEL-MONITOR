Noise Level Monitor 🔊
Overview

The Noise Level Monitor is a Python-based project that measures and monitors sound levels. It classifies the noise as Quiet, Moderate, Loud, or Dangerous based on the measured decibel (dB) value.

Features
Generates simulated noise-level data.
Displays noise levels in decibels (dB).
Classifies the noise level automatically.
Provides warnings when the noise exceeds the safe limit.
Includes a Python testbench for verification.
Displays simulation results using a graph.
Noise Level Classification
Noise Level	Classification
Below 40 dB	Quiet
40–60 dB	Moderate
60–85 dB	Loud
Above 85 dB	Dangerous
Project Structure
noise-level-monitor/
│
├── noise_monitor.py
├── test_noise_monitor.py
├── simulation.py
├── requirements.txt
└── README.md

Requirements
Python 3.x
NumPy
Matplotlib

Install the required libraries:

pip install numpy matplotlib

Run the Project

Run the main noise monitor:

python noise_monitor.py


Run the simulation:

python simulation.py


Run the testbench:

python test_noise_monitor.py

Example Output
Noise Level: 35.2 dB -> QUIET
Noise Level: 52.8 dB -> MODERATE
Noise Level: 72.4 dB -> LOUD
Noise Level: 91.6 dB -> DANGEROUS


The simulation also generates a graph showing the noise level variation over time.

Applications
Environmental noise monitoring
Industrial safety
Smart homes
School and hospital environments
Workplace noise monitoring
Author

Noise Level Monitor – Python Simulation Project
