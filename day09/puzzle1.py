import queue

with open('numbers.txt', 'r') as numbers_file:
    preamble_size = 25
    previous_nums = queue.Queue(preamble_size)
    for row_num, num in enumerate(numbers_file):
        num = int(num)
        print("Processing %d" % num)

        if row_num < preamble_size:
            print("Adding %d into the preamble" % num)
            previous_nums.put(num)
        else:

            found = False
            for item_num, num_i in enumerate(previous_nums.queue):
                for num_j in list(previous_nums.queue)[item_num:]:
                    if num_i + num_j == num:
                        found = True
                        break
                if found:
                    break
            if found:
                previous_nums.get()
                previous_nums.put(num)
            else:
                print("%d is not calculated as the sum of 2 of the previous %d numbers" % (num, preamble_size))
                break







