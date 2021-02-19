# Creating the new schedule for plane take off. Flag is included to only update the schedule if a plane is removed.
# Otherwise the schedule is passes onto a different function to add new planes to the list
def create_schedule(plane_list, current_time, current_queue):
    current_schedule = current_queue.copy()
    flag = False
    for plane in plane_list:
        # If the current time is the same as the time a request would be submitted, add that plane to the queue
        if int(current_time) == int(plane.get_submission_time()):
            x = get_index_for_insert(current_schedule, plane)
            current_schedule.insert(x, plane)
            make_takeoff_schedule(current_schedule, x)

        # If the plane currently taking off has cleared the runway than remove it from the queue
        if remove_plane(current_time, plane, current_schedule):
            plane_to_remove = get_index_to_remove(current_schedule, plane)
            del current_schedule[plane_to_remove]
            flag = True

    if len(current_schedule) != 0 or flag is True:
        return current_schedule

# Adding new planes to the queue as their requests are submitted
def make_takeoff_schedule(plane_list, index_of_new_plane):

    # Getting the time for when the next plane is scheduled to take off
    next_takeoff_time = plane_list[index_of_new_plane - 1].get_actual_takeoff()

    # Setting up the next_takeoff_time for when the runway will next be available
    for plane in range(len(plane_list)):
        if plane_list[plane].get_actual_takeoff() > next_takeoff_time or plane < index_of_new_plane:
            next_takeoff_time = plane_list[plane].get_actual_takeoff() + plane_list[plane].get_takeoff_duration()
            continue
        else:
            plane_list[plane].set_actual_takeoff(next_takeoff_time)
            next_takeoff_time = plane_list[plane].get_actual_takeoff() + plane_list[plane].get_takeoff_duration()

# Function to find where in the queue to add a new plane once its request has been submitted
def get_index_for_insert(plane_schedule, plane):
    for scheduled_plane in range(len(plane_schedule)):
        if plane.get_takeoff_time() < plane_schedule[scheduled_plane].get_takeoff_time():
            index = scheduled_plane
            return index
    return len(plane_schedule)

# Remove the plane from the queue once it has successfully taken off
def remove_plane(time, plane, list_to_check):
    if time > plane.get_actual_takeoff() + plane.get_takeoff_duration() > 0:
        if plane in list_to_check:
            return True

# Getting the index of the plane to remove from the queue
def get_index_to_remove(list_of_planes, plane):
    for remove_plane_index in range(len(list_of_planes)):
        if plane.get_name() == list_of_planes[remove_plane_index].get_name():
            return remove_plane_index
    print("\n\nprogram is gonna crash")
    return 100

# Test function to print out list of planes when modifying code
def print_all_planes(all_planes):
    for plane in all_planes:
        print(plane.get_name())
