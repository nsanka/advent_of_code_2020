'''
Day 1: Part 1
For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. 
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
'''

#%%
with open('day1_input.txt') as fp:
    data = fp.readlines()

print(len(data))
# %%
lenth = len(data)
for i in range(0, lenth-2):
    for j in range(i+1, lenth-1):
        total = int(data[i]) + int(data[j])
        if total == 2020:
            break
    if total == 2020:
        break

#%%
print(data[i], data[j])
print(int(data[i]) * int(data[j]))

'''
Day 1: Part 2
In your expense report, what is the product of the three entries that sum to 2020?
'''
# %%
for i in range(0, lenth-2):
    for j in range(i+1, lenth-1):
        for k in range(j+1, lenth):
            total = int(data[i]) + int(data[j]) + int(data[k])
            if total == 2020:
                break
        if total == 2020:
            break
    if total == 2020:
        break

#%%
print(data[i], data[j], data[k])
print(int(data[i]) * int(data[j]) * int(data[k]))