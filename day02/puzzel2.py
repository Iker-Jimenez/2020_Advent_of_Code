passwords_file = open("passwords.txt", "r")

valid_passwords = 0

# O(N)
for password_record in passwords_file:
    condition, password = password_record.split(':')
    password = password.strip()
    print("Condition is %s, password is '%s'" % (condition, password))
    positions, letter = condition.split(' ')
    position1, position2 = [int(x) for x in positions.split("-")]
    if (password[position1 - 1] == letter) != (password[position2 - 1] == letter):
        valid_passwords += 1

passwords_file.close()

print("There are %d valid passwords" % valid_passwords)
