
def calculate_row(rowcode):
    return rec_calc_row(rowcode, list(range(0, 128)))


def rec_calc_row(rowcode, rows):
    len_rows = len(rows)
    if len_rows > 2:
        if rowcode[0] == "F":
            return rec_calc_row(rowcode[1:], rows[0:int(len_rows/2)])
        else:
            return rec_calc_row(rowcode[1:], rows[int(len_rows/2):])
    else:
        if rowcode == "F":
            return rows[0]
        else:
            return rows[1]


def calculate_col(colcode):
    return rec_calc_col(colcode, list(range(0, 8)))


def rec_calc_col(colcode, cols):
    len_cols = len(cols)
    if len_cols > 2:
        if colcode[0] == "L":
            return rec_calc_col(colcode[1:], cols[0:int(len_cols/2)])
        else:
            return rec_calc_col(colcode[1:], cols[int(len_cols/2):])
    else:
        if colcode == "L":
            return cols[0]
        else:
            return cols[1]


seats = []

# O(N)
with open('seats.txt', 'r') as seat_file:
    for seat in seat_file:
        row = calculate_row(seat[:7])
        print("Row is %d" % row)
        col = calculate_col(seat[7:].strip())
        print("Col is %d" % col)

        seat_id = (row * 8) + col
        print("Seat id is %s" % seat_id)
        seats.append(seat_id)

seats.sort()
for seat_num, seat_id in enumerate(seats):
    print("Processing seat %d, with id %d" % (seat_num, seat_id))
    if seat_num > 0 and seat_id - 1 != seats[seat_num - 1]:
        print("My seat is %d" % (seats[seat_num - 1] + 1))
        break
