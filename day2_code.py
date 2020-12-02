'''
Day 2: Part 1
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given letter must appear 
for the password to be valid. For example, 1-3 a means that the password must contain 
a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; 
it contains no instances of b, but needs at least 1. The first and third passwords are valid: 
they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''
#%%
with open('day2_input.txt') as fp:
    data = fp.readlines()

#%%
import re
cnt = 0
regex = re.compile(r'''
(?P<l_min>\d+)-
(?P<l_max>\d+)[^\S]
(?P<let>\S*):[^\S]
(?P<pass>\S*)
''', re.VERBOSE)

#%%
m = regex.match('3-11 z: zzzzzdzzzzlzz')
if m:
    print(m.group('l_min'))
    print(m.group('l_max'))
    print(m.group('let'))
    print(m.group('pass'))

#%%
valid_cnt = 0
for i in range(len(data)):
    password = data[i].strip()
    m = regex.match(password)
    if m:
        print(i, data[i].strip(), m.group('l_min'), m.group('l_max'), m.group('let'), m.group('pass'))
        l_min = int(m.group('l_min'))
        l_max = int(m.group('l_max'))
        let = m.group('let')
        passwd = m.group('pass')

        cnt = passwd.count(let)
        print(cnt)
        if (cnt >= l_min) and (cnt <= l_max):
            valid_cnt += 1

# %%
print(valid_cnt)

'''
Day 2: Part 2
Each policy actually describes two positions in the password, where 1 means the first character, 
2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
'''

# %%
valid_cnt = 0
for i in range(len(data)):
    password = data[i].strip()
    m = regex.match(password)
    if m:
        print(i, data[i].strip(), m.group('l_min'), m.group('l_max'), m.group('let'), m.group('pass'))
        l_min = int(m.group('l_min')) - 1
        l_max = int(m.group('l_max')) - 1
        let = m.group('let')
        passwd = m.group('pass')

        if ((passwd[l_min] == let) and (passwd[l_max] != let)) or ((passwd[l_min] != let) and (passwd[l_max] == let)):
            print('valid', let, passwd[l_min], passwd[l_max])
            valid_cnt += 1
        else:
            print('not valid', let, passwd[l_min], passwd[l_max])

# %%
print(valid_cnt)
# %%
