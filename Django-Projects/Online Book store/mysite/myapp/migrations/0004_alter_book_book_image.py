# Generated by Django 5.0.7 on 2024-10-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_book_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='book_images/default.jpg', upload_to='book_images/'),
        ),
    ]
