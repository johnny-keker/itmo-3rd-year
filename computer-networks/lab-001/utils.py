import re

f_0 = {
  10: 0.5 * 10**7,
  100: 0.5 * 10**8,
  1000: 0.5 * 10**9
}

table_4b5b = {
  '0000' : '11110',
  '0001' : '01001',
  '0010' : '10100',
  '0011' : '10101',
  '0100' : '01010',
  '0101' : '01011',
  '0110' : '01110',
  '0111' : '01111',
  '1000' : '10010',
  '1001' : '10011',
  '1010' : '10110',
  '1011' : '10111',
  '1100' : '11010',
  '1101' : '11011',
  '1110' : '11100',
  '1111' : '11101'
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


def get_occurrence_counts(s, token_groups = None):
  tokens_provided = token_groups != None
  subs = []
  if not tokens_provided:
    subs += re.findall('0+', s)
    subs += re.findall('1+', s)
  else:
    for token_group in token_groups:
      subs += re.findall(token_group[1], s)
      subs += re.findall(token_group[0], s)

  res = {}
  for token in subs:
    key = token if tokens_provided else len(token)
    if res.get(key):
      res[key] += len(token)
    else:
      res[key] = len(token)
  if tokens_provided:
    for token_group in token_groups:
      if res.get(token_group[0]) and res.get(token_group[1]):
        res[f"{token_group[0]} и {token_group[1]}"] = res[token_group[0]] + res[token_group[1]]
        del res[token_group[0]]
        del res[token_group[1]]
  return res

def f_mean_man_nz(s):
  prev = '-'
  s = s + s[0]
  c1 = 0
  c2 = 0
  for c in s:
    if (c == prev):
        c1 = c1 + 1
    elif (prev != '-'):
        c2 = c2 + 1
    prev = c
  res = {}
  res['11 и 00'] = c1
  res['1 и 0'] = c2
  return res

def build_occurrence_table(occurrence, certain_tokens = False, f_0_mult = None):
  print('\\begin{tabular}{| c | c | c | c |}')
  print('\hline')
  print(' Частота & Участки & Кол-во битовых интервалов & Отношение к $f_0$ \\\\')
  print('\hline')
  cur_index = 1

  for key in occurrence:
    row = f"$f_{{{cur_index}}}$ & "
    row += key if certain_tokens else "1"*key + " и " + "0"*key
    row += f" & {occurrence[key]} & "
    row += f"$f_0 "
    row += f"* {str(f_0_mult[cur_index-1])}" if certain_tokens else f"/ {str(key)}"
    row += "$ \\\\"
    print(row)
    cur_index += 1
  print('\hline')
  print('\\end{tabular}')

def get_f_mean_math(occurrence, mes_len):
  f_mean_str = "$$f_{mean} = "
  cur_index = 1
  for key in occurrence:
    f_mean_str += f"{occurrence[key]} / {mes_len} * f_{cur_index} + "
    cur_index += 1
  f_mean_str = f_mean_str[:-3] + "$$"
  return f_mean_str

def get_f_mean(occurrence, mes_len, f_0, certain_tokens = False, f_0_mult = None):
  res = 0
  i = 0
  for key in occurrence:
    l = 1 / f_0_mult[i] if certain_tokens else key
    res += occurrence[key] / mes_len * f_0 / l
    i += 1
  return int(res)

def get_f_mean_table(occurrence, mes_len, certain_tokens = False, f_0_mult = None):
  print('\\begin{center}')
  print('\\begin{tabular}{| c | c |}')
  print('\hline')
  print('Пропускная способность, Mbps & $f_{mean}$, Гц \\\\')
  print('\hline')
  print(f'10 & {get_f_mean(occurrence, mes_len, f_0[10], certain_tokens, f_0_mult)} \\\\')
  print(f'100 & {get_f_mean(occurrence, mes_len, f_0[100], certain_tokens, f_0_mult)} \\\\')
  print(f'1000 & {get_f_mean(occurrence, mes_len, f_0[1000], certain_tokens, f_0_mult)} \\\\')
  print('\hline')
  print('\\end{tabular}')
  print('\\end{center}')

def convert_4b5b(s):
  i = 0
  res = ""
  while i != len(s):
    res += table_4b5b[s[i:i+4]]
    i += 4
  return res

def build_4b5b_table():
  print('\\begin{tabular}{| c | c | c | c |}')
  print('\hline')
  keys = list(table_4b5b.keys())
  for i in range(len(table_4b5b.keys()) // 2):
    print(f'{keys[i]} & {table_4b5b[keys[i]]} & {keys[i+8]} & {table_4b5b[keys[i+8]]} \\\\')
    print('\hline')
  print('\\end{tabular}')

