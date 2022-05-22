# Generated by Django 4.0.4 on 2022-05-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_product_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('name', models.CharField(max_length=70)),
                ('money', models.IntegerField()),
                ('star', models.CharField(max_length=3)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'iPhone',
                'verbose_name_plural': 'iPhone_Products',
            },
        ),
        migrations.CreateModel(
            name='Nokia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('name', models.CharField(max_length=70)),
                ('money', models.IntegerField()),
                ('star', models.CharField(max_length=3)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Nokia',
                'verbose_name_plural': 'Nokia_Products',
            },
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('name', models.CharField(max_length=70)),
                ('money', models.IntegerField()),
                ('star', models.CharField(max_length=3)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Other',
                'verbose_name_plural': 'Others',
            },
        ),
        migrations.CreateModel(
            name='Redmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('name', models.CharField(max_length=70)),
                ('money', models.IntegerField()),
                ('star', models.CharField(max_length=3)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Redmi',
                'verbose_name_plural': 'Redmi_Products',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]