from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

    def values(self):
    	return {
    		'username': self.user_name,
    		'name': self.name,
    		'email': self.email
    	}