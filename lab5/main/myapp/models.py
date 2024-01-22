from django.db import models


class Genre(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()

	def __str__(self):
		return self.name

class Actor(models.Model):
	name = models.CharField(max_length=30)
	age = models.SmallIntegerField()
	description = models.TextField()
	photo = models.CharField(max_length=30)

	def __str__(self):
		return self.name



class Category(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()

	def __str__(self):
		return self.name

class Film(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	poster = models.CharField(max_length=30)
	date = models.DateField()
	country = models.CharField(max_length=50)
	actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
		
class Rewiew(models.Model):
	user = models.CharField(max_length=30)
	message = models.TextField()
	film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.user