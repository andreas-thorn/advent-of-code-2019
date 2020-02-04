import math
from collections import defaultdict
import itertools

asteroid_map = '''###..#########.#####.
.####.#####..####.#.#
.###.#.#.#####.##..##
##.####.#.###########
###...#.####.#.#.####
#.##..###.########...
#.#######.##.#######.
.#..#.#..###...####.#
#######.##.##.###..##
#.#......#....#.#.#..
######.###.#.#.##...#
####.#...#.#######.#.
.######.#####.#######
##.##.##.#####.##.#.#
###.#######..##.#....
###.##.##..##.#####.#
##.########.#.#.#####
.##....##..###.#...#.
#..#.####.######..###
..#.####.############
..##...###..#########'''


def get_asteroids(input_data=None):
    asteroids = []
    for y, row in enumerate(input_data.split('\n')):
        for x, point in enumerate(row):
            if point == "#":
                asteroids.append((x, y))
    return asteroids


def find_visible_asteroids(asteroid, targets):
    visible_asteroids = []
    x, y = asteroid
    for target in targets:
        if asteroid == target:
            continue
        target_x, target_y = target
        delta_x = x - target_x
        delta_y = y - target_y
        radians = math.atan2(delta_y, delta_x)
        degrees = round(math.degrees(radians), 1)
        if degrees not in visible_asteroids:
            visible_asteroids.append(degrees)

    return visible_asteroids


def get_angle(source, target):
    delta_X = source[0] - target[0]
    delta_Y = source[1] - target[1]
    return math.degrees(math.atan2(delta_X, delta_Y) % (2 * math.pi))


asteroids = get_asteroids(asteroid_map)
targets = []

for asteroid in asteroids:
    targets.append((len(find_visible_asteroids(asteroid, asteroids)), asteroid))


lazer_asteroid = max(targets)
print(f"Part 1: {lazer_asteroid[1]}")


def get_distance(source, target):
    dx = source[0] - target[0]
    dy = target[1] - source[1]
    return math.sqrt(dx * dx + dy * dy)


def part_two():
    asteroids = get_asteroids(asteroid_map)
    asteroids.remove(lazer_asteroid[1])
    angles = defaultdict(list)

    for asteroid in asteroids:
        angle = 360 - get_angle(lazer_asteroid[1], asteroid)
        if angle == 360:
            angle = 0

        angles[angle].append(asteroid)

    sort_by_angle = [angles[angle] for angle in sorted(angles.keys())]
    for asteroids in sort_by_angle:
        asteroids.sort(key=lambda a: get_distance(lazer_asteroid[1], a), reverse=True)

    destroyed = 0
    for angle in itertools.cycle(sort_by_angle):
        if angle:
            asteroidtmp = angle.pop()
            destroyed += 1

            if destroyed == 200:
                return asteroidtmp[0] * 100 + asteroidtmp[1]


print(f"Part 2: {part_two()}")
