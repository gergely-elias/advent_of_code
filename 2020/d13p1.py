import fileinput

input_lines = list(fileinput.input())

earliest_timestamp = int(input_lines[0].strip())
buses = [int(bus) for bus in input_lines[1].strip().split(",") if bus != "x"]

timestamp = earliest_timestamp
while all([timestamp % bus != 0 for bus in buses]):
    timestamp += 1
print(
    (timestamp - earliest_timestamp)
    * buses[[timestamp % bus for bus in buses].index(0)],
)
