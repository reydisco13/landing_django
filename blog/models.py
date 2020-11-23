from django.db import models

# Create your models here.
from django.db import models


class Title(models.Model):
    my_photo = models.ImageField(upload_to='my_photo/')
    my_name = models.CharField(max_length=150)
    status = models.CharField(max_length=30)
    about_me = models.TextField()
    my_citi = models.CharField(max_length=30)
    contacts = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Мое фото+контакты'
        verbose_name_plural = 'Мое фото+контакты'


class MyService(models.Model):
    service_name = models.CharField(max_length=250)
    service_description = models.TextField()

    def __str__(self):
        return '%s' % self.service_name
    # def __str__(self):
    #     return '%s %s' % (id, self.title_skill)

    class Meta:
        verbose_name = 'Моя услуга'
        verbose_name_plural = 'Мои услуги'


class Experience(models.Model):
    my_experience = models.TextField()

    class Meta:
        verbose_name = 'Опыт работы и практика'
        verbose_name_plural = 'Опыт работы и практика'

    def __str__(self):
        return 'id = %s,  %s...' % (self.id, self.my_experience[:55])


class Price(models.Model):
    name_service = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    class Meta:
        ordering = ['name_service']
        verbose_name = 'Цены на мои услуги'
        verbose_name_plural = 'Цены на мои услуги'

    def __str__(self):
        return 'id = %s,  %s' % (self.id, self.name_service)

