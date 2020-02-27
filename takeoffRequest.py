class Requests:
    def __init__(self):
        self.name = " "
        self.submission_time = 0
        self.takeoff_time = 0
        self.takeoff_duration = 0

    def __init__(self, plane_name, submitted_time, requested_time, requested_duration):
        # do some thing here
        self.name = plane_name
        self.submission_time = submitted_time
        self.takeoff_time = requested_time
        self.takeoff_duration = requested_duration

    def get_name(self):
        return self.name

    def get_submission_time(self):
        return self.submission_time

    def get_takeoff_time(self):
        return self.takeoff_time

    def get_takeoff_duration(self):
        return self.takeoff_duration

# Need setter functions as well
    def set_name(self, new_name):
        self.name = new_name

    def set_submission_time(self, new_submission_time):
        self.submission_time = new_submission_time

    def set_takeoff_time(self, new_takeoff_time):
        self.takeoff_time = new_takeoff_time

    def set_takeoff_duration(self, new_takeoff_duration):
        self.takeoff_duration = new_takeoff_duration
