import fileinput
import heapq

input_lines = list(fileinput.input())

boss_stats = dict()
for line in input_lines:
    stat, score = line.split(":")
    boss_stats[stat] = int(score.strip())

initial_state = {
    "my turn": True,
    "mana": 500,
    "my hit points": 50,
    "opp damage": boss_stats["Damage"],
    "opp hit points": boss_stats["Hit Points"],
    "effect timers": {"shield": 0, "poison": 0, "recharge": 0},
}

heap_entry_id = 0
states = [(0, heap_entry_id, initial_state.copy())]
heap_entry_id += 1
while len(states) > 0:
    total_mana_spent, _, state_to_process = heapq.heappop(states)
    my_turn = state_to_process["my turn"]
    my_hit_points = state_to_process["my hit points"]
    mana = state_to_process["mana"]
    effect_timers = state_to_process["effect timers"].copy()
    opp_hit_points = state_to_process["opp hit points"]
    opp_damage = state_to_process["opp damage"]
    my_armor = 0

    if my_turn:
        my_hit_points -= 1

    if my_hit_points <= 0:
        continue

    if effect_timers["shield"] > 0:
        my_armor += 7
        effect_timers["shield"] -= 1
    if effect_timers["poison"] > 0:
        opp_hit_points -= 3
        effect_timers["poison"] -= 1
    if effect_timers["recharge"] > 0:
        mana += 101
        effect_timers["recharge"] -= 1

    if opp_hit_points <= 0:
        print(total_mana_spent)
        break

    if my_turn:
        if mana >= 53:
            heapq.heappush(
                states,
                (
                    total_mana_spent + 53,
                    heap_entry_id,
                    {
                        "my turn": False,
                        "mana": mana - 53,
                        "my hit points": my_hit_points,
                        "opp damage": opp_damage,
                        "opp hit points": opp_hit_points - 4,
                        "effect timers": effect_timers.copy(),
                    },
                ),
            )
            heap_entry_id += 1
        if mana >= 73:
            heapq.heappush(
                states,
                (
                    total_mana_spent + 73,
                    heap_entry_id,
                    {
                        "my turn": False,
                        "mana": mana - 73,
                        "my hit points": my_hit_points + 2,
                        "opp damage": opp_damage,
                        "opp hit points": opp_hit_points - 2,
                        "effect timers": effect_timers.copy(),
                    },
                ),
            )
            heap_entry_id += 1
        if mana >= 113 and effect_timers["shield"] == 0:
            heapq.heappush(
                states,
                (
                    total_mana_spent + 113,
                    heap_entry_id,
                    {
                        "my turn": False,
                        "mana": mana - 113,
                        "my hit points": my_hit_points,
                        "opp damage": opp_damage,
                        "opp hit points": opp_hit_points,
                        "effect timers": {**effect_timers.copy(), "shield": 6},
                    },
                ),
            )
            heap_entry_id += 1
        if mana >= 173 and effect_timers["poison"] == 0:
            heapq.heappush(
                states,
                (
                    total_mana_spent + 173,
                    heap_entry_id,
                    {
                        "my turn": False,
                        "mana": mana - 173,
                        "my hit points": my_hit_points,
                        "opp damage": opp_damage,
                        "opp hit points": opp_hit_points,
                        "effect timers": {**effect_timers.copy(), "poison": 6},
                    },
                ),
            )
            heap_entry_id += 1
        if mana >= 229 and effect_timers["recharge"] == 0:
            heapq.heappush(
                states,
                (
                    total_mana_spent + 229,
                    heap_entry_id,
                    {
                        "my turn": False,
                        "mana": mana - 229,
                        "my hit points": my_hit_points,
                        "opp damage": opp_damage,
                        "opp hit points": opp_hit_points,
                        "effect timers": {**effect_timers.copy(), "recharge": 5},
                    },
                ),
            )
            heap_entry_id += 1
    else:
        my_hit_points -= max(opp_damage - my_armor, 1)
        heapq.heappush(
            states,
            (
                total_mana_spent,
                heap_entry_id,
                {
                    "my turn": True,
                    "mana": mana,
                    "my hit points": my_hit_points,
                    "opp damage": opp_damage,
                    "opp hit points": opp_hit_points,
                    "effect timers": effect_timers.copy(),
                },
            ),
        )
        heap_entry_id += 1
