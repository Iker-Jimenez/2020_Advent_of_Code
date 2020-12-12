
with open('adapters.txt', 'r') as adapters_file:
    adapters = []
    for adapter in adapters_file:
        adapters.append(int(adapter))

    adapters.sort()
    print(adapters)

    diff_of_1 = 0
    diff_of_3 = 0
    previous_adapter = 0
    for adapter in adapters:
        voltage_diff = adapter - previous_adapter
        if voltage_diff == 1:
            diff_of_1 += 1
        elif voltage_diff == 3:
            diff_of_3 += 1
        previous_adapter = adapter

    #Add one more between the highest adapter and the device
    diff_of_3 += 1
    print("There are %d differences of 1 and %d differences of 3" % (diff_of_1, diff_of_3))

    print("Result is %d" % (diff_of_1 * diff_of_3))





