import takeoffRequest


def create_schedule(plane_list, current_time):
    current_schedule = []
    for plane in plane_list:
        if int(current_time) == int(plane.get_submission_time()):
            current_schedule.append(plane)
    return current_schedule
