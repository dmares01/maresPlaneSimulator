import takeoffRequest


def create_schedule(plane_list, current_time, current_queue):
    current_schedule = current_queue.copy()
    for plane in plane_list:
        if int(current_time) == int(plane.get_submission_time()):
            x = get_index_for_insert(current_schedule, plane)
            current_schedule.insert(x, plane)

        if remove_plane(current_time, plane, current_schedule):
            plane_to_remove = get_index(current_schedule, plane)
            del current_schedule[plane_to_remove]
            # print("removed ", plane.get_name())
            
    if len(current_schedule) != 0:
        return current_schedule


def get_index_for_insert(plane_schedule, plane):
    for scheduled_plane in range(len(plane_schedule)):
        if plane.get_takeoff_time() < plane_schedule[scheduled_plane].get_takeoff_time():
            index = scheduled_plane
            return index
    return len(plane_schedule)


def remove_plane(time, plane, list_to_check):
    if time > (plane.get_takeoff_time() + plane.get_takeoff_duration()):
        if plane in list_to_check:
            return True


def get_index(list_of_planes, plane):
    for compare_plane in range(len(list_of_planes)):
        if plane.get_name() == list_of_planes[compare_plane].get_name():
            return compare_plane
    print("\n\ngonna crash")
    return 100


def print_all_planes(all_planes):
    for plane in all_planes:
        print(plane.get_name())
