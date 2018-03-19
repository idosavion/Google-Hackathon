import Ride, Car


class Board:
    _time = 0
    _current_time = 0
    _car_list = []
    _ride_list = []
    _rows = 0
    _columns = 0
    _bunus = 0
    _relevant_index = 0

    def __init__(self, rows, cols, num_cars, num_rides, bonus, time, ride_description):
        self._time = time
        self._bunus = bonus
        self._columns = cols
        self._rows = rows
        for i in range(num_rides):
            self._ride_list.append(Ride.Ride(ride_description[i], i))
        for i in range(num_cars):
            self._car_list.append(Car.Car(self._bunus))
        self.sort_rides()

    def sort_rides(self):
        """
        sorts by finish time
        :return:
        """
        self._ride_list.sort(key=lambda x: x.get_finish_time()[0])

    def one_step(self):
        """
        runs one step of assignment
        every car is given a list of relevant assignments and chooses the best one
        :return:
        """
        ride = self._ride_list[self._relevant_index]
        while ride.f_time[0] < self._current_time and self._relevant_index < len(self._ride_list)-2:
            self._relevant_index += 1
            ride = self._ride_list[self._relevant_index]
        for a_car in self._car_list:
            a_car.move(self._current_time, self._ride_list[self._relevant_index:min((self._relevant_index+200),len(self._ride_list)-1)])

    def assign_rides(self):
        """
        runs the whole assignment process
        :return:
        """
        while self._current_time < self._time:
            self.one_step()
            self._current_time += 1
            print(self._current_time)
        print("Times Up!")

    def get_car_list(self):
        return self._car_list
