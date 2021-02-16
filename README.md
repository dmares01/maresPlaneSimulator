# Plane Simulator
This project is to simulate an airport schedules requests from planes for takeoff times. The input is read in from a 
file, parsed into a list, and then the list is read through and the plane's times are scheduled. The list is required 
to adapt so that each plane can get as close to it's requested take off time as possible. The list is not simply a 
first in first out style, as airports can not function that way. A plane may request a takeoff time for 6:00 pm while 
the current time is only 4:30 pm. Many other planes can request times in between then, or may have more urgent requests.


This project imports the sys library as well as a number of functions from other files in the repo

# How to Run
This program must be one from the command line with the input file listed as an argument.
Navigate to the directory where the program is downloaded.
**Please use the command _Python3 simulator.py "name of input file"_** to run the program.
If a file is not listed, the program will terminate without running any simulation.
Please run the program with Python 3, not Python 2 as the script has only been tested with versions of Python 3.  

# Future Plans
Currently the simulator will automatically close if an input file is not specified. I would like to change this so that 
if an input file is not specified instead the program will allow you to open up a file browser and select a file to 
input. 

I would also like to more extensively test the program to check for bugs or other unforeseen issues that arise

# Author
The author of this project is Drew Mares, a student at Augsburg University