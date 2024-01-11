from django.db import models

# Create your models here.
class Books(models.Model):
	name = models.CharField(max_length=40)
	annot = models.TextField()
	autor = models.CharField(max_length=30)
	year = models.DateField()

	def __str__(self):
		return self.name

# ну если таблица для авторов не нужна то ладно
# ато хотелось)) но если вы настаиваете...
# то не буду делать)