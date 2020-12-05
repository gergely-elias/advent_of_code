input_file = open("inputd20.txt", "r")
input_lines = input_file.readlines()

import re
import itertools
import numpy
import collections

particles = []

for line in input_lines:
    line = line.strip()
    line = re.findall("<[^>]*>", line)
    particle = {}
    particle["position"] = list(map(int, re.findall("-?\d+", line[0])))
    particle["velocity"] = list(map(int, re.findall("-?\d+", line[1])))
    particle["acceleration"] = list(map(int, re.findall("-?\d+", line[2])))
    particles.append(particle)

possible_collision_ticks = set()
for particle1, particle2 in itertools.combinations(particles, 2):
    pair_collision_ticks = set()
    for coordinate_index in range(3):
        delta_acceleration = (
            particle1["acceleration"][coordinate_index]
            - particle2["acceleration"][coordinate_index]
        )
        delta_velocity = (
            particle1["velocity"][coordinate_index]
            - particle2["velocity"][coordinate_index]
        )
        delta_position = (
            particle1["position"][coordinate_index]
            - particle2["position"][coordinate_index]
        )
        roots = numpy.roots(
            [
                delta_acceleration,
                delta_acceleration + 2 * delta_velocity,
                2 * delta_position,
            ]
        )
        nonnegative_roots_rounded = set(
            filter(lambda root: root >= 0, [int(numpy.real(root)) for root in roots])
        )
        if coordinate_index == 0:
            pair_collision_ticks = nonnegative_roots_rounded
        else:
            pair_collision_ticks.intersection_update(nonnegative_roots_rounded)
    possible_collision_ticks.update(pair_collision_ticks)
ordered_possible_collision_ticks = sorted(list(possible_collision_ticks))

not_collided_particles = set(range(len(particles)))
for tick in ordered_possible_collision_ticks:
    particles_at_position = collections.defaultdict(lambda: [])
    for particle_index in not_collided_particles:
        particle = particles[particle_index]
        particle_position = tuple(
            [
                particle["position"][coordinate_index]
                + particle["velocity"][coordinate_index] * tick
                + particle["acceleration"][coordinate_index] * tick * (tick + 1) // 2
                for coordinate_index in range(3)
            ]
        )
        particles_at_position[particle_position].append(particles.index(particle))
    for position in particles_at_position:
        collided = particles_at_position[position]
        if len(collided) > 1:
            not_collided_particles = not_collided_particles.difference(set(collided))
print(len(not_collided_particles))
