import takeoffRequest


def create_schedule(plane_list, current_time):
    current_schedule = []
    for plane in plane_list:
        if plane.get_submission_time() == current_time:
            current_schedule.append(plane)

    return current_schedule
