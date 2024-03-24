# Generated by Django 5.0.3 on 2024-03-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='categroy',
            field=models.CharField(choices=[('Trees', 'Trees'), (' Shrubs', ' Shrubs'), (' Flowering Plants', ' Flowering Plants'), ('Herbaceous Plants', 'Herbaceous Plants')], max_length=64),
        ),
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=2048),
        ),
    ]