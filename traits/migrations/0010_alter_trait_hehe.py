# Generated by Django 4.2 on 2023-04-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0009_remove_trait_name_trait_hehe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trait',
            name='hehe',
            field=models.CharField(default='heihe', max_length=20, unique=True),
        ),
    ]
