import numpy as np
import copy
import math
import random as rd


def different_column_violations(sol):
    conflicts = 0

    for i in range(len(sol)):
        for j in range(len(sol)):
            if i != j and sol[i] == sol[j]:
                conflicts += 1

    return conflicts


def different_diagonal_violations(sol):
    conflicts = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            deltax = abs(sol[i] - sol[j])
            deltay = abs(i - j)
            if deltax == deltay:
                conflicts += 1

    return conflicts


def obj(sol):
    return different_diagonal_violations(sol) + different_column_violations(sol)


def rand_in_rand_position(sol):
    neighbor = copy.copy(sol)

    idx = np.random.randint(0, len(sol))
    value = np.random.randint(0, len(sol))

    neighbor[idx] = value

    return neighbor


def swap(sol):
    neighbor = copy.copy(sol)

    idx1 = np.random.randint(0, len(sol))
    idx2 = np.random.randint(0, len(sol))

    neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]

    return neighbor


def acceptanceProbability(current_cost, neighbor_cost, temperature):
    if neighbor_cost < current_cost:
        return 1
    return math.exp((current_cost - neighbor_cost) / temperature)


def tempera_simulada(objective, temperature=1000, ABSOLUTE_ZERO=0000.1, COOLING_RATE=0.999999, current=[], best=[], max=1000):
    best_cost = 0
    neighbor = []

    bestVal = obj(sol)
    bestSol = copy.deepcopy(sol)

    currentVal = obj(sol)
    currentSol = copy.deepcopy(sol)

    T = temperature

    for i in range(0, max):
        print(T)
        neighbor = swap(currentSol)
        neighbor_cost = objective(neighbor)

        if (neighbor_cost - currentVal < 0):
            currentSol = copy.deepcopy(neighbor)
            currentVal = neighbor_cost

            if (currentVal < bestVal):
                bestSol = copy.deepcopy(currentSol)
                bestVal = currentVal

        else:
            x = abs(rd.random())
            if (x < acceptanceProbability(currentVal, neighbor_cost, temperature)):
                currentSol = copy.deepcopy(neighbor)
                currentVal = neighbor_cost
            else:
                neighbor = copy.deepcopy(currentSol)

        T *= COOLING_RATE
        if (T < 0.1):
            T = temperature
        if tempera_simulada == ABSOLUTE_ZERO:
            break

    return neighbor, best_cost


if __name__ == '__main__':
    temperature = 1
    ABSOLUTE_ZERO = 0000.1
    COOLING_RATE = 0.999999
    current = []

    sol = [0, 1, 2, 3]
    current = copy.copy(sol)
    best_cost = obj(sol)
    sol, val = tempera_simulada(
        obj, temperature, ABSOLUTE_ZERO, COOLING_RATE,  current=current, best=[], max=1000)

    print(sol)
