from settings import *
from bus import Bus
import plotter
import random

def getAmountOfPeople():
    return len([ None for _ in range(BUS_SEATS) if random.random() < SINGULAR_SEAT_OCCUPATION_PROBABILITY ])

def simulate(t, a):
    people_in_bus = getAmountOfPeople()
    
    people_before = int(people_in_bus * t)
    
    bus = Bus(BUS_SEATS)

    for x in range(people_before):
        bus.join(random.random())

    p_seat = bus.join(a)

    for x in range(people_in_bus - people_before - 1):
        bus.join(random.random())

    return bus.isAlone(p_seat)


result = {}

t_steps = 100
for x in range(t_steps + 1):
    t = x / t_steps
    print("Simulating for t = " + str(t))


    simulations = 10000
    successes = 0
    for x in range(simulations):
        if simulate(t, 0.5):
            successes += 1
    
    result[t] = successes / simulations

print(result)
plotter.plot_graph(result)

