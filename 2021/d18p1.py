import fileinput

input_lines = list(fileinput.input())


class SnailfishNumber:
    def __init__(self, line, level=0):
        self.level = level
        if isinstance(line, int):
            self.is_leaf = True
            self.regular_value = line
        elif isinstance(line, list):
            self.is_leaf = False
            self.child_left = SnailfishNumber(line[0], level + 1)
            self.child_right = SnailfishNumber(line[1], level + 1)

    def tolist(self):
        if self.is_leaf:
            return self.regular_value
        else:
            return [self.child_left.tolist(), self.child_right.tolist()]

    def carry_to_leftmost(self, increment):
        if self.is_leaf:
            self.regular_value += increment
        else:
            self.child_left.carry_to_leftmost(increment)

    def carry_to_rightmost(self, increment):
        if self.is_leaf:
            self.regular_value += increment
        else:
            self.child_right.carry_to_rightmost(increment)

    def explode(self):
        if (
            self.level >= 4
            and not self.is_leaf
            and self.child_left.is_leaf
            and self.child_right.is_leaf
        ):
            children_values = (
                self.child_left.regular_value,
                self.child_right.regular_value,
            )
            del self.child_left
            del self.child_right
            self.is_leaf = True
            self.regular_value = 0
            return (self, True, *children_values)
        else:
            if not self.is_leaf:
                result_left = self.child_left.explode()
                if result_left[1]:
                    self.child_left = result_left[0]
                    if result_left[3] is not None:
                        self.child_right.carry_to_leftmost(result_left[3])
                    return (self, True, result_left[2], None)
                else:
                    result_right = self.child_right.explode()
                    if result_right[1]:
                        self.child_right = result_right[0]
                        if result_right[2] is not None:
                            self.child_left.carry_to_rightmost(result_right[2])
                        return (self, True, None, result_right[3])
        return (self, False)

    def split(self):
        if self.is_leaf:
            if self.regular_value >= 10:
                return (
                    SnailfishNumber(
                        [self.regular_value // 2, (self.regular_value + 1) // 2],
                        level=self.level,
                    ),
                    True,
                )
            else:
                return (self.regular_value, False)
        else:
            result_left = self.child_left.split()
            if result_left[1]:
                return (
                    SnailfishNumber(
                        [result_left[0].tolist(), self.child_right.tolist()],
                        level=self.level,
                    ),
                    True,
                )
            else:
                result_right = self.child_right.split()
                if result_right[1]:
                    return (
                        SnailfishNumber(
                            [self.child_left.tolist(), result_right[0].tolist()],
                            level=self.level,
                        ),
                        True,
                    )
                else:
                    return (self, False)

    def reduce(self):
        reducable = True
        reduced = self
        while reducable:
            reducable = False
            explode_result = reduced.explode()
            if not explode_result[1]:
                split_result = reduced.split()
                if not split_result[1]:
                    return reduced
                else:
                    reducable = True
                    reduced = split_result[0]
            else:
                reducable = True
                reduced = explode_result[0]

    def add(self, other):
        return SnailfishNumber([self.tolist(), other.tolist()]).reduce()

    def magnitude(self):
        if self.is_leaf:
            return self.regular_value
        else:
            return 3 * self.child_left.magnitude() + 2 * self.child_right.magnitude()


snailfish_numbers = [SnailfishNumber(eval(line.strip())) for line in input_lines]

final_sum = snailfish_numbers[0]
for snailfish_number_to_add in snailfish_numbers[1:]:
    final_sum = final_sum.add(snailfish_number_to_add)
print(final_sum.magnitude())
