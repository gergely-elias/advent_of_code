import fileinput
import math
import itertools

input_lines = list(fileinput.input())

boss_stats = dict()
for line in input_lines:
    stat, score = line.split(":")
    boss_stats[stat] = int(score.strip())

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]


def battle_won(equipment):
    fighters_stats = [
        {
            "Hit Points": 100,
            "Damage": sum(item[1] for item in equipment),
            "Armor": sum(item[2] for item in equipment),
        },
        boss_stats,
    ]
    hits_needed = [
        math.ceil(
            fighters_stats[1 - fighter_index]["Hit Points"]
            / max(
                fighters_stats[fighter_index]["Damage"]
                - fighters_stats[1 - fighter_index]["Armor"],
                1,
            )
        )
        for fighter_index in range(2)
    ]
    return hits_needed[0] <= hits_needed[1]


most_expensive_loss = -float("inf")
weapon_options = set(itertools.combinations(weapons, 1))
armor_options = set.union(
    *[set(itertools.combinations(armor, armor_amount)) for armor_amount in range(2)]
)
ring_options = set.union(
    *[set(itertools.combinations(rings, ring_amount)) for ring_amount in range(3)]
)
for equipped_weapon, equipped_armor, equipped_rings in itertools.product(
    weapon_options, armor_options, ring_options
):
    equipment = list(equipped_weapon) + list(equipped_armor) + list(equipped_rings)
    if not battle_won(equipment):
        most_expensive_loss = max(
            most_expensive_loss, sum([item[0] for item in equipment])
        )
assert most_expensive_loss > -float("inf")
print(most_expensive_loss)
