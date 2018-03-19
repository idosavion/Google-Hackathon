class Ride:
    def __init__(self, params, index):
        self.start = [params[0], params[1]]  # a,b
        self.end = [params[2], params[3]]  # x,y
        self.s_time = [params[4]]
        self.f_time = [params[5]]
        self.is_taken = False
        self.index = index

    def get_start_loc(self):
        return self.start

    def get_finish_loc(self):
        return self.end

    def get_finish_time(self):
        return self.f_time

    def get_start_time(self):
        return self.s_time

    def is_taken(self):
        return self.is_taken

    def take(self):
        self.is_taken = True
