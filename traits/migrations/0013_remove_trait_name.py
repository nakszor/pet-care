# Generated by Django 4.2 on 2023-04-16 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0012_remove_trait_hehe_trait_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trait',
            name='name',
        ),
    ]
