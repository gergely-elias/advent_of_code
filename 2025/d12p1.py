import fileinput
import math

input_lines = list(fileinput.input())
*shapes_lineblocks, regions_lineblock = "".join(input_lines).split("\n\n")

shapes = [
    shape_lineblock.strip().split("\n")[1:] for shape_lineblock in shapes_lineblocks
]
shapes_cellcount = ["".join(shape).count("#") for shape in shapes]
shapes_dimensions = [
    (len(shape), max(len(shape_row) for shape_row in shape)) for shape in shapes
]
max_shape_square_box = max(
    max(shape_dimensions) for shape_dimensions in shapes_dimensions
)

number_of_fittable_regions = 0
for region_line in regions_lineblock.strip().split("\n"):
    region_dimensions_raw, shape_counts_raw = region_line.strip().split(":")
    region_dimensions = tuple(map(int, region_dimensions_raw.split("x")))
    shape_counts = tuple(map(int, shape_counts_raw.strip().split(" ")))

    total_cellcount = sum(a * b for a, b in zip(shape_counts, shapes_cellcount))
    cellcount_fits_in = math.prod(region_dimensions) >= total_cellcount

    number_of_tiling_boxes = math.prod(
        region_dimension // max_shape_square_box
        for region_dimension in region_dimensions
    )
    tileable_with_boxes = number_of_tiling_boxes >= sum(shape_counts)

    assert cellcount_fits_in == tileable_with_boxes
    if cellcount_fits_in:
        number_of_fittable_regions += 1
print(number_of_fittable_regions)
