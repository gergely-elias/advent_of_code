import fileinput

input_lines = list(fileinput.input())
input_blocks = "".join(input_lines).strip().split("\n\n")
products = set(map(int, input_blocks[0].split(":")[1].split()))

for step in range(1, len(input_blocks)):
    mapped_products_new = set()
    mapped_products_old = set()
    for destination_range_start, source_range_start, range_length in map(
        lambda x: map(int, x.split()), input_blocks[step].strip().split("\n")[1:]
    ):
        for product in products:
            if (
                product >= source_range_start
                and product < source_range_start + range_length
            ):
                mapped_products_new.add(
                    product - source_range_start + destination_range_start
                )
                mapped_products_old.add(product)
        products.difference_update(mapped_products_old)
    products.update(mapped_products_new)
print(min(products))
