from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cell_phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name


class FrequentlyAskedQuestion(models.Model):
	question = models.CharField(max_length=500)
	answer = models.TextField()

class Testimonial(models.Model):
	styling_goal = models.CharField(max_length=500)
	testimonial = models.TextField()