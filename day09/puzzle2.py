
with open('numbers.txt', 'r') as numbers_file:
    num_to_find = 22406676
    numbers = []
    for num in numbers_file:
        num = int(num)
        numbers.append(num)

    weakness_found = False
    for row_num, number in enumerate(numbers):
        total = number
        iteration = 1

        while total < num_to_find:
            total += numbers[row_num + iteration]
            iteration += 1
            if total == num_to_find:
                print("Found the weakness!")
                weakness_found = True
                break

        if weakness_found:
            smallest = min(numbers[row_num:(row_num + iteration)])
            biggest = max(numbers[row_num:(row_num + iteration)])
            weakness = smallest + biggest

            print("Weakness is %d" % weakness)
            break





