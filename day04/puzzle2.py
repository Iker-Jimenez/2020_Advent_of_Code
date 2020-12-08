import re

expected_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def validate_height(height):
    if height.endswith('cm') and len(height) == 5 and height[:3].isdigit():
        height_cm = int(height[:3])
        if 150 <= height_cm <= 193:
            return True
    elif height.endswith('in') and len(height) == 4 and height[:2].isdigit():
        height_in = int(height[:2])
        if 59 <= height_in <= 76:
            return True

    return False


def validate_year(year, min_year, max_year):
    return year.isdigit() and min_year <= int(year) <= max_year


def validate_hair_colour(hair_colour):
    return re.match(r"^#[0-9a-f]{6}$", hair_colour)


def validate_eye_colour(eye_colour):
    return eye_colour in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])


def validate_passport_id(passport_id):
    return re.match(r"^[0-9]{9}$", passport_id)


def validate_passport(passport):
    found_key_values = dict()
    for key_value in passport.split(' '):
        key, value = key_value.split(':')
        found_key_values[key] = value
    if not expected_fields.issubset(found_key_values.keys()):
        return False
    else:
        return validate_year(found_key_values['byr'], 1920, 2002) \
            and validate_year(found_key_values['iyr'], 2010, 2020) \
            and validate_year(found_key_values['eyr'], 2020, 2030) \
            and validate_height(found_key_values['hgt']) \
            and validate_hair_colour(found_key_values['hcl']) \
            and validate_eye_colour(found_key_values['ecl']) \
            and validate_passport_id(found_key_values['pid'])


valid_passports = 0
current_passport = ""

# O(N)
with open('passports.txt', 'r') as passport_file:
    for line in passport_file:
        if not line.strip():
            if validate_passport(current_passport.strip()):
                valid_passports += 1
            current_passport = ""
        else:
            current_passport += line.strip() + " "

    else:
        # No more lines to be read from file
        if validate_passport(current_passport.strip()):
            valid_passports += 1

print("There are %s valid passports" % valid_passports)
