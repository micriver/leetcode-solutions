"""
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
 

Example 1:

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]

notes: first list is equal to the # of spots for each size, in this case there are no small car spots in this parking system
second list is the actual cars and the ints correspond to their size. The len of the list corresponds to the # of cars! in this example, there are four but only two spots.

Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
 

Constraints:

0 <= big, medium, small <= 1000
carType is 1, 2, or 3
At most 1000 calls will be made to addCar

"""


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.vehicles = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.vehicles[0] > 0:
                self.vehicles[0] -= 1
                return True
        elif carType == 2:
            if self.vehicles[1] > 0:
                self.vehicles[1] -= 1
                return True
        elif carType == 3:
            if self.vehicles[2] > 0:
                self.vehicles[2] -= 1
                return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(1, 1, 0)
obj = ParkingSystem(1, 1, 3)
# param_1 = obj.addCar(3)  # should be false because there are (0) small spots from above
# print(param_1)
param_2 = obj.addCar(3)
param_3 = obj.addCar(3)
param_4 = obj.addCar(3)
param_5 = obj.addCar(3)
print(param_2)
print(param_3)
print(param_4)  # should return false after the first two method calls above, 2 + 3
print(param_5)  # should return false after the first two method calls above, 2 + 3


"""

failed to complete first attempt within 20 minutes 12.22.2020
2nd attempt took 6 minutes	51 seconds

SOLUTION

I was close, you need to creat a list with the given integers in the init method of the class
Then using, else if statements, check each index manually, to see if there is a space available for that car. If there is, subtract that car from the total, else return false 
The instance variables of the instance will change per each ParkingSystem created

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # create a list with the given integers
        self.vehicles  = [big,medium,small] 

    def addCar(self, carType: int) -> bool:
        if carType == 1 :
            if self.vehicles[0] > 0:
                self.vehicles[0]-=1
                return True
        elif carType == 2:
            if self.vehicles[1] > 0:
                self.vehicles[1]-=1
                return True
        elif carType == 3:
            if self.vehicles[2] > 0:
                self.vehicles[2]-=1
                return True
        return False

"""
