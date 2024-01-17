from django.db import models


class Director(models.Model):
	fio = models.CharField(max_length=90)
	year = models.SmallIntegerField()

	def __str__(self):
		return self.fio

class Genre(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name



class Films(models.Model):
	name = models.CharField(max_length=30)
	year = models.SmallIntegerField()
	country = models.CharField(max_length=40)
	director = models.ForeignKey(Director, on_delete=models.CASCADE)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Afisha(models.Model):
	date = models.DateField()
	films = models.ForeignKey(Films, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.films)