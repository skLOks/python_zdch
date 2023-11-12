# 1

class Point3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def get_res(self):
        print(f'x = {self.x}\ny = {self.y}\nz = {self.z}')

    def razn(self, a, b):
        return b - a
    
    def rr(self):
        return (f'От y до x примерно: {self.razn(self.x, self.y)}.\nОт y до z примерно: {self.razn(self.y, self.z)}\nНу и последнее: {self.razn(self.y, self.z)}')


# first = Point3D(5,12,3)
# first.get_res()

# first = Point3D(21,42,91)
# first.get_res()

# print(first.rr())


# 2

class Квадрат:

    def __init__(self, a=0):
        self.a = a
    
    def p(self):
        return self.a * 4

    def s(self):
        return self.a * self.a

# my_square = Квадрат(4)
# print(my_square.p())
# print(my_square.s())



# 3

class PSt:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c
    
    def p(self):
        if self.c == 0:
            self.c = (self.a**2 - self.b**2)**0.5
            return self.a + self.b + self.c 
        else:
            return self.a + self.b + self.c 

    def s(self):
        per = self.p()
        return (per * (per - self.a) * (per - self.b) * (per - self.c))**0.5

# a = PSt(5,2,12)

# print(a.p())
# print(a.s())


# 4

class Rast:

	try:

	    def __init__(self, a, b, c):
	        self.a = a
	        self.b = b
	        self.c = c

	    def perv(self):
	        self.x1 = [self.a[0], self.b[0]]
	        self.y1 = [self.a[1], self.b[1]]
	        self.x2 = max(self.x1) - min(self.x1)
	        self.y2 = max(self.y1) - min(self.y1)
	        return (self.x2**2 + self.y2**2)**0.50

	    def vt(self):
	        self.x1 = [self.a[0], self.c[0]]
	        self.y1 = [self.a[1], self.c[1]]
	        self.x2 = max(self.x1) - min(self.x1)
	        self.y2 = max(self.y1) - min(self.y1)
	        return (self.x2**2 + self.y2**2)**0.5

	    def tr(self):
	        self.x1 = [self.b[0], self.c[0]]
	        self.y1 = [self.b[1], self.c[1]]
	        self.x2 = max(self.x1) - min(self.x1)
	        self.y2 = max(self.y1) - min(self.y1)
	        return (self.x2**2 + self.y2**2)**0.5

	    def p(self):
	        return self.perv() + self.vt() + self.tr()

	except:
		print("Что то случилось, решайте сами, мой код идеален, наверное опять ваш Pycharm шалит")

# a = Rast((2,4), (6,9), (6,0))
# print(a.p())


# 5

class CPerson:

    def __init__(self, fam, name, otchestvo, dater, g):
        self.fam = fam
        self.name = name
        self.otchestvo = otchestvo
        self.dater = dater
        self.g = g

    def get_fam(self):
        return f'Фамилия: {self.fam}'

    def get_name(self):
        return f'Имя: {self.name}'

    def get_otch(self):
        return f'Отчество: {self.otchestvo}'

    def getd_date(self):
        return f'Хэппи бёздэй: {self.dater}'

    def get_gender(self):
        return f'Мужик или нет: {self.g}'

    def get_full(self):
        return f'Фамилия: {self.fam}\nИмя: {self.name}\nОтчество: {self.otchestvo}\nХэппи бёздэй: {self.dater}\nМужик или нет: {self.g}'
    
    def __del__(self):
        print("Вы его убили...")

# myPerson = CPerson("Krishtianu", "Ronaldu", "Alekseevich", "05.02.1985", "МУЖИК")
# print(myPerson.get_fam())
# print(myPerson.get_name())
# print(myPerson.get_otch())
# print(myPerson.getd_date())
# print(myPerson.get_gender())
# print(myPerson.get_full())
# myPerson.name = "Leonel"
# print(myPerson.get_full())
# del myPerson


# 6

class Phone:

    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def vivod(self):
        return(f'Номер: {self.number}\nМодель: {self.model}\nЖирнота телефона: {self.weight}\n=============')

    def zvonit(self, name):
        return(f'Как правильно: звонит или звонит?, короче, вам звонит: {name}\n')

    def gn(self):
        return(self.number)


# a1 = Phone(88005553535, "Samsung S23", "Malo")
# a2 = Phone(88888888888, "Xiamomi i-999 pro ultra mega redmi 38 ** 8 lite Yagami", 110)
# a3 = Phone(89898989898, "IS-3", 333)

# print(a1.zvonit("Ronaldu"))
# print(a1.vivod())
# print(a1.gn())

# print(a2.zvonit("Dimon"))
# print(a2.vivod())
# print(a2.gn())

# print(a3.zvonit("Mozyakin"))
# print(a3.vivod())
# print(a3.gn())


# 7

class Reader:

    def __init__(self, fam, name, otch, lc, uuu, dater, pn):
        self.fam = fam
        self.name = name
        self.otch = otch
        self.lc = lc
        self.uuu = uuu
        self.dater = dater
        self.pn = pn

    def vzyal(self, quantity):
        print(f'{self.fam} {self.name[0]}. {self.otch[0]}. взял {quantity} книги.')

    def vernul(self, quantity):
        print(f'{self.fam} {self.name[0]}. {self.otch[0]}. вернул {quantity} книги.')


# myReader = Reader("Петров", "Василиса", "Brodivshiy", 5, "Класс", "17.07.0007", "+79999999999")

# myReader.vzyal(3)
# myReader.vernul(3)