import fileinput
import math

input_lines = list(fileinput.input())


def prime_factors(n):
    to_factor = n
    factors = dict()
    factor_candidate = 2
    while factor_candidate ** 2 <= to_factor:
        factor_count = 0
        while to_factor % factor_candidate == 0:
            factor_count += 1
            to_factor //= factor_candidate
        if factor_count > 0:
            factors[factor_candidate] = factor_count
        factor_candidate += 1
    if to_factor > 1:
        factors[to_factor] = 1
    return factors


def number_from_factors(factorisation):
    return math.prod([factor ** power for factor, power in factorisation.items()])


def totient_from_factors(factorisation):
    return math.prod(
        [
            factor ** (power - 1) * (factor - 1)
            for factor, power in factorisation.items()
        ]
    )


def min_of_dicts(dictionaries):
    common_keys = set.intersection(
        *[set(dictionary.keys()) for dictionary in dictionaries]
    )
    return {
        key: min([dictionary[key] for dictionary in dictionaries])
        for key in common_keys
    }


def max_of_dicts(dictionaries):
    common_keys = set.union(*[set(dictionary.keys()) for dictionary in dictionaries])
    return {
        key: max([dictionary[key] for dictionary in dictionaries if key in dictionary])
        for key in common_keys
    }


def chinese_remainder_theorem(remainders):
    remainder_list_with_prime_factors = [
        (remainder, prime_factors(modulus)) for modulus, remainder in remainders.items()
    ]
    common_remainder = remainder_list_with_prime_factors.pop(0)
    while len(remainder_list_with_prime_factors) > 0:
        (remainder1, mod_prime_factors1), (remainder2, mod_prime_factors2) = (
            common_remainder,
            remainder_list_with_prime_factors.pop(0),
        )

        modulus1 = number_from_factors(mod_prime_factors1)
        modulus2 = number_from_factors(mod_prime_factors2)
        lcm_modulus_factor = max_of_dicts([mod_prime_factors1, mod_prime_factors2])
        lcm_modulus = number_from_factors(lcm_modulus_factor)
        gcd_modulus_factor = min_of_dicts([mod_prime_factors1, mod_prime_factors2])

        assert gcd_modulus_factor == {}

        common_remainder = (
            (
                remainder1
                * pow(modulus2, totient_from_factors(mod_prime_factors1), lcm_modulus)
                + remainder2
                * pow(modulus1, totient_from_factors(mod_prime_factors2), lcm_modulus)
            )
            % lcm_modulus,
            lcm_modulus_factor,
        )
    return common_remainder[0]


buses = {
    int(bus): -bus_index
    for (bus_index, bus) in enumerate(input_lines[1].strip().split(","))
    if bus != "x"
}
print(chinese_remainder_theorem(buses))
