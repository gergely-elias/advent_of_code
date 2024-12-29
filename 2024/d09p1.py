import bisect
import fileinput

input_lines = list(fileinput.input())
line = list(map(int, list(input_lines[0].strip())))

used_memory_list = []
free_memory_list = []
digit_marks_file = True
pointer = 0
file_id = 0
for length in line:
    if digit_marks_file:
        used_memory_list.append((pointer, length, file_id))
        file_id += 1
    else:
        if length > 0:
            free_memory_list.append((pointer, length))
    pointer += length
    digit_marks_file ^= True

while free_memory_list:
    first_free_memory_pointer, first_free_memory_length = free_memory_list[0]
    (
        last_used_memory_pointer,
        last_used_memory_length,
        last_used_memory_file_id,
    ) = used_memory_list[-1]
    if first_free_memory_pointer > last_used_memory_pointer:
        break
    free_memory_list.pop(0)
    used_memory_list.pop()
    if first_free_memory_length > last_used_memory_length:
        leftover_free_memory = (
            first_free_memory_pointer + last_used_memory_length,
            first_free_memory_length - last_used_memory_length,
        )
        free_memory_list.insert(0, leftover_free_memory)
    if last_used_memory_length > first_free_memory_length:
        leftover_used_memory = (
            last_used_memory_pointer,
            last_used_memory_length - first_free_memory_length,
            last_used_memory_file_id,
        )
        used_memory_list.append(leftover_used_memory)
    freshly_used_memory = (
        first_free_memory_pointer,
        min(first_free_memory_length, last_used_memory_length),
        last_used_memory_file_id,
    )
    bisect.insort(used_memory_list, freshly_used_memory)

print(
    sum(
        (file_id * (2 * pointer + (length - 1)) * length) // 2
        for pointer, length, file_id in used_memory_list
    )
)
