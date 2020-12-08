map_file = open("map.txt", "r")

num_trees = 0

length_row = len(map_file.readline())
print("Length of row is %d" % length_row)
position = 3  # Initialise it to the position of first row to be checked, row #2

for row in map_file:
    if row[position] == '#':
        num_trees += 1
    position = (position + 3) % (length_row - 1)

print("You would encounter %d trees" % num_trees)
