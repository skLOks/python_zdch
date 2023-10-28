# pytest

# 1

def otr(a):
  try:
    a = float(a)
    if a < 0:
      return "Отрицательное"
    if a > 0:
      return "Положительное"
    else:
      return "Ноль"
  except:
    return "Это не число"

# 2

def chyot(a):
  try:
    assert a % 2 == 0
    return "Чётное"
  except:
    try:
      a /= 1
      return "Не чётное"
    except:
      return "Это не число"

# 3

def kol(a):
  try:
    a / 1
    return len(str(a))
  except:
    return "Это не число"

# 4

def sumlist(l):
  f = 0
  try:
    for i in l:
      f += i
    return f
  except:
    return "Введите нормальный список"

# 5

def sumstr(s):
  f = 0
  try:
    a = [int(x) for x in s.split(',')]
    for i in a:
      f += i
    return f
  except:
    return "Что то не то, переделывай"

# unittest 

# 1

def sortmas(a):
  try:
    int(a[0]) // 2 
    res = tuple(' '.join(reversed(a.split("-"))).split())
    return res
  except:
    return "Ошибка, корявый ввод"

# 2

def sumlis(l):
  f = 0
  try:
    for i in l:
      f += int(i)
    return f
  except:
    return "Введите нормальный список"

# 3

def sumsum(l):
  f = 0
  e = 0
  try:
    for i in range(0, (len(l)//2)):
      f += int(l[i])
    for i in range((len(l)//2), len(l)):
      e += int(l[i])
    print(f, e)
    return f / e
  except:
    return "Введите нормальный список"

# 4

def obsv(sl1, sl2):
  try:
    return sl1 | sl2
  except:
    return "Введите нормальный список"

# 5

def sumvalsl(sl):
  try:
    d = sl.items()
    t = 0
    for key, value in d:
      t += sum(sl[key].values())
    return t
  except:
    return "Введите нормальный словарь"

# тоже 5, только другое

def get_min_max(l):
  try:
    sl = {
      'max': 0,
      'min': 0
    }
    max = l[0]
    min = l[0]
    for i in l:
        if i > max:
            max = i
        if i < min:
            min = i
    sl['max'] = int(max)
    sl['min'] = int(min)
    return sl
  except:
    return "Введите нормальный список"

# 6
def zamsp(l):
  try:
    for i in range(0, len(l)):
      znac = l[i]
      l[i] = []
      for g in range(1, i+2):
        if znac % g == 0:
          l[i].append(g)
    return l
  except:
    return "Введите нормальный список"

# 7
import random

def randsp(s1, s2):
  a = []
  b = random.randint(0, 10)
  c = 0
  a.append(random.randint(s1, s2))
  while c < b:
    k = random.randint(s1, s2)
    if a[c] != k:
      a.append(k)
      c += 1
  return a

# 8

colors = ["Жёлтый", "Зелёный", "Синий", "Чёрный", "Цвет детской неожиданности", "Цвет плесени"]

def color(l):
  return l[random.randint(0, len(l) - 1)]

# 9 

import rusyllab # там запарно с установкой этого модуля, по этому могу скриншоты прикрепить, если надо)
# но если вам не лень, то можете запариться

def raspil(text):
  try:
    a = rusyllab.split_words(text.split())
    return a
  except:
    return "Что то не то, переделывай"

# 10

def peremeshka(l):
  random.shuffle(l)
  return l

# Ура я сделал