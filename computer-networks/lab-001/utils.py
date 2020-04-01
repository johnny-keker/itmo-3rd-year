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

def get_occurrence_counts(s, tokens = None):
  tokens_provided = tokens != None
  subs = []
  if not tokens_provided:
    subs += re.findall('0+', s)
    subs += re.findall('1+', s)
  else:
    for token in tokens:
      subs += re.findall(token, s)

  res = {}
  for token in subs:
    key = token if tokens_provided else len(token)
    if res.get(key):
      res[key] += len(token)
    else:
      res[key] = len(token)
  return res

def build_occurrence_table(occurrence, certain_tokens = False):
  print('\\begin{tabular}{| c | c | c | c |}')
  print('\hline')
  print(' Частота & Участки & Кол-во битовых интервалов & Отношение к $f_0$ \\\\')
  print('\hline')
  cur_index = 1

  for key in occurrence:
    row = f"$f_{{{cur_index}}}$ & "
    row += key if certain_tokens else "1"*key + " и " + "0"*key
    row += f" & {occurrence[key]} & "
    row += f"$f_0 / "
    row += str(len(key)) if certain_tokens else str(key)
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

def get_f_mean(occurrence, mes_len, f_0, certain_tokens = False):
  res = 0
  for key in occurrence:
    l = len(key) if certain_tokens else key
    res += occurrence[key] / mes_len * f_0 / l
  return int(res)

def get_f_mean_table(occurrence, mes_len, certain_tokens = False):
  print('\\begin{center}')
  print('\\begin{tabular}{| c | c |}')
  print('\hline')
  print('Пропускная способность, Mbps & $f_{mean}$, Гц \\\\')
  print('\hline')
  print(f'10 & {get_f_mean(occurrence, mes_len, f_0[10], certain_tokens)} \\\\')
  print(f'100 & {get_f_mean(occurrence, mes_len, f_0[100], certain_tokens)} \\\\')
  print(f'1000 & {get_f_mean(occurrence, mes_len, f_0[1000], certain_tokens)} \\\\')
  print('\hline')
  print('\\end{tabular}')
  print('\\end{center}')



