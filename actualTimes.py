def print_out_final(plane_queue, output):
    for plane in plane_queue:
        take_off = plane.get_actual_takeoff()
        end_time = take_off + plane.get_takeoff_duration()
        print(plane.get_name(), " (", take_off, " - ", end_time, ")", file=output, sep='')


def print_queue_to_file(plane_queue, timer, output):
    print("The plane queue for timer", timer, "is:", file=output)
    for plane in plane_queue:
        if timer >= plane.get_actual_takeoff():
            print(plane.get_name(), "took off at", plane.get_actual_takeoff(), "for",
                  plane.get_takeoff_duration(), "counts", file=output)
        else:
            print(plane.get_name(), "will take off at", plane.get_actual_takeoff(), "for",
                  plane.get_takeoff_duration(), "counts", file=output)

    if len(plane_queue) == 0:
        print("empty\n", file=output)
    else:
        print("", file=output)
