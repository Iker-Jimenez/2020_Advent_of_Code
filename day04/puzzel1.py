
expected_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def validate_passport(passport):
    found_keys = set()
    for key_value in passport.split(' '):
        key = key_value.split(':')[0]
        found_keys.add(key)
    return expected_fields.issubset(found_keys)

valid_passports = 0
current_passport = ""

# O(N)
with open('passports.txt', 'r') as passport_file:
    for line in passport_file:
        if not line.strip():
            if validate_passport(current_passport.strip()):
                valid_passports += 1
            #print(current_passport)
            current_passport = ""
        else:
            current_passport += line.strip() + " "

    else:
        # No more lines to be read from file
        if validate_passport(current_passport.strip()):
            valid_passports += 1
        #print(current_passport)

print("There are %s valid passports" % valid_passports)
