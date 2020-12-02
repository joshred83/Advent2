import re
from collections import Counter

def validate_password_by_count(rule, pw):
  floor, ceiling, letter = tuple(rule)
  floor, ceiling = int(floor), int(ceiling)
  counts = Counter(pw)

  if floor <= counts[letter] <= ceiling:
    return True
  else:
    return False

def validate_password_by_position(rule, pw):
  position1, position2, letter = tuple(rule)
  position1, position2 = int(position1)-1, int(position2)-1

  if sum ((pw[position1] == letter, pw[position2] == letter)) ==1:
    print(f'True {position1} {position2} {letter} {password}')
    return True
  else:
    print(f'False {position1} {position2} {letter} {password}')
    return False

with open("passwords_d2") as f:
  entries = [l.strip().split(":") for l in f.readlines()]

policies = [re.split("[-\s]+",e[0]) for e in entries]
passwords = [e[1] for e in entries]

n_valid = 0 
for policy, password in zip(policies, passwords):
  n_valid += validate_password_by_count(policy, password)
print(n_valid)
n_valid = 0 
for policy, password in zip(policies, passwords):
  n_valid += validate_password_by_position(policy, password)
print(n_valid)

