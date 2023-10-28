import unittest
from main import *


#////////////////////////////////////////////////
class Test_sortmas(unittest.TestCase):
 def test1(self):
  self.assertEqual(sortmas('2025-12-1'), ('1', '12', '2025'))

 def test2(self):
  self.assertEqual(sortmas('2023-10-28'), ('28', '10', '2023'))

 def test3(self):
  self.assertEqual(sortmas('adad'), "Ошибка, корявый ввод")

 def test4(self):
  self.assertEqual(sortmas('2025-12-2'), ('2', '12', '2025'))

 def test5(self):
  self.assertEqual(sortmas('20-1-5'), ('5', '1', '20'))


#////////////////////////////////////////////////
class Test_sumlis(unittest.TestCase):
 def test1(self):
  self.assertEqual(sumlis(['1', '2', '3', '4', '5']), 15)

 def test2(self):
  self.assertEqual(sumlis(['5', '10']), 15)

 def test3(self):
  self.assertEqual(sumlis([5, 2, 3, 1, 4]), 15)

 def test4(self):
  self.assertEqual(sumlis('das'), "Введите нормальный список")

 def test5(self):
  self.assertEqual(sumlis(['15', 10, 5]), 30)


#////////////////////////////////////////////////
class Test_sumsum(unittest.TestCase):
 def test1(self):
  self.assertEqual(sumsum([1, 2, 3, 4, 5, 6]), 0.4)

 def test2(self):
  self.assertEqual(sumsum([5, 5, 2, 1, 2, 3]), 2)

 def test3(self):
  self.assertEqual(sumsum([6, 2]), 3)

 def test4(self):
  self.assertEqual(sumsum('das'), "Введите нормальный список")

 def test5(self):
  self.assertEqual(sumsum([15, 5, 5]), 1.5)


#////////////////////////////////////////////////
class Test_obsv(unittest.TestCase):
 def test1(self):
  self.assertEqual(obsv({'a': 1,'b': 2,}, {'c': 3, 'd': 4,}), {'a': 1,'b': 2,'c': 3, 'd': 4,})

 def test2(self):
  self.assertEqual(obsv({'a': 15,'b': '1231',}, {'y': 1, 'd': [22, 22, 22],}), {'a': 15,'b': '1231', 'y': 1, 'd': [22, 22, 22],})

 def test3(self):
  self.assertEqual(obsv({'Afanasiy': 157,'Boris': '1389',}, {'Yuriy': 19, 'Deariya': 13,}), {'Afanasiy': 157,'Boris': '1389', 'Yuriy': 19, 'Deariya': 13,})

 def test4(self):
  self.assertEqual(obsv('das', 2), "Введите нормальный список")

 def test5(self):
  self.assertEqual(obsv(123.23, 6), "Введите нормальный список")


#////////////////////////////////////////////////
class Test_sumvalsl(unittest.TestCase):
 def test1(self):
  self.assertEqual(sumvalsl({1: {1: 11, 2: 12, 3: 13,}, 2: {1: 21, 2: 22, 3: 23,},3: {1: 24, 2: 25, 3: 26,},}), 177)

 def test2(self):
  self.assertEqual(sumvalsl({1: {1: 15, 2: 12, 3: 13,}, 2: {1: 21, 2: 22, 3: 23,},3: {1: 24, 2: 25, 3: 26,},}), 181)

 def test3(self):
  self.assertEqual(sumvalsl({1: {1: 15, 2: 20, 3: 13,}, 2: {1: 21, 2: 22, 3: 24,},3: {1: 24, 2: 25, 3: 26,},}), 190)

 def test4(self):
  self.assertEqual(sumvalsl('das'), "Введите нормальный словарь")

 def test5(self):
  self.assertEqual(sumvalsl(123.23), "Введите нормальный словарь")


#////////////////////////////////////////////////
class Test_get_min_max(unittest.TestCase):
 def test1(self):
  self.assertEqual(get_min_max([1, 2, 3, 4, 5, 6]), {'max': 6, 'min': 1,})

 def test2(self):
  self.assertEqual(get_min_max([1, 0, 2, 3, 4, 99, 6]), {'max': 99, 'min': 0,})

 def test3(self):
  self.assertEqual(get_min_max([1, 1, 1, 1, 1]), {'max': 1, 'min': 1,})

 def test4(self):
  self.assertEqual(get_min_max('das'), "Введите нормальный список")

 def test5(self):
  self.assertEqual(get_min_max(123.23), "Введите нормальный список")


#////////////////////////////////////////////////
class Test_zamsp(unittest.TestCase):
 def test1(self):
  self.assertEqual(zamsp([1, 2, 3, 4, 5, 6]), [[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6]])

 def test2(self):
  self.assertEqual(zamsp([1, 2, 3, 4, 99, 6]), [[1], [1, 2], [1, 3], [1, 2, 4], [1, 3], [1, 2, 3, 6]])

 def test3(self):
  self.assertEqual(zamsp([1, 1, 1, 1, 1]), [[1], [1], [1], [1], [1]] )

 def test4(self):
  self.assertEqual(zamsp('das'), "Введите нормальный список")

 def test5(self):
  self.assertEqual(zamsp(123.23), "Введите нормальный список")


#////////////////////////////////////////////////
class Test_raspil(unittest.TestCase):
 def test1(self):
  self.assertEqual(raspil("Привет мир"), ['При', 'вет', ' ', 'мир'] )

 def test2(self):
  self.assertEqual(raspil("УРААА Я В ТЕЛЕФИЗОРЕ"), ['У', 'РА', 'А', 'А', ' ', 'Я', ' ', 'В', ' ', 'ТЕ', 'ЛЕ', 'ФИ', 'ЗО', 'РЕ'])

 def test3(self):
  self.assertEqual(raspil("ДАДАДАДАДАДАДАД"), ['ДА', 'ДА', 'ДА', 'ДА', 'ДА', 'ДА', 'ДАД'])

 def test4(self):
  self.assertEqual(raspil('Меня зовут Игорь'), ['Ме', 'ня', ' ', 'зо', 'вут', ' ', 'И', 'горь'])

 def test5(self):
  self.assertEqual(raspil(123.23), "Что то не то, переделывай")

# Мне лень тестировать рандомы, потому чт оразбираться надо, так что без этого

if __name__ == "__main__":
 unittest.main()