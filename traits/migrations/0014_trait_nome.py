# Generated by Django 4.2 on 2023-04-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0013_remove_trait_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='trait',
            name='nome',
            field=models.CharField(default='nomer', max_length=20, unique=True),
        ),
    ]
