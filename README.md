# Plane Simulator
This project is to simulate an airport schedules requests from planes for takeoff times. The input is read in from a 
file, parsed into a list, and then the list is read through and the plane's times are scheduled. The list is required 
to adapt so that each plane can get as close to it's requested take off time as possible. The list is not simply a 
first in first out style, as airports can not function that way. A plane may request a takeoff time for 6:00 pm while 
the current time is only 4:30 pm. Many other planes can request times in between then, or may have more urgent requests.


This project imports the sys library as well as a number of functions from other files in the repo

# How to Run
This program must be run from the command line.
1) Navigate to the directory where the program is downloaded.
2) **Please use the command _Python3 simulator.py "name of input file"_** to run the program.

With the newest version of the program you do not need to specify an input file on the command line. If an input file is
not specified instead of terminating the program will now open a file browser and allow you to select an input file.
However you can still select an input file from the command line if you so choose. 

Please run the program with Python 3, not Python 2 as the script has only been tested with versions of Python 3.  

# Input File Requirements
Unfortunately the requirements for the input file are quite strict. The input file must be a ".txt" file in order to be
successfully parsed. Inside the file each plane must be on it's own line. Each line must contain four pieces of
information separated by a comma. These four pieces of information, in order, are:

1) Plane Name
2) The time the request was submitted
3) What time the plane is requesting to take off
4) How long it will take the plane to exit the runway.

These times are simplified down to integer numbers representing whole units of time. The input *Delta 707, 4, 6, 2* 
can be  interpreted as, the plane Delta 707 put in a request at 4 to use the runway at 6 and will use the runway for 2
 units of time. 
 
# Future Plans
~~Currently the simulator will automatically close if an input file is not specified. I would like to change this so that 
if an input file is not specified instead the program will allow you to open up a file browser and select a file to 
input.~~

I would also like to more extensively test the program to check for bugs or other unforeseen issues that arise

# Author
The author of this project is Drew Mares, a student at Augsburg University