import fileinput

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
        valid_passports += 1
print(valid_passports)
