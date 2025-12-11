import collections
import fileinput
import math
import networkx

input_lines = list(fileinput.input())

network = networkx.DiGraph()
for line in input_lines:
    device, outputs_raw = line.strip().split(":")
    outputs = outputs_raw.strip().split(" ")
    for output in outputs:
        network.add_edge(device, output)

device_order = list(networkx.topological_sort(network))


def path_count(a, b):
    counts = collections.defaultdict(int)
    counts[a] = 1
    for current_device in device_order[
        device_order.index(a) + 1 : device_order.index(b) + 1
    ]:
        counts[current_device] = sum(
            counts[input_device] for input_device, _ in network.in_edges(current_device)
        )
    return counts[b]


must_pass_devices = ["dac", "fft"]
must_pass_devices.sort(key=lambda x: device_order.index(x))

print(
    math.prod(
        path_count(*segment)
        for segment in zip(["svr"] + must_pass_devices, must_pass_devices + ["out"])
    )
)
