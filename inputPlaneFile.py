# inputPlaneFile.py
# author: Drew Mares
# Created on: 02/27/2020
from takeoffRequest import Requests

# Taking the input from the input file and splitting each line into a Request variable that will then be used to simulate
# the planes
def create_plane_list(list_of_planes):
    plane_input = []
    largest_timer = 0
    for requests in list_of_planes:
        input_request = requests.split(",")
        new_request = Requests(input_request[0], int(input_request[1]), int(input_request[2]), int(input_request[3]))
        timer_value = (new_request.get_takeoff_time() + new_request.get_takeoff_duration())
        if timer_value >= largest_timer:
            largest_timer = timer_value
        plane_input.append(new_request)
    return plane_input, int(largest_timer) * 2
