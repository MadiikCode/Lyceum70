from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    subject = models.CharField(max_length=20, verbose_name='Предмет')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')

class Subject(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name



