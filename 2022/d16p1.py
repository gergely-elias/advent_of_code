import fileinput
import heapq
import collections
import networkx

input_lines = list(fileinput.input())
valve_pressures = {}
valve_graph = networkx.Graph()
for line in input_lines:
    values_on_line = line.strip().split(" ")
    valve = values_on_line[1]
    valve_pressure = int(values_on_line[4][5:-1])
    valve_pressures[valve] = valve_pressure
    neighbour_valves = [valve[:2] for valve in values_on_line[9:]]
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
total_time = 30
heap_entry_id = 0
start_state = (0, start_valve, valves_to_open, 0)
statesheap = [(0, heap_entry_id, start_state)]

max_pressures = collections.defaultdict(int)
processed_states = set()
heap_entry_id += 1
best_pressure = 0
while len(statesheap) > 0:
    _, _, current_state = heapq.heappop(statesheap)
    (
        timestamp,
        current_valve,
        valves_still_to_open,
        current_pressure_per_minute,
    ) = current_state
    current_state_max_pressure = max_pressures[current_state]
    best_pressure = max(
        best_pressure,
        (total_time - timestamp) * current_pressure_per_minute
        + current_state_max_pressure,
    )
    for next_valve in valves_still_to_open:
        distance_to_next_valve = all_distances[(current_valve, next_valve)]
        next_timestamp = timestamp + distance_to_next_valve + 1
        if next_timestamp < total_time:
            next_state = (
                next_timestamp,
                next_valve,
                tuple([valve for valve in valves_still_to_open if valve != next_valve]),
                current_pressure_per_minute + valve_pressures[next_valve],
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
