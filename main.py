import re
from collections import Counter

def pw_count_validator(rule, pw):
  floor, ceiling, letter = tuple(rule)
  floor, ceiling = int(floor), int(ceiling)
  counts = Counter(pw)

  if floor <= counts[letter] <= ceiling:
    return True
  else:
    return False

def pw_positional_validator(rule, pw):
  idx1, idx2, letter = tuple(rule)
  idx1, idx2 = int(idx1)-1, int(idx2)-1

  if sum ((pw[idx1] == letter, pw[idx2] == letter)) == 1:
    print(f'True {idx1} {idx2} {letter} |{pw}|')
    return True
  else:
    #print(f'False {idx1} {idx2} {letter} |{pw}|')
    return False

def count_valid(policies, passwords, validator):
  n_valid = 0 
  for policy, pw in zip(policies, passwords):
    n_valid += validator(policy, pw)
  return n_valid

with open("passwords_d2") as f:
  entries = [l.strip().split(":") for l in f.readlines()]

policies = [re.split("[-\s]+",e[0]) for e in entries]
passwords = [e[1].strip() for e in entries]

print(count_valid(policies, passwords, pw_count_validator))
print(count_valid(policies, passwords, pw_positional_validator))

