from django.db import models
from django.urls import reverse

# Create your models here.



class Product(models.Model):
    image = models.ImageField('image' , upload_to='images/')
    name = models.CharField(max_length=70)
    money = models.IntegerField()
    star = models.CharField(max_length=3)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products" 

    def get_absolute_url(self):
        return reverse("product", args=[self.slug])

    def __str__(self):
        return self.name