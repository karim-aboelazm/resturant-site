# Generated by Django 4.1.7 on 2023-02-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant", "0002_remove_resturantspecials_full_title_ar_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resturanttablereservasion",
            name="date",
            field=models.CharField(max_length=10, verbose_name="Date"),
        ),
        migrations.AlterField(
            model_name="resturanttablereservasion",
            name="time",
            field=models.CharField(max_length=10, verbose_name="Time"),
        ),
    ]
