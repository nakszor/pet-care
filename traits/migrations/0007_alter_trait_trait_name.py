# Generated by Django 4.2 on 2023-04-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0006_alter_trait_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trait',
            name='trait_name',
            field=models.CharField(db_column='name', max_length=20, unique=True),
        ),
    ]