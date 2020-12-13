import fileinput
import math

input_lines = list(fileinput.input())


def extended_gcd(a, b):
    u = (1, 0)
    v = (0, 1)
    while b:
        q = a // b
        u, v = v, (u[0] - q * v[0], u[1] - q * v[1])
        a, b = b, a % b
    return a, u


def chinese_remainder_theorem(remainders):
    while len(remainders) > 1:
        (modulo1, remainder1) = remainders.popitem()
        (modulo2, remainder2) = remainders.popitem()

        gcd, bezout_coeffs = extended_gcd(modulo1, modulo2)
        assert gcd == 1
        remainders[modulo1 * modulo2] = (
            remainder1 * modulo2 * bezout_coeffs[1]
            + remainder2 * modulo1 * bezout_coeffs[0]
        ) % (modulo1 * modulo2)
    return remainders.popitem()[1]


buses = {
    int(bus): -bus_index
    for (bus_index, bus) in enumerate(input_lines[1].strip().split(","))
    if bus != "x"
}
print(chinese_remainder_theorem(buses))
