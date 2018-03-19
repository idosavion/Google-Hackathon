import Ride

ride1 = Ride.Ride([0, 0, 1, 3, 2, 9],1)
ride2 = Ride.Ride([1, 2, 1, 0, 0, 30],2)
ride3 = Ride.Ride([2, 0, 2, 2, 0, 14],3)

LOOK_AHEAD = 30

class Car:
    _bonus = 0
    _locX = 0
    _locY = 0
    _timer = 0
    _curr_mission_end = None
    rideList = []
    totalPoints = 0

    def __init__(self, bonusPts):
        self._bonus = bonusPts
        self._locX = 0
        self._locY = 0

    def findNext(self, rides, time):
        self._timer = time  # update time
        curr_max = 0
        curr_max_i = 0
        pDist = 0
        pRideTime = 0
        pBonus = False
        pick = False
        for i, ride in enumerate(rides):
            if not ride.is_taken:
                x1,y1 = ride.get_start_loc()
                x2,y2 = ride.get_finish_loc()
                dist_from_car = abs(x1-self._locX) + abs(y1-self._locY)

                ride_time = abs(x2-x1) + abs(y2-y1)
                if dist_from_car + self._timer + ride_time > ride.get_finish_time()[0]:
                    continue
                # not doable - skip to next ride
                pick=True

                if dist_from_car + self._timer <= ride.get_start_time()[0]:
                    points = ride_time + self._bonus
                    bonusThis = True
                else:
                    points = ride_time
                    bonusThis = False

                value = points/ride_time
                if (value) > curr_max:
                    curr_max = value
                    curr_max_i = i
                    pDist = dist_from_car
                    pRideTime = ride_time
                    pBonus = bonusThis

        if(pick):
            pickedRide = rides[curr_max_i]
            pickedRide.take()
            self.rideList.append(pickedRide.index)

            if pBonus:
                self._curr_mission_end = pickedRide.get_start_time()[0] + pRideTime
                self.totalPoints += self._bonus + pRideTime
            else:
                self._curr_mission_end = time + pDist + pRideTime
                self.totalPoints += pRideTime

        return curr_max_i   # index of best ride




    def move(self, curr_time, rides):
        if curr_time >= self._curr_mission_end:
            next = self.findNext(rides, curr_time)
            return next
        return -1

    def getRides(self):
        return self.rideList


mycar = Car(4)
rides = [ride1, ride3, ride2]
print(mycar.findNext(rides, 0))
print(mycar.findNext(rides, 4))
print(mycar.findNext(rides, 16))
print(mycar.getRides())
print(mycar.totalPoints)
