from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Creator(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tovar(models.Model):
	name = models.CharField(max_length=30)
	size = models.IntegerField()
	creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.IntegerField()
