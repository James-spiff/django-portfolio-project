from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio_list/images/')
	url = models.URLField(blank=True) 

	def __str__(self):
		return self.title #returns the title when viewed from the admin page