import fileinput
import heapq
import collections
import networkx
import itertools

input_lines = list(fileinput.input())
valve_pressures = {}
valve_graph = networkx.Graph()
for line in input_lines:
    values_on_line = line.strip().split(" ")
    valve = values_on_line[1]
    valve_pressure = int(values_on_line[4][5:-1])
    neighbour_valves = [valve[:2] for valve in values_on_line[9:]]
    valve_pressures[valve] = valve_pressure
    for neighbour_valve in neighbour_valves:
        valve_graph.add_edge(valve, neighbour_valve)

valves_to_open = tuple(
    [valve for valve, pressure in valve_pressures.items() if pressure > 0]
)
all_distances = {}
for valve, neighbour_valves in networkx.all_pairs_shortest_path_length(valve_graph):
    for neighbour_valve, distance in neighbour_valves.items():
        all_distances[(valve, neighbour_valve)] = distance

start_valve = "AA"
total_time = 26
heap_entry_id = 0
workers = 2
start_state = (0, tuple([start_valve] * workers), valves_to_open, 0)
statesheap = [(0, heap_entry_id, start_state)]

max_pressures = collections.defaultdict(int)
processed_states = set()
heap_entry_id += 1
best_pressure = 0
while len(statesheap) > 0:
    _, _, current_state = heapq.heappop(statesheap)
    (
        timestamp,
        current_valves,
        valves_still_to_open,
        current_pressure_per_minute,
    ) = current_state
    current_state_max_pressure = max_pressures[current_state]
    remaining_time = total_time - timestamp
    upper_limit_from_current_state = (
        current_state_max_pressure
        + current_pressure_per_minute * remaining_time
        + sum(
            [
                a * b
                for a, b in zip(
                    list(
                        reversed(
                            sorted([valve_pressures[valve] for valve in valves_to_open])
                        )
                    )[: (remaining_time + 1) // 2 * workers],
                    list(
                        reversed(sorted(list(range(remaining_time, 0, -2)) * workers))
                    ),
                )
            ]
        )
    )
    if upper_limit_from_current_state <= best_pressure:
        continue
    best_pressure = max(
        best_pressure,
        (total_time - timestamp) * current_pressure_per_minute
        + current_state_max_pressure,
    )
    for worker_index in range(workers):
        worker_current_valve = current_valves[worker_index]
        other_workers_valves = (
            current_valves[:worker_index] + current_valves[worker_index + 1 :]
        )
        for next_valve in valves_still_to_open:
            distance_to_next_valve = all_distances[(worker_current_valve, next_valve)]
            next_timestamp = timestamp + distance_to_next_valve + 1
            if next_timestamp < total_time:
                next_valves = [
                    list(
                        set(
                            [
                                (
                                    "move",
                                    networkx.shortest_path(
                                        valve_graph,
                                        other_worker_valve,
                                        target_valve,
                                    )[distance_to_next_valve + 1],
                                )
                                for target_valve in valves_still_to_open
                                if all_distances[(other_worker_valve, target_valve)]
                                >= distance_to_next_valve + 1
                            ]
                            + [
                                ("open", valve)
                                for valve in valves_still_to_open
                                if all_distances[(other_worker_valve, valve)]
                                == distance_to_next_valve
                            ]
                        )
                    )
                    for other_worker_valve in other_workers_valves
                ]
                for next_valve_tuple in itertools.product(*next_valves):

                    next_valve_resorted = tuple(
                        sorted(
                            [next_valve]
                            + list([valve[1] for valve in next_valve_tuple])
                        )
                    )
                    next_open = tuple(
                        [
                            valve
                            for valve in valves_still_to_open
                            if valve != next_valve
                            and valve
                            not in [
                                new_open_valve[1]
                                for new_open_valve in next_valve_tuple
                                if new_open_valve[0] == "open"
                            ]
                        ]
                    )
                    next_state = (
                        next_timestamp,
                        next_valve_resorted,
                        next_open,
                        current_pressure_per_minute
                        + valve_pressures[next_valve]
                        + sum(
                            [
                                valve_pressures[new_open_valve[1]]
                                for new_open_valve in set(next_valve_tuple)
                                if new_open_valve[0] == "open"
                                and new_open_valve[1] != next_valve
                            ]
                        ),
                    )
                    next_state_pressure = (
                        next_timestamp - timestamp
                    ) * current_pressure_per_minute + current_state_max_pressure
                    if max_pressures[next_state] < next_state_pressure:
                        max_pressures[next_state] = next_state_pressure
                    if next_state not in processed_states:
                        processed_states.add(next_state)
                        heapq.heappush(
                            statesheap,
                            (
                                next_timestamp,
                                heap_entry_id,
                                next_state,
                            ),
                        )
                        heap_entry_id += 1

print(best_pressure)
