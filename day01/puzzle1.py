from collections import Counter
expenses_file = open("expenses.txt", "r")


# O(N)
expenses = Counter([int(expense) for expense in expenses_file])
expenses_file.close()

# O(N)
for expense in expenses:
    found = False
    remaining = 2020 - expense
    if remaining == expense:
        if expenses[expense] > 1:
            found = True
    elif remaining in expenses:
        found = True

    if found:
        print("Found numbers %d, %d" % (expense, remaining))
        print("Total value %d" % (remaining * expense))
