import fileinput

input_lines = list(fileinput.input())

image = input_lines[0].strip()
height = 6
width = 25
layer_size = height * width

result = ["?"] * layer_size
for layer_starting_pixel in range(0, len(image), layer_size):
    layer = image[layer_starting_pixel : layer_starting_pixel + layer_size]
    result = [
        " X?"[int(layer[pixel_index])]
        if result[pixel_index] == "?"
        else result[pixel_index]
        for pixel_index in range(layer_size)
    ]

for row_index in range(height):
    print("".join(result[row_index * width : (row_index + 1) * width]))
