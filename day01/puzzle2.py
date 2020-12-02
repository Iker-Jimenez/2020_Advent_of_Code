from collections import Counter
expenses_file = open("expenses.txt", "r")

expenses = set()
# O(N)
expenses = Counter([int(expense) for expense in expenses_file])
expenses_file.close()

# O(N^2)
found = False
for i, expense1 in enumerate(expenses):
    for j, expense2 in enumerate(expenses, i + 1):
        #print("i=%d, j=%d" % (i, j))
        remainder = 2020 - expense1 - expense2
        if remainder == expense1 or remainder == expense2:
            if expenses[remainder] > 1:
                found = True
        elif remainder in expenses:
            found = True
            break
    if found:
        print("Found numbers %d, %d, %d" % (expense1, expense2, remainder))
        print("Total value %d" % (expense1 * expense2 * remainder))
        break

