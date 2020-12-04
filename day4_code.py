'''
Day 4: Part 1
The expected fields are as follows:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Here is an example batch file containing four passports:
======================
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
======================
Count the number of valid passports - those that have all required fields. Treat cid as optional. 
In your batch file, how many passports are valid?
'''

#%%
expected_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

#%%
with open('day4_input.txt') as fp:
   data = fp.readlines()
   passport = ''
   all_passports = []
   for line in data:
      line = line.strip()
      if line == '':
         passport = passport.rstrip()
         p_dict = dict((x, y) for x, y in (element.split(':') for element in passport.split()))
         all_passports.append(p_dict)
         passport = ''
      else:
         passport += ' ' + line
   print(len(all_passports))

#%%
valid_cnt = 0
for passport in all_passports:
   #print(set(passport.keys()))
   if(expected_fields.issubset(set(passport.keys()))):
      valid_cnt += 1
print(valid_cnt)

#%%
'''
Part 2
You can continue to ignore the cid field, but each other field has strict rules 
about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and 
valid according to the above rules.
'''

#%%
import re
valid_cnt = 0
for passport in all_passports:
   #print(set(passport.keys()))
   if(expected_fields.issubset(set(passport.keys()))):
      if not ((len(passport['byr']) == 4) and (int(passport['byr']) >= 1920) and (int(passport['byr']) <= 2002)):
         continue
      if not ((len(passport['iyr']) == 4) and (int(passport['iyr']) >= 2010) and (int(passport['iyr']) <= 2020)):
         continue
      if not ((len(passport['eyr']) == 4) and (int(passport['eyr']) >= 2020) and (int(passport['eyr']) <= 2030)):
         continue
      if ('cm' not in passport['hgt']) and ('in' not in passport['hgt']):
         continue
      else:
         hgt = int(re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", passport['hgt'])[0])
         if ('cm' in passport['hgt']):
            if not (hgt >= 150 and hgt <= 193):
               continue
         if ('in' in passport['hgt']):
            if not (hgt >= 59 and hgt <= 76):
               continue
      if len(re.findall('^#[a-f0-9]{6}$', passport['hcl'])) == 0:
         continue
      if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
         continue
      if len(re.findall('^\d{9}$', passport['pid'])) == 0:
         continue
      print(passport)
      valid_cnt += 1
print(valid_cnt)