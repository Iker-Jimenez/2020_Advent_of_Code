passwords_file = open("passwords.txt", "r")

valid_passwords = 0

# O(N)
for password_record in passwords_file:
    condition, password = password_record.split(':')
    password = password.strip()
    print("Condition is %s, password is '%s'" % (condition, password))
    min_max, letter = condition.split(' ')
    min_occurrences, max_occurrences = [int(x) for x in min_max.split("-")]
    num_occurrences = password.count(letter)
    if min_occurrences <= num_occurrences <= max_occurrences:
        valid_passwords += 1

passwords_file.close()

print("There are %d valid passwords" % valid_passwords)
