import heapq
from pandas import np
from pylab import plot, show, bar
import matplotlib.pyplot as plt

plt.style.use("ggplot")


def get_hour(time):
    h = int((time % 1440) / 60)
    return h


def get_day(time):
    d = int(((time / 60) / 24))
    return d


class Event():  # event class for arraiving and leaving
    def __init__(self, time, eventType, component=None, system_policy=None):
        self.time = time  # event time
        self.eventType = eventType
        self.component = component  # type of the event , elevator or passenger
        self.system_policy = system_policy  # system policy , determine if elevarot working in shabbat or improved polity
        heapq.heappush(P, self)  # add the event to the events list

    def __lt__(self, event2):
        return self.time < event2.time


class Elevator():  # class elevator , saves multiple information
    def __init__(self, current_floor, working_floors, program, time=0, door_open=True):
        self.passengers = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [],
                           13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [],
                           24: [], 25: []}
        self.current_floor = current_floor
        self.working_floors = working_floors
        self.program = program
        self.time = time
        self.door_open = door_open
        self.num_of_clients = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0,
                               14: 0, 15: 0}  # saves number fo customers in every point

    def __repr__(self):
        return str(self.program)

    def number_of_costumers(self):  # return number of people in elevator
        count = 0
        for key in self.passengers:
            count += len(self.passengers[key])
        return count


class Passenger():  # class elevator , saves multiple information
    def __init__(self, current_floor, requested_floor, id=0, arrival_time=0, waiting_time=0, elevator=None,
                 switch_floor=-1):
        self.current_floor = current_floor
        self.requested_floor = requested_floor
        self.id = id
        self.arrival_time = arrival_time
        self.waiting_time = waiting_time
        self.elevator = elevator
        self.switch_floor = switch_floor  # saves information if customer is changing floor

    def __lt__(self, event2):
        return self.arrival_time < event2.arrival_time

    def __repr__(self):  # return how to show passenger
        return "passenger"


def customer_demand1(curr_time, i):  # initialize arriving events according to table in exercise
    i += 1
    hour = get_hour(curr_time)
    current_floor = 0
    requested_floor = 0
    t_1 = np.random.random(1)  # initialize 2 random numbers
    t_2 = np.random.random(1)
    if hour >= 7 and hour < 10:  # asking the simulation the time and determine the exact pace of arriving events
        if t_1 <= (550 / 1000):  # base role
            current_floor = 0
            if t_2 <= (150 / 550):  # base role
                requested_floor = np.random.randint(1, 15)
            else:
                requested_floor = np.random.randint(16, 25)
        elif t_1 > (550 / 1000) and t_1 <= (790 / 1000):  # base role
            current_floor = np.random.randint(1, 15)
            if t_2 <= (90 / 240):  # base role
                requested_floor = 0
            elif t_2 > (90 / 240) and t_2 <= (180 / 240):  # base role
                requested_floor = np.random.randint(1, 15)
            elif t_2 > (180 / 240):  # base role
                requested_floor = np.random.randint(16, 25)
        elif t_1 > (790 / 1000):  # base role
            current_floor = np.random.randint(16, 25)
            if t_2 <= (120 / 220):
                requested_floor = 0  # base role
            elif t_2 > (120 / 220) and t_2 <= (180 / 220):
                requested_floor = np.random.randint(1, 15)
            elif t_2 > (180 / 220):  # base role
                requested_floor = np.random.randint(16, 25)
        costumer = Passenger(current_floor, requested_floor, i)
        Event(curr_time + np.random.exponential(6 / 100), "arriving", costumer)  # creating event in 1000 per hour pace

    elif hour >= 15 and hour <= 17:
        if t_1 <= (210 / 1000):  # base role
            current_floor = 0
            if t_2 <= (90 / 210):  # base role
                requested_floor = np.random.randint(1, 15)
            else:
                requested_floor = np.random.randint(16, 25)
        elif t_1 > (210 / 1000) and t_1 <= (510 / 1000):  # base role
            current_floor = np.random.randint(1, 15)
            if t_2 <= (150 / 300):  # base role
                requested_floor = 0
            elif t_2 > (150 / 300) and t_2 <= (240 / 300):  # base role
                requested_floor = np.random.randint(1, 15)
            elif t_2 > (240 / 300):  # base role
                requested_floor = np.random.randint(16, 25)
        elif t_1 > (510 / 1000):  # base role
            current_floor = np.random.randint(16, 25)
            if t_2 <= (400 / 500):  # base role
                requested_floor = 0
            elif t_2 > (400 / 500) and t_2 <= (460 / 500):  # base role
                requested_floor = np.random.randint(1, 15)
            elif t_2 > (460 / 500):
                requested_floor = np.random.randint(16, 25)

        costumer = Passenger(current_floor, requested_floor, i)
        Event(curr_time + np.random.exponential(3 / 50), "arriving", costumer)  # creating event in 1000 per hour pace

    elif hour == 6 or (hour >= 10 and hour < 15) or (hour >= 18 and hour <= 19):  # base role
        if t_1 <= (130 / 510):  # base role
            current_floor = 0
            if t_2 <= (60 / 130):  # base role
                requested_floor = np.random.randint(1, 15)
            else:
                requested_floor = np.random.randint(16, 25)
        elif t_1 > (130 / 510) and t_1 <= (340 / 510):  # base role
            current_floor = np.random.randint(1, 15)
            if t_2 <= (60 / 210):  # base role
                requested_floor = 0
            elif t_2 > (60 / 210) and t_2 <= (150 / 210):  # base role
                requested_floor = np.random.randint(1, 15)
            elif t_2 > (150 / 210):  # base role
                requested_floor = np.random.randint(16, 25)
        elif t_1 > (340 / 510):  # base role
            current_floor = np.random.randint(16, 25)
            if t_2 <= (70 / 170):  # base role
                requested_floor = 0
            elif t_2 > (70 / 170) and t_2 <= (130 / 170):  # base role
                requested_floor = np.random.randint(1, 15)
            elif t_2 > (130 / 170):  # base role
                requested_floor = np.random.randint(16, 25)
        costumer = Passenger(current_floor, requested_floor, i)
        Event(curr_time + np.random.exponential(3 / 25), "arriving", costumer)  # creating event in 500 per hour pace

    elif hour >= 20 or hour <= 5:
        print("office building close")
        costumer = Passenger(0, 1, i)
        if get_hour(curr_time) <= 5:
            Event(curr_time + abs(get_hour(curr_time) - 6) * 60, "arriving", costumer)
        elif get_hour(curr_time) >= 20:
            Event(curr_time + abs(24 - get_hour(curr_time) + 6) * 60, "arriving", costumer)


