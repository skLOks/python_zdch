class DataBase:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port


    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.password}, {self.port}')

    def close(self):
        print('соединение разорвано')

    def read(self):
        print(f'Чтение данных')

    def write(self, data):
        print(f'Запись в БД: {data}')

# db = DataBase('user1', 'psw1', '8000')
# db2 = DataBase('user1', 'psw1', '8000')
# print(db)
# print(db2)
# class Test:
#     pass
#
#     def __bool__(self):
#         return 2>6
#
#
# t = Test()
# if t:
#     print('hello gays')
#
#
class Clock:
    __DAY = 86400

    def __init__(self, seconds : int):
        if not isinstance(seconds, int):
            raise TypeError(f'Нужно ввести целое число, придурок!')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = self.seconds // 60 % 60
        h = self.seconds // 3600 % 24
        return f'{h} : {m} : {s}'

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Нужно ввести целое число')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Type Error')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc



    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(' Не можем сложить')

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(' Не можем сложить')

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __mul__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(' Не можем сложить')

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds * sc)
#
# cl = Clock(86400)
# cl2 = Clock(54)
# cl3 = Clock(155)
# print(cl.get_time())
# cl = cl + cl2 + cl3
# print(cl.get_time())
#
class Passport:
    def __init__(self, first_name, last_name, country, date_of_birth, num_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_of_birth = date_of_birth
        self.num_of_passport = num_of_passport

    def print_info(self):
        print(f'''
Full name: {self.first_name}, {self.last_name}
Date of birth: {self.date_of_birth}
Country: {self.country}
Passport: {self.num_of_passport}''')

    def __repr__(self):
        return f'name {self.first_name} {self.last_name}, Passport {self.num_of_passport}'


class ForeignPassport(Passport):

    def __init__(self, first_name, last_name, country, date_of_birth, num_of_passport, visa):
        super().__init__(first_name, last_name, country, date_of_birth, num_of_passport)
        self.visa = visa

    def print_info(self):
        super().print_info()
        print(f'Visa {self.visa}')
#
#
# MFC = []
# p = Passport('Ivan', 'Ivanov', 'Russia', '14.05.2005', '0719 539804')
# MFC.append(p)
# Fp = ForeignPassport('Petr', 'Petrov', 'Russia', '25.03.1999','4785 485647', 'China')
# MFC.append(Fp)
# print(MFC)
# for item in MFC:
#     item.print_info()
#
#
class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'Не определено'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает'

    def __str__(self):
        return f'{self.name}, {self.series}, {self.make}, {self.year}'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return f'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return f'Копирует и печатает'

# storage = []
# e = Equipment('Noname', 'X', 2001)
# storage.append(e)
# s = Printer('Azaza', 'Lalka', 'chicony',1337)
# storage.append(s)
# x = Xerox('Xexexerox', 'Yabujin', 228)
# storage.append(x)
# for item in storage:
#     print(item)

from random import randint
class Soldier: # класс описывающий одного солдата
    def __init__(self,name='Noname',health = 100): # конструктор
        self.name = name # задаем имя воина
        self.health = health # задаем начальное здоровье
    def set_name(self, name):
        self.name = name # есть возможность поменять имя
    def make_kick(self, enemy): # метод моделирующий атаку на солдата enemy
        enemy.health -= 20 # при атаке здоровье врага уменьшаем на 20
        if enemy.health<0 :
            enemy.health = 0
        self.health += 10 # а собственное здоровье увеличиваем на 10
        print(self.name, "бьет", enemy.name) # выводим кто кого бьет
        print('%s = %d' % (enemy.name, enemy.health)) # выводим состояние враг

class Battle:
    def __init__(self,u1,u2): # конструктор
    # композиция: класс включает двух солдат u1 и u2
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражения не было" # строка для хранения состояния сражения
    def battle(self): # метод моделирующий сражение
        while self.u1.health > 0 and self.u2.health > 0:
            n = randint(1, 2) # определяем, кто атакует
            if n == 1:
                self.u1.make_kick(self.u2) # если атакует первый
            else:
                self.u2.make_kick(self.u1) # если атакует второй
        if self.u1.health > self.u2.health:# определяем, кто победил
            self.result = self.u1.name + " ПОБЕДИЛ"
        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + " ПОБЕДИЛ"
    def who_win(self): # вывод результата
        print(self.result)

# first = Soldier('Mr. First',140) # созаем 1 солдата с именем Mr. First и здоровьем 140
# second = Soldier() # созаем 2 солдата с паметрами по умолчанию 
# second.set_name('Mr. Second') # меняем имя 2 солдата
# b = Battle(first,second) # создаем объект Battle
# b.battle() # запускаем сражение
# b.who_win() # выводим итог

#
import time
import random
class Card(): # класс Карта
    NumsList = ["Джокер",'2','3','4','5','6','7','8','9','10', "Валет","Дама","Король","Туз"]
    MastList = ["пик","крестей","бубей","червей"]
    def __init__(self, i, j):# конструктор
        self.Mastb = self.MastList[i-1]; # карта
        self.Num = self.NumsList[j-1]; # масть

class DeckOfCards(): # класс Колода карт
    def __init__(self): # конструктор
        self.deck = [None] * 56; # список из 56 карт
        k = 0;
        for i in range(1, 4 + 1):
            for j in range(1, 14 + 1):
                self.deck[k] = Card(i, j); # очередная карта
                k += 1;
    def shuffle(self): # перемешивание карт
        random.shuffle(self.deck);
    def get(self, i): # вытаскивание i-й карты из колоды
        if 0 <= i <=55 :
            answer = self.deck[i].Num;
            answer += " ";
            answer += self.deck[i].Mastb;
        else :
            answer = "В колоде только 56 карт"
        return answer;

# deck = DeckOfCards(); # создали колоду
# deck.shuffle(); # перемешали
# print('Выберите карту из колоды в 56 карт:');
# n=int(input())
# if n<=56 :
#     card = deck.get(n-1);
#     print('Вы взяли карту: ', card, end='.\n');
# else :
#     print("В колоде только 56 карт")


#

from numpy import *

class Vector3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, vkt):
        return Vector3D(vkt.x + self.x, vkt.y + self.y, vkt.z + self.z)

    def __sub__(self, vkt):
        return Vector3D(self.x - vkt.x, self.y - vkt.y, self.z - vkt.z)

    def __mul__(self, vkt):
        try:
            return Vector3D(self.x * vkt, self.y * vkt, self.z * vkt)
        except:
            return Vector3D(self.x * vkt.x, self.y * vkt.y, self.z * vkt.z)

    def __matmul__(self, vkt):
        return Vector3D(cross([self.x, self.y, self.z], [vkt.x, vkt.y, vkt.z]))

    def display(self):
        print((self.x, self.y, self.z))

    def read(self):
        self.x, self.y, self.z = map(int, input().split(', '))


# v1 = Vector3D(4, 1, 2)
# v1.display()
# v2 = Vector3D()
# v2.read()
# v3 = Vector3D(1, 2, 3)
# v4 = v1 + v2
# v4.display()
# a = v4 * v3 
# print(a) 
# v4 = v1 * 10 
# v4.display() 
# v4 = v1 @ v3 
# v4.display()


#

# class tr:

#     def __init__(self, )

from math import atan, degrees, hypot
 
 
class ya_ne_znau_kak_nazvat:
    def __init__(self, a, b):
        self.a = a
        self.b =b
 
    def prochent(self, percent, st):
        if -100 <= percent <= 100:
            self.st = percent * self.st / 100
            return True
        print('Ащипка')
        return False
 
    def funkcziya_kotoraya_chtoto_delaet(self):
        return hypot(self.a, self.b) / 2
 
    def per(self):
        return (self.a + self.b + hypot(self.a, self.b))
 
    def ugls(self):
        a = degrees(atan(self.a / self.b))
        b = 90 - a
        return a, b, 90

# Dalshe len