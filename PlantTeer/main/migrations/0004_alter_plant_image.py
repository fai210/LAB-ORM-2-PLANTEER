# Generated by Django 5.0.3 on 2024-03-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(default='/media/images/succulent-1031033_1280.jpg', upload_to='images/'),
        ),
    ]
