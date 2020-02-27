# inputPlaneFile.py
# author: Drew Mares
# Created on: 02/27/2020
from takeoffRequest import Requests


def create_plane_list(list_of_planes):
    plane_input = []

    for requests in list_of_planes:
        input_request = requests.split(",")
        new_request = Requests(input_request[0], input_request[1], input_request[2], input_request[3])
        plane_input.append(new_request)
    return plane_input
