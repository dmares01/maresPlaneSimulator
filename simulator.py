# need to read in data from a file and add planes to a waiting list
# as requests come in, place them into the waiting queue where they belong
# third list for listing the planes that have taken off already
# print off a list of each flight and their actual takeoff times
from takeoffRequest import Requests as Rq

def main():
    plane_input = []
    plane_queue = []
    timer = 0

    print("Testing program")
    simulator_file = open("input.txt", "r")
    simulator_data = simulator_file.readlines()

    for requests in simulator_data:
        input_request = requests.split(",")
        new_request = Rq(input_request[0], input_request[1], input_request[2], input_request[3])
        plane_input.append(new_request)

    for single_request in plane_input:
        print(single_request.get_name())


if __name__ == "__main__":
    main()
