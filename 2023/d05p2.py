import fileinput

input_lines = list(fileinput.input())
input_blocks = "".join(input_lines).strip().split("\n\n")
product_ranges_raw = list(map(int, input_blocks[0].split(":")[1].split()))
product_ranges = sorted(
    [tuple(product_ranges_raw[i : i + 2]) for i in range(0, len(product_ranges_raw), 2)]
)


def map_product_ranges(product_ranges, mapping):
    next_product_ranges = []
    while len(product_ranges):
        product_start, product_length = product_ranges[0]
        if len(mapping):
            mapping_source_start, mapping_destination_start, mapping_length = mapping[0]
            if mapping_source_start < product_start:
                if mapping_source_start + mapping_length <= product_start:
                    mapping.pop(0)
                else:
                    mapping[0] = (
                        product_start,
                        mapping_destination_start
                        - mapping_source_start
                        + product_start,
                        mapping_length + mapping_source_start - product_start,
                    )
            elif product_start < mapping_source_start:
                if product_start + product_length <= mapping_source_start:
                    next_product_ranges.append(product_ranges.pop(0))
                else:
                    next_product_ranges.append(
                        (product_start, mapping_source_start - product_start)
                    )
                    product_ranges[0] = (
                        mapping_source_start,
                        product_length - mapping_source_start + product_start,
                    )
            else:
                if product_length <= mapping_length:
                    next_product_ranges.append(
                        (mapping_destination_start, product_length)
                    )
                    product_ranges.pop(0)
                    mapping[0] = (
                        product_start + product_length,
                        mapping_destination_start + product_length,
                        mapping_length - product_length,
                    )
                else:
                    next_product_ranges.append(
                        (mapping_destination_start, mapping_length)
                    )
                    product_ranges[0] = (
                        product_start + mapping_length,
                        product_length - mapping_length,
                    )
                    mapping.pop(0)
        else:
            next_product_ranges.extend(product_ranges)
            product_ranges.clear()
    return next_product_ranges


def merge_product_ranges(product_ranges):
    under_merge_start, under_merge_length = product_ranges.pop(0)
    next_product_ranges = []
    while len(product_ranges):
        product_start, product_length = product_ranges.pop(0)
        if product_start > under_merge_start + under_merge_length:
            next_product_ranges.append((under_merge_start, under_merge_length))
            under_merge_start, under_merge_length = product_start, product_length
        else:
            under_merge_length = max(
                under_merge_length, product_length + product_start - under_merge_start
            )
    next_product_ranges.append((under_merge_start, under_merge_length))
    return next_product_ranges


for step in range(1, len(input_blocks)):
    mapping = sorted(
        [
            (source_range_start, destination_range_start, range_length)
            for destination_range_start, source_range_start, range_length in map(
                lambda x: map(int, x.split()),
                input_blocks[step].strip().split("\n")[1:],
            )
        ]
    )
    product_ranges = merge_product_ranges(
        sorted(map_product_ranges(product_ranges, mapping))
    )
print(product_ranges[0][0])
