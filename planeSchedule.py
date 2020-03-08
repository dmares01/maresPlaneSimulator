import takeoffRequest


def create_schedule(plane_list, current_time, current_queue):
    # current_schedule = []
    current_schedule = current_queue.copy()
    for plane in plane_list:
        # print("in for loop")
        if int(current_time) == int(plane.get_submission_time()):
            x = get_index(current_schedule, plane)
            print(x)
            current_schedule.insert(x, plane)
            # print(current_schedule)
    if len(current_schedule) != 0:
        return current_schedule


def get_index(plane_schedule, plane):
    for scheduled_plane in range(len(plane_schedule)):
        if plane.get_takeoff_time() < plane_schedule[scheduled_plane].get_takeoff_time():
            index = scheduled_plane
            return index
    return len(plane_schedule)
