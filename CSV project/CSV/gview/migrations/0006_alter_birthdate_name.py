# Generated by Django 3.2.5 on 2022-08-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gview', '0005_alter_birthdate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthdate',
            name='name',
            field=models.DateField(),
        ),
    ]