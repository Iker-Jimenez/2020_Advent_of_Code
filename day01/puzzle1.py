expenses_file = open("expenses.txt", "r")

expenses = set()
# O(N)
for expense in expenses_file:
    expenses.add(int(expense))
expenses_file.close()
# O(N)
for expense in expenses:
    remaining = 2020 - expense
    if remaining in expenses:
        print("Found numbers %d, %d" % (expense, remaining))
        print("Total value %d" % (remaining * expense))
