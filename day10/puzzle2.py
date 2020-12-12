
def count_paths(current_idx, current_adapter, adapters):
    num_paths = 0

    if current_idx == len(adapters) - 1:
        num_paths += 1
    else:
        if current_idx + 1 < len(adapters) and adapters[current_idx + 1] - current_adapter <= 3:
            num_paths += count_paths(current_idx + 1, adapters[current_idx + 1], adapters)
        if current_idx + 2 < len(adapters) and adapters[current_idx + 2] - current_adapter <= 3:
            num_paths += count_paths(current_idx + 2, adapters[current_idx + 2], adapters)
        if current_idx + 3 < len(adapters) and adapters[current_idx + 3] - current_adapter <= 3:
            num_paths += count_paths(current_idx + 3, adapters[current_idx + 3], adapters)

    return num_paths

with open('adapters.txt', 'r') as adapters_file:
    adapters = []
    for adapter in adapters_file:
        adapters.append(int(adapter))

    adapters.sort()
    print(adapters)

    current_idx = -1

    total_paths = count_paths(current_idx, 0, adapters)

    print("Total number of paths is %d" % total_paths)






