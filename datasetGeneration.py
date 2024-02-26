import math
import matplotlib.pyplot as plt
import numpy as np


def initBoids(numBoids=100, width=300, height=300):
    global boids
    boids = []
    for _ in range(numBoids):
        boids.append({
            'x': np.random.random() * width - width / 2,
            'y': np.random.random() * height - height / 2,
            'dx': np.random.random() * 10 - 5,
            'dy': np.random.random() * 10 - 5,
            'history': []
        })


def distance(boid1, boid2):
    return np.sqrt((boid1['x'] - boid2['x']) ** 2 + (boid1['y'] - boid2['y']) ** 2)


def nClosestBoids(boid, n):
    sortedBoids = boids[np.argsort(distance(boid, boids))][1:n + 1]
    return sortedBoids  # Closest agent is itself, so range is from 1 to n


def sizeCanvas():
    global width, height
    width = plt.gcf().get_size_inches()[0] * plt.gcf().dpi
    height = plt.gcf().get_size_inches()[1] * plt.gcf().dpi


def flyInDirection(boid, speed=0, direction=0, speedNoiseFactor=0., directionNoiseFactor=0.):
    speed_ = speed + np.random.normal(0.0, speedNoiseFactor)
    direction_ = np.radians(direction + np.random.random() * 360 / np.pi)
    boid['x'] += speed_ * np.cos(direction_)
    boid['y'] += speed_ * np.sin(direction_)


def keepWithinBounds(boid, margin=200, turnFactor=1, isBounded=False):
    if isBounded:
        if boid['x'] < -margin:
            boid['dx'] += turnFactor
        if boid['x'] > margin:
            boid['dx'] -= turnFactor
        if boid['y'] < -margin:
            boid['dy'] += turnFactor
        if boid['y'] > margin:
            boid['dy'] -= turnFactor


def flyTowardsCenter(boid, visualRange=40, centeringFactor=0.005):
    centerX = 0
    centerY = 0
    numNeighbors = 0
    for otherBoid in boids:
        if distance(boid, otherBoid) < visualRange:
            centerX += otherBoid['x']
            centerY += otherBoid['y']
            numNeighbors += 1
    if numNeighbors:
        centerX /= numNeighbors
        centerY /= numNeighbors
        boid['dx'] += (centerX - boid['x']) * centeringFactor
        boid['dy'] += (centerY - boid['y']) * centeringFactor


def avoidOthers(boid, minDistance=20, avoidFactor=0.05):
    moveX = 0
    moveY = 0
    for otherBoid in boids:
        if otherBoid != boid:
            if distance(boid, otherBoid) < minDistance:
                moveX += boid['x'] - otherBoid['x']
                moveY += boid['y'] - otherBoid['y']
    boid['dx'] += moveX * avoidFactor
    boid['dy'] += moveY * avoidFactor


def matchVelocity(boid, matchingFactor=0.05, visualRange=40):
    avgDX = 0
    avgDY = 0
    numNeighbors = 0
    for otherBoid in boids:
        if distance(boid, otherBoid) < visualRange:
            avgDX += otherBoid['dx']
            avgDY += otherBoid['dy']
            numNeighbors += 1
    if numNeighbors:
        avgDX /= numNeighbors
        avgDY /= numNeighbors
        boid['dx'] += (avgDX - boid['dx']) * matchingFactor
        boid['dy'] += (avgDY - boid['dy']) * matchingFactor


def limitSpeed(boid, speedLimit=15):
    speed = math.sqrt(boid['dx'] ** 2 + boid['dy'] ** 2)
    if speed > speedLimit:
        boid['dx'] = (boid['dx'] / speed) * speedLimit
        boid['dy'] = (boid['dy'] / speed) * speedLimit


def drawBoid(boid):
    # angle = math.atan2(boid['dy'], boid['dx'])
    plt.plot(boid['x'], boid['y'], 'o', color='#558cf4', markersize=1)
    # plt.arrow(boid['x'], boid['y'], 5 * math.cos(angle), 5 * math.sin(angle), head_width=1, color='#558cf4')


