# Generated by Django 4.2 on 2023-04-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0008_remove_trait_trait_name_trait_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trait',
            name='name',
        ),
        migrations.AddField(
            model_name='trait',
            name='hehe',
            field=models.CharField(default='hehe', max_length=20, unique=True),
        ),
    ]
