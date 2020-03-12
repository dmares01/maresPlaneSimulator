def create_schedule(plane_list, current_time, current_queue):
    current_schedule = current_queue.copy()
    flag = False
    for plane in plane_list:
        if int(current_time) == int(plane.get_submission_time()):
            x = get_index_for_insert(current_schedule, plane)
            current_schedule.insert(x, plane)
            make_takeoff_schedule(current_schedule, x)

        if remove_plane(current_time, plane, current_schedule):
            plane_to_remove = get_index(current_schedule, plane)
            del current_schedule[plane_to_remove]
            flag = True
            # print("removed ", plane.get_name())

    if len(current_schedule) != 0 or flag is True:
        return current_schedule


def make_takeoff_schedule(plane_list, index_of_new_plane):
    # print("The index is", index_of_new_plane)
    # print("The length is", len(plane_list))
    next_takeoff_time = plane_list[index_of_new_plane - 1].get_actual_takeoff()

    for plane in range(len(plane_list)):
        # print("Next takeoff time is ", next_takeoff_time)
        if plane_list[plane].get_actual_takeoff() > next_takeoff_time or plane < index_of_new_plane:
            next_takeoff_time = plane_list[plane].get_actual_takeoff() + plane_list[plane].get_takeoff_duration()
            continue
        else:
            plane_list[plane].set_actual_takeoff(next_takeoff_time)
            next_takeoff_time = plane_list[plane].get_actual_takeoff() + plane_list[plane].get_takeoff_duration()


def get_index_for_insert(plane_schedule, plane):
    for scheduled_plane in range(len(plane_schedule)):
        if plane.get_takeoff_time() < plane_schedule[scheduled_plane].get_takeoff_time():
            index = scheduled_plane
            return index
    return len(plane_schedule)


def remove_plane(time, plane, list_to_check):
    if time > plane.get_actual_takeoff() + plane.get_takeoff_duration() > 0:
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
