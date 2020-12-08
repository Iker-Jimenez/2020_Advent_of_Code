from collections import Counter

count = 0

group_answers = Counter()
group_size = 0
# O(N)
with open('answers.txt', 'r') as answers_file:
    for line in answers_file:
        if not line.strip():
            for answer_count in group_answers.most_common():
                if answer_count[1] == group_size:
                    count += 1

            group_answers.clear()
            group_size = 0
        else:
            for character in line.strip():
                group_answers[character] += 1
            group_size += 1

print("Count is  %d " % count)
