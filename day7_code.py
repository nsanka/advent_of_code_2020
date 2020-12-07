'''
Day 7: Part 1
For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, 
every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, 
how many different bag colors would be valid for the outermost bag? 
(In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag?
'''
#%%
with open('day7_input.txt') as fp:
   data = fp.readlines()

#%%
import re
final_bags = {}
for line in data:
   line = line.strip()
   bag = line.split('s contain ')[0]
   match = re.findall(r'((\d)([\s\w]+bag))(?:,|.)', line)
   if bag not in final_bags.keys():
      final_bags[bag] = {}
      for item in match:
         final_bags[bag][item[2].lstrip()] = int(item[1])
#print(final_bags)

#%%
other_bags = ['shiny gold bag']
new_bags = []
while len(other_bags) > 0:
   #print(other_bags)
   bag = other_bags.pop()
   if bag not in new_bags:
      new_bags.append(bag)
   for key in final_bags.keys():
      if bag in final_bags[key].keys():
         if (key not in other_bags) and (key not in new_bags):
            other_bags.append(key)
print(new_bags)
print(len(new_bags)-1)

# %%
'''
Part 2
Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) 
plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

How many individual bags are required inside your single shiny gold bag?
'''

#%%
def get_number_of_bags(bag, num, total):
   #print(bag, num, total[-1])
   #print(final_bags[bag])
   if len(final_bags[bag].keys()) == 0:
      return total[-1]

   total.append(total[-1] + num * sum(final_bags[bag].values()))
   for new_bag in final_bags[bag].keys():
      get_number_of_bags(new_bag, num * final_bags[bag][new_bag], total)

total = [0]
get_number_of_bags('shiny gold bag', 1, total)
print(total)