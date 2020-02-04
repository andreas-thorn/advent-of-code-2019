from functools import reduce
import math

velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
moons = [[7, 10, 17], [-2, 7, 0], [12, 5, 12], [5, -8, 6]]


def calculate_velocity(moon, moons):
    x, y, z = 0, 0, 0
    for idx, tmp in enumerate(moons):
        if tmp == moon:
            continue
        if moon[0] < tmp[0]:
            x += 1
        elif moon[0] > tmp[0]:
            x -= 1
        if moon[1] < tmp[1]:
            y += 1
        elif moon[1] > tmp[1]:
            y -= 1
        if moon[2] < tmp[2]:
            z += 1
        elif moon[2] > tmp[2]:
            z -= 1

    return [x, y, z]


def calculate_total_energy(moons, velocities):
    total = 0
    for i in range(0, 4):
        moon = moons[i]
        vel = velocities[i]

        pot = reduce(lambda x, y: abs(x)+abs(y), moon)
        kin = reduce(lambda x, y: abs(x)+abs(y), vel)
        total += (pot * kin)

    return total


def calculate(x, y, z):
    def lcm(a, b):
        return a*b//math.gcd(a, b)

    return lcm(lcm(x, y), z)


def run():
    xlist, ylist, zlist = set(), set(), set()
    x_d, y_d, z_d = 0, 0, 0
    iterations = 0
    while True:
        # Calculate the new velocities
        changed_vel = []
        for moon in moons:
            changed_vel.append(calculate_velocity(moon, moons))

        # Append the new velocity to the existing velocity
        for idx, delta in enumerate(changed_vel):
            current_vel = velocities[idx]
            velocities[idx] = [current_vel[0] + delta[0], current_vel[1] + delta[1], current_vel[2] + delta[2]]

        # Set the new positions
        for m, v in zip(moons, velocities):
            m[0] += v[0]
            m[1] += v[1]
            m[2] += v[2]

        x = list()
        y = list()
        z = list()
        for m in zip(moons, velocities):
            x.append([m[0][0], m[1][0]])
            y.append([m[0][1], m[1][1]])
            z.append([m[0][2], m[1][2]])

        if iterations == 999:
            print("Part 1: %s" % calculate_total_energy(moons, velocities))

        if x_d == 0:
            if str(x) in xlist:
                x_d = iterations
            else:
                xlist.add(str(x))
        if y_d == 0:
            if str(y) in ylist:
                y_d = iterations
            else:
                ylist.add(str(y))
        if z_d == 0:
            if str(z) in zlist:
                z_d = iterations
            else:
                zlist.add(str(z))

        if x_d and y_d and z_d:
            break
        iterations += 1

    print(f"Part 2: {calculate(x_d, y_d, z_d)}")


if __name__ == '__main__':
    run()
