'''
Day 5: Part 1
For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). 
The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
'''
#%%
# Simple Code in two lines
seats = [int(s,2) for s in open('day5_input.txt','r').read().replace("F","0").replace("B","1").replace("L","0").replace("R","1").split()]
(max(seats),set(range(min(seats),max(seats))).difference(seats).pop())

#%%
with open('day5_input.txt') as fp:
   data = fp.readlines()

#%%
seats = []
for line in data:
   line = line.strip()
   print(line)
   row = 0
   col = 0
   rmin = 0
   rmax = 127
   for i in range(7):
      let = line[i]
      if let == 'F':
         rmax = ((rmax + rmin + 1) / 2) - 1
         row = rmax
      if let == 'B':
         rmin = (rmax + rmin + 1) / 2
         row = rmin
      #print(let, rmin, rmax, row)
   cmin = 0
   cmax = 7
   for i in [7, 8, 9]:
      let = line[i]
      if let == 'R':
         cmin = (cmax + cmin + 1) / 2
         col = cmin
      if let == 'L':
         cmax = ((cmax + cmin + 1) / 2) - 1
         col = cmax
      #print(let, cmin, cmax, col)
   
   seat_id = row * 8 + col
   print(row, col, seat_id)
   seats.append(seat_id)

print(max(seats))

'''
Part 2
It's a completely full flight, so your seat should be the only missing boarding pass in your list. 
However, there's a catch: some of the seats at the very front and back of the plane don't exist on 
this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''
# %%
seats.sort()
print(seats)
# %%
for i in range(len(seats)):
   if seats[i + 1] != seats[i] + 1:
      print("My Seat ID: ", seats[i] + 1)
      break
