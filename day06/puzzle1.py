
count = 0

group_answers = set()
# O(N)
with open('answers.txt', 'r') as answers_file:
    for line in answers_file:
        if not line.strip():
            count += len(group_answers)
            group_answers.clear()
        else:
            for character in line.strip():
                group_answers.add(character)

print("Count is  %d " % count)
