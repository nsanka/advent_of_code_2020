'''
Day 3: Part 1
From your starting position at the top-left, check the position that is right 3 and down 1. 
Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
'''
#%%
with open('day3_input.txt') as fp:
    data = fp.readlines()

#%%
def count_trees(right, down):
    tree_cnt = 0
    cur_right = 0
    cur_down = 0
    for line in data:
        line = line.strip()
        length = len(line)
        if cur_down == down:
            cur_right += right
            if cur_right >= length:
                cur_right -= length
            ch = line[cur_right]
            #print('char', ch)
            if ch == '#':
                tree_cnt += 1
            cur_down = 0
        cur_down += 1
        #print(line[:cur_right+1])
    #print(tree_cnt)
    return tree_cnt

# %%
count_trees(3, 1)
# %%
t1 = count_trees(1, 1)
t2 = count_trees(3, 1)
t3 = count_trees(5, 1)
t4 = count_trees(7, 1)
t5 = count_trees(1, 2)
print(t1, t2, t3, t4, t5)
print(t1 * t2 * t3 * t4 * t5)
# %%
