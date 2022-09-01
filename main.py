from random import random
import numpy as np
import math
import csv

# column 0 is id
# column 1 is mass (Solar masses)
# column 2 is age  (Years)
# column 3 is xcor (lightyears)
# column 4 is ycor
# column 5 is xvel (lightyears/year)
# column 6 is yvel
# column 7 is xacc (lightyears/year^2)
# column 8 is yacc
# column 9 is c0x
# column 10 is c0y
# column 11 is c1x
# column 12 is c1y
# column 13 is c2x
# column 14 is c2y
# column 15 is c3x
# column 16 is c3y
# column 17 is k0x
# column 18 is k0y
# column 19 is k1x
# column 20 is k1y
# column 21 is k2x
# column 22 is k2y
# column 23 is k3x
# column 24 is k3y



#setup
def setup() :
    mass = 4000000 #mass of black hole
    global timestep
    timestep = 1000000 #timestep
    global id
    id = 1
    global time
    time = 0
    global particles
    particles = np.zeros((1, 25))
    particles[0, 1] = mass
    global G
    G = 6.674 * (10 ** -11) * 5.03018108651911 * (10 ** 31) * 1.1809322 * (10 ** -48) * 9.9451879 * (10 ** 14) #kg-> M, m^2 -> ly ^2

#functions
def createparticle(mass, xcor, ycor, xvel, yvel):
    global id
    info = np.append(np.array([[id, mass, 0, xcor, ycor, xvel, yvel]]), np.zeros(18))
    info = np.reshape(info, (1, 25))
    id += 1
    global particles
    particles = np.append(particles, info, axis=0)

def grav(mass, x2, y2, x1, y1): # 2 is the object with a mass
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    if distance == 0.0:
        return 0, 0
    acc = (G * mass) / (distance ** 2)
    return acc * ((x2-x1)/distance), acc * ((y2-y1)/distance)

def c0():
    global particles
    for each in particles:
        each[9] = each[5]
        each[10] = each[6]
def k0():
    global particles
    for row in particles:
        xacc = 0
        yacc = 0
        for each in particles:
            x, y = grav(each[1], each[3], each[4], row[3], row[4])
            xacc += x
            yacc += y
        row[17] = xacc
        row[18] = yacc
def c1():
    global particles
    for each in particles:
        each[11] = each[5] + (timestep / 2) * each[17]
        each[12] = each[6] + (timestep / 2) * each[18]
def k1():
    global particles
    for row in particles:
        xacc = 0
        yacc = 0
        updated = row[3] + (timestep / 2) * row[9], row[4] + (timestep / 2) * row[10]
        for each in particles:
            x, y = grav(each[1], each[3] + (timestep / 2) * each[9], each[4] + (timestep / 2) * each[10], updated[0], updated[1])
            xacc += x
            yacc += y
        row[19] = xacc
        row[20] = yacc
def c2():
    global particles
    for each in particles:
        each[13] = each[5] + (timestep / 2) * each[19]
        each[14] = each[6] + (timestep / 2) * each[20]
def k2():
    global particles
    for row in particles:
        xacc = 0
        yacc = 0
        updated = row[3] + (timestep / 2) * row[11], row[4] + (timestep / 2) * row[12]
        for each in particles:
            x, y = grav(each[1], each[3] + (timestep / 2) * each[11], each[4] + (timestep / 2) * each[12], updated[0], updated[1])
            xacc += x
            yacc += y
        row[21] = xacc
        row[22] = yacc
def c3():
    global particles
    for each in particles:
        each[15] = each[5] + timestep * each[21]
        each[16] = each[6] + timestep * each[22]
def k3():
    global particles
    for row in particles:
        xacc = 0
        yacc = 0
        updated = row[3] + timestep * row[13], row[4] + timestep * row[14]
        for each in particles:
            x, y = grav(each[1], each[3] + timestep * each[13], each[4] + timestep * each[14], updated[0], updated[1])
            xacc += x
            yacc += y
        row[23] = xacc
        row[24] = yacc


def step():
    c0()
    k0()
    c1()
    k1()
    c2()
    k2()
    c3()
    k3()
    for each in particles:
        each[3] = each[3] + (timestep / 6) * (each[9] + 2 * each[11] + 2 * each[13] + each[15])
        each[4] = each[4] + (timestep / 6) * (each[10] + 2 * each[12] + 2 * each[14] + each[16])
        each[5] = each[5] + (timestep / 6) * (each[17] + 2 * each[19] + 2 * each[21] + each[23])
        each[6] = each[6] + (timestep / 6) * (each[18] + 2 * each[20] + 2 * each[22] + each[24])

def simulate(steps):
    global time
    with open('Data/data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(np.insert(particles.flatten(), 0, time))
        for i in range(steps):
            step()
            time += timestep
            writer.writerow(np.insert(particles.flatten(), 0, time))




gravconst = (6.674 * (10 ** -11) * 5.03018108651911 * (10 ** 31) * 1.1809322 * (10 ** -48) * 9.9451879 * (10 ** 14))
print(gravconst)
print(math.sqrt((gravconst * 4000000) / 10000))
setup()
createparticle(1, 10000, 0, 0, 3.97131087904067e-05)
for i in range(200):
    createparticle(1, int((random() - 0.5) * 20000), int((random() - 0.5) * 20000), 0, 0)
simulate(500)