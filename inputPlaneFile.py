# inputPlaneFile.py
# author: Drew Mares
# Created on: 02/27/2020
from takeoffRequest import Requests


def create_plane_list(list_of_planes):
    plane_input = []
    largest_timer = 0
    for requests in list_of_planes:
        input_request = requests.split(",")
        new_request = Requests(input_request[0], int(input_request[1]), int(input_request[2]), int(input_request[3]))
        if new_request.get_submission_time() >= largest_timer:
            largest_timer = new_request.get_submission_time()
        plane_input.append(new_request)
    return plane_input, int(largest_timer) * 2
