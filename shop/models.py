from django.db import models
from django.urls import reverse

# Create your models here.



class Iphone(models.Model):
    image = models.ImageField('image' , upload_to='images/')
    name = models.CharField(max_length=70)
    money = models.IntegerField()
    star = models.CharField(max_length=3)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'iPhone'
        verbose_name_plural = "iPhone Products" 

    def get_absolute_url(self):
        return f"{self.slug}/"

    def __str__(self):
        return self.name

class Nokia(models.Model):
    image = models.ImageField('image' , upload_to='images/')
    name = models.CharField(max_length=70)
    money = models.IntegerField()
    star = models.CharField(max_length=3)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Nokia'
        verbose_name_plural = "Nokia Products" 

    def get_absolute_url(self):
        return f"{self.slug}/"

    def __str__(self):
        return self.name

class Redmi(models.Model):
    image = models.ImageField('image' , upload_to='images/')
    name = models.CharField(max_length=70)
    money = models.IntegerField()
    star = models.CharField(max_length=3)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Redmi'
        verbose_name_plural = "Redmi Products" 

    def get_absolute_url(self):
        return f"{self.slug}/"

    def __str__(self):
        return self.name

class Others(models.Model):
    image = models.ImageField('image' , upload_to='images/')
    name = models.CharField(max_length=70)
    money = models.IntegerField()
    star = models.CharField(max_length=3)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Other'
        verbose_name_plural = "Others" 

    def get_absolute_url(self):
        return f"{self.slug}/"

    def __str__(self):
        return self.name