import fileinput
import collections

input_lines = list(fileinput.input())

image = input_lines[0].strip()
height = 6
width = 25
layer_size = height * width

min_zeroes = float("inf")
result = 0
for layer_starting_pixel in range(0, len(image), layer_size):
    layer = image[layer_starting_pixel : layer_starting_pixel + layer_size]
    digit_frequency = collections.Counter(layer)
    if digit_frequency["0"] < min_zeroes:
        min_zeroes = digit_frequency["0"]
        result = digit_frequency["1"] * digit_frequency["2"]
print(result)
