import fileinput
import functools

input_lines = list(fileinput.input())


@functools.cache
def count_record(springs, damaged_groups):
    if springs.count("?") + springs.count("#") < sum(damaged_groups):
        return 0
    if springs.count("#") > sum(damaged_groups):
        return 0
    if springs.count("?") == 0:
        return (
            1
            if tuple(len(group) for group in springs.split(".") if group != "")
            == damaged_groups
            else 0
        )
    first_unknown_spring_index = springs.index("?")
    known_prefix_ends_with_damaged = springs[:first_unknown_spring_index].endswith("#")
    damaged_groups_in_known_prefix = tuple(
        len(group)
        for group in springs[:first_unknown_spring_index].split(".")
        if group != ""
    )
    number_of_damaged_groups_in_known_prefix = len(damaged_groups_in_known_prefix)
    if known_prefix_ends_with_damaged:
        if (
            damaged_groups_in_known_prefix[:-1]
            != damaged_groups[: number_of_damaged_groups_in_known_prefix - 1]
        ):
            return 0
        last_prefix_damaged_group_start = first_unknown_spring_index
        while (
            last_prefix_damaged_group_start > 0
            and springs[last_prefix_damaged_group_start - 1] == "#"
        ):
            last_prefix_damaged_group_start -= 1

        last_prefix_damaged_group_length = damaged_groups_in_known_prefix[-1]
        if (
            len(springs)
            < first_unknown_spring_index
            - last_prefix_damaged_group_length
            + damaged_groups[number_of_damaged_groups_in_known_prefix - 1]
        ):
            return 0
        if (
            "."
            in springs[
                first_unknown_spring_index
                - last_prefix_damaged_group_length : first_unknown_spring_index
                - last_prefix_damaged_group_length
                + damaged_groups[number_of_damaged_groups_in_known_prefix - 1]
            ]
        ):
            return 0
        if (
            len(springs)
            > first_unknown_spring_index
            - last_prefix_damaged_group_length
            + damaged_groups[number_of_damaged_groups_in_known_prefix - 1]
            and "#"
            == springs[
                first_unknown_spring_index
                - last_prefix_damaged_group_length
                + damaged_groups[number_of_damaged_groups_in_known_prefix - 1]
            ]
        ):
            return 0
        return count_record(
            springs[
                first_unknown_spring_index
                - last_prefix_damaged_group_length : first_unknown_spring_index
            ]
            + "#"
            * (
                damaged_groups[number_of_damaged_groups_in_known_prefix - 1]
                - last_prefix_damaged_group_length
            )
            + "."
            + springs[
                first_unknown_spring_index
                - last_prefix_damaged_group_length
                + damaged_groups[number_of_damaged_groups_in_known_prefix - 1]
                + 1 :
            ],
            damaged_groups[number_of_damaged_groups_in_known_prefix - 1 :],
        )
    else:
        if (
            damaged_groups_in_known_prefix
            != damaged_groups[:number_of_damaged_groups_in_known_prefix]
        ):
            return 0
        else:
            return count_record(
                "." + springs[first_unknown_spring_index + 1 :],
                damaged_groups[number_of_damaged_groups_in_known_prefix:],
            ) + count_record(
                "#" + springs[first_unknown_spring_index + 1 :],
                damaged_groups[number_of_damaged_groups_in_known_prefix:],
            )


total_arrangement_count = 0
for condition_record in [line.strip() for line in input_lines]:
    springs, damaged_groups_raw = condition_record.split()
    damaged_groups = tuple(map(int, damaged_groups_raw.split(",")))
    total_arrangement_count += count_record(springs, damaged_groups)
print(total_arrangement_count)
