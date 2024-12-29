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


def merge_free_memory(free_memory_index):
    if free_memory_index >= 0 and free_memory_index < len(free_memory_list) - 1:
        free_memory = free_memory_list[free_memory_index]
        next_free_memory = free_memory_list[free_memory_index + 1]
        if free_memory[0] + free_memory[1] == next_free_memory[0]:
            merged_free_memory = (free_memory[0], free_memory[1] + next_free_memory[1])
            free_memory_list.pop(free_memory_index + 1)
            free_memory_list.pop(free_memory_index)
            free_memory_list.insert(free_memory_index, merged_free_memory)


used_memory_index = len(used_memory_list) - 1
while used_memory_index > 0:
    used_memory_pointer, used_memory_length, used_memory_file_id = used_memory_list[
        used_memory_index
    ]
    free_memory_index = 0
    while free_memory_index < len(free_memory_list):
        free_memory_pointer, free_memory_length = free_memory_list[free_memory_index]
        if free_memory_pointer > used_memory_pointer:
            break
        if free_memory_length >= used_memory_length:
            free_memory_list.pop(free_memory_index)
            used_memory_list.pop(used_memory_index)
            freshly_used_memory = (
                free_memory_pointer,
                used_memory_length,
                used_memory_file_id,
            )
            used_memory_list.append(freshly_used_memory)
            freshly_free_memory = (used_memory_pointer, used_memory_length)
            freshly_free_memory_index = bisect.bisect(
                free_memory_list, freshly_free_memory
            )
            free_memory_list.insert(freshly_free_memory_index, freshly_free_memory)
            merge_free_memory(freshly_free_memory_index)
            merge_free_memory(freshly_free_memory_index - 1)
            if free_memory_length > used_memory_length:
                leftover_free_memory = (
                    free_memory_pointer + used_memory_length,
                    free_memory_length - used_memory_length,
                )
                free_memory_list.insert(free_memory_index, leftover_free_memory)
                merge_free_memory(free_memory_index)
            break
        free_memory_index += 1
    used_memory_index -= 1

print(
    sum(
        (file_id * (2 * pointer + (length - 1)) * length) // 2
        for pointer, length, file_id in used_memory_list
    )
)
