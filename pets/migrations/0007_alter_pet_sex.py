# Generated by Django 4.2 on 2023-04-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_alter_pet_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Informed', 'Default')], default='Not Informed', max_length=20, null=True),
        ),
    ]
