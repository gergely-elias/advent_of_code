import fileinput

input_lines = list(fileinput.input())

freq = 0
former_freqs = set([0])
while True:
    for line in input_lines:
        line = int(line.strip())
        freq += line
        if freq in former_freqs:
            print(freq)
            exit()
        else:
            former_freqs.add(freq)
