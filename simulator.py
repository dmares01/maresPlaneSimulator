# need to read in data from a file and add planes to a waiting list
# as requests come in, place them into the waiting queue where they belong
# third list for listing the planes that have taken off already
# print off a list of each flight and their actual takeoff times
# shows gaps in schedule or queue by __no_plane__

import sys
from inputPlaneFile import create_plane_list
from planeSchedule import create_schedule


def main():
    simulator_file = open(sys.argv[1], "r")
    simulator_data = simulator_file.readlines()
    input_list_of_planes = create_plane_list(simulator_data)

    # Pass list of planes into plane schedule to return schedule
    timer = 0
    plane_queue = create_schedule(input_list_of_planes, timer)

    # checking to make sure data is inputted into Request Objects
    for plane in plane_queue:
        print(plane.get_name(), plane.get_takeoff_time())


if __name__ == "__main__":
    number_of_arguments = len(sys.argv)
    if number_of_arguments == 1: # If there is only 1 argument then an input argument was not specified
        print("Please specify an input file")
        exit()
    else:
        print("There are", number_of_arguments, "arguments")
    main()