def Patience_Over(floor_line, current_floor, curr_time):  # checks if people wait in line over 15 minutes
    get_switchers = []
    num_of_leavers = 0
    if len(floor_line[current_floor]) > 0:
        while (curr_time - floor_line[current_floor][
            0].arrival_time) > 15:  # checks the first person in line 'if he waits over 15 minutes he will removed from heap
            top_info = heapq.heappop(floor_line[event.component.current_floor])
            num_of_leavers += 1
            if top_info.switch_floor != -1 and current_floor == 0:  # if person in floor number 0 is changing floor , we will re incert him back to line
                get_switchers.append(top_info)
                num_of_leavers -= 1
            if len(floor_line[event.component.current_floor]) == 0:
                break
        for switcher in get_switchers:  # re insert people that change floor to the line
            heapq.heappush(floor_line[current_floor], switcher)
    return num_of_leavers  # return number of people that left


def Improved_policy(floor_line,
                    elevator):  # function that return the nearest floors that people are waiting for service/wait to get off
    index_current = elevator.working_floors.index(elevator.current_floor)
    index_floor = None
    index_demand = None
    if elevator.program == "up":
        for floor in elevator.working_floors[
                     index_current + 1:]:  # check what is the closest floor where people are waiting
            if len(floor_line[floor]) > 0:
                index_floor = elevator.working_floors.index(floor)
                break
        for demand in elevator.working_floors[
                      index_current + 1:]:  # check what is the closest floor where people in elevator are planing to get off
            if len(elevator.passengers[demand]) > 0:
                index_demand = elevator.working_floors.index(demand)
                break
    if elevator.program == "down":
        for floor in reversed(
                elevator.working_floors[:index_current]):  # check what is the closest floor where people are waiting
            if len(floor_line[floor]) > 0:
                index_floor = elevator.working_floors.index(floor)
                break
        for demand in reversed(elevator.working_floors[
                               :index_current]):  # check what is the closest floor where people in elevator are planing to get off
            if len(elevator.passengers[demand]) > 0:
                index_demand = elevator.working_floors.index(demand)
                break
    return index_floor, index_demand  # return the indexes


how_long = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
            15: 0}  # dictionary to calculate number of people
prev_time = 0
i = 0
P = []
sys_leaving = 0
total_service_time = 0
T = 60 * 24 * 10  # initialize time of simulation
curr_time = 0
floor_line = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [],
              14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [],
              25: []}  # dictionary for lines , heap in every value
