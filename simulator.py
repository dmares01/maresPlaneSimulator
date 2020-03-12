# need to read in data from a file and add planes to a waiting list
# as requests come in, place them into the waiting queue where they belong
# third list for listing the planes that have taken off already
# print off a list of each flight and their actual takeoff times
# shows gaps in schedule or queue by __no_plane__

import sys
from inputPlaneFile import create_plane_list
from planeSchedule import create_schedule
from actualTimes import print_queue_to_file as print_queue
from actualTimes import print_out_final


def main():
    # Opening file, and inputting data into list
    simulator_file = open(sys.argv[1], "r")
    simulator_data = simulator_file.readlines()
    input_list_of_planes, largest_submit_time = create_plane_list(simulator_data)

    # setting up timer and plane_queue to be used
    timer = 0
    plane_queue = []

    # Pass list of planes into plane schedule to return schedule
    output_file = open("mares_output.txt", 'w')
    while timer <= 100000:
        test = create_schedule(input_list_of_planes, timer, plane_queue)
        if test is not None:
            plane_queue = test
        print_queue(plane_queue, timer, output_file)
        if len(plane_queue) == 0:
            print_out_final(input_list_of_planes, output_file)
            break
        timer += 1
    output_file.close()


# Function to only run code if file is original file that is called
if __name__ == "__main__":
    number_of_arguments = len(sys.argv)
    if number_of_arguments == 1:  # If there is only 1 argument then an input argument was not specified
        print("Please specify an input file")
        exit()
    else:
        # print("There are", number_of_arguments, "arguments")
        main()
