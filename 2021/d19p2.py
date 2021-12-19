import fileinput
import re
import itertools

input_lines = list(fileinput.input())

dimension = 3
input_blocks = [
    scanner_block.strip().split("\n")
    for scanner_block in "".join(input_lines).split("\n\n")
]
beacons_by_scanner = dict()
for input_block in input_blocks:
    scanner_id = int(re.findall(r"\d+", input_block[0])[0])
    beacon_positions = [list(map(int, line.split(","))) for line in input_block[1:]]
    beacons_by_scanner[scanner_id] = beacon_positions

scanner_ids = list(beacons_by_scanner)
scanners_to_locate = scanner_ids[1:]
known_beacon_locations = set(map(tuple, beacons_by_scanner[scanner_ids[0]]))
known_scanner_locations = [(0,) * dimension]

scanner_to_locate = scanners_to_locate[-1]
prev_scanners_to_locate = scanners_to_locate
while len(scanners_to_locate) > 0:
    scanner_to_locate = scanners_to_locate[
        (prev_scanners_to_locate.index(scanner_to_locate) + 1) % len(scanners_to_locate)
    ]
    scanner_located = False
    for axis_direction in itertools.product([-1, 1], repeat=dimension):
        for coordinate_shuffle in itertools.permutations(range(dimension)):
            aligned_beacons = [
                tuple(
                    beacon[coordinate_shuffle[coord_index]]
                    * axis_direction[coord_index]
                    for coord_index in range(dimension)
                )
                for beacon in beacons_by_scanner[scanner_to_locate]
            ]
            for already_located_beacon in known_beacon_locations:
                for current_scanner_aligned_beacon in aligned_beacons:
                    possible_translation = tuple(
                        current_scanner_aligned_beacon[coord_index]
                        - already_located_beacon[coord_index]
                        for coord_index in range(dimension)
                    )
                    translated_beacons = set(
                        tuple(
                            beacon_to_translate[coord_index]
                            - possible_translation[coord_index]
                            for coord_index in range(dimension)
                        )
                        for beacon_to_translate in aligned_beacons
                    )
                    if (
                        len(translated_beacons.intersection(known_beacon_locations))
                        >= 12
                    ):
                        known_beacon_locations.update(translated_beacons)
                        known_scanner_locations.append(possible_translation)
                        prev_scanners_to_locate = scanners_to_locate[:]
                        scanners_to_locate.remove(scanner_to_locate)
                        scanner_located = True
                        break
                if scanner_located:
                    break
            if scanner_located:
                break
        if scanner_located:
            break
print(
    max(
        [
            sum(
                [
                    abs(coordinate_pair[0] - coordinate_pair[1])
                    for coordinate_pair in zip(*scanner_pair_locations)
                ]
            )
            for scanner_pair_locations in itertools.permutations(
                known_scanner_locations, 2
            )
        ]
    )
)
