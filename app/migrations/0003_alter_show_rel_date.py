# Generated by Django 3.2.2 on 2021-07-05 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_show_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='rel_date',
            field=models.DateField(),
        ),
    ]
