import re

f_0 = {
  10: 0.5 * 10**7,
  100: 0.5 * 10**8,
  1000: 0.5 * 10**9
}

def longest_substing(s):
  list_0 = re.findall('0+', s)
  max_0 = max([len(x) for x in list_0])

  list_1 = re.findall('1+', s)
  max_1 = max([len(x) for x in list_1])

  if max_0 > max_1:
    return [max_0, '0']
  else:
    return [max_1, '1']
