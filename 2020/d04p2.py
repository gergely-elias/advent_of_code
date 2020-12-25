import fileinput
import re

input_lines = list(fileinput.input())

passports = " ".join([line.strip() for line in input_lines]).split("  ")


def parse_passport(passport):
    fields = {}
    for field in passport.split():
        field_name, field_value = field.split(":")
        fields[field_name] = field_value
    return fields


valid_passports = 0
for passport in passports:
    passport_fields = parse_passport(passport)
    if len(passport_fields) == 8 or (
        len(passport_fields) == 7 and "cid" not in passport_fields
    ):
        if (
            (int(passport_fields["byr"]) in range(1920, 2003))
            and (int(passport_fields["iyr"]) in range(2010, 2021))
            and (int(passport_fields["eyr"]) in range(2020, 2031))
            and (
                (
                    passport_fields["hgt"][-2:] == "cm"
                    and int(passport_fields["hgt"][:-2]) in range(150, 194)
                )
                or (
                    passport_fields["hgt"][-2:] == "in"
                    and int(passport_fields["hgt"][:-2]) in range(59, 77)
                )
            )
            and re.match(r"^#[0-9a-f]{6}$", passport_fields["hcl"])
            and (
                passport_fields["ecl"]
                in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            )
            and re.match(r"^[0-9]{9}$", passport_fields["pid"])
        ):
            valid_passports += 1
print(valid_passports)
