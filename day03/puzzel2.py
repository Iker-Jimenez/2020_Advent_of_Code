map_file = open("map.txt", "r")

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
multiplied_trees = 1

for slope in slopes:
    num_trees = 0
    print("Processing slope %s" % str(slope))
    position = slope[0]  # Initialise it to the position of first row to be checked
    map_file.seek(0)
    for line_num, row in enumerate(map_file):
        if line_num == 0:
            length_row = len(row)
            # print("Length of row is %d" % length_row)
        else:
            if line_num % slope[1] == 0:
                # print("Processing line %d" % line_num)
                if row[position] == '#':
                    num_trees += 1
                position = (position + slope[0]) % (length_row - 1)
    print("For slope %s you would encounter %d trees" % (str(slope), num_trees))
    multiplied_trees *= num_trees

print("Multiplied trees is %d" % multiplied_trees)
