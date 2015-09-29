from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	about_me = models.TextField()

	def __str__(self):
		return self.first_name + " " + self.last_name


class Pet(models.Model):
	pet_name = models.CharField(max_length=20)
	pet_type = models.CharField(max_length=15)
	pet_color = models.CharField(max_length=25)
	pet_owner = models.ForeignKey(Person)

	def __str__(self):
		return self.pet_name