elevator_1 = Elevator(0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "up")  # initialize elevator
elevator_2 = Elevator(15, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "down")  # initialize elevator
elevator_3 = Elevator(16, [0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "up")  # initialize elevator
elevator_4 = Elevator(25, [0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "down")  # initialize elevator
elevator_list = [elevator_1, elevator_2, elevator_3, elevator_4]  # elevator list
Event(curr_time, "door_open", elevator_1, "improved")  # initialize door open event
Event(curr_time, "door_open", elevator_2, "improved")  # initialize door open event
Event(curr_time, "door_open", elevator_3, "improved")  # initialize door open event
Event(curr_time, "door_open", elevator_4, "improved")  # initialize door open event
first = Passenger(0, 1, i)  # first arrival time
Event(curr_time, "arriving", first)  # first arrival time
leaving = 0  # counter fo leavers
over_15 = 0  # counter of leavers that waited over 15 minutes
while curr_time <= T:  # check if p is empty or not
    event = heapq.heappop(P)
    prev_time = curr_time
    curr_time = event.time
    if get_hour(curr_time) >= 6 and get_hour(curr_time) < 20 and (
            curr_time - prev_time) < 15:  # incert into dictionery in key that represent the number fo people in each elevator the total time that they occupied it
        elevator_1.num_of_clients[elevator_1.number_of_costumers()] += (curr_time - prev_time)
        elevator_2.num_of_clients[elevator_2.number_of_costumers()] += (curr_time - prev_time)
        elevator_3.num_of_clients[elevator_3.number_of_costumers()] += (curr_time - prev_time)
        elevator_4.num_of_clients[elevator_4.number_of_costumers()] += (curr_time - prev_time)
    if event.eventType == "arriving":
        # print("customer arrived at : " , curr_time)
        count = True
        customer = event.component
        current_floor = event.component.current_floor
        requested_floor = event.component.requested_floor
        event.component.arrival_time = curr_time
        customer_demand1(curr_time, i)  # initialize next arriving event
        if current_floor != requested_floor:
            if len(floor_line[current_floor]) == 0:  # if the line in that certain flor is empty
                for elevator in elevator_list:  # checks all elevators
                    if current_floor == elevator.current_floor and elevator.door_open and elevator.number_of_costumers() < 15:  # if all conditions are true
                        if requested_floor in elevator.working_floors and ((
                                                                                   requested_floor > current_floor and  # if elevator in the currect movment according to requested floor
                                                                                   elevator.program == "up") or (
                                                                                   requested_floor < current_floor and elevator.program == "down")):
                            count = False
                            elevator.passengers[requested_floor].append(customer)
                            break
                        elif elevator.program == "down" and requested_floor not in elevator.working_floors:  # if coustomer want to reach floor that he cannot go to directly
                            event.component.switch_floor = requested_floor
                            event.component.requested_floor = 0
                            elevator.passengers[0].append(event.component)
                            count = False
                            break
                if count:  # if none of the elevator answers the conditions
                    heapq.heappush(floor_line[current_floor],
                                   event.component)  # if none of the elevators are suitable , push to line
            else:
                heapq.heappush(floor_line[current_floor], event.component)  # if the line is not empty , push to line

    elif event.eventType == "door_open":
        event.component.door_open = True
        new_line = []
        elevator = event.component
        current_floor1 = elevator.current_floor
        temp11 = Patience_Over(floor_line, current_floor1, curr_time)
        over_15 += temp11
        leaving += temp11
        total_service_time += (temp11 * 15)
        while elevator.passengers[current_floor1]:  # removes all passengers that need to get off in the current floor
            finisher = elevator.passengers[current_floor1].pop()
            leaving += 1
            if finisher.switch_floor != -1 and current_floor1 == 0:  # if customer is changing floor
                finisher.requested_floor = finisher.switch_floor
                heapq.heappush(floor_line[0], finisher)  # push him into line in num 0 floor
                leaving -= 1
            else:
                key = int(curr_time - finisher.arrival_time)
                if key in how_long:  # insert duration of service into dictionary
                    how_long[key] += 1
                else:
                    how_long[key] = 1
        # print("elevator arrived in floor num :" , current_floor1 , "total people served :" ,count_1)
        while elevator.number_of_costumers() < 15 and floor_line[
            current_floor1]:  # checks that elevator can handle more people
            individual = heapq.heappop(
                floor_line[current_floor1])  # pop from line , and check all parameters for hoping on elevator
            if individual.requested_floor in elevator.working_floors and \
                    ((individual.requested_floor > elevator.current_floor and
                      elevator.program == "up") or (individual.requested_floor < elevator.current_floor and
                                                    elevator.program == "down")):
                elevator.passengers[individual.requested_floor].append(individual)
            elif elevator.program == "down" and individual.requested_floor not in elevator.working_floors:
                individual.switch_floor = individual.requested_floor
                individual.requested_floor = 0
                elevator.passengers[individual.requested_floor].append(individual)
            else:
                new_line.append(individual)  # if non of the parameters fit ,return customer to line
        for new in new_line:  # insert people back to line if they didn't hope on elevator
            heapq.heappush(floor_line[current_floor1], new)
        event.component = elevator
        z = np.random.random(1)
        if z <= 0.005:  # check possibility for jamming
            Event(curr_time + np.random.randint(5, 15) + 5 / 60, "door_close", event.component, "improved")
            # print("door jam at :" , curr_time)
        else:
            Event(curr_time + 5 / 60, "door_close", event.component, "improved")

    elif event.eventType == "door_close":
        event.component.door_open = False
        max_passenger = (0, 0)
        elevator = event.component
        last_floor = elevator.current_floor
        j = elevator.working_floors.index(elevator.current_floor)
        if event.system_policy == "shabat":  # shabat system
            if elevator.program == "up" and (
                    elevator.current_floor < elevator.working_floors[-2]):  # check elevator status
                elevator.current_floor = elevator.working_floors[
                    j + 1]  # if going up and current floor is smaller then the max floor
            elif elevator.program == "up" and (
                    elevator.current_floor == elevator.working_floors[-2]):  # check elevator status
                elevator.current_floor = elevator.working_floors[
                    -1]  # if going up and next floor is max , change program to down
                elevator.program = "down"
            elif elevator.program == "down" and (
                    elevator.current_floor > elevator.working_floors[1]):  # check elevator status
                elevator.current_floor = elevator.working_floors[j - 1]  # if current floor is bigger than min floor
            elif elevator.program == "down" and (
                    elevator.current_floor == elevator.working_floors[1]):  # check elevator status
                elevator.current_floor = elevator.working_floors[0]  # if next floor is 0 , change program to up
                elevator.program = "up"
            Event(curr_time + abs(last_floor - elevator.current_floor) * 1 / 60 + 4 / 60, "door_open", elevator,
                  "shabat")  # initialize door open event after 2 sec acceleration , 2 second braking and 1 second opening

        elif event.system_policy == "improved":  # new method
            if elevator.program == "up" and (elevator.current_floor < elevator.working_floors[-2]):
                index_floor, index_demand = Improved_policy(floor_line, elevator)  # call for function
                if index_floor != None or index_demand != None:  # if one of them is not None
                    if index_floor != None and index_demand != None:  # if both of them are not none
                        go_to = min(index_floor, index_demand)  # choose the closest one
                        elevator.current_floor = elevator.working_floors[go_to]
                    elif index_floor != None and index_demand == None:  # if one is not none and the other one is , chose him
                        elevator.current_floor = elevator.working_floors[index_floor]
                    elif index_floor == None and index_demand != None:
                        elevator.current_floor = elevator.working_floors[index_demand]
                    if elevator.current_floor == elevator.working_floors[-1]:
                        elevator.program = "down"
                    Event(curr_time + abs(last_floor - elevator.current_floor) * (1 / 60) + (4 / 60), "door_open",
                          elevator, "improved")  # inithalize new event
                else:
                    Event(curr_time + 6 / 100, "door_open",
                          elevator)  # if both are none , wait for 3.6 second until nex event
            elif elevator.program == "up" and (elevator.current_floor == elevator.working_floors[-2]):
                elevator.current_floor = elevator.working_floors[-1]
                elevator.program = "down"
                Event(curr_time + abs(last_floor - elevator.current_floor) * (1 / 60) + (4 / 60), "door_open", elevator,
                      "improved")

            elif elevator.program == "down" and (
                    elevator.current_floor > elevator.working_floors[1]):  # similar method as up
                index_floor, index_demand = Improved_policy(floor_line, elevator)
                if index_floor != None or index_demand != None:
                    if index_floor != None and index_demand != None:
                        go_to = max(index_floor, index_demand)
                        elevator.current_floor = elevator.working_floors[go_to]
                    elif index_floor != None and index_demand == None:
                        elevator.current_floor = elevator.working_floors[index_floor]
                    elif index_floor == None and index_demand != None:
                        elevator.current_floor = elevator.working_floors[index_demand]
                    if elevator.current_floor == elevator.working_floors[0]:
                        elevator.program = "up"
                    Event(curr_time + abs(last_floor - elevator.current_floor) * (1 / 60) + (4 / 60), "door_open",
                          elevator, "improved")
                else:
                    Event(curr_time + 6 / 100, "door_open", elevator)
            elif elevator.program == "down" and (elevator.current_floor == elevator.working_floors[1]):
                elevator.current_floor = elevator.working_floors[0]
                elevator.program = "up"
                Event(curr_time + abs(last_floor - elevator.current_floor) * (1 / 60) + 4 / 60, "door_open", elevator,
                      "improved")

print(over_15 / 10)
plt.bar(range(len(elevator_4.num_of_clients)), elevator_4.num_of_clients.values(),
        tick_label=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
plt.savefig('bar.png')
plt.show()