def saveData(fileName):
    global boids
    numBoids = len(boids)

    # Save the coordinates of each boid for each frame
    data = []
    for frame in range(len(boids[0]['history'])):
        frameData = []
        for boid in boids:
            x, y = boid['history'][frame]
            frameData.extend([x, y])
        data.append(frameData)

    # Write the data to the file
    with open(fileName, 'w') as f:
        # Write the header line with x1, y1, x2, y2, ...
        header = ','.join([f'x{i},y{i}' for i in range(1, numBoids + 1)])
        f.write(header + '\n')

        # Write the data for each frame
        for frameData in data:
            line = ','.join([str(coord) for coord in frameData])
            f.write(line + '\n')


# def animationLoop(speed=0, direction=45, speednNoiseFactor=0., directionNoiseFactor=0.0, visualRange=40, centeringFactor=0.005, minDistance=20, avoidFactor = 0.05, matchingFactor = 0.05, speedLimit=15, margin=200, turnFactor=1, isBounded=True, draw=True):
#     global boids
#     for boid in boids:
#         # flyInDirection(boid, speed, direction, speednNoiseFactor, directionNoiseFactor)
#         flyTowardsCenter(boid, visualRange, centeringFactor)
#         avoidOthers(boid, minDistance, avoidFactor)
#         matchVelocity(boid, matchingFactor, visualRange)
#         limitSpeed(boid, speedLimit)
#         keepWithinBounds(boid, margin, turnFactor, isBounded)
#         boid['x'] += boid['dx']
#         boid['y'] += boid['dy']
#         boid['history'].append((boid['x'], boid['y']))
#         # boid['history'] = boid['history'][-50:]

#     if draw:
#         plt.clf()
#         for boid in boids:
#             drawBoid(boid)
#         plt.xlim(-1500, 1500)
#         plt.ylim(-1500, 1500)
#         plt.gca().set_aspect('equal', adjustable='box')
#         plt.xticks([])
#         plt.yticks([])
#         plt.pause(0.01)

def animationLoop(speed=0, direction=45, speedNoiseFactor=0., directionNoiseFactor=0.0, visualRange=40,
                  centeringFactor=0.005, minDistance=20,
                  avoidFactor=0.05, matchingFactor=0.05, speedLimit=15, margin=200, turnFactor=1, isBounded=True,
                  draw=True):
    global boids
    tempBoids = boids.copy()
    for i, boid in enumerate(boids):
        flyInDirection(tempBoids[i], speed, direction, speedNoiseFactor, directionNoiseFactor)
        flyTowardsCenter(tempBoids[i], visualRange, centeringFactor)
        avoidOthers(tempBoids[i], minDistance, avoidFactor)
        matchVelocity(tempBoids[i], matchingFactor, visualRange)
        limitSpeed(tempBoids[i], speedLimit)
        keepWithinBounds(tempBoids[i], margin, turnFactor, isBounded)
        tempBoids[i]['x'] += tempBoids[i]['dx']
        tempBoids[i]['y'] += tempBoids[i]['dy']
        tempBoids[i]['history'].append((tempBoids[i]['x'], tempBoids[i]['y']))
    boids = tempBoids

    if draw:
        plt.clf()
        for boid in boids:
            drawBoid(boid)
        plt.xlim(-1000, 1000)
        plt.ylim(-1000, 1000)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xticks([])
        plt.yticks([])
        plt.pause(0.01)


if __name__ == '__main__':
    sizeCanvas()
    speed = 0
    direction = 0
    speednNoiseFactor = np.random.random() * 0.1
    directionNoiseFactor = np.random.random() * 0.1

    minDistance = np.random.random() * 20 + 15
    visualRange = np.random.random() * 40 + minDistance + 40
    centeringFactor = np.random.random() * 0.01 + 0.005
    avoidFactor = np.random.random() * 0.02 + 0.04
    matchingFactor = np.random.random() * 0.02 + 0.04
    speedLimit = np.random.random() * 10 + 10
    margin = 600
    turnFactor = 1


    initBoids(numBoids=100, width=200, height=200)
    print(speed, direction, speednNoiseFactor, directionNoiseFactor, visualRange, centeringFactor, minDistance,
          avoidFactor, matchingFactor, speedLimit)

    for i in range(500):
        animationLoop(speed, direction, speednNoiseFactor, directionNoiseFactor, visualRange, centeringFactor,
                      minDistance,
                      avoidFactor, matchingFactor, speedLimit, margin, turnFactor, isBounded=True, draw=True)

    plt.show()
