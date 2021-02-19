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
    output_file_name = "mares_output.txt"
    output_file = open(output_file_name, 'w')
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
    print("Please open the output file " + output_file_name + " to see the results of the simulation.")


# Function to only run code if file is original file that is called
if __name__ == "__main__":
    number_of_arguments = len(sys.argv)
    if number_of_arguments == 1:  # If there is only 1 argument then an input argument was not specified
        from userGUI import browse_files
        main()
    else:
        main()
