# 1

class Student:
	def __init__(self, name, age, score, training_course, phonen):
		self.name = name
		self.age = age
		self.score = score
		self.training_course = training_course
		self.phonen = phonen

	def getfull(self):
		print(f"Имя: {self.name}\nВозраст: {self.age}\nСредний балл: {self.score}\nУчебный курс: {self.training_course}\nНомер телефона: {self.phonen}\n")

	def get_name(self):
		print(f"Имя: {self.name}")

	def get_age(self):
		print(f"Возраст: {self.age}")

	def get_score(self):
		print(f"Средний балл: {self.score}")

	def get_tc(self):
		print(f"Учебный курс: {self.training_course}")

	def get_phone(self):
		print(f"Номер телефона: {self.phonen}")

	def setz(self, name, age, score, training_course, phonen):
		self.name = name
		self.age = age
		self.score = score
		self.training_course = training_course
		self.phonen = phonen

	def set_name(self, name):
		self.name = name

	def set_age(self, age):
		self.age = age

	def set_score(self, score):
		self.score =  score

	def set_tc(self, training_course):
		self.training_course = training_course

	def set_phone(self, phonen):
		self.phonen = phonen

# a = Student("Aqua", 16, 4.7, 1, 79123456789)

# a.get_name()
# a.set_phone("+79999999999")

# a.getfull()

# 2

class rectangle:

	def __init__(self, height, width):
		self.height = height
		self.width = width

	def get_P(self):
		print((self.height+self.width)*2)

	def get_S(self):
		print(self.height*self.width)

# a = rectangle(4, 9)

# a.get_P()
# a.get_S()


# 3

class Auto:

	def __init__(self, brand, model, age, mileage):
		self.brand = brand
		self.model = model
		self.age = age
		self.mileage = mileage

	def getfull(self):
		print(f"Марка: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.age}\nПробег: {self.mileage}\n")

	def get_brand(self):
		print(f"Марка: {self.brand}")

	def get_model(self):
		print(f"Модель: {self.model}")

	def get_age(self):
		print(f"Год выпуска: {self.age}")

	def get_mileage(self):
		print(f"Пробег: {self.mileage}")

	def setz(self, brand, model, age, mileage):
		self.brand = brand
		self.model = model
		self.age = age
		self.mileage = mileage

	def set_brand(self, brand):
		self.brand = brand

	def set_model(self, model):
		self.model = model

	def set_age(self, age):
		self.age = age

	def set_mileage(self, mileage):
		self.mileage = mileage

# kia = Auto("Kia", "K7", 2018, 85000)
# kia.getfull()

# kia.set_mileage(90000)
# kia.get_mileage()

# 4

class Bank_score:
	def  __init__(self, name, age, pnumb, pser, balance):
		assert age > 14, "Клиент слишком молод"
		self.name = name
		self.age = age
		self.pnumb = pnumb
		self.pser = pser
		self.balance = balance
		self.operations = []

	def addm(self, summ):
		self.balance += summ
		self.operations.append(f"Пополнение счёта на сумму: {summ}")

	def rem(self, summ):
		self.balance -= summ
		self.operations.append(f"Снятие средств со счёта на сумму: {summ}")

	def get_b(self):
		print(f"Баланс: {self.balance}")

	def get_info(self):
		print(f"Имя клиента: {self.name}\nВозраст: {self.age}\nНомер паспорта: {self.pnumb}\nСерия паспорта: {self.pser}\nБаланс: {self.balance}")

	def get_operations(self):
		for i in self.operations:
			print(i)


# user1 = Bank_score("Ronaldo", 38, 1234, 111111, 900)
# user1.addm(80000)
# user1.get_b()
# user1.rem(10)
# user1.get_info()
# user1.get_operations()

# user2 = Bank_score("Hasbik", 9, 1111, 222222, 100)


# 5

class type_triangle:

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def typetr(self):
		a = self.a
		b = self.b
		c = self.c

		if a == b == c:
			return "Треугольник равносторонний"

		elif a == b or b == c or a == c:
			return "Треугольник равнобедренный"

		else:
			return "Треугольник разносторонний"

	def get_S(self):
		a = self.a
		b = self.b
		c = self.c
		p = (a + b + c) / 2
		S = (p*(p - a)*(p - b)*(p - c))**0.5
		return S



# abc = type_triangle(3, 4, 5)
# k = abc.typetr()
# print(abc.get_S())
# print(k, "\n")
# abc = type_triangle(2, 2, 2)
# k = abc.typetr()
# print(abc.get_S())
# print(k, "\n")
# abc = type_triangle(4, 4, 6)
# k = abc.typetr()
# print(abc.get_S())
# print(k, "\n")