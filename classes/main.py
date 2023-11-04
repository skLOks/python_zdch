# 1

import random

class MusicAlbum:
	def __init__(self, title, artist, release_year, genre, tracklist):
		self.title = title
		self.artist = artist
		self.release_year = release_year
		self.genre = genre
		self.tracklist = tracklist
	def play_random_track(self):
		try:
			a = random.randint(0, len(self.tracklist) - 1)
			print(f"Воспроизводится трек {a+1}: {self.tracklist[a]}")
		except:
			print("Ошибка ввода")

# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte", 
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex", 
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo", 
#                      "Hallomann"])
# print("Название:", album4.title)
# print("Исполнитель:", album4.artist)
# print("Год:", album4.release_year)
# print("Жанр:", album4.genre)
# print("Треки:", album4.tracklist)
# album4.play_random_track()


# 2

class Student:
	def __init__(self, name, age, grade, scores):
		self.name = name
		self.age = age
		self.grade = grade
		self.scores = scores

	def average_score(self):
		try:
			g = 0
			for i in self.scores:
				g += i
			return g / len(self.scores)
		except:
			print("Ошибка ввода")
		
# student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
# print("Имя:", student2.name)
# print("Возраст:", student2.age)
# print("Класс:", student2.grade)
# print("Оценки:", *student2.scores)
# print("Средний балл:", student2.average_score())

# 3

import time

class Recipe:
	def __init__(self, namepr, spisok):
		self.namepr = namepr
		self.spisok = spisok

	def print_ingredients(self):
		try:
			time.sleep(1)
			print(f"Ингредиенты для {self.namepr}:")
			for i in self.spisok:
				time.sleep(1)
				print(f"-{i}")
		except:
			print("Ошибка ввода")

	def cook(self):
		try:
			time.sleep(2)
			print(f"Сегодня мы готовим {self.namepr}.")
			time.sleep(2)
			print(f"Выполняем инструкцию по приготовлению блюда {self.namepr}...")
			time.sleep(3)
			print(f"Блюдо {self.namepr} готово!")
			time.sleep(3)
		except:
			print("Ошибка ввода")

# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

# # печатаем список продуктов для рецепта спагетти
# spaghetti.print_ingredients()

# # готовим спагетти
# spaghetti.cook()  

# # создаем рецепт для кекса
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

# # печатаем рецепт кекса
# cake.print_ingredients()

# # готовим кекс 
# cake.cook()

# 4

class Publisher:
	def __init__(self, name, location):
		self.name = name
		self.location = location
	def get_info(self):
		print(self.name, "\n" + self.location)
	def publish(self, message):
		print(f'Готовим "{message}" к публикации в {self.name} ({self.location})')

class BookPublisher(Publisher):
	def __init__(self, name, location, num_authors):
		super().__init__(name, location)
		self.num_authors = num_authors
	def publish(self, message, author):
		print(f'Передаем рукопись "{message}", написанную автором {author} в издательство {self.name} ({self.location})')

class NewspaperPublisher(Publisher):
	def __init__(self, name, location, num_pages):
		super().__init__(name, location)
		self.num_pages = num_pages
	def publish(self, message):
		print(f'Печатаем свежий номер со статьей "{message}" на главной странице в издательстве {self.name} ({self.location})')

# publisher = Publisher("АБВГД Пресс", "Москва")
# publisher.publish("Справочник писателя")

# book_publisher = BookPublisher("Важные Книги", "Самара", 52)
# book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

# newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
# newspaper_publisher.publish("Новая версия Midjourney будет платной")

# 5

class BankAccount:
	def __init__(self, balance, interest_rate, transations = []):
		self.balance = balance
		self.interest_rate = interest_rate
		transations = []
		self.transations = transations

	def deposit(self, amount):
		self.balance += amount
		self.transations.append(f"Внесение наличных на счет: {amount}")
	
	def withdraw(self, amount):
		self.balance -= amount
		self.transations.append(f"Снятие наличных: {amount}")
	
	def add_interest(self):
		b = self.balance
		self.balance += (self.balance * self.interest_rate)
		self.transations.append(f"Начислены проценты по вкладу: {(b* self.interest_rate)}")

	def history(self):
		for i in self.transations:
			print(i)

# # создаем объект счета с балансом 100000 и процентом по вкладу 0.05
# account = BankAccount(100000, 0.05)

# # вносим 15 тысяч на счет
# account.deposit(15000)

# # снимаем 7500 рублей
# account.withdraw(7500)

# # начисляем проценты по вкладу
# account.add_interest()

# # печатаем историю операций
# account.history()

# 6

class Employee:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary
		self.bonus = 0

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_salary(self):
		return self.salary

	def set_bonus(self, bonus):
		self.bonus = bonus

	def get_bonus(self):
		return self.bonus

	def get_total_salary(self):
		return self.bonus + self.salary

# employee = Employee("Марина Арефьева", 30, 90000)

# # устанавливаем бонус для сотрудника
# employee.set_bonus(15000)

# # выводим имя, возраст, зарплату, бонус и общую зарплату сотрудника
# print("Имя:", employee.get_name())
# print("Возраст:", employee.get_age())
# print("Зарплата:", employee.get_salary())
# print("Бонус:", employee.get_bonus())
# print("Итого начислено:", employee.get_total_salary())


# 7

class Animal:
	def __init__(self, name, species, legs):
		self.name = name
		self.species = species
		self.legs = legs

	def voice(self):
		print(f"{self.name} подаёт голос")

	def move(self):
		print(f"{self.name} дёргает хвостом")

class Dog(Animal):
	def __init__(self, name, breed, legs, species="Собака"):
		super().__init__(name, legs, species)
		self.breed = breed

	def bark(self):
		print(f"{self.breed} {self.name} лает")

class Bird(Animal):
	def __init__(self, name, legs, species="Птица", wingspan=0):
		super().__init__(name, legs, species)
		self.wingspan = wingspan
	def fly(self):
		print(f"{self.species} {self.name} летает")

# dog = Dog("Геральт", "доберман", 4)
# bird = Bird("Вася", "попугай", 2)
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()

# 8

class Shape:
	def __init__(self, color, name="геометрическая фигура"):
		self.name = name
		self.color = color

	def describe(self):
		print(f"Это геометрическая фигура, цвет - {self.color}.")

class Circle(Shape):
	def __init__(self,color, radius, name="окружность"):
		super().__init__(color)
		self.name = name
		self.radius = radius
	def describe(self):
		super().describe()
		print(f"Это {self.name}. Радиус - {self.radius} см, цвет - {self.color}.")
	def area(self):
		return 3.14 * self.radius**2

class Rectangle(Shape):
	def __init__(self, color, length, width, name="прямоугольник"):
		super().__init__(color)
		self.name = name
		self.length = length
		self.width = width

	def describe(self):
		super().describe()
		print(f"Это {self.color} {self.name}. Длина - {self.length} см, ширина - {self.width} см.")
	
	def area(self):
		return self.length * self.width

class Triangle(Shape):
	def __init__(self, color, base, height, name="треугольник"):
		super().__init__(color)
		self.name = name
		self.base = base
		self.height = height

	def describe(self):
		super().describe()
		print(f"Это {self.color} {self.name} с основанием {self.base} см и высотой {self.height} см.")
	
	def area(self):
		return (self.height * self.base) / 2

# circle = Circle("красный", 5)
# rectangle = Rectangle("синий", 3, 4)
# triangle = Triangle("фиолетовый", 6, 8)
# circle.describe()
# rectangle.describe() 
# triangle.describe()
# print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")

# Дальше лень